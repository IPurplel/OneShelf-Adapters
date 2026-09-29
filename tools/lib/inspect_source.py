"""Scrapling-assisted source inspection: development evidence for adapter authors, never an adapter.

    ./tools/inspect-source URL                         # fetch (once; cached) and report
    ./tools/inspect-source URL --css "li.result a::attr(href)"   # also evaluate selectors, as the runtime would
    ./tools/inspect-source --from saved.html --url URL  # the same report for a saved page, fully offline

What it reports: the final URL and redirect chain, status, content type, caching and rate-limit headers,
robots.txt verdicts, title, canonical URL, language and direction signals, feeds and machine-readable
endpoints (RSS/Atom/OPDS, OpenSearch, IIIF, OAI-PMH, JSON APIs, sitemaps), file links by format, media and
file hosts, recurring link shapes with a sample selector, pagination candidates, stable-id candidates, and
whether the page appears to need JavaScript. JSON responses get a map of their arrays and scalar paths.

Boundaries (Master §12.1; CONTRIBUTING.md "Never commit"):

- Every request goes through OneShelf Core's own HTTP client: its egress policy refuses private, loopback
  and link-local addresses, re-checks every redirect and DNS answer, and sends OneShelf's honest
  User-Agent. Only the URL's own host is allowlisted; a redirect elsewhere stops and is reported, and
  `--allow-host` adds a host deliberately. Scrapling's fetchers are not used: they impersonate a browser.
- robots.txt is read first, and a disallowed URL is not fetched.
- One request per URL: responses are cached under `.inspect-cache/` (git-ignored) and reused.
- Parsing is Scrapling's `Selector` — the parser the runtime uses — and `--css`/`--xpath`/`--json` are
  evaluated by the runtime's own extraction function, so what matches here matches in OneShelf.
- Suggested selectors are leads, not answers. Adaptive matching is never used: an adapter's selectors
  must be explicit, reviewed and backed by fixtures and packaged tests.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import parse_qsl, urljoin, urlsplit
from urllib.robotparser import RobotFileParser

from oneshelf.net.http import USER_AGENT, FetchFailed, HttpClient, TooManyRedirects
from oneshelf.net.policy import BlockedDestination, DisallowedTarget, EgressPolicy
from oneshelf.plugins import jsonpath
from oneshelf.plugins.runtime import _raw_for, parse_document
from oneshelf.plugins.schema import FieldSpec

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".inspect-cache"
FILE_FORMATS = ("epub", "pdf", "cbz", "cbr", "zip", "djvu", "mobi", "azw3", "txt", "kfx", "fb2")
FEED_TYPES = {"application/rss+xml": "RSS", "application/atom+xml": "Atom", "application/opensearchdescription+xml":
              "OpenSearch", "application/json": "JSON", "application/ld+json": "JSON-LD"}
ENDPOINT_HINTS = [("IIIF", re.compile(r"iiif|/manifest(?:\.json)?(?:$|[?#/])", re.I)),
                  ("OAI-PMH", re.compile(r"[/?]oai(?:[/?_-]|$)|verb=", re.I)),
                  ("OPDS", re.compile(r"opds", re.I)),
                  ("API", re.compile(r"/api(?:/|\.php|$)|/w/api\.php|/rest(?:_v\d)?/", re.I)),
                  ("feed", re.compile(r"/(?:feed|rss|atom)(?:[/.?]|$)", re.I)),
                  ("sitemap", re.compile(r"sitemap[^/]*\.xml", re.I))]
NEXT_TEXT = re.compile(r"^\s*(?:next|older|more|›|»|→|التالي|التالية|التالى|suivant|weiter|次へ|次)\s*[›»→]?\s*$", re.I)
PAGE_PARAMS = {"page", "p", "pg", "offset", "start", "from", "skip", "cursor", "paged", "pagenum", "sf"}
SPA_MARKERS = ("__NEXT_DATA__", "__NUXT__", "id=\"root\"", "id=\"app\"", "ng-version", "data-reactroot",
               "window.__INITIAL_STATE__", "window.__APOLLO_STATE__")
ARABIC = re.compile(r"[؀-ۿݐ-ݿࢠ-ࣿ]")
LATIN = re.compile(r"[A-Za-z]")
CJK = re.compile(r"[぀-ヿ一-鿿]")


# -- fetching: Core's client, robots first, cached ---------------------------------------------------------

def _cache_path(url: str) -> Path:
    return CACHE / hashlib.sha256(url.encode()).hexdigest()[:32]


async def _fetch(client: HttpClient, url: str, max_bytes: int) -> dict:
    cached = _cache_path(url)
    if (cached / "meta.json").is_file():
        meta = json.loads((cached / "meta.json").read_text())
        meta["body"] = (cached / "body").read_bytes()
        meta["from_cache"] = True
        return meta
    started = time.monotonic()
    response = await client.fetch(url, max_bytes=max_bytes)
    meta = {"url": url, "final_url": response.url, "status": response.status, "redirects": response.redirects,
            "headers": {k: v for k, v in response.headers.items() if k.lower() != "set-cookie"},
            "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "elapsed_s": round(time.monotonic() - started, 2)}
    cached.mkdir(parents=True, exist_ok=True)
    (cached / "meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False))
    (cached / "body").write_bytes(response.body)
    meta["body"], meta["from_cache"] = response.body, False
    return meta


async def _fetch_robots(robots: dict, policy: EgressPolicy) -> dict:
    """robots.txt may redirect to another host (RFC 9309 §2.3.1.2: follow at least five hops) — api.wikimedia.org
    serves www.mediawiki.org's. Each hop is allowed by name, one at a time, still through Core's client and its
    checks on every address; nothing but robots.txt is ever fetched this way."""
    hosts = list(policy.domains)
    for _hop in range(6):
        async with HttpClient(EgressPolicy(domains=tuple(hosts)), connect_timeout=15, read_timeout=45) as client:
            try:
                meta = await _fetch(client, robots["url"], 2 * 1024 * 1024)
            except DisallowedTarget as exc:
                found = re.search(r"domain not allowlisted: (\S+)", str(exc))
                if not found or found.group(1) in hosts:
                    raise
                hosts.append(found.group(1))
                robots.setdefault("redirected_via", []).append(found.group(1))
                continue
        return meta
    raise TooManyRedirects("robots.txt redirected too many times")


async def fetch_with_robots(url: str, extra_hosts: list[str], max_bytes: int, ignore_robots: bool) -> tuple[dict, dict]:
    host = urlsplit(url).hostname or ""
    policy = EgressPolicy(domains=tuple(dict.fromkeys([host.lower(), *[h.lower() for h in extra_hosts]])))
    robots: dict = {"url": urljoin(url, "/robots.txt")}
    async with HttpClient(policy, connect_timeout=15, read_timeout=45) as client:
        try:
            meta = await _fetch_robots(robots, policy)
            robots["status"] = meta["status"]
            if meta["status"] == 200:
                text = meta["body"].decode("utf-8", "replace")
                parser = RobotFileParser()
                parser.parse(text.splitlines())
                robots["oneshelf_allowed"] = parser.can_fetch("OneShelf", url)
                robots["any_agent_allowed"] = parser.can_fetch("*", url)
                robots["crawl_delay"] = parser.crawl_delay("OneShelf") or parser.crawl_delay("*")
                robots["sitemaps"] = parser.site_maps() or []
            else:  # RFC 9309: an unavailable robots.txt (4xx) means no restrictions
                robots["oneshelf_allowed"] = robots["any_agent_allowed"] = meta["status"] < 500
        except (FetchFailed, DisallowedTarget, BlockedDestination, TooManyRedirects, TimeoutError) as exc:
            robots["error"] = f"{type(exc).__name__}: {exc}"
            robots["oneshelf_allowed"] = None
        if robots.get("oneshelf_allowed") is False and not ignore_robots:
            raise SystemExit(f"robots.txt at {robots['url']} disallows {url} for OneShelf; not fetched.\n"
                             "An adapter may not use a disallowed path either (docs/review-policy.md).")
        return await _fetch(client, url, max_bytes), robots


# -- analysis ----------------------------------------------------------------------------------------------

def _shape(url: str, base_host: str) -> str:
    """A URL with its variable parts named: /books/{n}/ , /ebooks/{slug}/{slug}."""
    parts = urlsplit(url)
    segments = []
    for seg in parts.path.split("/"):
        if re.fullmatch(r"\d+", seg):
            seg = "{n}"
        elif re.fullmatch(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", seg, re.I):
            seg = "{uuid}"
        elif re.fullmatch(r"[A-Za-z0-9]*\d[A-Za-z0-9]*", seg) and len(seg) >= 6:
            seg = "{id}"
        elif re.search(r"%[0-9A-F]{2}|-", seg, re.I) and len(seg) > 12:
            seg = "{slug}"
        segments.append(seg)
    host = "" if (parts.hostname or "") == base_host else f"//{parts.hostname}"
    query = "&".join(sorted(f"{k}={{v}}" for k, _ in parse_qsl(parts.query, keep_blank_values=True)))
    return host + "/".join(segments) + (f"?{query}" if query else "")


def _script_ratio(text: str) -> dict:
    arabic, latin, cjk = len(ARABIC.findall(text)), len(LATIN.findall(text)), len(CJK.findall(text))
    total = arabic + latin + cjk or 1
    return {"arabic": round(arabic / total, 2), "latin": round(latin / total, 2), "cjk": round(cjk / total, 2)}


def analyse_markup(body: bytes, url: str, base_host: str) -> dict:
    text = body.decode("utf-8", "replace")
    doc = parse_document(text, url=url)
    report: dict = {}
    first = lambda sel: (doc.css(sel) or [None])[0]  # noqa: E731
    title = first("title")
    report["title"] = title.get_all_text(strip=True) if title is not None else None
    report["canonical"] = doc.css("link[rel='canonical']::attr(href)").get()
    html_node = first("html")
    report["language"] = {
        "html_lang": html_node.attrib.get("lang") if html_node is not None else None,
        "html_dir": html_node.attrib.get("dir") if html_node is not None else None,
        "meta_content_language": doc.css("meta[http-equiv='content-language']::attr(content)").get(),
        "og_locale": doc.css("meta[property='og:locale']::attr(content)").get(),
        "script_share": _script_ratio(doc.get_all_text(separator=" ", strip=True)[:200_000]),
    }
    report["metadata"] = {m.attrib.get("property") or m.attrib.get("name"): m.attrib.get("content", "")[:160]
                          for m in doc.css("meta[property^='og:'], meta[name^='citation_'], meta[name^='dc.'],"
                                           " meta[name^='DC.'], meta[name='description']")[:40]}
    report["jsonld_types"] = sorted({t for blob in doc.css("script[type='application/ld+json']::text").getall()
                                     for t in re.findall(r'"@type"\s*:\s*"([^"]+)"', blob)})

    feeds = []
    for link in doc.css("link[rel='alternate'], link[rel='search'], link[rel='next'], link[rel='prev'],"
                        " link[type*='opds'], link[rel='manifest']"):
        kind = link.attrib.get("type", "")
        feeds.append({"rel": link.attrib.get("rel"), "type": kind, "kind": FEED_TYPES.get(kind.split(";")[0], kind),
                      "href": urljoin(url, link.attrib.get("href", ""))})
    report["declared_links"] = feeds

    anchors = [(a.attrib.get("href", "").strip(), a.get_all_text(separator=" ", strip=True), a) for a in doc.css("a[href]")]
    absolute = [(urljoin(url, h), t, a) for h, t, a in anchors if h and not h.startswith(("#", "javascript:", "mailto:"))]
    report["links"] = {"total": len(absolute), "unique": len({h for h, _, _ in absolute}),
                       "duplicates": len(absolute) - len({h for h, _, _ in absolute})}

    endpoints = defaultdict(set)
    for href in [h for h, _, _ in absolute] + [f["href"] for f in feeds] + doc.css("script::attr(src)").getall():
        for label, pattern in ENDPOINT_HINTS:
            if pattern.search(href):
                endpoints[label].add(urljoin(url, href))
    report["endpoint_hints"] = {k: sorted(v)[:8] for k, v in endpoints.items()}

    files = defaultdict(list)
    for href, _, _ in absolute:
        ext = urlsplit(href).path.rsplit(".", 1)[-1].lower() if "." in urlsplit(href).path.rsplit("/", 1)[-1] else ""
        if ext in FILE_FORMATS:
            files[ext].append(href)
    report["file_links"] = {k: {"count": len(v), "hosts": sorted({urlsplit(h).hostname for h in v}), "example": v[0]}
                            for k, v in files.items()}

    media_hosts = Counter()
    for attr in ("src", "data-src", "data-url", "data-original", "srcset"):
        for value in doc.css(f"img::attr({attr}), source::attr({attr})").getall():
            candidate = urljoin(url, value.split()[0]) if value.strip() else ""
            if candidate.startswith("http"):
                media_hosts[urlsplit(candidate).hostname] += 1
    report["media_hosts"] = dict(media_hosts.most_common(10))
    report["link_hosts"] = dict(Counter(urlsplit(h).hostname for h, _, _ in absolute).most_common(10))

    shapes: dict[str, list] = defaultdict(list)
    for href, text_, node in absolute:
        shapes[_shape(href, base_host)].append((href, text_, node))
    recurring = []
    for shape, members in sorted(shapes.items(), key=lambda kv: -len(kv[1])):
        if len(members) < 3 or not re.search(r"\{(n|id|slug|uuid)\}", shape):
            continue
        href, text_, node = members[0]
        try:
            selector = node.generate_css_selector
        except Exception:  # generation is a convenience; a failure here says nothing about the page
            selector = None
        recurring.append({"shape": shape, "count": len(members), "example": href, "example_text": text_[:80],
                          "sample_selector_for_first": selector})
    report["recurring_link_shapes"] = recurring[:12]

    pagination = []
    for href, text_, node in absolute:
        query_keys = {k.lower() for k, _ in parse_qsl(urlsplit(href).query)}
        if NEXT_TEXT.match(text_ or "") or node.attrib.get("rel") == "next" or query_keys & PAGE_PARAMS:
            pagination.append({"text": text_[:30], "href": href, "rel": node.attrib.get("rel")})
    report["pagination_candidates"] = pagination[:12]

    data_attrs = Counter(k for el in doc.css("[class], [id], a, li, div, article")[:5000] for k in el.attrib
                         if k.startswith("data-"))
    report["data_attributes"] = dict(data_attrs.most_common(12))

    scripts = len(doc.css("script"))
    body_node = first("body")
    visible = len(body_node.get_all_text(separator=" ", strip=True)) if body_node is not None else 0
    markers = [m for m in SPA_MARKERS if m in text]
    report["javascript"] = {
        "script_tags": scripts, "visible_text_chars": visible, "spa_markers": markers,
        "noscript": bool(doc.css("noscript")),
        "verdict": ("likely required: little visible text and an application shell" if visible < 400 and (markers or scripts > 5)
                    else "embedded data present — look for the JSON it carries before thinking of a browser" if markers
                    else "not required for what is visible"),
    }
    return report


def _json_map(node, path: str = "$", out: list | None = None, depth: int = 0) -> list:
    """Array and scalar paths, as the runtime's JSON path subset spells them."""
    out = [] if out is None else out
    if depth > 6 or len(out) > 120:
        return out
    if isinstance(node, dict):
        for key, value in list(node.items())[:60]:
            step = f".{key}" if re.fullmatch(r"[^\W\d][\w-]*", str(key)) else f"['{key}']"
            _json_map(value, path + step, out, depth + 1)
    elif isinstance(node, list):
        out.append({"path": path + "[*]", "kind": "array", "length": len(node)})
        if node:
            _json_map(node[0], path + "[0]", out, depth + 1)
    else:
        out.append({"path": path, "kind": type(node).__name__, "sample": str(node)[:80]})
    return out


def evaluate(body: bytes, url: str, is_json: bool, selectors: list[tuple[str, str]], limit: int) -> list[dict]:
    """Selectors run through the runtime's own extraction (`_raw_for`), on the runtime's own parse."""
    document = json.loads(body) if is_json else parse_document(body.decode("utf-8", "replace"), url=url)
    results = []
    for kind, expression in selectors:
        try:
            spec = FieldSpec.model_validate({kind: expression})
            values = _raw_for(document, spec)
            results.append({"kind": kind, "selector": expression, "matches": len(values),
                            "values": [str(v)[:200] for v in values[:limit]]})
        except (ValueError, jsonpath.JsonPathError) as exc:
            results.append({"kind": kind, "selector": expression, "error": str(exc)})
    return results


# -- report ------------------------------------------------------------------------------------------------

def _print(report: dict) -> None:
    def show(key, value, indent=0):
        pad = "  " * indent
        if isinstance(value, dict):
            if not value:
                return
            print(f"{pad}{key}:")
            for k, v in value.items():
                show(k, v, indent + 1)
        elif isinstance(value, list):
            if not value:
                return
            print(f"{pad}{key}: ({len(value)})")
            for v in value:
                print(f"{pad}  - {json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v}")
        elif value not in (None, ""):
            print(f"{pad}{key}: {value}")
    for key, value in report.items():
        show(key, value)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="inspect-source", description=__doc__.splitlines()[0])
    parser.add_argument("url", nargs="?", help="the page or endpoint to inspect")
    parser.add_argument("--from", dest="from_file", type=Path, help="inspect a saved response instead (offline)")
    parser.add_argument("--url", dest="as_url", help="with --from: the URL the saved response came from")
    parser.add_argument("--css", action="append", default=[], help="evaluate a CSS selector (repeatable)")
    parser.add_argument("--xpath", action="append", default=[], help="evaluate an XPath expression (repeatable)")
    parser.add_argument("--json", dest="json_paths", action="append", default=[], help="evaluate a JSON path (repeatable)")
    parser.add_argument("--allow-host", action="append", default=[], help="also allow redirects to this host")
    parser.add_argument("--save", type=Path, help="write the response body here (a fixture draft to trim)")
    parser.add_argument("--limit", type=int, default=5, help="values shown per selector (default 5)")
    parser.add_argument("--max-bytes", type=int, default=8 * 1024 * 1024)
    parser.add_argument("--ignore-robots", action="store_true",
                        help="report robots.txt but fetch anyway (for pages a person may read; never for an adapter path)")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)

    if args.from_file:
        url = args.as_url or args.url or "https://example.invalid/"
        body = args.from_file.read_bytes()
        meta = {"url": url, "final_url": url, "status": None, "redirects": [], "headers": {}, "source": str(args.from_file)}
        robots = {"note": "offline: not checked"}
    elif args.url:
        url = args.url
        try:
            meta, robots = asyncio.run(fetch_with_robots(url, args.allow_host, args.max_bytes, args.ignore_robots))
        except DisallowedTarget as exc:
            print(f"refused by the egress policy: {exc}\n(a redirect to another host? rerun with --allow-host HOST"
                  " if that host belongs to the source)", file=sys.stderr)
            return 1
        except (FetchFailed, BlockedDestination, TooManyRedirects, TimeoutError) as exc:
            print(f"fetch failed: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 1
        body = meta.pop("body")
    else:
        parser.error("give a URL, or --from FILE --url URL")

    headers = {k.lower(): v for k, v in meta.get("headers", {}).items()}
    content_type = headers.get("content-type", "")
    stripped = body.lstrip()[:1]
    is_json = "json" in content_type or (not content_type and stripped in (b"{", b"["))
    report: dict = {
        "fetch": {"url": meta["url"], "final_url": meta["final_url"], "status": meta["status"],
                  "redirect_chain": meta.get("redirects"), "content_type": content_type, "bytes": len(body),
                  "from_cache": meta.get("from_cache"), "fetched_at": meta.get("fetched_at"),
                  "user_agent": USER_AGENT if args.url and not args.from_file else None},
        "caching_and_limits": {k: headers[k] for k in ("cache-control", "etag", "last-modified", "expires", "age",
                                                       "retry-after", "x-ratelimit-limit", "x-ratelimit-remaining",
                                                       "ratelimit", "ratelimit-policy", "content-language", "vary")
                               if k in headers},
        "robots": robots,
    }
    base_host = urlsplit(meta["final_url"]).hostname or ""
    if is_json:
        try:
            report["json_map"] = _json_map(json.loads(body))
        except ValueError as exc:
            report["json_map"] = [f"not valid JSON: {exc}"]
    else:
        report["markup"] = analyse_markup(body, meta["final_url"], base_host)
    selectors = [("css", s) for s in args.css] + [("xpath", s) for s in args.xpath] + [("json", s) for s in args.json_paths]
    if selectors:
        report["selectors"] = evaluate(body, meta["final_url"], is_json, selectors, args.limit)
    if args.save:
        args.save.write_bytes(body)
        report["saved"] = f"{args.save} ({len(body)} bytes) — trim it to the minimum before it becomes a fixture"
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        _print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
