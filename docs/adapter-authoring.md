# Authoring an adapter

This is the reference for the files in an adapter. The OneShelf package format is defined and validated
by OneShelf Core (the `oneshelf.osp/1` schema); when anything here and the validator disagree, the
validator is right and `./tools/check-adapter` will say so.

## Files

| File | Required | Purpose |
|---|---|---|
| `manifest.yaml` | yes | identity, version, plugin API, capabilities, network domains, optional browser/auth |
| `source.yaml` | yes | `base_url`, `url_patterns` (recognising the site's URLs), `rate_limit`, `timeouts` |
| `recipes/<capability>.yaml` | one per capability | request + response format + extraction |
| `tests/tests.yaml` | yes | packaged test cases; at least one |
| `tests/fixtures/*` | yes | the saved responses the cases use |

## manifest.yaml

```yaml
schema: oneshelf.osp/1
id: oneshelf.example-site        # = directory name; never changes after publication
name: Example Site
version: 1.0.0
api: '1.0'
description: >-
  What the source is, what this adapter does, and — plainly — what it does not.
publisher: Your name or handle
capabilities: [search, work, catalog]
network:
  domains: [example-site.org]    # exact hosts; as narrow as possible
  cdn_domains: []                # hosts for images/files only
defaults:
  language: en
```

Capabilities: `search`, `work` (details of one work), `catalog` (its units: chapters/volumes/files),
`reader` (pages of a unit), `downloads` (files of a unit), `latest`, `health`. Declare only what works.

A browser (`browser:`) or a signed-in session (`auth:`) are exceptional: they must be justified in the Pull
Request, and reviewers will ask whether the site's own public endpoints make them unnecessary.

## source.yaml

```yaml
base_url: https://example-site.org
url_patterns:
  - pattern: '^https://example-site\.org/books/([^/?#]+)'
    capability: work
    id_group: 1
rate_limit:
  requests_per_minute: 20
  concurrency: 1
```

`base_url` must be `https` on a declared domain. Keep the rate limit polite.

## Recipes

```yaml
capability: search
inputs: [query]
request:
  url: "{base_url}/search?q={query}"
response:
  format: html                   # html | json | xml
extract:
  items: {css: "li.result"}
  fields:
    listing_key: {css: "a::attr(href)", transforms: [{regex_extract: {pattern: '/books/([^/?#]+)', group: 1}}], required: true}
    title: {css: "a::text", transforms: [trim], required: true}
pagination:
  mode: none
  complete_when: single_response
```

Fields can use `css`, `xpath`, `json` (JSON path) or `template`, with transforms such as `trim`,
`regex_extract`, and others the validator lists. Every request URL must resolve to a declared domain.
`adapters/official/` has complete examples of HTML, JSON-API, OPDS/XML and paginated sources.

## Tests

```yaml
cases:
- capability: search
  inputs: {query: frankenstein}
  fixtures:
  - url: https://example-site.org/search?q=frankenstein
    file: fixtures/search.html
  expect:
    min_items: 1
    fields_present: [listing_key, title]
    first: {listing_key: frankenstein, title: Frankenstein}
```

Each fixture answers exactly one URL the recipe requests. See [testing.md](testing.md).

## From the OneShelf Adapter Generator

OneShelf's Adapter Generator can draft an adapter from a site and export a **submission bundle**. That
bundle is the same set of files: copy them into `adapters/community/<id>/`, run `./tools/check-adapter`, and
open a Pull Request. OneShelf never publishes anything by itself — generating, installing and publishing
remain separate steps.
