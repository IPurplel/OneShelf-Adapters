# Contributing an adapter

Thank you for helping OneShelf read more of the world. This guide assumes no knowledge of OneShelf's
internals.

> **Before you contribute:** no licence or contribution terms have been chosen for this repository yet
> ([docs/legal-status.md](docs/legal-status.md)). You are welcome to open Pull Requests, and they will be
> reviewed, but the project cannot rely on them as redistributable assets until those terms exist.

## What an adapter is

A directory of declarative files that tells OneShelf how to use one site:

```
adapters/community/oneshelf.example-site/
├── manifest.yaml     # identity, version, capabilities, the domains it may reach
├── source.yaml       # base URL, URL patterns, rate limit
├── recipes/          # one recipe per capability: the request, and how to read the response
│   └── search.yaml
└── tests/
    ├── tests.yaml    # packaged tests: inputs, the fixture each request returns, what must come out
    └── fixtures/     # small saved responses the tests run against
```

**Adapters are data, not code.** Only `.yaml`, `.yml`, `.json`, `.html`, `.htm`, `.xml`, `.txt` and small
`.png`/`.jpg`/`.jpeg`/`.webp` fixtures are accepted. OneShelf performs every request itself.

## Create one

```bash
./tools/bootstrap                                  # once
./tools/new-adapter example-site --name "Example Site" --domain example-site.org
```

This creates `adapters/community/oneshelf.example-site` from `templates/basic-source/` — a small working
adapter with a search recipe, a synthetic fixture and a packaged test. Replace them with the real site's.

### manifest.yaml

- `id` — `oneshelf.<name>`, lowercase, **equal to the directory name**, and never changed once published.
  Name the site or project, not a transient domain.
- `version` — `MAJOR.MINOR.PATCH`. New adapters start at `0.1.0` or `1.0.0`.
- `api` — the OneShelf plugin API it targets (`'1.0'` today). You cannot raise this here: plugin API changes
  belong in OneShelf Core.
- `capabilities` — only what the adapter really does: `search`, `work`, `catalog`, `reader`, `downloads`,
  `latest`, `health`. Say plainly what it cannot do in `description`.
- `network.domains` — the exact hosts it may reach, as narrow as possible. `cdn_domains` for images/files.

### recipes

One file per capability: a `request` (URL template on an allowlisted domain), a `response.format`
(`html`, `json`, `xml`), and `extract` rules (CSS, XPath or JSON path, with transforms). Look at
`adapters/official/` for real examples; [docs/adapter-authoring.md](docs/adapter-authoring.md) covers every field.

### packaged tests and fixtures

Every capability needs at least one packaged test. Tests run **offline** against fixtures: CI never
depends on the live site. Fixtures must be:

- **minimal** — the smallest response that exercises the parser; trim everything else;
- **sanitized** — no session ids, cookies, tokens, account names or personal data;
- **not content** — never commit whole chapters, books, image sets or other copyrighted media. A few
  entries of a listing are enough; a synthetic fixture is often better.

Limits: 512 KiB per text fixture, 128 KiB per image fixture, 4 MiB per adapter.

## Check it

```bash
./tools/check-adapter oneshelf.example-site   # one adapter
./tools/check-all                             # everything, as CI does
```

The checks build the package with OneShelf's own builder, validate it exactly as an install would, run the
packaged tests, scan for secrets and forbidden files, and compare with what is already published.

## Open a Pull Request

Fill in the template. CI runs without any secrets. A maintainer reviews against
[docs/review-policy.md](docs/review-policy.md) and may ask for narrower domains, better fixtures, an honest
capability list or a version bump.

## Updating an adapter

**Any change to a published adapter needs a version bump.** CI fails if content changes under a published
version, or if a version goes backwards. Adding a permission (a new domain, a browser capability, a
session) is fine, but every OneShelf installation will ask its owner to review it before the update runs.

## Trust levels

New adapters enter `adapters/community/`. Moving to Verified Community or Official is a separate,
maintainer-made change after review and live verification — asking for it in a PR does not make it
happen, and changing a label anywhere inside an adapter does nothing. See [docs/trust-levels.md](docs/trust-levels.md).

## Never commit

- executable code of any kind: Python, JavaScript, shell, WebAssembly, native binaries;
- credentials, cookies, tokens, passwords, API keys, session exports, `.env` files;
- private or personal data;
- anything that bypasses DRM, paywalls, CAPTCHAs or anti-bot systems, or pretends to be a browser it is not;
- requests to anything but the declared public domains (no LAN, no IP addresses, no open proxies).

Adapters that do any of these are rejected, and security reports go to [SECURITY.md](SECURITY.md).
