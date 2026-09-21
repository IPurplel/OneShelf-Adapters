<!-- Adapter Pull Request. Delete sections that do not apply. -->

## Adapter

- **Adapter id:** `oneshelf.`
- **New adapter or update:**
- **Version:** (an update must bump it)
- **Site / source name:**
- **Base URL:**
- **Source language(s):**
- **Content type(s):** (manga / comics / books / papers / …)
- **Capabilities implemented:**
- **Known unsupported capabilities, and why:**
- **Network domains requested:** (and CDN domains)
- **Login or session needed?** (if yes: why the public endpoints are not enough)
- **Packaged tests added:**

New adapters go in `adapters/community/`. Trust levels are decided by maintainers after review; this PR
cannot set them.

## Local validation

<!-- Paste the output of ./tools/check-adapter <id> -->

```
```

## Checklist

- [ ] No secrets: no credentials, cookies, tokens, passwords, session data or personal data
- [ ] No executable code: only declarative files (YAML/JSON/HTML/XML/TXT, small image fixtures)
- [ ] No bypasses: nothing that defeats DRM, paywalls, CAPTCHAs or anti-bot systems; robots.txt respected
- [ ] Packaged tests included for every capability, with minimal sanitized fixtures
- [ ] The manifest `id` matches the directory name
- [ ] For an existing adapter: the version is bumped
- [ ] I have read CONTRIBUTING.md and docs/legal-status.md
