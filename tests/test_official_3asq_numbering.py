"""3asq numbering: lettered units are not chapter 0 (OneShelf audit 2026-10-19, BE-014 / I-104).

Master §4.4: a derived number is presentation only and "may be used only when ordering/pattern evidence is
reliable". 3asq lists Berserk's prologue arcs as "0A" … "0P"; reading their leading digit made sixteen different
units all "0". They now carry no number, and real chapter numbers are untouched.
"""
import asyncio
import zipfile
from pathlib import Path

from oneshelf.plugins.package import load_package
from oneshelf.plugins.runtime import FixtureFetcher, RecipeRuntime

ADAPTER = Path(__file__).resolve().parents[1] / "adapters" / "official" / "oneshelf.3asq"


def package(tmp_path):
    osp = tmp_path / "3asq.osp"
    with zipfile.ZipFile(osp, "w") as archive:
        for path in sorted(ADAPTER.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(ADAPTER).as_posix())
    return load_package(osp)


def catalog(tmp_path, listing_key):
    pkg = package(tmp_path)
    case = next(c for c in pkg.tests.cases if c.capability == "catalog" and c.inputs.get("listing_key") == listing_key)
    return asyncio.run(RecipeRuntime(pkg, FixtureFetcher(pkg, case.fixtures)).run("catalog", dict(case.inputs)))


def test_lettered_units_carry_no_number(tmp_path):
    result = catalog(tmp_path, "berserk")
    assert result.complete and len(result.entries) == 404
    lettered = {f"0{letter}" for letter in "abcdefghijklmnop"}       # 0A … 0P: the prologue arcs
    assert {u.unit_key for u in result.entries if u.number is None} == lettered
    assert all(u.number.replace(".", "", 1).isdigit() for u in result.entries if u.unit_key not in lettered)


def test_ordinary_chapter_numbers_are_unchanged(tmp_path):
    result = catalog(tmp_path, "baki-dou")
    assert result.entries[0].unit_key == "1" and result.entries[0].number == "1"
