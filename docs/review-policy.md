# Review policy

Merging a Pull Request is a governance decision; it does not by itself make an adapter trusted by any
OneShelf installation (see the supply chain in the README). Reviewers check:

- **Identity** — a real, lawful source; a stable id naming the site or project; id = directory name.
- **Honest capabilities** — only what works; what does not work is stated in `description`.
- **Narrow network scope** — exact domains; CDN domains only for media; no wildcards without reason.
- **No unnecessary browser or session** — public endpoints first; a browser or login must be justified.
- **No bypasses** — nothing that defeats DRM, paywalls, CAPTCHAs, rate limits or anti-bot systems, and
  no robots.txt-disallowed paths.
- **Meaningful packaged tests** — they assert real fields, not just that something parsed.
- **Safe fixtures** — minimal, sanitized, not whole works.
- **Robust parsing** — selectors that survive small layout changes where the site allows.
- **Versioning** — a bump for every change to a published adapter.
- **Reachability** — for promotion, live evidence that the source works now.

Popularity is never a trust or security criterion.

Changes to `.github/workflows/`, `tools/`, `tooling/`, `registry-trust/`, `adapters/official/`,
`adapters/verified-community/` and this policy are security-sensitive and require the maintainer's review
(`CODEOWNERS`). Workflow changes deserve particular care: a workflow runs with the repository's
permissions.
