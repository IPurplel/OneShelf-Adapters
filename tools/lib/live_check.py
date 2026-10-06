"""Live verification of an adapter through OneShelf Core's own runtime: evidence, never a gate.

    ./tools/live-check oneshelf.example              # inputs from the adapter's own packaged tests
    ./tools/live-check oneshelf.example --query X --listing-key Y
    ./tools/live-check oneshelf.example --no-files   # skip fetching the file/page bytes

The adapter is built with the canonical builder and loaded exactly as an install would load it. Each declared
capability then runs against the live source through `RecipeRuntime`, with Core's `SourceFetcher`, its
`HttpClient` and the egress policy derived from the manifest (private addresses refused, every redirect and
DNS answer re-checked), under the Traffic Governor configured with the adapter's own rate limit. The chain is
the one a library follows: search → work → catalog → downloads/reader, each step fed by the one before.
Where content is involved the bytes are fetched and checked with Core's own validators — an EPUB opened, a
PDF read, an image decoded — because a 200 proves nothing (source-capability-ledger §"States").

The result is printed with the date, every URL requested, its status and redirects, and any Retry-After.
Packaged tests remain the gate; a live pass never changes a trust level by itself (docs/testing.md).
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
import tempfile
import time
from pathlib import Path

from oneshelf.integrity.validators import _validate_image, validate
from oneshelf.net.governor import Priority, TrafficGovernor
from oneshelf.net.http import HttpClient
from oneshelf.net.policy import policy_for_plugin
from oneshelf.plugins.adapter_repo import discover
from oneshelf.plugins.bundled import build_package
from oneshelf.plugins.package import load_package
from oneshelf.plugins.results import ListResult
from oneshelf.plugins.runtime import CapabilityError, FetchedResponse, RecipeRequest, RecipeRuntime
from oneshelf.sources.fetcher import SourceFetcher

sys.path.insert(0, str(Path(__file__).resolve().parent))
from inspect_source import Robots, _fetch_robots  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
MAX_FILE_BYTES = 150 * 1024 * 1024


class RecordingFetcher:
    """Core's SourceFetcher, with every request written down for the evidence record."""

    def __init__(self, inner: SourceFetcher) -> None:
        self.inner = inner
        self.log: list[dict] = []

    async def fetch(self, request: RecipeRequest) -> FetchedResponse:
        started = time.monotonic()
        try:
            response = await self.inner.fetch(request)
        except Exception as exc:
            self.log.append({"capability": request.capability, "url": request.url, "error": f"{type(exc).__name__}: {exc}"})
            raise
        entry = {"capability": request.capability, "url": request.url, "status": response.status,
                 "seconds": round(time.monotonic() - started, 2), "bytes": len(response.body)}
        if response.url != request.url:
            entry["final_url"] = response.url
        retry_after = response.header("Retry-After")
        if retry_after:
            entry["retry_after"] = retry_after
        self.log.append(entry)
        return response


def _inputs_from_tests(package) -> dict[str, dict]:
    found: dict[str, dict] = {}
    for case in package.tests.cases:
        found.setdefault(case.capability, dict(case.inputs))
    return found


def _summary(result) -> dict:
    if isinstance(result, ListResult):
        first = result.entries[0] if result.entries else None
        return {"entries": len(result.entries), "complete": result.complete, "stop_reason": result.evidence.stop_reason,
                "pages": result.evidence.pages, "skipped": result.evidence.skipped,
                "duplicates": result.evidence.duplicates,
                "issues": [f"{i.category}: {i.detail}" for i in result.evidence.issues][:5],
                "first": first.__dict__ if first is not None else None,
                "last": result.entries[-1].__dict__ if len(result.entries) > 1 else None}
    return {"result": result.__dict__}


async def run(adapter_id: str, args) -> int:
    adapters, problems = discover(ROOT)
    match = [a for a in adapters if a.id == adapter_id]
    if not match:
        print(f"no adapter {adapter_id!r} under adapters/", file=sys.stderr)
        return 2
    adapter = match[0]
    with tempfile.TemporaryDirectory() as work:
        package = load_package(build_package(adapter.path, Path(work) / f"{adapter.id}.osp"))
        manifest, source = package.manifest, package.source
        policy = policy_for_plugin(package.id, domains=list(manifest.network.domains),
                                   cdn_domains=list(manifest.network.cdn_domains),
                                   allow_http=manifest.network.allow_http, dev_test_source_enabled=False)
        governor = TrafficGovernor()
        governor.configure_source(package.id, concurrency=source.rate_limit.concurrency,
                                  requests_per_minute=source.rate_limit.requests_per_minute)
        report: dict = {"adapter": package.id, "version": package.version, "tier": adapter.tier,
                        "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                        "domains": list(manifest.network.domains), "cdn_domains": list(manifest.network.cdn_domains),
                        "capabilities": {}}
        failures: list[str] = []
        async with HttpClient(policy, connect_timeout=source.timeouts.connect_seconds,
                              read_timeout=source.timeouts.read_seconds) as client:
            fetcher = RecordingFetcher(SourceFetcher(package, client, governor, None, Priority.MANUAL))
            runtime = RecipeRuntime(package, fetcher)
            declared = set(manifest.capabilities)
            tested = _inputs_from_tests(package)
            chain: dict = {}

            async def attempt(capability: str, inputs: dict) -> object | None:
                inputs = {k: v for k, v in inputs.items() if k in package.recipes[capability].inputs and v is not None}
                try:
                    result = await runtime.run(capability, inputs)
                except CapabilityError as exc:
                    report["capabilities"][capability] = {"inputs": inputs, "error": f"{exc.category}: {exc}"}
                    failures.append(f"{capability}: {exc.category}: {exc}")
                    return None
                summary = {"inputs": inputs, **_summary(result)}
                report["capabilities"][capability] = summary
                if isinstance(result, ListResult):
                    if not result.entries:
                        failures.append(f"{capability}: no entries")
                    elif capability in ("catalog", "reader", "downloads") and not result.complete:
                        failures.append(f"{capability}: incomplete ({result.evidence.stop_reason})")
                return result

            if "health" in declared:
                await attempt("health", tested.get("health", {}))
            if "search" in declared:
                inputs = dict(tested.get("search", {}))
                if args.query:
                    inputs["query"] = args.query
                inputs.pop("page", None), inputs.pop("offset", None)
                result = await attempt("search", inputs)
                if isinstance(result, ListResult) and result.entries:
                    chain["listing_key"] = result.entries[0].listing_key
            if "latest" in declared:
                await attempt("latest", tested.get("latest", {}))
            listing_key = args.listing_key or chain.get("listing_key") or tested.get("work", tested.get("catalog", {})).get("listing_key")
            if "work" in declared and listing_key is not None:
                await attempt("work", {"listing_key": listing_key, "language": manifest.defaults.language})
            unit = None
            if "catalog" in declared and listing_key is not None:
                result = await attempt("catalog", {"listing_key": listing_key, "language": manifest.defaults.language})
                if isinstance(result, ListResult) and result.entries:
                    unit = result.entries[0]
            unit_inputs = {"unit_key": args.unit_key or (unit.unit_key if unit else None)
                           or tested.get("downloads", tested.get("reader", {})).get("unit_key"),
                           "url": unit.url if unit else None, "language": manifest.defaults.language}
            for capability in ("downloads", "reader"):
                if capability not in declared or unit_inputs["unit_key"] is None:
                    continue
                result = await attempt(capability, unit_inputs)
                if args.no_files or not isinstance(result, ListResult) or not result.entries:
                    continue
                if capability == "reader" and any(entry.html is not None for entry in result.entries):
                    # Text units (plugin API 1.2) carry their content: there are no bytes to fetch. The check
                    # is what Download Missing would store — Core's own container, through Core's validator.
                    check = _text_unit_check(result.entries, Path(work) / "unit.ostext", manifest.defaults.language)
                    if check.get("problem"):
                        failures.append(f"reader: text unit: {check['problem']}")
                    report["capabilities"][capability]["text_checked"] = check
                    continue
                picks = [result.entries[0]] if capability == "downloads" else [result.entries[0], result.entries[-1]]
                checks = []
                for entry in picks:
                    try:
                        response = await fetcher.inner.request(entry.url, capability=capability, auth_mode="none",
                                                               headers=dict(package.recipes[capability].resource_headers) or None,
                                                               max_bytes=MAX_FILE_BYTES)
                    except Exception as exc:  # an egress refusal (unlisted host, http downgrade) is a finding, not a crash
                        problem = f"{type(exc).__name__}: {exc}"
                        failures.append(f"{capability}: {entry.url}: {problem}")
                        checks.append({"url": entry.url, "problem": problem})
                        continue
                    check = {"url": entry.url, "status": response.status, "final_url": response.url,
                             "bytes": len(response.body), "content_type": response.headers.get("Content-Type")}
                    if response.status != 200:
                        check["problem"] = f"HTTP {response.status}"
                    elif capability == "reader":
                        check["problem"] = _validate_image(response.body)
                    else:
                        path = Path(work) / "download.bin"
                        path.write_bytes(response.body)
                        verdict = validate(path)
                        check.update({"validated_as": verdict.format, "declared_format": entry.format,
                                      "pages": verdict.page_count})
                        if not verdict.ok:
                            check["problem"] = verdict.reason or "not a valid epub, pdf or cbz"
                        elif verdict.format != entry.format:
                            check["problem"] = f"declared {entry.format} but the bytes are {verdict.format}"
                    if check.get("problem"):
                        failures.append(f"{capability}: {entry.url}: {check['problem']}")
                    checks.append({k: v for k, v in check.items() if v is not None})
                report["capabilities"][capability]["bytes_checked"] = checks
        report["requests"] = fetcher.log
        # Every URL the adapter requested, checked against its host's robots.txt (RFC 9309): an adapter may
        # not use a disallowed path, however well it works (docs/review-policy.md).
        verdicts: dict[str, Robots | None] = {}
        requested = [{entry["url"], entry.get("final_url", entry["url"])} for entry in fetcher.log]
        requested += [{check["url"], check.get("final_url", check["url"])}
                      for capability in report["capabilities"].values() for check in capability.get("bytes_checked", [])]
        for urls in requested:
            for url in urls:
                host = url.split("/")[2]
                if host not in verdicts:
                    record = {"url": f"https://{host}/robots.txt"}
                    try:
                        meta = await _fetch_robots(record, policy_for_plugin(package.id, domains=[host], cdn_domains=[],
                                                                            allow_http=False, dev_test_source_enabled=False))
                        verdicts[host] = Robots(meta["body"].decode("utf-8", "replace")) if meta["status"] == 200 else None
                    except Exception as exc:  # unreachable robots.txt is recorded, not guessed at
                        verdicts[host] = None
                        report.setdefault("robots_unavailable", {})[host] = f"{type(exc).__name__}: {exc}"
                robots = verdicts[host]
                if robots is not None and not robots.can_fetch("OneShelf", url):
                    failures.append(f"robots.txt disallows {url}")
        report["robots_checked_hosts"] = sorted(verdicts)
        report["result"] = "PASS" if not failures else "FAIL"
        report["failures"] = failures
        print(json.dumps(report, ensure_ascii=False, indent=1, default=str))
        return 0 if not failures else 1


def _text_unit_check(entries, path: Path, language: str | None) -> dict:
    # Imported here: only a Core with text units (plugin API 1.2) has them, and only such a Core can
    # have produced an entry with text.
    from oneshelf.text.container import TextUnit, write_text_container
    from oneshelf.text.direction import content_direction
    from oneshelf.text.sanitise import plain_text, sanitise, split_sections

    sections = []
    for entry in entries:
        if not entry.html:
            return {"problem": f"item {entry.index} has no text"}
        sections.extend(split_sections(sanitise(entry.html)))
    if not sections:
        return {"problem": "no text once sanitised"}
    write_text_container(path, TextUnit(title=entries[0].title, language=language,
                                        direction=content_direction(language), source_url=None, sections=sections))
    verdict = validate(path)
    check = {"validated_as": verdict.format, "sections": len(sections),
             "characters": sum(s.characters for s in sections), "direction": content_direction(language),
             "first_text": plain_text(sections[0].html)[:160]}
    if not verdict.ok:
        check["problem"] = verdict.reason or "not a valid text unit"
    return check


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="live-check", description=__doc__.splitlines()[0])
    parser.add_argument("adapter", help="plugin id, e.g. oneshelf.gutenberg")
    parser.add_argument("--query", help="search query (default: the packaged search test's)")
    parser.add_argument("--listing-key", help="work to follow (default: the first search result)")
    parser.add_argument("--unit-key", help="unit to fetch (default: the first catalog unit)")
    parser.add_argument("--no-files", action="store_true", help="do not fetch file or page bytes")
    args = parser.parse_args(argv)
    return asyncio.run(run(args.adapter, args))


if __name__ == "__main__":
    sys.exit(main())
