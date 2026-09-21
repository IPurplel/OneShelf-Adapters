# OneShelf Adapters

The source adapters for [OneShelf](https://github.com/IPurplel/OneShelf), the self-hosted personal reading library — and the
**OneShelf Source Registry** they are published through.

An adapter teaches OneShelf how to search, list and read one site. It is a small declarative package
(`.osp`): YAML and fixture files that describe requests and how to read the responses. **An adapter
contains no code.** OneShelf fetches everything itself, under its own network policy, and only from the
domains the adapter declares and you approve.

## Using adapters

You do not need this repository to use adapters, and you never download files from it by hand. In
OneShelf, open **Sources → Source Registry**: every published adapter is listed there with its trust
level, what it can do and what it may reach. Install, update and reinstall happen from that screen, each
after a review and the adapter's own tests.

The Registry is published from this repository's [`registry` branch](https://github.com/IPurplel/OneShelf-Adapters/tree/registry) and read over
HTTPS from `https://raw.githubusercontent.com/IPurplel/OneShelf-Adapters/registry/index.json`. Adapters are updated independently of OneShelf releases: a new or fixed adapter
reaches existing installations without a new version of OneShelf.

## Trust levels

| Level | Meaning |
|---|---|
| **Official** | Maintained or adopted by the OneShelf project; strongest review; live evidence |
| **Verified Community** | Community-contributed, then reviewed and verified by maintainers |
| **Community** | Passes every automated check; not (yet) maintainer-verified |

The level comes from the directory an adapter lives in — `adapters/official/`,
`adapters/verified-community/` or `adapters/community/` — which only a maintainer-reviewed change can
alter. Nothing inside an adapter can raise its trust. OneShelf treats this repository's Registry as its
**first-party** Registry and trusts its tiers as they are; any other Registry's claims count only with a
signature from a key the installation trusts. Signing is optional extra evidence here.
See [docs/trust-levels.md](docs/trust-levels.md).

## Contributing an adapter

```bash
git clone https://github.com/IPurplel/OneShelf-Adapters.git
cd OneShelf-Adapters
./tools/bootstrap                     # once: installs the pinned OneShelf tooling into .venv
./tools/new-adapter example-site      # creates adapters/community/oneshelf.example-site
# edit it: manifest, source, recipes, tests and fixtures
./tools/check-adapter oneshelf.example-site
```

Then open a Pull Request. CI runs the same checks, and a maintainer reviews it. Start with
[CONTRIBUTING.md](CONTRIBUTING.md); the full guide is [docs/adapter-authoring.md](docs/adapter-authoring.md).

## How an adapter reaches a library

```
adapter source → Pull Request → CI validation → maintainer review → merge
  → Registry build (canonical builder, packaged tests) → signing where the tier requires it
  → Registry verification → publish to the registry branch
  → OneShelf: review screen → PluginManager validation, hash, signature, permissions → install
```

A merge is repository governance, not runtime trust. Every later layer still applies: OneShelf
validates the package, checks its hash, checks the signature against its own trusted keys, shows the
permissions for approval, and enforces its network policy on every request.

## Relationship to OneShelf

OneShelf Core owns the package format, the validators, the packaged-test runtime and the Registry
protocol (`oneshelf.registry/1`). This repository does not copy them: its tools run the Core revision
pinned in [`tooling/oneshelf-core-ref.txt`](tooling/oneshelf-core-ref.txt). OneShelf ships a release
snapshot of the eight Official adapters so a fresh installation has sources even offline; that snapshot is
synced from here.

## Licence

**No licence has been chosen for this repository yet**, and no contribution terms (licence of
contributions, CLA or similar) have been decided. Until the owner decides, the default applies: the
content is published for reading and review, and no rights to use, modify or redistribute it are granted.
Contributions can be proposed and reviewed technically, but the project cannot rely on third-party
contributions as redistributable project assets until these terms exist. See
[docs/legal-status.md](docs/legal-status.md).
