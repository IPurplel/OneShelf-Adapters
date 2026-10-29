"""The rights model (docs/rights-model.md): every adapter's rights.yaml is complete, consistent with what the
adapter declares, and backed by packaged tests that prove ineligible items are not offered.

OneShelf Core does not read rights.yaml; this repository does, so a rights claim cannot drift away from the
capabilities and recipes it describes without a failing test.
"""
import datetime
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]

# Adapters that predate the rights model. Their rights are recorded in docs/source-matrix.md and their
# recipes gate eligibility, but they carry no rights.yaml yet. Nothing may be added to this list: every
# new adapter ships a rights.yaml.
PREDATING = {
    "oneshelf.3asq", "oneshelf.arxiv", "oneshelf.gutenberg", "oneshelf.hindawi", "oneshelf.mangadex",
    "oneshelf.standard-ebooks", "oneshelf.tapas", "oneshelf.webtoon",
    "oneshelf.anu-press", "oneshelf.arabic-collections-online", "oneshelf.athabasca-university-press",
    "oneshelf.bccampus-open-textbooks", "oneshelf.books-by-habiba", "oneshelf.comic-book-plus",
    "oneshelf.digital-bodleian", "oneshelf.english-storybooks-arabic", "oneshelf.fsu-arabic-short-stories",
    "oneshelf.gallica", "oneshelf.intechopen", "oneshelf.lever-press", "oneshelf.libretexts",
    "oneshelf.manchester-arabic-manuscripts", "oneshelf.mdz-arabic-manuscripts", "oneshelf.oapen",
    "oneshelf.openstax", "oneshelf.peppercarrot", "oneshelf.storybooks-canada-arabic", "oneshelf.ucl-press",
    "oneshelf.wellcome-collection", "oneshelf.wikimedia-commons",
}

ACCESS_SCOPE = {"whole_source", "collection", "per_item"}
ACCESS_TYPE = {"public_domain", "open_license", "open_access_publisher", "free_to_read", "mixed"}
GRANULARITY = {"source", "collection", "item"}
PERMISSION = {"allowed", "allowed_with_conditions", "not_allowed", "unknown"}
VISIBILITY = {"all_listed_items", "eligible_items_only"}
LOCAL_COPY = {"allowed", "eligible_items_only", "not_allowed", "reader_cache_only"}
COPYING = {"reader", "downloads"}
REQUIRED = {"schema", "access_scope", "access_type", "rights_granularity", "license", "commercial_use",
            "redistribution", "derivatives", "attribution", "visibility", "local_copy", "enforcement",
            "evidence", "last_verified"}


def adapter_dirs() -> list[Path]:
    return sorted(p for p in (ROOT / "adapters").glob("*/*") if (p / "manifest.yaml").is_file())


def with_rights() -> list[Path]:
    return [p for p in adapter_dirs() if (p / "rights.yaml").is_file()]


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_every_adapter_after_the_rights_model_has_a_rights_file():
    missing = [p.name for p in adapter_dirs() if p.name not in PREDATING and not (p / "rights.yaml").is_file()]
    assert not missing, f"new adapters need rights.yaml (docs/rights-model.md): {missing}"


def test_the_predating_list_only_shrinks():
    existing = {p.name for p in adapter_dirs()}
    assert PREDATING <= existing, f"remove deleted adapters from PREDATING: {sorted(PREDATING - existing)}"


@pytest.mark.parametrize("adapter", with_rights(), ids=lambda p: p.name)
def test_rights_file_is_complete_and_consistent(adapter):
    rights, manifest = load(adapter / "rights.yaml"), load(adapter / "manifest.yaml")
    tests = load(adapter / "tests" / "tests.yaml")["cases"]
    problems: list[str] = []
    missing = REQUIRED - set(rights)
    assert not missing, f"missing keys: {sorted(missing)}"
    unknown = set(rights) - REQUIRED
    assert not unknown, f"unknown keys: {sorted(unknown)}"

    def choice(key, allowed):
        if rights[key] not in allowed:
            problems.append(f"{key}: {rights[key]!r} is not one of {sorted(allowed)}")

    assert rights["schema"] == "oneshelf.rights/1"
    choice("access_scope", ACCESS_SCOPE), choice("access_type", ACCESS_TYPE)
    choice("rights_granularity", GRANULARITY), choice("visibility", VISIBILITY), choice("local_copy", LOCAL_COPY)
    for key in ("commercial_use", "redistribution", "derivatives"):
        choice(key, PERMISSION)

    licence = rights["license"] or {}
    if rights["access_type"] == "open_license" and not (licence.get("id") and str(licence.get("url", "")).startswith("https://")):
        problems.append("an open_license source names its licence id and https url")
    attribution = rights["attribution"] or {}
    if not isinstance(attribution.get("required"), bool):
        problems.append("attribution.required must be true or false")
    if attribution.get("required") and not attribution.get("text"):
        problems.append("attribution required but no attribution text")

    capabilities = set(manifest.get("capabilities", []))
    copies = capabilities & COPYING
    cache_only = rights["local_copy"] == "reader_cache_only"
    if manifest.get("native_profile") is not None and not cache_only:
        problems.append("native profiles must declare reader_cache_only, never permanent copying")
    if cache_only:
        network = manifest.get("network") or {}
        source = load(adapter / "source.yaml")
        reviewed_native = (
            manifest.get("id") == "oneshelf.noorbook" and manifest.get("native_profile") == "noorbook"
            and str(manifest.get("api")) == "1.3" and capabilities == {"work", "catalog", "reader"}
            and set((manifest.get("browser") or {}).get("capabilities", [])) == {"reader"}
            and network.get("domains") == ["www.noor-book.com"] and not network.get("cdn_domains")
            and not network.get("allow_http") and manifest.get("auth") is None
            and source.get("base_url") == "https://www.noor-book.com"
            and not any(p.suffix in {".yaml", ".yml"} for p in (adapter / "recipes").rglob("*"))
        )
        if not reviewed_native or rights["access_type"] != "free_to_read" or any(licence.values()):
            problems.append("reader_cache_only requires the exact reviewed native Noor contract and no licence claim")
        else:
            # This reader has app-managed cached images, not the recipe reader's permanent CBZ path.
            copies.discard("reader")
    # Visible is not downloadable: a source that only grants reading on its own site gets no copying capability.
    if rights["access_type"] == "free_to_read" and rights["local_copy"] not in {"not_allowed", "reader_cache_only"}:
        problems.append("free_to_read grants no local copy")
    if rights["local_copy"] == "not_allowed" and copies:
        problems.append(f"local_copy is not_allowed but the adapter declares {sorted(copies)}")
    # Rights decided per item or per collection must be enforced per item by the adapter.
    mixed = rights["access_type"] == "mixed" or rights["rights_granularity"] != "source"
    if mixed and copies and rights["local_copy"] != "eligible_items_only":
        problems.append("rights vary within the source, so local_copy must be eligible_items_only")
    if mixed and rights["visibility"] == "all_listed_items" and copies and rights["local_copy"] == "allowed":
        problems.append("items are listed regardless of rights, so copying cannot be unconditional")

    enforcement = rights["enforcement"] or {}
    if not enforcement.get("summary"):
        problems.append("enforcement.summary says how ineligible items are kept out")
    exclusion = enforcement.get("exclusion_tests") or []
    if rights["local_copy"] == "eligible_items_only" and not exclusion:
        problems.append("eligible_items_only needs exclusion_tests")
    for index in exclusion:
        if not (isinstance(index, int) and 0 <= index < len(tests)):
            problems.append(f"exclusion test {index!r} is not a case in tests.yaml")
            continue
        case = tests[index]
        first = (case.get("expect") or {}).get("first") or {}
        # "first: {url: null}" (or another key null) asserts the list is empty — the item is not offered.
        if case["capability"] not in COPYING | {"search", "catalog"} or not any(v is None for v in first.values()):
            problems.append(f"exclusion test {index} must expect an empty {sorted(COPYING)}/search/catalog result")

    evidence = rights["evidence"] or []
    if not evidence:
        problems.append("at least one evidence entry")
    for item in evidence:
        if not (item.get("claim") and str(item.get("url", "")).startswith("https://")):
            problems.append(f"evidence needs a claim and an https url: {item}")
    verified = rights["last_verified"]
    if not isinstance(verified, datetime.date) or verified > datetime.date.today():
        problems.append("last_verified is an ISO date, not in the future")
    assert not problems, "\n".join(problems)


def scaffold(tmp_path) -> Path:
    """A fresh adapter from ./tools/new-adapter, in a copy of the repository layout."""
    import shutil
    import subprocess
    import sys
    copy = tmp_path / "repo"
    for part in ("tools", "templates"):
        shutil.copytree(ROOT / part, copy / part)
    (copy / "adapters" / "community").mkdir(parents=True)
    subprocess.run([sys.executable, str(copy / "tools" / "new-adapter"), "example-site", "--domain", "example-site.org"],
                   check=True, capture_output=True)
    return copy / "adapters" / "community" / "oneshelf.example-site"


def test_a_new_adapter_starts_with_a_valid_read_only_rights_file(tmp_path):
    created = scaffold(tmp_path)
    assert load(created / "rights.yaml")["local_copy"] == "not_allowed"
    test_rights_file_is_complete_and_consistent(created)


def test_the_consistency_rules_reject_a_copying_adapter_for_a_read_only_source(tmp_path):
    """Declaring reader while rights.yaml still says free_to_read fails — the rule is not vacuous."""
    created = scaffold(tmp_path)
    manifest = created / "manifest.yaml"
    manifest.write_text(manifest.read_text(encoding="utf-8").replace("capabilities: [search]",
                                                                       "capabilities: [search, reader]"), encoding="utf-8")
    with pytest.raises(AssertionError, match="not_allowed but the adapter declares"):
        test_rights_file_is_complete_and_consistent(created)


def test_the_consistency_rules_require_exclusion_tests_for_per_item_rights(tmp_path):
    created = scaffold(tmp_path)
    rights = load(created / "rights.yaml")
    rights.update(access_type="mixed", rights_granularity="item", local_copy="eligible_items_only",
                  license={"id": None, "url": None})
    (created / "rights.yaml").write_text(yaml.safe_dump(rights), encoding="utf-8")
    manifest = created / "manifest.yaml"
    manifest.write_text(manifest.read_text(encoding="utf-8").replace("capabilities: [search]",
                                                                       "capabilities: [search, downloads]"), encoding="utf-8")
    with pytest.raises(AssertionError, match="eligible_items_only needs exclusion_tests"):
        test_rights_file_is_complete_and_consistent(created)


@pytest.mark.parametrize("adapter", adapter_dirs(), ids=lambda p: p.name)
def test_no_list_case_passes_whatever_the_recipe_returns(adapter):
    """A list case must expect items, specific values, or an empty result (first: {key: null}).

    `min_items: 0` alone passes any output — an exclusion test written that way proves nothing.
    """
    vacuous = []
    for index, case in enumerate(load(adapter / "tests" / "tests.yaml")["cases"]):
        if case["capability"] in ("work", "health", "check_session"):
            continue
        expect = case.get("expect") or {}
        if not expect.get("min_items") and not (expect.get("first") or {}):
            vacuous.append(index)
    assert not vacuous, f"cases {vacuous} assert nothing about the result; add first: {{url: null}} (or the key) for an empty one"


@pytest.mark.parametrize("case", [
    "valid", "recipe", "recipe-yml", "wrong-id", "missing-profile", "wrong-profile", "old-api",
    "downloads", "extra-capability", "missing-capability", "no-browser", "extra-domain",
    "cdn", "http", "auth", "wrong-origin", "open-license", "native-permanent", "native-eligible",
])
def test_reader_cache_only_is_bound_to_the_reviewed_native_contract(tmp_path, case):
    import shutil
    created = tmp_path / "noor"
    shutil.copytree(ROOT / "adapters" / "official" / "oneshelf.noorbook", created)
    manifest = load(created / "manifest.yaml")
    source = load(created / "source.yaml")
    rights = {
        "schema": "oneshelf.rights/1", "access_scope": "per_item", "access_type": "free_to_read",
        "rights_granularity": "item", "license": {"id": None, "url": None},
        "commercial_use": "unknown", "redistribution": "unknown", "derivatives": "unknown",
        "attribution": {"required": True, "text": "Test source"}, "visibility": "all_listed_items",
        "local_copy": "reader_cache_only", "enforcement": {"summary": "Fixture cache only", "exclusion_tests": []},
        "evidence": [{"claim": "Fixture only", "url": "https://example.org/"}],
        "last_verified": datetime.date(2026, 10, 29),
    }
    if case in {"recipe", "recipe-yml"}:
        (created / "recipes").mkdir()
        filename = "reader.yml" if case == "recipe-yml" else "reader.yaml"
        (created / "recipes" / filename).write_text("capability: reader\n")
    elif case == "wrong-id": manifest["id"] = "oneshelf.other"
    elif case == "missing-profile": manifest.pop("native_profile")
    elif case == "wrong-profile": manifest["native_profile"] = "other"
    elif case == "old-api": manifest["api"] = "1.2"
    elif case == "downloads": manifest["capabilities"].append("downloads")
    elif case == "extra-capability": manifest["capabilities"].append("search")
    elif case == "missing-capability": manifest["capabilities"].remove("catalog")
    elif case == "no-browser": manifest["browser"] = {"capabilities": []}
    elif case == "extra-domain": manifest["network"]["domains"].append("example.org")
    elif case == "cdn": manifest["network"]["cdn_domains"] = ["example.org"]
    elif case == "http": manifest["network"]["allow_http"] = True
    elif case == "auth": manifest["auth"] = {"mode": "browser"}
    elif case == "wrong-origin": source["base_url"] = "https://example.org"
    elif case == "open-license":
        rights.update(access_type="open_license", license={"id": "CC0-1.0", "url": "https://creativecommons.org/publicdomain/zero/1.0/"})
    elif case in {"native-permanent", "native-eligible"}:
        rights.update(access_type="public_domain", rights_granularity="source", local_copy="allowed")
        if case == "native-eligible":
            rights["local_copy"] = "eligible_items_only"
            rights["enforcement"]["exclusion_tests"] = [0]
            (created / "tests" / "tests.yaml").write_text(yaml.safe_dump({"cases": [
                {"capability": "catalog", "expect": {"first": {"url": None}}}
            ]}), encoding="utf-8")
    for name, data in [("manifest.yaml", manifest), ("source.yaml", source), ("rights.yaml", rights)]:
        (created / name).write_text(yaml.safe_dump(data), encoding="utf-8")
    if case == "valid":
        test_rights_file_is_complete_and_consistent(created)
    else:
        with pytest.raises(AssertionError):
            test_rights_file_is_complete_and_consistent(created)
