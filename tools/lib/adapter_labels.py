#!/usr/bin/env python3
"""Adapter labels: every adapter's display name reads `Source · Category · LANG`.

OneShelf's Registry screen shows an adapter by its manifest `name` alone, so the name carries what a
reader needs to choose one: what the source is, what kind of thing it holds, and in which language.

    3asq (Al-Aasheq) · Manga · AR
    مجلة آداب الكوفة (University of Kufa, Iraq) · Journal · AR
    OAPEN Library · Academic books · Multi

    ./tools/adapter-catalogue           # rewrite docs/adapter-catalogue.md from the manifests
    ./tools/adapter-catalogue --check   # exit 1 if a name breaks the rule or the catalogue is stale

See docs/adapter-labels.md. The rule is checked by tests/test_labels.py.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CATALOGUE = ROOT / "docs" / "adapter-catalogue.md"
SEP = " · "
MAX_NAME = 80  # OneShelf Core's limit on a manifest name

# Category -> the manifest `defaults.content_type` values it may sit with (an unset one always may).
# The order is the catalogue's order.
CATEGORIES: dict[str, set[str]] = {
    "Manga": {"manga"},
    "Webtoons": {"comic", "manhwa", "manhua"},
    "Comics": {"comic"},
    "Books": {"book", "novel"},
    "Children's books": {"book"},
    "Academic books": {"book"},
    "Textbooks": {"book"},
    "Poetry": {"book"},
    "Religious texts": {"book"},
    "Journal": {"paper"},
    "Papers": {"paper"},
    "Reports": {"paper", "book"},
    "Manuscripts": {"book", "other"},
    "Newspapers": {"other"},
    "Digital library": {"book", "other"},
}
MULTI = "Multi"
LANGS = re.compile(r"^[A-Z]{2,3}(?:/[A-Z]{2,3}){0,3}$")
# A manifest language whose label is its macrolanguage: Egyptian Arabic is shown as Arabic.
LABEL_OF = {"arz": "AR"}
LANGUAGE_NAMES = {
    "AR": "Arabic", "BG": "Bulgarian", "DE": "German", "EN": "English", "ES": "Spanish", "FA": "Persian",
    "FR": "French", "HE": "Hebrew", "HU": "Hungarian", "JA": "Japanese", "NO": "Norwegian", "PL": "Polish",
    "RU": "Russian", "SV": "Swedish", MULTI: "Several languages",
}
TIER_LABELS = {"official": "Official", "verified-community": "Verified Community", "community": "Community"}


@dataclass(frozen=True)
class Label:
    id: str
    tier: str
    name: str
    source: str
    category: str
    languages: tuple[str, ...]  # ("Multi",) or ISO 639 codes in upper case


def parse(name: str) -> tuple[str, str, tuple[str, ...]]:
    """Split a name into (source, category, languages), or raise ValueError saying what is wrong."""
    parts = name.split(SEP)
    if len(parts) != 3:
        raise ValueError(f"must read 'Source{SEP}Category{SEP}LANG' (three parts joined by '{SEP}')")
    source, category, langs = parts
    if not source.strip() or source != source.strip():
        raise ValueError("the source part is empty or has stray spaces")
    if category not in CATEGORIES:
        raise ValueError(f"category {category!r} is not one of: {', '.join(CATEGORIES)}")
    if langs != MULTI and not LANGS.match(langs):
        raise ValueError(f"languages {langs!r} must be {MULTI!r} or upper-case codes joined by '/', e.g. AR or FA/AR")
    return source, category, tuple(langs.split("/"))


def problems_of(manifest: dict) -> list[str]:
    name = str(manifest.get("name", ""))
    if len(name) > MAX_NAME:
        return [f"name is {len(name)} characters; OneShelf allows {MAX_NAME}"]
    try:
        _, category, languages = parse(name)
    except ValueError as exc:
        return [f"name {name!r}: {exc}"]
    problems = []
    defaults = manifest.get("defaults") or {}
    content_type = defaults.get("content_type")
    if content_type and content_type not in CATEGORIES[category]:
        problems.append(f"category {category!r} does not fit defaults.content_type {content_type!r}")
    language = defaults.get("language")
    if language and languages != (MULTI,):
        primary = language.split("-")[0]
        expected = LABEL_OF.get(primary, primary.upper())
        if expected not in languages:
            problems.append(f"languages {'/'.join(languages)} leave out defaults.language {language!r} ({expected})")
    return problems


def load(root: Path = ROOT) -> tuple[list[Label], list[str]]:
    import yaml  # imported here so that tools/new-adapter can use the vocabulary without PyYAML

    labels, problems = [], []
    for path in sorted(root.glob("adapters/*/*/manifest.yaml")):
        manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
        found = problems_of(manifest)
        problems += [f"{manifest.get('id', path.parent.name)}: {p}" for p in found]
        if not found:
            source, category, languages = parse(manifest["name"])
            labels.append(Label(manifest["id"], path.parent.parent.name, manifest["name"], source, category,
                                languages))
    return labels, problems


def language_heading(code: str) -> str:
    return f"{LANGUAGE_NAMES.get(code, code)} ({code})" if code != MULTI else LANGUAGE_NAMES[MULTI]


def catalogue(labels: list[Label]) -> str:
    def row(label: Label) -> str:
        source = label.source.replace("|", "\\|")
        return f"| {source} | {'/'.join(label.languages)} | {TIER_LABELS[label.tier]} | `{label.id}` |"

    out = ["# Adapter catalogue", "",
           "<!-- Generated by ./tools/adapter-catalogue from every manifest's name. Do not edit by hand. -->", "",
           f"Every adapter is named `Source{SEP}Category{SEP}LANG`, as the OneShelf Registry screen shows it "
           "([docs/adapter-labels.md](adapter-labels.md)). This page lists them by category, then by language.", "",
           f"**{len(labels)} adapters.**", ""]
    counts = []
    for category in CATEGORIES:
        n = sum(1 for label in labels if label.category == category)
        if n:
            anchor = re.sub(r"[^a-z0-9 -]", "", category.lower()).replace(" ", "-")
            counts.append(f"[{category}](#{anchor}) {n}")
    out += [" · ".join(counts), "", "## By category", ""]
    for category in CATEGORIES:
        members = [label for label in labels if label.category == category]
        if not members:
            continue
        members.sort(key=lambda label: (label.languages[0] == MULTI, label.languages, label.id))
        out += [f"### {category}", "", "| Source | Language | Tier | Adapter id |", "|---|---|---|---|"]
        out += [row(label) for label in members]
        out.append("")
    out += ["## By language", "",
            "An adapter with several languages is listed under each of them.", "",
            "| Language | Adapters | Categories |", "|---|---|---|"]
    codes = sorted({code for label in labels for code in label.languages},
                   key=lambda code: (code == MULTI, code))
    for code in codes:
        members = [label for label in labels if code in label.languages]
        cats = [c for c in CATEGORIES if any(label.category == c for label in members)]
        per = ", ".join(f"{c} {sum(1 for label in members if label.category == c)}" for c in cats)
        out.append(f"| {language_heading(code)} | {len(members)} | {per} |")
    out.append("")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="change nothing; fail if anything is out of order")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    labels, problems = load(args.root)
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        return 1
    target = args.root / "docs" / "adapter-catalogue.md"
    text = catalogue(labels)
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != text:
            print(f"{target.relative_to(args.root)} is out of date: run ./tools/adapter-catalogue", file=sys.stderr)
            return 1
        print(f"{len(labels)} adapter names follow the label rule; the catalogue is current.")
        return 0
    target.write_text(text, encoding="utf-8")
    print(f"Wrote {target.relative_to(args.root)} ({len(labels)} adapters).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
