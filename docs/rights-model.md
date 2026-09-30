# Rights and access model

A source being **visible** — its items listed, searchable, readable on its own site — says nothing about
whether OneShelf may **keep a copy**. OneShelf's `reader` capability saves page images into a local CBZ and
`downloads` saves a file; both are copies. So every adapter answers several separate questions, and none of
them is a single "open" boolean.

OneShelf Core has no licence model: it runs recipes and stores what they return. The model therefore lives
in this repository, in two places that must agree:

1. **The recipes enforce it.** An item that may not be copied is never returned by `reader` or `downloads`
   (and, where the source mixes material, not by `search` or `catalog` either). The recipe requires a field
   that exists only when the source's own machine-readable evidence does — a licence link, a rights URI, an
   open-access flag — so a missing or ambiguous statement makes the item disappear rather than be guessed
   at ([source-discovery.md §4](source-discovery.md#4-open-access-eligibility)).
2. **`rights.yaml` declares it.** Each adapter added from now on carries a `rights.yaml` beside its
   `manifest.yaml`. It travels in the `.osp` (Core ignores it), is read by reviewers, and is checked by
   `tests/test_rights.py` against the adapter's own manifest and packaged tests, so a claim cannot drift
   away from what the recipes do.

This is the smallest extension that keeps the pinned Core untouched. If Core later grows a rights field on
work or unit results, `rights.yaml` is where its values come from.

## `rights.yaml`

```yaml
schema: oneshelf.rights/1
access_scope: whole_source          # whole_source | collection | per_item — what part of the source the adapter covers
access_type: open_license           # public_domain | open_license | open_access_publisher | free_to_read | mixed
rights_granularity: source          # source | collection | item — the level at which the source states rights
license: {id: CC-BY-NC-2.5, url: https://creativecommons.org/licenses/by-nc/2.5/}   # null id/url when there is none
commercial_use: not_allowed         # allowed | allowed_with_conditions | not_allowed | unknown
redistribution: allowed_with_conditions
derivatives: allowed_with_conditions
attribution: {required: true, text: "…"}
visibility: all_listed_items        # all_listed_items | eligible_items_only — what search/catalog show
local_copy: allowed                 # allowed | eligible_items_only | not_allowed — what reader/downloads may save
enforcement:
  summary: how the recipes keep ineligible items out
  exclusion_tests: [4]              # indexes of tests.yaml cases proving an ineligible item is not offered
evidence:
  - {claim: "…", url: https://…}    # every important claim, with the page that states it
last_verified: 2026-09-29
```

| Term | Meaning |
|---|---|
| `public_domain` | No copyright restriction (PDM, NoC, or expired). Copies allowed. |
| `open_license` | A licence that grants copying — Creative Commons or similar. Its conditions (NC, ND, SA, BY) are the permission fields. |
| `open_access_publisher` | A publisher's own grant of free access and copying without a standard licence. The grant is cited as evidence. |
| `free_to_read` | Free to view on the source's site, with no grant to copy. **No `reader`, no `downloads`.** |
| `mixed` | Items differ. Copying only for items whose own evidence grants it. |

## Rules `tests/test_rights.py` enforces

- Every adapter not on the test's `PREDATING` list has a complete `rights.yaml`, with no unknown keys and only
  the values above. The list only shrinks.
- `free_to_read` ⇒ `local_copy: not_allowed`; `local_copy: not_allowed` ⇒ no `reader` or `downloads`.
- Rights stated per item or per collection (or `mixed`), with a copying capability ⇒
  `local_copy: eligible_items_only`.
- `eligible_items_only` ⇒ at least one exclusion test. Each named `tests.yaml` case must run `reader`,
  `downloads`, `search` or `catalog` and expect an empty result — `first: {url: null}` (Core's test schema has
  no `max_items`; an absent first entry compares as null, so this asserts the list is empty).
- An `open_license` names its licence id and an https URL. Every evidence entry has a claim and an https URL.
  `last_verified` is a date, not in the future.
- `./tools/new-adapter` scaffolds a read-only `rights.yaml` (`free_to_read`, `not_allowed`). Adding `reader` or
  `downloads` without revisiting it fails the test.

## What a reviewer still checks

The test proves consistency, not truth. A reviewer opens every evidence URL and checks that:

- the licence applies to the content OneShelf copies (images and text, not only metadata or the website
  design);
- a per-item rights field is the source's own statement, not an aggregator's guess;
- terms of use do not forbid automated access or local copies that the licence would otherwise allow;
- nothing is reached through a login, a CAPTCHA, a signed or referer-locked URL obtained outside the
  ordinary public page, or a path robots.txt disallows.

## Adapters that predate the model

The 30 adapters on the `PREDATING` list already gate eligibility in their recipes, and their access model
is recorded in [source-matrix.md](source-matrix.md). Adding their `rights.yaml` files is follow-up work.
Each one removed from the list must pass the same test.
