# Discovery round 12: books, manga and comics — 2026-10-10

Scope: **books, manga and comics only**, in any language. Every domain was checked first against the docs of
the comics round ([discovery-comics-2026-09.md](discovery-comics-2026-09.md), 204 sites), rounds 3–11,
`candidate-sources.md`, `source-matrix.md` and every adapter's `source.yaml` (1,225 recorded domains). Most
well-known open book and comic sites were already there: Feedbooks, Global Grey, Planet eBook, Liber Liber,
StoryWeaver, Bloom, African Storybook, Book Dash, Unglue.it, Gunnerkrigg Court, Geek and Poke, Mimi and
Eunice, Manga Library Z, Digital Comic Museum, GlobalComix and the King Fahd National Library, among others.

- **Access:** OneShelf's own User-Agent, robots.txt first, about one request per 1.5 s, a few pages per site.
  Nothing was bypassed. One file was downloaded to confirm its format, then deleted (row 3).
- **Rights:** unchanged. A copy is offered only on item-level, machine-readable evidence
  ([rights-model.md](rights-model.md), [source-discovery.md §4](source-discovery.md#4-open-access-eligibility)).
  Free to read is not free to copy.

This round is discovery only: **nothing was built.**

**Outcomes (13 sources):** ELIGIBLE NOT BUILT 2, RIGHTS NEED REVIEW 2, TECHNICALLY BLOCKED 4,
NOT EXAMINED FURTHER 5.

**Manga:** no new eligible source. Openly licensed manga is rare: the 2009 *Mikako-san* CC BY-NC-ND release
and Shuho Sato's works are the only cases found, and the comics round already recorded Sato's site as gone.
Official free manga platforms (MANGA Plus, K MANGA, Magazine Pocket and others) are free to read only, and
the comics round already records them.

## Recommended for the next build round

| Candidate | Label | Evidence per item | Files | Sampled |
|---|---|---|---|---|
| Framabook archive (row 1) | `Framabook · Books · FR` | `Licence :` field linking the book's own licence: `creativecommons.org/licenses/by-sa/3.0/fr/`, `…/by-sa/2.0/fr`, or `artlibre.org` | PDF and EPUB on the same host | 6 of 8 books carry the field; the *Mimi & Eunice* calendar has none (refusal case); 2 have no file |
| Comloc Vault (row 2) | `Comloc Vault · Comics · EN` | JSON-LD `Book.license` = `https://creativecommons.org/publicdomain/mark/1.0/`, plus "Public domain — verified 2026-07-06. Scan: Internet Archive" | page images `pages/p001.webp`… on the same host | 2 of 2 issues; `p001.webp` is a real WebP (149,710 bytes), and Core's reader accepts `.webp` |

Build notes:
- **Framabook:**
  - A static WordPress export (`…/index.html` pages) with categories *Bédés* (comics: *Grise Bouille* 1–4,
    *GKND* 1–5), *Romans*, *Manuels* and *Essais*, two listing pages each.
  - Its CC links carry a jurisdiction port (`/3.0/fr/`), which the journal gate's regex
    (`…/[0-9.]+/?$`) would refuse. An adapter needs its own gate: a CC licence URL with an optional
    jurisdiction, or Art Libre.
  - The successor project, *Des livres en communs* (deslivresencommuns.org), states its licence only
    site-wide, so it is not included.
- **Comloc Vault** is a section of a commercial comic-shop site ("© 2026 Comloc. All rights reserved"
  covers the site). The per-issue public-domain mark and the credited scan source are the evidence. About
  11 issues (sitemap), so the adapter would be small. An issue is one work with one unit, and its pages are
  listed in the issue page itself.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Outcome | Adapter / blocker |
|---|---|---|---|---|---|---|---|
| 1 | [Framabook (archive)](https://archives.framabook.org/) | books, comics, manuals | fr | per book `Licence :` link: CC BY-SA 2.0/3.0 FR or Licence Art Libre | `User-agent: *` with no rules | ELIGIBLE NOT BUILT | **Recommended** |
| 2 | [Comloc Vault](https://www.comicshoplocator.com/comics/read/) | golden-age comics (1940s–50s) | en | per issue JSON-LD `license` = Public Domain Mark 1.0; renewal check and scan source stated | `Allow: /` | ELIGIBLE NOT BUILT | **Recommended.** Small (about 11 issues) |
| 3 | [Project Ben-Yehuda](https://benyehuda.org/) | Hebrew literature | he | per work: public domain, or "published by express permission" (popover text, machine-readable) | blocks only Semrushbot | TECHNICALLY BLOCKED | Files come only from `POST /download/<id>`: a 302 to a stable `rails/active_storage/blobs/redirect/…` address, then a presigned S3 URL (`bybeprod.s3.amazonaws.com`). The EPUB is valid. A downloads recipe cannot return a URL that only a POST reveals. The API needs a personal key |
| 4 | [Ανοικτή Βιβλιοθήκη (openbook.gr)](https://www.openbook.gr/) | Greek books | el | per book text "Άδεια διανομής": "Public Domain", "Creative Commons BY-NC-ND" (no version, no URL) or "Ελεύθερη διάθεση" (free distribution, no licence) | only `/wp-admin/` | RIGHTS NEED REVIEW | Text-only, unversioned licence. Files on Dropbox (`?dl=0` preview links) and other third-party hosts |
| 5 | [Fodongo](https://fodongo.ca/) | free-culture comics zine | en, es | per issue licence **badge images** (CCBY, CCBYSA, FAL); contributions differ, and issue 17 announces a move to MIT-0/MIT | blocks AI crawlers, not OneShelf | RIGHTS NEED REVIEW | No machine-readable licence; mixed per contribution. PDFs on the same host |
| 6 | [Zlatý fond SME](https://zlatyfond.sme.sk/) | Slovak literature | sk | — | allows reading paths | TECHNICALLY BLOCKED | HTTP 403 to OneShelf's User-Agent |
| 7 | [Projecto Adamastor](https://adamastor.pt/) | Portuguese public-domain e-books | pt | — | not reached | TECHNICALLY BLOCKED | Timed out |
| 8 | [itch.io](https://itch.io/) (e.g. CC comics such as *Terminal*, *Fodongo*) | comics, zines | various | per page licence field | `Disallow: /*/download/` | TECHNICALLY BLOCKED | Downloads are a disallowed path |
| 9 | [ComicBooks.com Reading Room](https://comicbooks.com/) | golden-age comics | en | claims public domain | `User-agent: *` with no rules | NOT EXAMINED FURTHER | The front page is now a store page; the reading room reported in August 2026 was not found from it |
| 10 | [DIGAR (National Library of Estonia)](https://www.digar.ee/arhiiv/et/raamatud) | books | et, ru | — | no robots.txt | NOT EXAMINED FURTHER | The sampled book page shows no licence and no file link |
| 11 | [Městská knihovna v Praze, e-knihy](https://www.mlp.cz/cz/katalog/e-knihy) | Czech public-domain e-books | cs | — | system paths only | NOT EXAMINED FURTHER | The old `web2.mlp.cz/koweb` e-book pages answer 404; the new catalogue lists no e-book links without its search |
| 12 | [공유마당 Gongu (Korea Copyright Commission)](https://gongu.copyright.or.kr/) | CC and public-domain works incl. comics and e-books | ko | per work CC / KOGL label (reported) | `Disallow: /upload/` for every agent | NOT EXAMINED FURTHER | Item pages not reached from the front page; files may sit under the disallowed `/upload/` |
| 13 | [Des livres en communs](https://deslivresencommuns.org/) | books | fr | site-wide "CC-By-Sa sauf mention contraire" only | no rules | NOT EXAMINED FURTHER | Successor of Framabook; no item-level licence seen yet |

## Notes for maintainers

- **Framabook vs the journal gate.** Framabook's links are versioned and item-level, but they carry a
  jurisdiction port (`/fr/`). An adapter's own regex can accept that; the journal adapters' gate is not changed.
- **Ben-Yehuda** has exactly the per-work rights flag the policy asks for. If Core ever lets a downloads
  recipe issue a POST and keep the redirect location as the file URL, it would qualify (declaring
  `bybeprod.s3.amazonaws.com` as a CDN domain).
- **Pinned Core.** No Core change is needed for rows 1–2.
