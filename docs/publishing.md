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
./tools/publish-registry --signing-key ~/.config/oneshelf-registry/official-2026.pem --key-id official-2026
```

This builds every adapter with OneShelf's canonical builder, runs the packaged tests, refuses to change a
published id+version, signs Official and Verified Community entries, verifies the result against
`registry-trust/trusted-keys.txt` with signatures required, and stages the result in a worktree of the
`registry` branch (`.registry-worktree/`). It shows what changed and commits nothing. Then:

```bash
git -C .registry-worktree commit -m "registry: <what changed>"
git -C .registry-worktree push origin registry          # never --force
```

The signing key must live outside every Git work tree; the tool refuses it otherwise.

### Before the project key exists

`./tools/publish-registry --unsigned-preview` publishes Official and Verified Community entries unsigned.
Every OneShelf installation then treats them as Community ("not verified"). This is the current state.

## Setting up the project signing key (owner, once)

```bash
umask 077
mkdir -p ~/.config/oneshelf-registry
openssl genpkey -algorithm ed25519 -out ~/.config/oneshelf-registry/official-2026.pem
# back it up offline now — it is the only copy
./tools/public-key --signing-key ~/.config/oneshelf-registry/official-2026.pem --key-id official-2026
```

Put the printed **public** line in `registry-trust/trusted-keys.txt` (and in OneShelf's
`ONESHELF_REGISTRY_TRUSTED_KEYS` default), commit it, then publish with the key as above.

**Rotation:** create a new key, list both public keys, publish signed with the new one, update OneShelf's
trusted keys, and remove the old key once installations have moved.

**CI signing (not enabled).** Signing could later move to a GitHub Actions job behind a protected
Environment with required manual approval, triggered only from `main`, never from pull requests. The key
is not in GitHub and will not be put there without the owner's explicit decision.

## Immutability

A published id+version never changes content: `check-all` compares against the published Registry and
fails on it. "Content" means the files inside the package. The zip container around them is OneShelf's
canonical builder's business: in September 2026 it stopped compressing, because zlib and zlib-ng produce
different bytes and packages were only reproducible on one platform. Every package was re-published once
under its existing version with byte-identical files and a new sha256 — the one documented exception to
byte-level immutability, and one the check itself verifies (same files, or it fails). Registry entries keep only each adapter's current version; installations keep their own
previous versions for rollback.

## Repository settings (recommended; configured by the owner)

`CODEOWNERS` requests review but does not enforce it on its own. Recommended rulesets:

- `main`: require a pull request, require review from Code Owners, require the **Validate adapters** check,
  block force pushes and deletion.
- `registry`: restrict pushes to the maintainer, block force pushes and deletion.
- Actions: "Require approval for all outside collaborators" for fork PR workflows; default workflow
  permissions read-only.
