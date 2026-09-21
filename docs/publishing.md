# Publishing the Registry

The published Registry lives on the **`registry` branch** — generated artifacts only:

```
index.json              # oneshelf.registry/1
packages/<id>-<version>.osp
```

OneShelf reads it from `https://raw.githubusercontent.com/IPurplel/OneShelf-Adapters/registry/index.json`. `main` holds sources; nothing on `main` or in a Pull Request is ever
served to installations.

## Publish (maintainer, on their own machine)

```bash
./tools/publish-registry
```

This builds every adapter with OneShelf's canonical builder, runs the packaged tests, refuses to change a
published id+version, verifies the result with OneShelf's Registry parser, and stages it in a worktree of the
`registry` branch (`.registry-worktree/`). It shows what changed and commits nothing. Then:

```bash
git -C .registry-worktree commit -m "registry: <what changed>"
git -C .registry-worktree push origin registry          # never --force
```

Signatures are **optional** (owner decision, 2026-09-21): OneShelf trusts this Registry's tiers because it is
its configured first-party Registry. Nothing in CI signs or publishes.

## Optional: signing with a project key

Signing adds evidence that does not depend on GitHub: installations that trust the public key show
*Official · Signed*. If the owner chooses to use it:

```bash
umask 077
mkdir -p ~/.config/oneshelf-registry
openssl genpkey -algorithm ed25519 -out ~/.config/oneshelf-registry/official-2026.pem   # back it up offline
./tools/public-key --signing-key ~/.config/oneshelf-registry/official-2026.pem --key-id official-2026
./tools/publish-registry --signing-key ~/.config/oneshelf-registry/official-2026.pem --key-id official-2026
```

Put the printed **public** line in `registry-trust/trusted-keys.txt` (and, if wanted, in OneShelf's
`ONESHELF_REGISTRY_TRUSTED_KEYS`). The key must live outside every Git work tree; the tool refuses it
otherwise. With a key, publication also verifies every signed entry against `registry-trust/trusted-keys.txt`.

**Rotation:** create a new key, list both public keys, publish signed with the new one, and remove the old key
once installations have moved.

**CI signing (not enabled).** Signing could later move to a GitHub Actions job behind a protected Environment
with required manual approval, triggered only from `main`, never from pull requests. No key is in GitHub.

## Immutability

A published id+version never changes content: `check-all` compares against the published Registry and
fails on it. "Content" means the files inside the package. The zip container around them is OneShelf's
canonical builder's business: in September 2026 it stopped compressing, because zlib and zlib-ng produce
different bytes and packages were only reproducible on one platform. Every package was re-published once
under its existing version with byte-identical files and a new sha256 — the one documented exception to
byte-level immutability, and one the check itself verifies (same files, or it fails). Registry entries keep only each adapter's current version; installations keep their own
previous versions for rollback.

## Repository settings

**Configured** (2026-09-21):

- ruleset *Protect main and registry*: no force pushes and no deletion on `main` and `registry`;
- default workflow token is read-only, and workflows cannot approve pull requests;
- secret scanning with push protection.

**Recommended, for the owner to enable** (they change how the maintainer pushes, so they are not set
automatically): on `main`, require a pull request, require review from Code Owners, and require the
**Validate adapters** check; keep "Require approval for all outside collaborators" for workflows from forks.
`CODEOWNERS` requests reviews but does not by itself enforce them.
