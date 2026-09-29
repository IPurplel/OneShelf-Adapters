# Investigating a source

How a new source is investigated before it becomes an adapter, what the tools here do, and which sources
qualify for the open-access part of the Registry. The adapter format itself is in
[adapter-authoring.md](adapter-authoring.md); the status of every candidate source is in
[source-matrix.md](source-matrix.md).

```
Scrapling-assisted discovery → evidence → declarative recipes → fixtures → packaged tests → live check → .osp
```

Scrapling helps find a selector. OneShelf executes the final one. Nothing from Scrapling ever becomes part
of an adapter except a selector a person has checked, written down, and backed with a fixture and a test.

## 1. Prefer what the source publishes for machines

In this order: an official API, OPDS/Atom/RSS feed, IIIF manifest, OAI-PMH endpoint or MediaWiki API → stable
static markup → public JSON the site's own pages use → (only when nothing else exists, and justified in the Pull
Request) a browser. Never a private or protected endpoint when ordinary public access exists, and never a path
robots.txt disallows.

## 2. `./tools/inspect-source`

```bash
./tools/inspect-source https://example.org/books/123/                 # fetch once, report
./tools/inspect-source https://example.org/search?q=x --css "li.result a::attr(href)" --xpath "//li/@data-id"
./tools/inspect-source https://api.example.org/items/1 --json '$.items[*].id'
./tools/inspect-source URL --save draft.html                          # a fixture draft, to trim by hand
./tools/inspect-source --from draft.html --url URL --css "..."        # offline, against a saved response
```

It reports the final URL and redirect chain, status, content type, caching and rate-limit headers
(`Cache-Control`, `ETag`, `Last-Modified`, `Retry-After`, `RateLimit-*`), the robots.txt verdict for the URL,
the page title, canonical URL, `lang`/`dir` and the share of Arabic, Latin and CJK script, OpenGraph /
`citation_*` / Dublin Core metadata and JSON-LD types, declared feeds and links that look like IIIF, OAI-PMH,
OPDS, API or sitemap endpoints, file links grouped by format with their hosts, image hosts, recurring link
shapes (`/books/{n}/`) with a sample CSS path, pagination candidates, `data-*` attributes (stable-id
candidates), duplicate links, and whether the visible content appears to need JavaScript. A JSON response
gets a map of its arrays and scalar paths, written the way recipes write them.

`--css`, `--xpath` and `--json` are evaluated by the **runtime's own extraction function** on the runtime's
own parse, so a selector that matches here matches in OneShelf — including XML feeds, which the runtime
reads as markup.

What it deliberately does not do:

- **It uses Scrapling's parser (`scrapling.parser.Selector`), not its fetchers.** Scrapling's fetchers
  impersonate a browser's TLS fingerprint and headers by default. OneShelf does not pretend to be a browser,
  so requests go through OneShelf Core's own HTTP client with its honest User-Agent and its egress policy:
  private, loopback and link-local destinations are refused, and every redirect and DNS answer is re-checked.
  Only the URL's own host is allowed; a redirect elsewhere is reported, and `--allow-host` allows another host
  on purpose — which is also how you learn which domains an adapter would need.
- **robots.txt first.** A disallowed URL is not fetched (`--ignore-robots` exists only to look at a page a
  person may read; an adapter can never use such a path).
- **One request per URL.** Responses are cached in `.inspect-cache/` (git-ignored) and reused.
- **No adaptive selectors.** Scrapling can relocate an element after a redesign; OneShelf must not. If a site
  changes so much that identity, completeness or open-access status becomes unclear, the adapter must fail
  and keep the previous trusted data, not guess. The "sample selector" in a report is a lead for a person to
  improve — prefer `data-*` ids, canonical links, schema.org and OpenGraph metadata and stable URL shapes over
  positional paths such as `nth-of-type`.
- No stealth, CAPTCHA or Turnstile solving, fingerprint spoofing, proxy rotation, logins, or anything that
  reaches content an ordinary permitted visitor cannot.

Scrapling is already a dependency of OneShelf Core (its parser is the runtime's), so the tool adds no new
package: `./tools/bootstrap` installs it at the pinned Core revision. It is development tooling only.

## 3. `./tools/live-check`

```bash
./tools/live-check oneshelf.example                       # inputs from the adapter's own packaged tests
./tools/live-check oneshelf.example --query "تاريخ" --listing-key 123
```

Runs every declared capability against the live source through OneShelf Core's `RecipeRuntime`, `SourceFetcher`,
HTTP client and egress policy, under the Traffic Governor configured with the adapter's rate limit — the same
path an installation uses. The steps are chained as a library would chain them (search → work → catalog →
downloads/reader). File and page bytes are fetched and checked with Core's validators: an EPUB is opened, a
PDF read, an image decoded, and a file whose bytes are not the format it was declared as fails. The JSON output
records the date, every request with its status, redirects and any `Retry-After`. Keep the summary in
[source-matrix.md](source-matrix.md); never commit raw live responses.

Live success is evidence, never a substitute for packaged tests, and never changes a trust level.

## 4. Open-access eligibility

The open-access part of the Registry lists sources where the **complete** readable item is free to everyone:
public domain, Creative Commons or other open licences, open-access publishing, or free access granted by the
publisher. Not samples, previews, "first chapters free", coins, passes, subscriptions, or anything needing a
paid entitlement, and never by circumventing DRM or access control.

A site that mixes open and restricted material qualifies only if the adapter can restrict itself **from
machine-readable evidence** — an open-access flag, licence field, collection, or access status in the response
— and the packaged tests prove it: an open item is included, a restricted one is excluded, and an ambiguous
one is not offered as downloadable. The usual declarative way is a required field that exists only when the
evidence does, so an item without it is skipped rather than guessed at. Without such evidence the source is
Blocked, not approximated.

## 5. What OneShelf can read, and what that means for capabilities

- `downloads` files must be **EPUB, PDF or CBZ**: those are the formats OneShelf's download path validates and
  its reader opens. A source that only offers plain text, HTML chapters, DjVu or MOBI cannot declare
  `downloads` for them.
- `reader` resources are **images**, one per page, in source order (IIIF canvases are a good fit).
- A book offered as one file is one Reading Unit of type `one_shot` — not invented chapters.
- `catalog` may claim `complete_when: single_response` only when one response is the whole list. A catalog is
  per work; a source with millions of items offers search, not a pretend global catalogue.
- Every host a request or file comes from — including every redirect target — must be declared, narrowly:
  `domains` for the source, `cdn_domains` for media and files. No wildcard escape hatch. An aggregator whose
  files live on arbitrary third-party hosts gets search and work only, or no adapter.

## 6. New adapters and trust

New adapters enter `adapters/community/`. Promotion is a separate maintainer decision on review and live
evidence ([trust-levels.md](trust-levels.md)); adding a source to the Registry does not add it to the
snapshot OneShelf bundles.
