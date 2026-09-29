"""The development tools: offline behaviour only — nothing here touches the network."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "lib"))

import inspect_source  # noqa: E402

PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><title>كتب</title>
<link rel="canonical" href="https://books.example.org/list/">
<link rel="alternate" type="application/atom+xml" href="/feed.atom">
<meta property="og:image" content="https://cdn.example.org/c/1.jpg"></head><body>
<ul class="results">
 <li data-id="101"><a href="/books/101/">الأول</a> <a href="https://files.example.org/101.epub">EPUB</a></li>
 <li data-id="102"><a href="/books/102/">الثاني</a> <a href="https://files.example.org/102.pdf">PDF</a></li>
 <li data-id="103"><a href="/books/103/">الثالث</a></li>
</ul><a rel="next" href="/list/?page=2">التالي</a>
<img src="https://cdn.example.org/c/101.jpg"></body></html>"""


def report_for(tmp_path, *extra):
    saved = tmp_path / "page.html"
    saved.write_text(PAGE, encoding="utf-8")
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "lib" / "inspect_source.py"), "--from", str(saved),
                          "--url", "https://books.example.org/list/", "--format", "json", *extra],
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def test_inspect_reports_structure_offline(tmp_path):
    markup = report_for(tmp_path)["markup"]
    assert markup["title"] == "كتب" and markup["canonical"] == "https://books.example.org/list/"
    assert markup["language"]["html_lang"] == "ar" and markup["language"]["html_dir"] == "rtl"
    assert markup["file_links"]["epub"]["hosts"] == ["files.example.org"]
    assert markup["file_links"]["pdf"]["count"] == 1
    assert markup["media_hosts"] == {"cdn.example.org": 1}
    assert markup["recurring_link_shapes"][0]["shape"] == "/books/{n}/" and markup["recurring_link_shapes"][0]["count"] == 3
    assert any(p["href"].endswith("?page=2") for p in markup["pagination_candidates"])
    assert markup["data_attributes"] == {"data-id": 3}
    assert any(link["kind"] == "Atom" for link in markup["declared_links"])


def test_inspect_evaluates_selectors_with_the_runtime_semantics(tmp_path):
    selectors = report_for(tmp_path, "--css", "li a[href*='/books/']::attr(href)", "--xpath", "//li/@data-id",
                           "--css", "li")["selectors"]
    assert selectors[0]["matches"] == 3 and selectors[0]["values"][0] == "/books/101/"
    # --css selectors are reported first, then --xpath
    assert selectors[1]["values"][0].startswith("الأول")  # an element yields its text, as in a recipe
    assert selectors[2]["values"] == ["101", "102", "103"]


def test_inspect_refuses_an_invalid_selector_without_crashing(tmp_path):
    assert "error" in report_for(tmp_path, "--css", "li[")["selectors"][0]


def test_url_shapes_name_the_variable_parts():
    assert inspect_source._shape("https://a.org/books/123/", "a.org") == "/books/{n}/"
    assert inspect_source._shape("https://b.org/x/1?page=2", "a.org") == "//b.org/x/{n}?page={v}"


def test_the_inspector_uses_no_scrapling_fetcher():
    """Scrapling's fetchers impersonate browsers; the tool fetches through OneShelf Core's client only."""
    text = (ROOT / "tools" / "lib" / "inspect_source.py").read_text(encoding="utf-8")
    assert "scrapling.fetchers" not in text and "StealthyFetcher" not in text and "auto_match" not in text
    assert "from oneshelf.net.http import" in text


def test_live_check_names_an_unknown_adapter():
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "lib" / "live_check.py"), "oneshelf.does-not-exist"],
                         capture_output=True, text=True)
    assert out.returncode == 2 and "no adapter" in out.stderr


def test_the_inspection_cache_is_ignored():
    assert subprocess.run(["git", "-C", str(ROOT), "check-ignore", "-q", ".inspect-cache/x"]).returncode == 0


def test_inspect_refuses_headers_a_recipe_may_not_send():
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "lib" / "inspect_source.py"), "https://example.org/",
                          "--header", "Cookie:session=1"], capture_output=True, text=True)
    assert out.returncode != 0 and "not allowed" in out.stderr


UCL_LIKE = """User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

User-agent: CCBot
Disallow: /

User-agent: *
Disallow: /*.pdf
Disallow: /?s=
Disallow: /private$
Crawl-delay: 10
"""


def test_robots_follows_rfc_9309():
    robots = inspect_source.Robots(UCL_LIKE)
    assert not robots.can_fetch("OneShelf", "https://x.org/app/uploads/book.pdf")      # "*" wildcard
    assert not robots.can_fetch("OneShelf", "https://x.org/app/uploads/book.pdf.html")  # no "$": a prefix pattern
    assert not robots.can_fetch("OneShelf", "https://x.org/?s=arabic")                # second "*" group merged
    assert robots.can_fetch("OneShelf", "https://x.org/wp-admin/admin-ajax.php")      # longer Allow wins
    assert not robots.can_fetch("OneShelf", "https://x.org/wp-admin/options.php")
    assert not robots.can_fetch("OneShelf", "https://x.org/private") and robots.can_fetch("OneShelf", "https://x.org/private/x")
    assert not robots.can_fetch("CCBot", "https://x.org/books/")                        # a named group replaces "*"
    assert robots.can_fetch("OneShelf", "https://x.org/books/") and robots.crawl_delay("OneShelf") == 10
