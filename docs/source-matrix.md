# Open-access source matrix

Every candidate source for the open-access Registry expansion, investigated on **2026-09-29** against
[source-discovery.md](source-discovery.md#4-open-access-eligibility): whether it is free in full, whether
robots.txt and the site allow the requests, which machine-readable interface it has, and what OneShelf can
actually read from it. Every source was inspected with `./tools/inspect-source` (Scrapling's parser, Core's
HTTP client, robots.txt first); every adapter passed its packaged tests and `./tools/live-check`, which runs
it through Core's runtime and fails on any robots-disallowed request. The capability and domain columns are
generated from the adapters' manifests.

| Status | Meaning |
|---|---|
| `EXISTING_VERIFIED` | Already an adapter; audited, fixed where needed, and live-verified in this pass |
| `VERIFIED` | New adapter: packaged tests pass and every declared capability passed a live check |
| `BLOCKED` | Not implementable now; the reason, the evidence and what would unblock it are recorded |


**60 candidates:** 3 existing and verified, 23 rows served by new verified adapters, 34 blocked. Two rows (Arabic and international Wikimedia Commons) share one adapter, so the rows map to 22 new adapters. New adapters are in `adapters/community/`; none is added to the snapshot OneShelf bundles.


## Arabic and Arabic-content sources

| # | Source | Adapter | Status | Tier | Capabilities | Languages | Access |
|---:|---|---|---|---|---|---|---|
| 1 | [Safahat / Hindawi Foundation](https://www.safahat.org/) | `oneshelf.hindawi` | `EXISTING_VERIFIED` | Official | search, work, catalog, downloads | ar | Free (publisher-offered) |
| 2 | [Booktime](https://www.booktime.org/ar/books) | — | `BLOCKED` | — | — | ar | Free, account-gated |
| 3 | [Arabic Wikisource](https://ar.wikisource.org/) | — | `BLOCKED` | — | — | ar | PD / CC |
| 4 | [Arabic Wikibooks](https://ar.wikibooks.org/) | — | `BLOCKED` | — | — | ar | CC BY-SA |
| 5 | [Arabic Collections Online (NYU)](https://aco.dlib.nyu.edu/) | `oneshelf.arabic-collections-online` | `VERIFIED` | Community | search, work, catalog, downloads | ar | Free (PD and permissioned) |
| 6 | [OpenITI Corpus](https://openiti.org/) | — | `BLOCKED` | — | — | ar, fa | CC |
| 7 | [DADD Library](https://dadd-initiative.org/library/) | — | `BLOCKED` | — | — | ar | Free (app) |
| 8 | [DADD Stories](https://dadd-initiative.org/library/dadd-stories-2/) | — | `BLOCKED` | — | — | ar | Free (app) |
| 9 | [Books by Habiba](https://booksbyhabiba.wordpress.com/) | `oneshelf.books-by-habiba` | `VERIFIED` | Community | search, work, catalog, downloads | arz (Egyptian Arabic) | CC (site statement) |
| 10 | [Global Storybooks](https://globalstorybooks.net/) | — | `BLOCKED` | — | — | ar and others | CC BY |
| 11 | [Storybooks Canada — Arabic](https://www.storybookscanada.ca/stories/ar/) | `oneshelf.storybooks-canada-arabic` | `VERIFIED` | Community | search, work, catalog, downloads | ar | CC BY 3.0/4.0 |
| 12 | [Multilingual English Storybooks — Arabic](https://englishstorybooks.org/stories/ar/) | `oneshelf.english-storybooks-arabic` | `VERIFIED` | Community | search, work, catalog, downloads | ar | CC BY |
| 13 | [African Storybook](https://www.africanstorybook.org/) | — | `BLOCKED` | — | — | many | CC |
| 14 | [Read, Learn and Play Arabic — Yale](https://campuspress.yale.edu/readlearnplayarabic/) | — | `BLOCKED` | — | — | ar | Free |
| 15 | [FSU Arabic Short Stories](https://arabicshortstories.create.fsu.edu/) | `oneshelf.fsu-arabic-short-stories` | `VERIFIED` | Community | search, work, catalog, downloads | ar | Free (licence not stated) |
| 16 | [Qatru](https://www.qatru.com/) | — | `BLOCKED` | — | — | ar | Unknown |
| 17 | [Qatar Digital Library](https://www.qdl.qa/) | — | `BLOCKED` | — | — | ar, en | Free |
| 18 | [Library of Congress — Arabic Language Rare Materials](https://www.loc.gov/collections/arabic-language-rare-materials-collection/) | — | `BLOCKED` | — | — | ar | PD / free |
| 19 | [Princeton — Islamic Manuscripts](https://digital-collections.princeton.edu/collections/islamicmss) | — | `BLOCKED` | — | — | ar, fa, tr | Copyright Not Evaluated |
| 20 | [University of Michigan — Islamic Manuscripts](https://www.lib.umich.edu/collections/collecting-areas/special-collections/islamic-manuscripts/) | — | `BLOCKED` | — | — | ar, fa, tr | PD (HathiTrust full view) |
| 21 | [Wellcome Collection — Arabic manuscripts](https://wellcomecollection.org/) | `oneshelf.wellcome-collection` | `VERIFIED` | Community | search, work, catalog, reader, downloads | ar, fa, en and more (ISO 639-2 mapped) | PDM / CC / open (per location) |
| 22 | [Digital Bodleian](https://digital.bodleian.ox.ac.uk/) | `oneshelf.digital-bodleian` | `VERIFIED` | Community | search, work, catalog, reader | ar, fa, tr and more (mapped) | Free to view (CC BY-NC 4.0 images) |
| 23 | [British Library — Digitised Arabic Manuscripts](https://www.bl.uk/) | — | `BLOCKED` | — | — | ar | Free |
| 24 | [University of Manchester — Arabic Manuscripts](https://www.digitalcollections.manchester.ac.uk/collections/arabic/) | `oneshelf.manchester-arabic-manuscripts` | `VERIFIED` | Community | search, work, catalog, reader | ar | Free to view (downloads CC BY-NC) |
| 25 | [Ambrosiana — Arabic Manuscripts](https://www.ambrosiana.it/en/discover/online-resources/arabic-manuscripts/) | — | `BLOCKED` | — | — | ar | Unknown |
| 26 | [University of Birmingham — Mingana Collection](https://www.birmingham.ac.uk/facilities/cadbury/birmingham-quran-mingana-collection/mingana-collection/digitized-manuscripts) | — | `BLOCKED` | — | — | ar, syr, fa, … | Free |
| 27 | [Munich Digital Collections (MDZ) — Arabic Manuscripts](https://www.digitale-sammlungen.de/en/arabic-manuscripts) | `oneshelf.mdz-arabic-manuscripts` | `VERIFIED` | Community | search, work, catalog, reader | ar | PDM / NoC (per object) |
| 28 | [Gallica — BnF](https://gallica.bnf.fr/) | `oneshelf.gallica` | `VERIFIED` | Community | work, catalog, reader | Unknown (multilingual) | Free (Gallica conditions of use) |
| 29 | [Wikimedia Commons — Scanned Arabic Books in PDF](https://commons.wikimedia.org/wiki/Category:Scanned_Arabic_books_in_PDF) | `oneshelf.wikimedia-commons` | `VERIFIED` | Community | search, work, catalog, downloads | per file, not stated | PD / free licences (Commons policy) |
| 30 | [Digital Library of the Middle East](https://dlmenetwork.org/) | — | `BLOCKED` | — | — | many | Aggregator |

## International sources

| # | Source | Adapter | Status | Tier | Capabilities | Languages | Access |
|---:|---|---|---|---|---|---|---|
| 1 | [Project Gutenberg](https://www.gutenberg.org/) | `oneshelf.gutenberg` | `EXISTING_VERIFIED` | Official | work, catalog, downloads | per book (mapped) | PD (US) |
| 2 | [Standard Ebooks](https://standardebooks.org/) | `oneshelf.standard-ebooks` | `EXISTING_VERIFIED` | Official | search, work, catalog, downloads | en | PD |
| 3 | [Wikisource](https://wikisource.org/) | — | `BLOCKED` | — | — | many | PD / CC |
| 4 | [Wikibooks](https://www.wikibooks.org/) | — | `BLOCKED` | — | — | many | CC BY-SA |
| 5 | [Directory of Open Access Books](https://www.doabooks.org/) | — | `BLOCKED` | — | — | many | OA (aggregator) |
| 6 | [OAPEN Library](https://library.oapen.org/) | `oneshelf.oapen` | `VERIFIED` | Community | search, work, catalog, downloads | many (mapped) | OA (mostly CC) |
| 7 | [OpenStax](https://openstax.org/) | `oneshelf.openstax` | `VERIFIED` | Community | search, work, catalog, downloads | en, es, pl | CC BY / BY-NC-SA |
| 8 | [Open Textbook Library](https://open.umn.edu/opentextbooks) | — | `BLOCKED` | — | — | many | OER (aggregator) |
| 9 | [LibreTexts](https://libretexts.org/) | `oneshelf.libretexts` | `VERIFIED` | Community | work, catalog, downloads | en, es, uk (from library) | OER (mostly CC; some permissioned) |
| 10 | [BCcampus Open Collection](https://open.bccampus.ca/) | `oneshelf.bccampus-open-textbooks` | `VERIFIED` | Community | work, catalog, downloads | en | CC (per book) |
| 11 | [Open Book Publishers](https://www.openbookpublishers.com/) | — | `BLOCKED` | — | — | en | OA |
| 12 | [MIT Press — Open Access Books](https://mitpress.mit.edu/open-access-at-mit-press/books/) | — | `BLOCKED` | — | — | en | OA subset |
| 13 | [MDPI Books](https://www.mdpi.com/books) | — | `BLOCKED` | — | — | en | OA |
| 14 | [Lever Press](https://www.leverpress.org/) | `oneshelf.lever-press` | `VERIFIED` | Community | search, work, catalog, downloads | en | OA (CC) |
| 15 | [Open Humanities Press](https://www.openhumanitiespress.org/books/) | — | `BLOCKED` | — | — | en | OA |
| 16 | [UCL Press](https://uclpress.co.uk/) | `oneshelf.ucl-press` | `VERIFIED` | Community | work, catalog, downloads | en | OA (CC) |
| 17 | [ANU Press](https://press.anu.edu.au/) | `oneshelf.anu-press` | `VERIFIED` | Community | search, work, catalog, downloads | en | Free (OA) |
| 18 | [Athabasca University Press](https://www.aupress.ca/) | `oneshelf.athabasca-university-press` | `VERIFIED` | Community | search, work, catalog, downloads | en | OA (CC) |
| 19 | [IntechOpen](https://www.intechopen.com/books) | `oneshelf.intechopen` | `VERIFIED` | Community | work, catalog, downloads | en | OA (CC BY) |
| 20 | [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/) | — | `BLOCKED` | — | — | en | Free subset |
| 21 | [JSTOR Open Content](https://www.jstor.org/open/) | — | `BLOCKED` | — | — | en | OA subset |
| 22 | [Biodiversity Heritage Library](https://www.biodiversitylibrary.org/) | — | `BLOCKED` | — | — | many | PD / CC |
| 23 | [National Academies Press](https://nap.nationalacademies.org/) | — | `BLOCKED` | — | — | en | Free, account-gated |
| 24 | [punctum books](https://punctumbooks.com/) | — | `BLOCKED` | — | — | en | OA |
| 25 | [Pepper&Carrot](https://www.peppercarrot.com/) | `oneshelf.peppercarrot` | `VERIFIED` | Community | work, catalog, reader | 47 ISO-identical site codes | CC BY 4.0 |
| 26 | [Comic Book Plus](https://comicbookplus.com/) | `oneshelf.comic-book-plus` | `VERIFIED` | Community | work, catalog, reader | per series (schema.org) | PD (read online free; downloads need an account) |
| 27 | [Library of Congress — Selected Digitized Books](https://www.loc.gov/collections/selected-digitized-books/) | — | `BLOCKED` | — | — | en | PD |
| 28 | [Library of Congress — World Digital Library](https://www.loc.gov/collections/world-digital-library/) | — | `BLOCKED` | — | — | many | PD |
| 29 | [Aozora Bunko](https://www.aozora.gr.jp/) | — | `BLOCKED` | — | — | ja | PD / free |
| 30 | [Wikimedia Commons](https://commons.wikimedia.org/) | `oneshelf.wikimedia-commons` | `VERIFIED` | Community | search, work, catalog, downloads | per file, not stated | PD / free licences |

## Details

Fields for every source. *Login* is no for every adapter; *Scrapling used* is `inspect-source` for every row (page structure, selectors, feeds and robots.txt), and the selectors that became recipes were checked with its `--css`/`--xpath`/`--json`, which run the runtime's own extraction. Packaged tests pass for every adapter.


### Arabic and Arabic-content

**1. Safahat / Hindawi Foundation** — `EXISTING_VERIFIED`, `oneshelf.hindawi`
- Access model: Free (publisher-offered)
- Transport: HTML
- Domains: www.safahat.org; files/media: downloads.hindawi.org
- Stable id: numeric book id
- Pagination / completeness: search: one page, whole result; catalog: one unit
- Formats: EPUB, PDF
- Languages: ar
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 611 results, 2.5 MB EPUB opened
- Notes: Unchanged. hindawi.org redirects to safahat.org; files on downloads.hindawi.org.

**2. Booktime** — `BLOCKED`
- Access model: Free, account-gated
- Blocker: Reading needs sign-in: the page's Read() sends visitors without a user id to /ar/account/sign-in; no downloadable files (app otherwise).

**3. Arabic Wikisource** — `BLOCKED`
- Access model: PD / CC
- Blocker: *.wikisource.org robots.txt disallows /w/, /api/ and Special:. Search works via api.wikimedia.org, but the only whole-book format is WS-Export (ws-export.wmcloud.org), whose robots.txt is Disallow: /. Wiki pages are HTML, which OneShelf cannot read as a book. Unblock: robots permission for WS-Export, or a Core HTML/text book format.

**4. Arabic Wikibooks** — `BLOCKED`
- Access model: CC BY-SA
- Blocker: Same robots.txt rules as Wikisource; WS-Export covers Wikisource only and the REST PDF renderer is under the disallowed /api/. No whole-book file.

**5. Arabic Collections Online (NYU)** — `VERIFIED`, `oneshelf.arabic-collections-online`
- Access model: Free (PD and permissioned)
- Transport: HTML
- Domains: aco.dlib.nyu.edu; files/media: mc.dlib.nyu.edu
- Stable id: ACO book id (e.g. aub_aco002657)
- Pagination / completeness: search: next link, capped at 2 pages, reports incomplete; work/catalog/downloads read the id search and require exactly one result
- Formats: PDF (low res; high res as variant)
- Languages: ar
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 63 MB PDF, 536 pages

**6. OpenITI Corpus** — `BLOCKED`
- Access model: CC
- Blocker: Corpus is OpenITI mARkdown plain text on GitHub/Zenodo; no EPUB, PDF or page images. Unblock: a Core plain-text book format.

**7. DADD Library** — `BLOCKED`
- Access model: Free (app)
- Blocker: App-only: the pages link only the App Store / Google Play apps and YouTube; no story files or pages on the web.

**8. DADD Stories** — `BLOCKED`
- Access model: Free (app)
- Blocker: As DADD Library: the "حكايات ض" app only.

**9. Books by Habiba** — `VERIFIED`, `oneshelf.books-by-habiba`
- Access model: CC (site statement)
- Transport: HTML
- Domains: booksbyhabiba.wordpress.com
- Stable id: decoded page slug
- Pagination / completeness: search: whole five-book menu, one response
- Formats: PDF (monolingual Egyptian Arabic edition)
- Languages: arz (Egyptian Arabic)
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: all five books' PDFs opened
- Notes: The site says the books are Cairene Arabic, not MSA; recorded as arz.

**10. Global Storybooks** — `BLOCKED`
- Access model: CC BY
- Blocker: The Arabic site (global-asp.github.io/storybooks-arabic) has no PDF or EPUB: HTML text over wordless pictures. The same 40 Arabic stories are readable through the two adapters below.

**11. Storybooks Canada — Arabic** — `VERIFIED`, `oneshelf.storybooks-canada-arabic`
- Access model: CC BY 3.0/4.0
- Transport: HTML
- Domains: www.storybookscanada.ca
- Stable id: African Storybook number (4 digits)
- Pagination / completeness: search: the whole one-page index
- Formats: PDF (monolingual Arabic)
- Languages: ar
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 40 stories, 412 kB PDF

**12. Multilingual English Storybooks — Arabic** — `VERIFIED`, `oneshelf.english-storybooks-arabic`
- Access model: CC BY
- Transport: HTML
- Domains: englishstorybooks.org; files/media: globalstorybooks.net
- Stable id: African Storybook number
- Pagination / completeness: search: the whole one-page index
- Formats: PDF (monolingual Arabic)
- Languages: ar
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 40 stories, 371 kB PDF
- Notes: No covers: they are on raw.githubusercontent.com, which would allow all of GitHub's raw files.

**13. African Storybook** — `BLOCKED`
- Access model: CC
- Blocker: Unsupported by Declarative Adapter: downloads (read/downloadepub.php, use/download.php) need an asbtoken cookie computed in the browser (CryptoJS.MD5 of the URL); recipes cannot set cookies.

**14. Read, Learn and Play Arabic — Yale** — `BLOCKED`
- Access model: Free
- Blocker: The "audio e-books" are MP4 videos and the reader helpers PowerPoint shows in an Office viewer; no EPUB, PDF or page images.

**15. FSU Arabic Short Stories** — `VERIFIED`, `oneshelf.fsu-arabic-short-stories`
- Access model: Free (licence not stated)
- Transport: HTML
- Domains: arabicshortstories.create.fsu.edu
- Stable id: slug book-<n>
- Pagination / completeness: search: whole one-page list
- Formats: PDF
- Languages: ar
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: all three stories' PDFs opened
- Notes: The site states no licence; the PDFs are offered publicly for free download.

**16. Qatru** — `BLOCKED`
- Access model: Unknown
- Blocker: TLS certificate verification fails for www.qatru.com; OneShelf does not connect to it.

**17. Qatar Digital Library** — `BLOCKED`
- Access model: Free
- Blocker: Every path, IIIF manifests included, answers with a Cloudflare "Just a moment…" challenge (403). Not bypassed.

**18. Library of Congress — Arabic Language Rare Materials** — `BLOCKED`
- Access model: PD / free
- Blocker: www.loc.gov, JSON API (?fo=json) included, answers with a Cloudflare challenge (403). Not bypassed.

**19. Princeton — Islamic Manuscripts** — `BLOCKED`
- Access model: Copyright Not Evaluated
- Blocker: IIIF manifests and PDFs are on figgy.princeton.edu, whose robots.txt is Disallow: /. Item pages show 51 reduced images without completeness evidence, and the rights statement is "Copyright Not Evaluated".

**20. University of Michigan — Islamic Manuscripts** — `BLOCKED`
- Access model: PD (HathiTrust full view)
- Blocker: The digitised copies are in HathiTrust; babel.hathitrust.org's robots.txt disallows /cgi/ (reader, page images, PDF).

**21. Wellcome Collection — Arabic manuscripts** — `VERIFIED`, `oneshelf.wellcome-collection`
- Access model: PDM / CC / open (per location)
- Transport: JSON API + IIIF
- Domains: api.wellcomecollection.org, iiif.wellcomecollection.org
- Stable id: work id; unit = b-number
- Pagination / completeness: search: page number to totalResults (capped at 4); catalog: id query through the access filter
- Formats: IIIF pages; PDF
- Languages: ar, fa, en and more (ISO 639-2 mapped)
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 147 pages, 44.9 MB PDF; the mixed-access work and a restricted manifest gave nothing
- Notes: Works with any non-open copy are excluded entirely; pages and PDF also need the manifest's own "open" hint.

**22. Digital Bodleian** — `VERIFIED`, `oneshelf.digital-bodleian`
- Access model: Free to view (CC BY-NC 4.0 images)
- Transport: JSON search + IIIF
- Domains: digital.bodleian.ox.ac.uk, iiif.bodleian.ox.ac.uk
- Stable id: object UUID
- Pagination / completeness: search: next links, 4 pages; only fq=completeness:Yes
- Formats: IIIF pages (≤2048 px)
- Languages: ar, fa, tr and more (mapped)
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 224 pages (= surfaceCount)
- Notes: No URL patterns, so partially digitised objects cannot enter by address.

**23. British Library — Digitised Arabic Manuscripts** — `BLOCKED`
- Access model: Free
- Blocker: www.bl.uk/manuscripts (Digitised Manuscripts) answers 404; not restored since the 2023 cyber-attack. BL's Arabic manuscripts on QDL are behind Cloudflare.

**24. University of Manchester — Arabic Manuscripts** — `VERIFIED`, `oneshelf.manchester-arabic-manuscripts`
- Access model: Free to view (downloads CC BY-NC)
- Transport: JSON search + IIIF
- Domains: www.digitalcollections.manchester.ac.uk; files/media: image.digitalcollections.manchester.ac.uk
- Stable id: classmark id MS-ARABIC-nnnnn
- Pagination / completeness: search: results 0–200 in one request, only the MS-ARABIC series kept
- Formats: IIIF pages (≤2048 px)
- Languages: ar
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 444 pages
- Notes: Catalogue is transliterated: Arabic-script queries find nothing.

**25. Ambrosiana — Arabic Manuscripts** — `BLOCKED`
- Access model: Unknown
- Blocker: The online resources lead to ambrosiana.nainuwa.com, whose robots.txt is Disallow: /.

**26. University of Birmingham — Mingana Collection** — `BLOCKED`
- Access model: Free
- Blocker: ePapers PDF links fail (http 301 → https 404, eprint 154); no machine-readable manuscript language ("Islamic Arabic 1154" is described as a Persian manuscript; the language field is the record's); its search is robots-disallowed.

**27. Munich Digital Collections (MDZ) — Arabic Manuscripts** — `VERIFIED`, `oneshelf.mdz-arabic-manuscripts`
- Access model: PDM / NoC (per object)
- Transport: JSON search + IIIF
- Domains: www.digitale-sammlungen.de, api.digitale-sammlungen.de
- Stable id: BSB id (bsbNNNNNNNN)
- Pagination / completeness: search: collection 154 + language ar, page number to numTotal (capped at 4)
- Formats: IIIF pages (≤2048 px)
- Languages: ar
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 391 pages; an InC book gave no unit and no page
- Notes: Scoped to the collection: MDZ also holds in-copyright works whose manifests list every page. Units and pages need an open rights statement.

**28. Gallica — BnF** — `VERIFIED`, `oneshelf.gallica`
- Access model: Free (Gallica conditions of use)
- Transport: IIIF
- Domains: gallica.bnf.fr
- Stable id: ark id
- Pagination / completeness: catalog: one unit per manifest
- Formats: IIIF pages (2048 px wide)
- Languages: Unknown (multilingual)
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 355 pages (Arabe 5847)
- Notes: No search: robots.txt Disallow: /*? covers the SRU API. Gallica stalled every connection for hours earlier the same day.

**29. Wikimedia Commons — Scanned Arabic Books in PDF** — `VERIFIED`, `oneshelf.wikimedia-commons`
- Access model: PD / free licences (Commons policy)
- Transport: API Portal (REST)
- Domains: api.wikimedia.org; files/media: upload.wikimedia.org, thumb.wikimedia.org
- Stable id: File: page name
- Pagination / completeness: search: first 100 matches
- Formats: PDF
- Languages: per file, not stated
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 12.8 MB, 350 pages
- Notes: Same adapter as the international Commons row: add incategory:"Scanned Arabic books in PDF" to a query.

**30. Digital Library of the Middle East** — `BLOCKED`
- Access model: Aggregator
- Blocker: robots.txt Disallow: / for every agent.


### International

**1. Project Gutenberg** — `EXISTING_VERIFIED`, `oneshelf.gutenberg`
- Access model: PD (US)
- Transport: OPDS (per book)
- Domains: www.gutenberg.org
- Stable id: ebook number
- Pagination / completeness: catalog: one unit
- Formats: EPUB 3
- Languages: per book (mapped)
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 474 kB EPUB opened
- Notes: Fixed to 2.0.0: Gutendex's robots.txt disallows /books/ (the API 1.x used), so it now reads gutenberg.org's per-book OPDS and has no search (gutenberg.org disallows /ebooks/search). Needs Core's live test updated.

**2. Standard Ebooks** — `EXISTING_VERIFIED`, `oneshelf.standard-ebooks`
- Access model: PD
- Transport: OPDS (query feeds)
- Domains: standardebooks.org
- Stable id: author/title path
- Pagination / completeness: search: one feed page (12)
- Formats: EPUB (+ advanced variant)
- Languages: en
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 711 kB EPUB opened
- Notes: Fixed to 1.1.0: a key's query could return several books and the first was taken; now only the entry whose id is the key. Unfiltered feeds are Patrons Circle only (401); query feeds are public.

**3. Wikisource** — `BLOCKED`
- Access model: PD / CC
- Blocker: As Arabic Wikisource.

**4. Wikibooks** — `BLOCKED`
- Access model: CC BY-SA
- Blocker: As Arabic Wikibooks.

**5. Directory of Open Access Books** — `BLOCKED`
- Access model: OA (aggregator)
- Blocker: Aggregator: DOAB hosts covers and exports only. In a 100-record sample 84 of 86 full-text links lead to library.oapen.org (readable through oneshelf.oapen), the rest to publishers' sites.

**6. OAPEN Library** — `VERIFIED`, `oneshelf.oapen`
- Access model: OA (mostly CC)
- Transport: DSpace REST (XML)
- Domains: library.oapen.org
- Stable id: handle number 20.500.12657/<n>
- Pagination / completeness: search: offset to an empty page (4 pages)
- Formats: PDF, EPUB (ORIGINAL bundle only)
- Languages: many (mapped)
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 29.8 MB PDF
- Notes: Crawl-delay 10 → 6 requests a minute.

**7. OpenStax** — `VERIFIED`, `oneshelf.openstax`
- Access model: CC BY / BY-NC-SA
- Transport: CMS API
- Domains: openstax.org; files/media: assets.openstax.org
- Stable id: book slug
- Pagination / completeness: search: one response; slug filter exact
- Formats: PDF
- Languages: en, es, pl
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 79 MB, 913 pages

**8. Open Textbook Library** — `BLOCKED`
- Access model: OER (aggregator)
- Blocker: Aggregator: in a 40-book sample the files are on 30 different hosts (Pressbooks sites, github.io, web.archive.org, amazon.com …). Its OpenStax books are covered by oneshelf.openstax.

**9. LibreTexts** — `VERIFIED`, `oneshelf.libretexts`
- Access model: OER (mostly CC; some permissioned)
- Transport: Commons API
- Domains: commons.libretexts.org; files/media: downloads.libretexts.org, storage.downloads.libretexts.org
- Stable id: Commons book id
- Pagination / completeness: catalog: one unit
- Formats: PDF
- Languages: en, es, uk (from library)
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 153-page Spanish PDF
- Notes: No search: the Commons catalogue endpoint ignores query and page and returns all 4,098 books.

**10. BCcampus Open Collection** — `VERIFIED`, `oneshelf.bccampus-open-textbooks`
- Access model: CC (per book)
- Transport: Pressbooks API + HTML
- Domains: opentextbc.ca
- Stable id: address slug on opentextbc.ca
- Pagination / completeness: catalog: one unit
- Formats: EPUB
- Languages: en
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 4.5 MB EPUB
- Notes: Scoped to opentextbc.ca (outcome B). The collection site is script-built with records on many hosts; the Pressbooks directory ignores its search parameter, so no search.

**11. Open Book Publishers** — `BLOCKED`
- Access model: OA
- Blocker: Vercel security checkpoint (429) for ordinary clients. Not bypassed. OBP books are deposited in OAPEN.

**12. MIT Press — Open Access Books** — `BLOCKED`
- Access model: OA subset
- Blocker: 403 Access Denied (bot protection) for ordinary clients. Not bypassed.

**13. MDPI Books** — `BLOCKED`
- Access model: OA
- Blocker: 403 Access Denied (bot protection). Not bypassed.

**14. Lever Press** — `VERIFIED`, `oneshelf.lever-press`
- Access model: OA (CC)
- Transport: Fulcrum JSON + HTML
- Domains: www.fulcrum.org
- Stable id: Fulcrum monograph id
- Pagination / completeness: search: page number to total_count (3 pages)
- Formats: EPUB, PDF
- Languages: en
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 117 MB EPUB opened
- Notes: Fulcrum also hosts restricted books: needs the Open Access indicator and a CC licence.

**15. Open Humanities Press** — `BLOCKED`
- Access model: OA
- Blocker: 403 Forbidden, and robots.txt times out. Not bypassed.

**16. UCL Press** — `VERIFIED`, `oneshelf.ucl-press`
- Access model: OA (CC)
- Transport: HTML (schema.org JSON-LD)
- Domains: uclpress.co.uk; files/media: discovery.ucl.ac.uk
- Stable id: book slug
- Pagination / completeness: catalog: one unit
- Formats: PDF (UCL Discovery)
- Languages: en
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 5.9 MB, 312 pages
- Notes: No search: robots.txt disallows /?s= and /search/. Also in OAPEN.

**17. ANU Press** — `VERIFIED`, `oneshelf.anu-press`
- Access model: Free (OA)
- Transport: HTML
- Domains: press.anu.edu.au; files/media: press-files.anu.edu.au
- Stable id: Drupal node id
- Pagination / completeness: search: page number to an empty page, capped at 2, reports incomplete
- Formats: PDF, EPUB
- Languages: en
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: whole-book PDF
- Notes: Forthcoming titles are excluded. Pasted addresses are not recognised (they do not carry the node id).

**18. Athabasca University Press** — `VERIFIED`, `oneshelf.athabasca-university-press`
- Access model: OA (CC)
- Transport: HTML
- Domains: www.aupress.ca
- Stable id: id-and-slug
- Pagination / completeness: search: next link (3 pages)
- Formats: PDF
- Languages: en
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: whole-book PDF
- Notes: Needs both the CC statement and the PDF on the page.

**19. IntechOpen** — `VERIFIED`, `oneshelf.intechopen`
- Access model: OA (CC BY)
- Transport: HTML
- Domains: www.intechopen.com; files/media: api.intechopen.com, cdnintech.com
- Stable id: book id; unit = chapter id
- Pagination / completeness: catalog: every chapter in book order, one response
- Formats: PDF per chapter
- Languages: en
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: six chapters, a chapter PDF
- Notes: No search: the site's search is built in the browser.

**20. NCBI Bookshelf** — `BLOCKED`
- Access model: Free subset
- Blocker: E-utilities work, but the books themselves are on www.ncbi.nlm.nih.gov, which answers with a reCAPTCHA page.

**21. JSTOR Open Content** — `BLOCKED`
- Access model: OA subset
- Blocker: Redirects to about.jstor.org; JSTOR's content is behind bot protection. Not bypassed.

**22. Biodiversity Heritage Library** — `BLOCKED`
- Access model: PD / CC
- Blocker: The API needs a personal key (none can ship in an adapter) and the site answers with a Cloudflare challenge.

**23. National Academies Press** — `BLOCKED`
- Access model: Free, account-gated
- Blocker: Now redirects to nationalacademies.org; free PDFs are behind login or guest login; online reading is per-chapter HTML.

**24. punctum books** — `BLOCKED`
- Access model: OA
- Blocker: Downloads are rendered by script; its books are in OAPEN and readable through oneshelf.oapen (e.g. The Poet as Experiencer).

**25. Pepper&Carrot** — `VERIFIED`, `oneshelf.peppercarrot`
- Access model: CC BY 4.0
- Transport: HTML
- Domains: www.peppercarrot.com
- Stable id: language code (listing); episode id (unit)
- Pagination / completeness: catalog: the whole episode list, translated episodes only
- Formats: page images
- Languages: 47 ISO-identical site codes
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: Arabic 8 episodes, 5 pages decoded; French 39
- Notes: No search (the site has none).

**26. Comic Book Plus** — `VERIFIED`, `oneshelf.comic-book-plus`
- Access model: PD (read online free; downloads need an account)
- Transport: HTML
- Domains: comicbookplus.com; files/media: box01.comicbookplus.com
- Stable id: series cid; issue dlid
- Pagination / completeness: catalog: every issue on the series page
- Formats: page images
- Languages: per series (schema.org)
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 217 pages decoded
- Notes: Images need the site as Referer (declared, as WEBTOON's). No search (embedded Google search).

**27. Library of Congress — Selected Digitized Books** — `BLOCKED`
- Access model: PD
- Blocker: Cloudflare challenge (403), JSON API included.

**28. Library of Congress — World Digital Library** — `BLOCKED`
- Access model: PD
- Blocker: Cloudflare challenge (403), JSON API included.

**29. Aozora Bunko** — `BLOCKED`
- Access model: PD / free
- Blocker: No EPUB or PDF. Unblock: a Core plain-text/HTML book format.

**30. Wikimedia Commons** — `VERIFIED`, `oneshelf.wikimedia-commons`
- Access model: PD / free licences
- Transport: API Portal (REST)
- Domains: api.wikimedia.org; files/media: upload.wikimedia.org, thumb.wikimedia.org
- Stable id: File: page name
- Pagination / completeness: search: first 100 matches
- Formats: PDF
- Languages: per file, not stated
- robots.txt: checked 2026-09-29; every live request allowed
- Live check: 2026-09-29: PASS: 12.8 MB, 350 pages
- Notes: commons.wikimedia.org's robots.txt disallows /w/ and /api/; the API Portal is allowed.

## Later additions

Adapters added after the 60-candidate audit, from the investigation backlog in
[candidate-sources.md](candidate-sources.md). Each carries a `rights.yaml` ([rights-model.md](rights-model.md)).

| Source | Adapter | Status | Tier | Capabilities | Languages | Access |
|---|---|---|---|---|---|---|
| [xkcd](https://xkcd.com/) | `oneshelf.xkcd` | `VERIFIED` | Community | work, catalog, reader | en | CC BY-NC 2.5 (site-wide) |

**xkcd** — `VERIFIED`, `oneshelf.xkcd`
- Access model: CC BY-NC 2.5 for the whole site ([licence](https://xkcd.com/license.html)); `rights.yaml`: open_license, source granularity, non-commercial, attribution required
- Transport: JSON interface ([documented](https://xkcd.com/json.html)) for each comic; the archive page (HTML) for the list
- Domains: xkcd.com; files/media: imgs.xkcd.com
- Stable id: comic number (its address, and the JSON's `num`)
- Pagination / completeness: catalog: the whole archive in one response (3,303 comics on 2026-09-29; there is no 404); reader: one page per comic
- Formats: page images (PNG/JPEG/GIF)
- Languages: en
- robots.txt: checked 2026-09-29; only /personal/ disallowed for all agents; every live request allowed
- Live check: 2026-09-29: PASS: catalog 3,303 complete, comic 1 image decoded (24,848 bytes JPEG); comic 3142 PASS; failure modes: 1608 (interactive, no image file) → no page offered; 404 (no such comic) → page_failed; 1190 → image redirects via c.xkcd.com to plain http and is refused by the egress policy. 12 of 12 randomly sampled comics serve their image directly
- Notes: No search (the site has none). The archive title of 3142 contains an unescaped tag and reads "-Style Pizza".

## Source Registry check — 2026-09-30

The whole tree was built into a Registry (`adapter_repo build-registry`, then `verify-registry`: verified)
and served as a local `file://` mirror to OneShelf Core at its current `main` (fa58db4), started with its
eight bundled Official adapters. Through the API the Sources → Source Registry screen calls:

- `GET /api/registry` lists all 31 adapters. The 23 Community adapters read `available`; Hindawi,
  3asq, arXiv, MangaDex, Tapas and WEBTOON read `installed`; Gutenberg 2.0.0 and Standard Ebooks 1.1.0 read
  `update_available`.
- Every Community adapter passes review (packaged tests run by Core), installs, and appears in
  `GET /api/sources` as active with the capabilities its manifest declares. The review lists exactly the
  manifest's domains as permissions — for xkcd `network:domain:xkcd.com` and `network:cdn:imgs.xkcd.com`.
- The Gutenberg 2.0.0 update adds `network:domain:www.gutenberg.org` and asks for it; Standard Ebooks 1.1.0
  adds none. Both install and read `installed` afterwards.
- An unsigned local mirror confers no trust: every package, Official ones included, has effective trust
  `community` from it. Official status reaches an installation only from the signed first-party Registry
  (review-policy.md), which this check does not replace.

## Blocker re-check — 2026-09-30

The blockers that are about access rather than structure were screened again with OneShelf's own
User-Agent, robots.txt first. None has lifted:

| Source | Result today |
|---|---|
| Qatru | no TLS connection |
| Qatar Digital Library | robots.txt disallows the search path; 403 challenge page |
| Library of Congress (three collections, `?fo=json`) | 403 challenge page, robots.txt included |
| Open Book Publishers | 429, robots.txt included |
| MIT Press OA, MDPI Books, Open Humanities Press | 403 |
| NCBI Bookshelf | **200 whose body is a reCAPTCHA page** ("Checking your browser") — a success status is not content |
| Biodiversity Heritage Library | 403 challenge page |
| British Library Digitised Manuscripts | `/manuscripts/` → 308 → 404 |

The structural blockers (robots.txt rules, app-only or text-only content, aggregators' third-party
hosts, cookies computed by page script) were not re-screened; they do not change without the source
changing its design.

## Findings outside the open-access scope

- **arXiv** and **MangaDex** (Official) request paths their robots.txt disallows: `export.arxiv.org` is
  `Disallow: /`, `api.mangadex.org` disallows `/at-home/` (the MangaDex reader). Not changed here; they need
  a maintainer decision.
- OneShelf Core's live suite (`tests/live`) searches Gutenberg; Gutenberg 2.0.0 has no search, so the
  **Live source check** workflow needs that test updated in Core.
- Core's runtime raises an uncategorised `TypeError` on an XPath that returns a number (such as `count()`),
  which its schema accepts.
- The Core package that `./tools/bootstrap` installs from the pinned commit carries no `.sql` schema
  migrations (they are not package data), so tooling that opens a OneShelf library fails with "no such
  table". The final install check here loaded them from the pinned commit instead.
- JSON recipes cannot filter items by a value, and a strict list (catalog, reader, downloads) marks itself
  incomplete when any item is skipped. Open-access gates here use XPath predicates or a template joined with
  a document-level value and a pattern; a small Core filter primitive would make these simpler.
