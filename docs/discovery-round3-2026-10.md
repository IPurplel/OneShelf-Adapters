# Discovery round 3: new open-access sources — 2026-10-07

**35 sites** not investigated before (checked against every domain in [source-matrix.md](source-matrix.md),
[candidate-sources.md](candidate-sources.md), [discovery-comics-2026-09.md](discovery-comics-2026-09.md) and
[architecture-reviews-2026-09.md](architecture-reviews-2026-09.md): 328 domains), found by web search and
by following publishers and platforms. Each was screened with `./tools/inspect-source` (Core's HTTP client,
robots.txt first, OneShelf's own User-Agent); rights were read on the site's own copyright, licence or
terms pages. Nothing was bypassed or retried around a refusal: a challenge, 403, 429 or redirect to plain
http is recorded as what an ordinary permitted client meets. This table is generated from one list
(the counts below come from the same rows).

## Summary

- **Technical grade:** A 2, B 9, C 9, D 1, F 14
- **Rights:** `CREATOR_AUTHORIZED` 1, `FREE_OFFICIAL` 2, `OPEN_LICENSED` 16, `PUBLIC_DOMAIN` 8, `RESTRICTED` 2, `RIGHTS_UNCLEAR` 6
- **robots/access:** Allowed 18, Disallowed 1, Partial 4, Unavailable 12
- **Decision:** BLOCKED 21, COVERED 1, HELD 1, IMPLEMENTED 7, QUEUED 5

Grades: A straightforward and stable; B viable with normal recipe features; C viable but fragile or limited;
D major obstacle; F unsuitable now (unreachable, forbidden or gone). Access: Allowed (no rule against the
requests an adapter needs), Partial (some paths disallowed, none of them needed), Disallowed (the needed
paths are disallowed), Unavailable (challenge, block, rate limit, http downgrade or gone).

## All candidates

| # | Source | Category | Rights | Rights evidence | robots / access | Grade | Endpoints | Decision | Reason / adapter |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | [Sefaria](https://www.sefaria.org/) | Jewish texts (Hebrew, Aramaic, English, …) | `OPEN_LICENSED` | Each text version carries its own `license` in `/api/v3/texts` (PD, CC0, CC BY, CC BY-SA, CC BY-NC; some none); Sefaria's licensing help page | Allowed | C | `/api/v3/texts/<ref>`, `/api/shape/<title>`, `/api/v2/index/<title>`, `/api/name/<q>` | `QUEUED` | Needs Core work: chapters exist only as positions in `/api/shape` (no reference per chapter; Talmud amudim 2a/2b with empty leading slots), verses arrive as separate items, and the version must follow the track's language. See *Queued* below. |
| 2 | [Projekt Runeberg](https://runeberg.org/) | Nordic literature (sv, no, da, fi, is …) | `PUBLIC_DOMAIN` | /admin/: works published once the author has been dead 70+ years; newer works carry a copyright notice (pol95: "view it on screen") | Partial | B | `/<work>/` (table of contents), `/<work>/NN.html` (chapters) | `IMPLEMENTED` | `oneshelf.runeberg` — text editions only; scanned-facsimile works and works under copyright have no units |
| 3 | [Chinese Text Project](https://ctext.org/) | Chinese classics | `RESTRICTED` | Terms page: "you do not have authorization to scrape this page"; data access is through a subscription API | Partial | F | `api.ctext.org` (robots-disallowed), HTML text pages | `BLOCKED` | The site forbids automated access and runs anti-scraping measures; the API host is robots-disallowed |
| 4 | [Kanripo](https://www.kanripo.org/) | Chinese texts | `RIGHTS_UNCLEAR` | Not reachable | Unavailable | F | — | `BLOCKED` | Cloudflare challenge ("Just a moment…") on the front page |
| 5 | [The Latin Library](https://www.thelatinlibrary.com/) | Latin texts | `PUBLIC_DOMAIN` | Ancient and medieval texts from old editions; the site states no licence of its own | Allowed | C | `/<author>.html`, `/<author>/<book>.shtml` | `QUEUED` | Hand-made HTML that differs from author to author; no machine-readable structure or licence statement |
| 6 | [Bibliotheca Augustana](https://www.tha.de/~harsch/augustana.html) | Texts in many languages | `RIGHTS_UNCLEAR` | No rights statement on the site (moved from hs-augsburg.de) | Allowed | C | Static HTML pages | `BLOCKED` | No statement of rights for the digital texts |
| 7 | [Feedbooks (public domain)](https://www.feedbooks.com/) | Books (EPUB, OPDS) | `PUBLIC_DOMAIN` | Public-domain catalogue | Unavailable | F | `/catalog/public_domain.atom` | `BLOCKED` | Cloudflare challenge on the OPDS feed |
| 8 | [HathiTrust](https://babel.hathitrust.org/) | Books (full view) | `PUBLIC_DOMAIN` | Full-view volumes are public domain | Disallowed | F | `catalog.hathitrust.org/api/volumes/brief/…` (allowed, metadata only); `babel…/cgi/pt` (disallowed) | `BLOCKED` | robots.txt disallows the reader paths; the allowed API is metadata only |
| 9 | [National Library of Scotland Digital Gallery](https://digital.nls.uk/) | Chapbooks, maps, manuscripts | `PUBLIC_DOMAIN` | Not reachable | Unavailable | F | — | `BLOCKED` | "Human Verification" page (405) |
| 10 | [e-codices](https://www.e-codices.unifr.ch/) | Swiss manuscripts (IIIF) | `OPEN_LICENSED` | IIIF manifests state `license: http://creativecommons.org/licenses/by-nc/4.0/` per manuscript | Allowed | B | `/metadata/iiif/<id>/manifest.json`, `/en/search/all?sQueryString=` | `HELD` | robots.txt allows `*` (Crawl-delay 10) but disallows AI agents by name, anthropic-ai and ClaudeBot among them. This round's work was done by an AI agent, so it stopped after four requests; a maintainer can build and verify it with OneShelf's own client |
| 11 | [NASA History Series](https://www.nasa.gov/history/history-publications-and-resources/nasa-history-series/) | US government history books (PDF) | `PUBLIC_DOMAIN` | US federal government works | Allowed | C | One long HTML page of PDF links (`/wp-content/uploads/…pdf`) | `QUEUED` | No per-book pages or search: a catalogue would be one page of a few hundred unrelated PDFs |
| 12 | [MetPublications](https://www.metmuseum.org/met-publications) | Museum books (PDF) | `RIGHTS_UNCLEAR` | Not reached | Unavailable | F | — | `BLOCKED` | HTTP 429 on the first request; not retried |
| 13 | [Getty Publications Virtual Library](https://www.getty.edu/publications/virtuallibrary/) | Museum books (PDF) | `RIGHTS_UNCLEAR` | Not reached | Unavailable | F | — | `BLOCKED` | The https address redirects to plain http, which OneShelf's egress policy refuses |
| 14 | [Pressbooks Directory](https://pressbooks.directory/) | Open textbooks | `OPEN_LICENSED` | Index of CC-licensed Pressbooks books | Unavailable | F | — | `BLOCKED` | Cloudflare challenge |
| 15 | [eCampusOntario Open Library](https://openlibrary.ecampusontario.ca/) | Open textbooks | `OPEN_LICENSED` | CC-licensed textbooks; licensing page | Allowed | C | Catalogue pages render in the browser; books live on many Pressbooks hosts | `QUEUED` | Item pages carry no book data in their HTML; each book's host would need its own domain |
| 16 | [SciELO Books](https://books.scielo.org/) | Open-access books (pt, es) | `OPEN_LICENSED` | Not reached | Unavailable | F | — | `BLOCKED` | "Establishing a secure connection…" bot-protection page (403) |
| 17 | [OpenEdition Books](https://books.openedition.org/) | Humanities books (fr, en, es, pt, it) | `OPEN_LICENSED` | Per book: CC licence block (a.license__logo) or the non-open "Licence OpenEdition Books" (Freemium) | Partial | B | `/<publisher>/<id>` (book, a.summary__link parts), part pages (div.full_text--main) | `IMPLEMENTED` | `oneshelf.openedition-books` — CC books as text; Freemium books have no units |
| 18 | [Fulcrum (catalogue facets)](https://www.fulcrum.org/) | Publishing platform | `OPEN_LICENSED` | Per book: Open Access indicator and CC licence | Partial | B | `/<press>.json?q=` and `/concern/monographs/<id>` reachable; faceted catalogue URLs behind Cloudflare | `COVERED` | Platform, not a source: its presses are read through the per-press JSON, as Lever Press already is — rows 34 and 35 |
| 19 | [African Minds](https://www.africanminds.org.za/) | Open-access books | `OPEN_LICENSED` | Not reached | Unavailable | F | — | `BLOCKED` | The https address redirects to plain http (refused by the egress policy) |
| 20 | [Firenze University Press](https://books.fupress.com/) | Open-access books (it, en) | `OPEN_LICENSED` | Book pages link CC BY 4.0 | Allowed | C | `/catalogue/<slug>/<id>`; no robots.txt (404) | `QUEUED` | The served HTML has no file links (downloads are assembled in the browser) |
| 21 | [meson press](https://meson.press/) | Media studies books (en, de) | `OPEN_LICENSED` | Per book: CC link on the page (81 of 91) | Allowed | B | `/books/<slug>/` (citation_language, Download PDF), `/wp-sitemap-posts-books-1.xml` | `IMPLEMENTED` | `oneshelf.meson-press` |
| 22 | [Give My Regards to Black Jack](https://mangaonweb.com/) | Manga | `CREATOR_AUTHORIZED` | Shuho Sato has allowed free secondary use since 2012 | Unavailable | F | — | `BLOCKED` | The site's domain is for sale; no official reading host found |
| 23 | [Diesel Sweeties](https://www.dieselsweeties.com/) | Webcomic | `RIGHTS_UNCLEAR` | The 2008 archive release was CC BY-NC (PDF volumes); the current site states no licence and links no PDFs | Allowed | C | Strip pages, RSS | `BLOCKED` | No licence on the current site |
| 24 | [eBible.org](https://ebible.org/) | Bible translations (1,551, ~1,000 languages) | `OPEN_LICENSED` | Per translation: /<id>/copyright.htm (public domain, CC BY-NC-ND, CC BY-SA, or All rights reserved); catalogue CSV | Allowed | A | `/find/details.php?id=`, `/<id>/copyright.htm`, `/epub/<id>.epub` | `IMPLEMENTED` | `oneshelf.ebible` |
| 25 | [eScholarship](https://escholarship.org/) | University of California OA | `OPEN_LICENSED` | Not reached | Unavailable | F | — | `BLOCKED` | CloudFront "request could not be satisfied" (403) |
| 26 | [University of Adelaide Press](https://adelaide.edu.au/library/about-the-library/university-press/) | Open-access books | `OPEN_LICENSED` | "most works offering a free online edition" | Allowed | D | Library page about the closed press | `BLOCKED` | The press closed in 2018; no live catalogue to adapt |
| 27 | [Tuwhera Open Access Books](https://ojs.aut.ac.nz/tuwhera-open-monographs/1/catalog) | Monographs (NZ) | `OPEN_LICENSED` | Per book: rel="license" CC BY / CC BY-NC 4.0 (all 12) | Allowed | A | OMP `search`, `catalog/book/<id>`, `catalog/download/<id>/<format>/<file>` | `IMPLEMENTED` | `oneshelf.tuwhera-open-books` |
| 28 | [Mominoun Without Borders](https://www.mominoun.com/) | Arabic studies and books | `RESTRICTED` | "© Copyright Mominoun Without Borders … All Rights Reserved" | Allowed | C | HTML | `BLOCKED` | All rights reserved; no grant to copy |
| 29 | [Project Gutenberg Canada](https://gutenberg.ca/) | Public-domain books | `PUBLIC_DOMAIN` | Canadian public domain | Unavailable | F | — | `BLOCKED` | The https address redirects to plain http (refused by the egress policy) |
| 30 | [Art Institute of Chicago publications](https://www.artic.edu/digital-publications) | Museum books (PDF) | `RIGHTS_UNCLEAR` | Free PDF downloads; no licence stated for the publications (the open-access programme covers images) | Allowed | B | `/print-publications/<id>/…` with PDF links | `BLOCKED` | No licence for the publications |
| 31 | [Ozy and Millie](https://ozyandmillie.org/) | Webcomic | `FREE_OFFICIAL` | "Copyright © 2025 Dana Simpson", free to read, no licence | Allowed | B | Strip pages | `BLOCKED` | Free to read only: no grant to keep a copy |
| 32 | [Spacetrawler](https://www.baldwinpage.com/spacetrawler/) | Webcomic | `FREE_OFFICIAL` | "Spacetrawler is copyright 2023 Christopher Baldwin", no licence | Allowed | B | WordPress, RSS | `BLOCKED` | Free to read only: no grant to keep a copy |
| 33 | [Bartleby](https://www.bartleby.com/) | Reference and classics | `PUBLIC_DOMAIN` | Not reached | Unavailable | F | — | `BLOCKED` | CloudFront "request could not be satisfied" (403) |
| 34 | [Amherst College Press](https://www.fulcrum.org/amherst) | Humanities books | `OPEN_LICENSED` | Per book: Open Access indicator and CC BY-NC(-ND) | Allowed | B | `/amherst.json`, `/concern/monographs/<id>` | `IMPLEMENTED` | `oneshelf.amherst-college-press` |
| 35 | [University of Michigan Press (open access)](https://www.fulcrum.org/michigan) | Scholarly books | `OPEN_LICENSED` | Per book: Open Access indicator and CC licence; the press also sells books | Allowed | C | `/michigan.json`, `/concern/monographs/<id>` | `IMPLEMENTED` | `oneshelf.university-of-michigan-press` — search lists sold books too (the open-access facet is challenged) |

## Implemented — seven adapters

All in `adapters/community/`, each with `rights.yaml`, packaged tests with exclusion cases where rights are
per item, and live checks on real works (`./tools/live-check`, 2026-10-07). Text adapters need a Core with
plugin API 1.2 (see *Core* below).

| Adapter | Capabilities | Rights gate | Live (2026-10-07) |
|---|---|---|---|
| `oneshelf.ebible` | work, catalog, downloads (EPUB) | the translation's own `/<id>/copyright.htm` says public domain or Creative Commons | 7 translations PASS (World English Bible, Arabic Van Dyck, Arabic NAV (CC BY-SA), Miniafia (CC BY-NC-ND), Louis Segond 1910, Lutherbibel 1912, Reina Valera 1909): EPUBs 1.8–11.5 MB validated; `mza` (All rights reserved) and `ronbtf` (copyright holder named) refused |
| `oneshelf.runeberg` | work, catalog, reader (text) | no Runeberg copyright notice; text editions only | 6 works PASS (Röda rummet 30, Kalevala 50, Nils Holgersson 99, Fadren 22, Peer Gynt 39 units; sv, fi, no); `pol95` (copyright notice), `aofram`, `nfbb`, `karenina` (facsimile scans) refused |
| `oneshelf.openedition-books` | work, catalog, reader (text) | the page's CC licence block | 6 books PASS (Open Book Publishers ×4, OpenEdition Press ×2; en, fr; 9–18 parts each); `cdf/10192` and `pur/314943` (Freemium) refused |
| `oneshelf.tuwhera-open-books` | search, work, catalog, downloads (EPUB, PDF) | rel="license" CC link | 7 of 12 books PASS (EPUB and PDF validated, 56–278 pages); all 12 checked for licences (9 CC BY, 3 CC BY-NC) |
| `oneshelf.meson-press` | work, catalog, downloads (PDF) | a CC link on the book page | 5 books PASS (PDFs 127–344 pages; de, en); `the-cyborg`, `politik-der-mikroentscheidungen` (no licence) refused; all 91 books read for licences (81 CC) |
| `oneshelf.amherst-college-press` | search, work, catalog, downloads (EPUB, PDF) | Open Access indicator and CC licence (as `oneshelf.lever-press`) | 5 of 6 books PASS; `3197xq18h` has an EPUB over live-check's 150 MB cap (a tooling limit; Core's download cap is 256 MB) |
| `oneshelf.university-of-michigan-press` | search, work, catalog, downloads (EPUB, PDF) | the same | 6 open-access books PASS; `td96k4269` (sold) and `1n79h7388` (open access without a licence) refused |

**Language and direction.** eBible maps Ethnologue codes to two-letter codes for 15 common languages (others stay
ISO 639-3). meson maps its language words. Runeberg and OpenEdition read the page's own language; text-unit
direction comes from it (Core). EPUBs are read in the Book Reader, whose frame follows the interface direction
(an existing Book Reader behaviour; the EPUB's own `dir` attributes survive sanitising).

**Identity.** Stable source ids throughout: eBible translation id, Runeberg `<work>/<page>`, OpenEdition
`<publisher>/<id>`, OMP book id, meson slug, Fulcrum monograph id. Where the source has no query search
(eBible, Runeberg, OpenEdition, meson) the adapter declares `url_patterns` so a pasted address opens the work —
OneShelf matches a pasted address against an adapter's own domains. Catalogs are single responses; a cut or
failed page is never complete (see *Core*).

## Core (OneShelf `feature/text-reading-units`, not on main, not the tooling pin)

Two generic fixes found while building these adapters, each with tests (backend: 1,361 passed):

- **c7fcce8 — a page cut at the item cap is never a complete list.** A list page with more than 5,000 items was
  cut silently and could still be reported complete, so a shortened catalog could replace a trusted one. Found
  on Runeberg's Nordisk familjebok index (12,786 links, 795 pages): 323 units, complete.
- **656550c — refuse an xpath field that yields a string or number.** `normalize-space()`, `string()`, `count()`
  return a value; Scrapling splits it into characters and the recipe crashed at run time. Package validation
  now refuses them (no published adapter used one).

## Queued — eligible or likely eligible, not built

- **Sefaria** (`C`, high value: Hebrew/Aramaic originals and translations, per-version licences, RTL). Design:
  search through `/api/name/<q>` (`completion_objects` of type `ref`); work from `/api/v2/index/<title>`;
  catalog from `/api/shape/<title>` — which gives only an array of verse counts, so a unit key needs the
  item's position (`<title>.<n>`) — a Core template placeholder for an item's 1-based position would express
  it; reader from `/api/v3/texts/<ref>?version=source`, whose verses are separate strings: the version's
  `license` gates through a document value (the NIJL/Acomics pattern), and Core would need to treat all text
  items of one reader result as one unit (today each item is sectioned separately). Talmud (amudim 2a/2b,
  empty leading slots) and complex texts do not map to positions and would be excluded. Translation choice
  by track language has no declarative form yet.
- **e-codices** (`B`, held): IIIF manifests with CC BY-NC 4.0, an HTML search, one adapter like
  `oneshelf.digital-bodleian`. Its robots.txt disallows AI agents by name; a maintainer should build and
  verify it with OneShelf's client (rate 6/min for its Crawl-delay 10).
- **The Latin Library**, **NASA History Series**, **eCampusOntario**, **Firenze University Press** (`C`): see the
  table for what each lacks.

## Findings outside these adapters

- `oneshelf.lever-press` still passes live; fulcrum.org's Cloudflare challenge applies only to faceted
  catalogue URLs.
- Tuwhera's own search does not find its newest book (17, *Rimurimu o Matapouri*), even by title — the
  press's index, not the adapter.
- OpenEdition keeps paragraph numbers inside paragraphs ("1The present volume…"); they remain in the text.
- Runeberg is mostly scanned facsimiles with raw OCR; its text editions (the older classics) are what this
  adapter reads. A facsimile reader would need a way to take the OCR without its proofreading notices.
