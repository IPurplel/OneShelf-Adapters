"""Adapter labels: every name reads `Source · Category · LANG`, so the Registry screen says what each one is."""
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "lib"))

import adapter_labels  # noqa: E402


def test_every_adapter_name_follows_the_label_rule():
    labels, problems = adapter_labels.load(ROOT)
    assert problems == []
    assert len(labels) == len(list(ROOT.glob("adapters/*/*/manifest.yaml")))


def test_the_catalogue_is_current():
    labels, _ = adapter_labels.load(ROOT)
    assert (ROOT / "docs" / "adapter-catalogue.md").read_text(encoding="utf-8") == adapter_labels.catalogue(labels), \
        "run ./tools/adapter-catalogue"


@pytest.mark.parametrize("name, expected", [
    ("3asq (Al-Aasheq) · Manga · AR", ("3asq (Al-Aasheq)", "Manga", ("AR",))),
    ("مجلة آداب الكوفة (University of Kufa, Iraq) · Journal · AR",
     ("مجلة آداب الكوفة (University of Kufa, Iraq)", "Journal", ("AR",))),
    ("Translation Researches (ATU) · Journal · FA/AR", ("Translation Researches (ATU)", "Journal", ("FA", "AR"))),
    ("OAPEN Library · Academic books · Multi", ("OAPEN Library", "Academic books", ("Multi",))),
])
def test_parse_reads_the_three_parts(name, expected):
    assert adapter_labels.parse(name) == expected


@pytest.mark.parametrize("name", [
    "3asq (Al-Aasheq)",                      # no label
    "3asq - manga - ar",                     # wrong separator
    "3asq · Mangas · AR",                    # not a category
    "3asq · Manga · ar",                     # lower-case language
    "3asq · Manga · Arabic",                 # a word, not a code
    " 3asq · Manga · AR",                    # stray space
    "3asq · Manga · AR · extra",             # four parts
])
def test_parse_refuses_names_that_break_the_rule(name):
    with pytest.raises(ValueError):
        adapter_labels.parse(name)


@pytest.mark.parametrize("defaults, ok", [
    ({"language": "ar", "content_type": "manga"}, True),
    ({"language": "en"}, False),                           # the label says AR
    ({"content_type": "book"}, False),                     # Manga is not a book
    ({}, True),
])
def test_the_label_agrees_with_the_manifest_defaults(defaults, ok):
    manifest = {"name": "3asq (Al-Aasheq) · Manga · AR", "defaults": defaults}
    assert (adapter_labels.problems_of(manifest) == []) is ok


def test_egyptian_arabic_is_labelled_arabic_and_multi_accepts_any_language():
    assert adapter_labels.problems_of({"name": "Habiba · Children's books · AR", "defaults": {"language": "arz"}}) == []
    assert adapter_labels.problems_of({"name": "MangaDex · Manga · Multi", "defaults": {"language": "en"}}) == []


def test_a_name_over_the_core_limit_is_refused():
    assert adapter_labels.problems_of({"name": "x" * 70 + " · Journal · AR"})


def new_adapter(tmp_path, *args):
    import shutil
    copy = tmp_path / "repo"
    for part in ("tools", "templates", "adapters"):
        shutil.copytree(ROOT / part, copy / part)
    result = subprocess.run([sys.executable, str(copy / "tools" / "new-adapter"), *args], capture_output=True, text=True)
    return copy, result


def test_new_adapter_writes_a_labelled_name(tmp_path):
    copy, result = new_adapter(tmp_path, "example-manga", "--name", "Example Manga", "--category", "Manga",
                               "--language", "AR", "--domain", "example-manga.org")
    assert result.returncode == 0, result.stderr
    manifest = yaml.safe_load((copy / "adapters/community/oneshelf.example-manga/manifest.yaml").read_text("utf-8"))
    assert manifest["name"] == "Example Manga · Manga · AR"
    assert manifest["defaults"]["language"] == "ar"
    assert adapter_labels.problems_of(manifest) == []
    rights = (copy / "adapters/community/oneshelf.example-manga/rights.yaml").read_text("utf-8")
    assert "Example Manga — https://example-manga.org/" in rights      # the plain name, not the label


@pytest.mark.parametrize("args", [["--category", "Mangas"], ["--language", "arabic"], ["--name", "x" * 70]])
def test_new_adapter_refuses_a_bad_label(tmp_path, args):
    _, result = new_adapter(tmp_path, "example-site", *args)
    assert result.returncode != 0
