# Architecture reviews — round 2 (2026-09-30)

Three reviews asked for after the NIJL and Acomics adapters, each on live evidence gathered with
`./tools/inspect-source` (Core's HTTP client, robots.txt first) and Scrapling's parser, plus the decisions for the
remaining candidates of [discovery-comics-2026-09.md](discovery-comics-2026-09.md). Nothing here changes Core.

## A. ComicControl — `EXISTING_RECIPES_SUFFICIENT` (template recommended; rights block every site today)

**Sample.** 24 hosts from Hiveworks and independent webcomics were fingerprinted; ComicControl was confirmed on
12 (the ~210 figure from usage trackers was not relied on): SMBC, El Goonish Shive, Paranatural, Awkward Zombie,
Sleepless Domain, Johnny Wander, Three Panel Soul, Mac Hall, Namesake, Wilde Life, Never Satisfied, Balderdash.

| Question | Answer (evidence: survey of the 12, 2026-09-30) |
|---|---|
| 1. What identifies a deployment? | `id="cc-comic"` on the page image, `cc-prev`/`cc-next` navigation classes, the string "comiccontrol" in the markup, `/comic/rss`. Present on 11 of 12; Balderdash runs a heavily customised theme without `#cc-comic` |
| 2. Is the archive consistent? | Mostly. 9 sites: `/comic/archive` holds a `<select name="comic">` listing every page in order (SMBC 7,926; EGS 3,615; Namesake 2,092; Wilde Life 1,668; Paranatural 920; Three Panel Soul 904; Sleepless Domain 820; Never Satisfied 701; Mac Hall 365). 2 sites (Awkward Zombie, Johnny Wander) list pages as links instead. Balderdash's options are root-relative slugs |
| 3. Is page identity stable? | Yes: `/comic/<slug>`; the slug is the page's permanent address |
| 4. Generic search? | No — ComicControl has no public search; RSS carries only the latest 20 items |
| 5. Existing recipes? | Yes: work (fixed), catalog (`select[name=comic] option`, `single_response`), reader (`#cc-comic` src) — the xkcd/Sandra and Woo pattern |
| 6. Stable image URLs? | Yes, and on the site's own host (`/comics/…`) on every sampled site, so one domain per adapter |
| 7. Metadata? | Page title text in `#cc-comic[title]`; no JSON; RSS 20 items; og:image on some |
| 8. One reusable pattern? | Yes for the `<select>` variant (9/12); the link-list variant needs its own selector; custom themes need review |
| 9. Authoring profile? | Practical: a `templates/comiccontrol/` scaffold for `./tools/new-adapter --template comiccontrol` with the three recipes, the host as the only domain, and a fixture checklist. One adapter per host, own identity, own fixtures |
| 10. Avoid Core change? | Yes — none needed |

**Blockers found.** SMBC's `/comic/archive` answers **HTTP 500** while still sending the full list; Core treats a
500 as a failed page, so SMBC's catalog cannot be trusted until the site answers 200. **Rights:** none of the 12
states a licence; they are free to read (`CREATOR_AUTHORIZED`). OneShelf's reader keeps a local copy (the CBZ that
"Download Missing" builds from reader pages), so under [rights-model.md](rights-model.md) each needs a licence or
the creator's written permission before an adapter ships. Recommendation: add the template when the first
permitted ComicControl site exists; do not build adapters before.

## B. WordPress / Toocheke — `EXISTING_RECIPES_SUFFICIENT`; header extraction not justified

**Sample.** Octopus Pie (1,937 comic posts), Trying Human (1,392), Puck (898) and Daughter of the Lilies (519) expose
the REST post type `comic` at `/wp-json/wp/v2/comic`; Dumbing of Age (5,578) and the Toocheke demo
(infinite.toocheke.com) do too, but their robots.txt disallows the path for `*`. Comic Easel/ComicPress sites (Kill Six Billion Demons, O Human Star,
Sandra and Woo) have no REST route for comics (`rest_no_route`).

**The header question.** WordPress puts the total in `X-WP-Total`/`X-WP-TotalPages`, and requesting past the last
page answers 400 (`rest_post_invalid_page_number`) — so a catalog must know the total. But WordPress's standard
`_envelope` parameter returns the headers inside the JSON body, verified on every Toocheke site above:

```
GET /wp-json/wp/v2/comic?per_page=100&page=1&order=asc&orderby=date&_envelope=1
{"body": [...], "status": 200, "headers": {"X-WP-Total": 1937, "X-WP-TotalPages": 20, "Link": "<…>; rel=\"next\""}}
```

so a recipe reads `items: $.body[*]` and `total: $.headers['X-WP-Total']` with `stop_when: total_count` today.
Items carry a numeric `id`, `slug`, `link`, `date`, `chapters` and the page image in `content.rendered`.

**Core primitive review** (§36 gate). Response-header extraction would help (1) WordPress — solved without it by
`_envelope`; (2) `Link: rel=next` APIs (GitHub-style) — none among current candidates; (3) `ETag`/`Last-Modified`
— conditional requests belong to Core's fetcher and Traffic Governor, not to recipes. It would be declarative,
statically validatable and fixture-testable (fixtures already carry a content type; they would need headers), but
no current legitimate source needs it. **Not justified now.** If a source appears whose only completeness signal
is a header, the design would be an allowlist (`X-WP-Total`, `X-WP-TotalPages`, `Link`, `X-Total-Count`,
`Content-Range`) readable only from the recipe's own response, never `Set-Cookie`/`Authorization`.

**Rights** as for ComicControl: the Toocheke sites state no licence; one adapter per permitted site. Note per-site
image hosts (Octopus Pie serves images from `test.octopuspie.com`), declared per adapter.

## C. HTML/text Reading Units — decision **B: a generic new reading format is needed** (not in this round)

**Sources it would unlock** (all blocked today on format, not access): Wikisource and Arabic Wikisource (their
WS-Export host is also robots-disallowed — they would read chapter HTML via the allowed API Portal), Wikibooks,
Aozora Bunko, OpenITI, Global Storybooks (Arabic), Syosetu (official JSON API), Kakuyomu, Royal Road, Scribble
Hub, Grise Bouille's text-and-drawing posts, Zeno.org, Projekt Gutenberg-DE, Sacred Texts, Alwaraq.

**What exists.** The Book Reader already renders untrusted HTML safely: EPUB chapters are sanitised
(`REMOVED_TAGS` script, iframe, object, embed, link, meta, base, form; event attributes dropped) and shown in an
`<iframe sandbox="">` with its own CSP — no scripts, opaque origin — with OneShelf's typography, themes,
RTL/LTR, logical progress (chapter share), bookmarks, highlights and in-book search. That renderer is reusable.

**What is missing** (the architectural surface):

1. Runtime: a recipe result kind for text units — a `reader` item that is an HTML fragment, not an image URL —
   with a size cap and schema validation.
2. A server-side sanitiser (the same allowlist as `epub.ts`, in Python) applied before storage, so nothing
   unsanitised is ever persisted.
3. Storage: a local artefact format for text units (sanitised HTML per unit, plus assets or none), its validator
   in `integrity/validators.py`, and a migration adding the format to the asset tables.
4. Downloads contract: the format in the allowed set, and "Download Missing" producing it from reader output —
   without manufacturing EPUB (the source's format is preserved; conversion stays a separate, explicit action).
5. Frontend: `BookReader` taking a one-chapter document; progress locators by character offset; Japanese
   vertical text is a later option, horizontal first.

**Security.** Remote HTML never reaches the app origin: sanitise on the server, render in the empty-sandbox frame
with CSP `default-src 'none'` (images only from the unit's own stored assets), no remote embeds, no forms, no
links that navigate the app. **Persistence/migration:** one additive migration (a format value), no change to
existing rows. **Tests:** sanitiser corpus (script, event handler, `javascript:` URL, SVG, CSS injection), a
packaged-test kind for text units, reader tests for RTL Arabic and Japanese, a live Wikisource-API adapter as the
first consumer.

**Recommendation:** a separate, gated Core task (not this round): it touches runtime, storage, migrations,
downloads and the reader. It is bounded and reuses the EPUB renderer, and it unblocks more legitimate sources than
any other single change found so far.

**Related Core gap:** OneShelf has no reading-direction field for image units; NIJL's manifests declare
right-to-left, which the adapter cannot pass on.

## Secondary candidates

| Candidate | Result | Evidence and reason | What would change it |
|---|---|---|---|
| Sandra and Woo | `VERIFIED` — `oneshelf.sandra-and-woo` | CC BY-NC-ND 3.0 in every footer; archive of 1,372 strips in one response | — |
| GDL content API | `VERIFIED_CANDIDATE`, not built | Every book has a Creative Commons licence term (11 terms, all CC; `/wp-json/wp/v2/license`); robots allows all. **Arabic:** 94 books, each with a static EPUB and PDF on `content.digitallibrary.io` (both validated by Core's validator). **But:** (1) its search API defaults to English and takes the language as a parameter, which OneShelf's search cannot pass (Core sends only `query`), and Arabic titles match only with full diacritics; (2) most English books are H5P-only, and their EPUB link (`/wp-json/epub-generator/v1/book/<h5pId>`, also a valid EPUB) appears only in list and search results, never on a per-book record (`/wp/v2/book/<id>` has no H5P id; the documented `/h5p-restapi-content/v1/book/<id>` returned an empty list). An adapter today would reach Arabic books only by pasted URL | Core passing a search language (the user's content language), or GDL exposing `epubUrl` on its per-book record |
| Unglue.it | `BLOCKED` (aggregator) | Its OPDS feed (`/api/opds/all/`) points every acquisition link at `unglue.it/download_ebook/<id>/`, which redirects to unbounded hosts: its own S3 bucket (`tieulgnu.s3.amazonaws.com`), `library.oapen.org`, `archive.org`, `github.com` releases, and `http://books.google.com` (plain http). The final host is unknown until fetched, so a bounded subset cannot be chosen declaratively | Unglue.it exposing the final file URL in the feed, so its own-bucket files could be selected |
| Grise Bouille | Waits on the HTML/text format | CC BY-SA 4.0 on every page; posts mix substantial French text with drawings (index `/tout`, ~700 posts). Image-only reading would drop the text | Review C's reading format |
| ComicControl / Toocheke creator sites | Rights needed | See A and B | A licence or written permission per site |
