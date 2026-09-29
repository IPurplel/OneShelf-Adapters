# Testing adapters

## Locally

```bash
./tools/bootstrap                 # once, or after tooling/oneshelf-core-ref.txt changes
./tools/check-adapter <id>        # one adapter
./tools/check-all                 # every adapter, the repository policy tests, and a Registry build
./tools/fetch-baseline            # optional: fetch the published Registry so checks compare against it
```

## What runs

For each adapter, with the pinned OneShelf Core:

1. structure: `adapters/<tier>/<id>/`, id = directory name, one id in one tier only;
2. files: declarative types only; no symlinks, hidden files, unsafe names or executables; fixture size
   limits; a scan for private keys, tokens, cookies and credentials;
3. the canonical `.osp` build (deterministic: same sources, same bytes);
4. the package loaded exactly as an install would: schemas, recipes, templates, domains, capabilities;
5. plugin API compatibility with the pinned Core;
6. **the packaged tests**, offline against the fixtures — mandatory;
7. against the published Registry: a published id+version never changes content, and versions never go
   backwards;
8. reproducibility: every already-published version rebuilds to exactly its published bytes. CI runs on a
   different platform from the one that publishes, so this proves the builder is platform-independent.

CI also builds a Registry from the whole tree and verifies it with Core's Registry parser — the contract
OneShelf itself depends on — and runs the repository policy tests in `tests/`.

## Live checks

Packaged tests are the gate; they never touch the network. Live verification against the real sites is
evidence for promotion and for noticing breakage. A live pass is never a substitute for packaged tests and
never changes a trust level by itself.

```bash
./tools/live-check <id>           # any adapter, any tier, on your machine
```

runs every declared capability of one adapter against the live site through OneShelf Core's runtime, fetcher
and egress policy, chained as a library chains them, and opens the files and images it reaches with Core's
validators; any request robots.txt disallows (RFC 9309, redirects included) fails the check ([source-discovery.md](source-discovery.md#3-toolslive-check)). Record the outcome in
[source-matrix.md](source-matrix.md). Maintainers can also run OneShelf's own live suite against the Official
adapters through the **Live source check** workflow (manual dispatch).
