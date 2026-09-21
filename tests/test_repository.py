"""Repository policy: the rules that keep this repository safe to accept contributions into.

Adapter validation itself is OneShelf Core's (`oneshelf.plugins.adapter_repo`); these check what is
specific to this repository — its structure, its review controls, its workflows, and that no secret or
key material is tracked.
"""
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
EIGHT = ["oneshelf.3asq", "oneshelf.arxiv", "oneshelf.gutenberg", "oneshelf.hindawi", "oneshelf.mangadex",
         "oneshelf.standard-ebooks", "oneshelf.tapas", "oneshelf.webtoon"]
TIERS = ["official", "verified-community", "community"]
KEY_MARKER = re.compile(rb"-----BEGIN [A-Z ]*PRIVATE" + rb" KEY-----")


def tracked() -> list[str]:
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z"], capture_output=True, check=True).stdout
    return [n for n in out.decode().split("\0") if n]


def adapters_in(tier: str) -> list[str]:
    return sorted(p.name for p in (ROOT / "adapters" / tier).iterdir() if p.is_dir())


def test_the_three_tiers_exist():
    assert all((ROOT / "adapters" / tier).is_dir() for tier in TIERS)
    assert sorted(p.name for p in (ROOT / "adapters").iterdir() if p.is_dir()) == sorted(TIERS)


def test_the_eight_official_adapters_exist_exactly_once():
    assert set(EIGHT) <= set(adapters_in("official"))
    everywhere = [a for tier in TIERS for a in adapters_in(tier)]
    for plugin in EIGHT:
        assert everywhere.count(plugin) == 1, plugin


def test_the_tooling_pin_is_a_full_commit():
    assert re.fullmatch(r"[0-9a-f]{40}\n?", (ROOT / "tooling" / "oneshelf-core-ref.txt").read_text())


@pytest.mark.parametrize("path", [".github/workflows/", "tools/", "tooling/", "registry-trust/",
                                  "adapters/official/", "adapters/verified-community/", "SECURITY.md",
                                  "docs/review-policy.md", ".github/CODEOWNERS"])
def test_security_sensitive_paths_need_the_maintainer(path):
    owners = (ROOT / ".github" / "CODEOWNERS").read_text(encoding="utf-8").splitlines()
    rules = [l.split() for l in owners if l.strip() and not l.startswith("#")]
    assert any(r[0].lstrip("/") == path and "@IPurplel" in r[1:] for r in rules), path


def workflows():
    return sorted((ROOT / ".github" / "workflows").glob("*.yml"))


def test_no_workflow_runs_contributor_code_with_privileges():
    for wf in workflows():
        text = wf.read_text(encoding="utf-8")
        assert "pull_request_target" not in text, wf.name
        assert re.search(r"(?m)^permissions:\s*\n\s+contents:\s*read\s*$", text), f"{wf.name}: default must be read-only"
        assert "write" not in re.findall(r"(?m)^\s+\w[\w-]*:\s*(\w+)\s*$", text.split("jobs:")[0]), wf.name


def test_the_pull_request_workflow_uses_no_secrets():
    text = (ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
    assert "secrets." not in text
    assert "persist-credentials: false" in text


def test_the_pull_request_workflow_refuses_a_core_pin_that_is_not_on_oneshelf_main():
    text = (ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
    assert "merge-base --is-ancestor" in text
    assert text.index("merge-base --is-ancestor") < text.index("./tools/bootstrap")


def test_no_workflow_signs_or_publishes():
    for wf in workflows():
        text = wf.read_text(encoding="utf-8")
        assert "--signing-key" not in text and "publish-registry" not in text, wf.name


def test_no_tracked_file_holds_private_key_material():
    offenders = [n for n in tracked() if (ROOT / n).is_file() and KEY_MARKER.search((ROOT / n).read_bytes())]
    assert offenders == []


def test_no_key_or_env_file_is_tracked():
    assert [n for n in tracked() if n.endswith((".pem", ".key", ".p8")) or Path(n).name.startswith(".env")] == []


def test_the_trusted_keys_file_holds_only_public_key_lines():
    for line in (ROOT / "registry-trust" / "trusted-keys.txt").read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            assert re.fullmatch(r"[A-Za-z0-9._-]+:[A-Za-z0-9+/]{43}=", line.strip()), line


@pytest.mark.parametrize("path", ["x.pem", "keys/owner.key", "a.p8", ".env", ".registry-worktree/index.json"])
def test_git_ignores_keys_and_local_registry_work(path):
    assert subprocess.run(["git", "-C", str(ROOT), "check-ignore", "-q", path]).returncode == 0


def test_the_template_is_not_itself_an_adapter():
    assert not any("{{" in p.name for tier in TIERS for p in (ROOT / "adapters" / tier).iterdir())


def new_adapter(tmp_path, *args):
    """Run tools/new-adapter against a copy of the repository layout."""
    import shutil
    copy = tmp_path / "repo"
    for part in ("tools", "templates", "adapters"):
        shutil.copytree(ROOT / part, copy / part)
    result = subprocess.run([sys.executable, str(copy / "tools" / "new-adapter"), *args], capture_output=True, text=True)
    return copy, result


def test_new_adapter_creates_a_community_adapter_that_passes_the_checks(tmp_path):
    copy, result = new_adapter(tmp_path, "example-site", "--domain", "example-site.org")
    assert result.returncode == 0, result.stderr
    created = copy / "adapters" / "community" / "oneshelf.example-site"
    assert "id: oneshelf.example-site" in (created / "manifest.yaml").read_text(encoding="utf-8")
    from oneshelf.plugins import adapter_repo
    assert adapter_repo.main(["check", "--root", str(copy), "oneshelf.example-site"]) == 0


@pytest.mark.parametrize("args", [["Bad_Slug"], ["ok", "--domain", "192.168.1.10"], ["ok", "--domain", "localhost"],
                                  ["tapas"]])
def test_new_adapter_refuses_bad_input_and_existing_ids(tmp_path, args):
    if args == ["tapas"]:
        copy, result = new_adapter(tmp_path, "tapas")          # oneshelf.tapas already exists in official/
    else:
        copy, result = new_adapter(tmp_path, *args)
    assert result.returncode != 0


def test_new_adapter_never_creates_code():
    for path in (ROOT / "templates").rglob("*"):
        if path.is_file():
            assert path.suffix in {".yaml", ".html", ".md", ".json"}, path
