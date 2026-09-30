# Candidate sources — investigation backlog

Sources proposed after the 60-candidate audit in [source-matrix.md](source-matrix.md). **Nothing here is
verified because it is listed.** A row moves to `VERIFIED_CANDIDATE` only on evidence, and an adapter reaches
source-matrix.md only after its packaged tests and a live check pass. Rights terms follow
[rights-model.md](rights-model.md): being free to view is not a licence to keep a copy.

Screened **2026-09-29** from this environment with OneShelf's own User-Agent
(`OneShelf/0.1 (+self-hosted personal library)`): one request for each host's robots.txt, evaluated with the
repository's RFC 9309 matcher (`tools/lib/inspect_source.py`), then one request for the path an adapter would
need. No challenge was solved, no browser identity assumed, no login used. A 403 or 429 on the very first
request is recorded as what this client meets, not worked around.

| Status | Meaning |
|---|---|
| `RESEARCH` | Reachable or plausible; the rights, formats or interface are not established yet |
| `VERIFIED_CANDIDATE` | Evidence shows an adapter is feasible within the rules; not built |
| `IMPLEMENTING` | An adapter is being built |
| `BLOCKED` | Cannot be built now; the blocker and what would unblock it are recorded |
| `OUT_OF_SCOPE` | Content OneShelf cannot read today (e.g. plain text only) |
| `REJECTED` | Should not be built (closed, or rights cannot be satisfied) |

A field reading *not checked* has not been established — it is not a guess of "no".

## Summary

### The four sources assigned for implementation

| Source | Status | Result |
|---|---|---|
| xkcd | `VERIFIED_CANDIDATE` → built | `oneshelf.xkcd`, verified; in source-matrix.md |
| Book Dash | `BLOCKED` | Full books only through a reCAPTCHA download flow; files 403 on signed CloudFront; page gallery is partial |
| OPenn — Manuscripts of the Muslim World | `BLOCKED` | Host unreachable from here (three attempts, three clients) |
| Leiden University Digital Collections | `BLOCKED` | IIIF manifests now served from a host whose robots.txt is `Disallow: /`; portal behind an F5 bot challenge |

### Arabic and Arabic-content

| # | Source | Status | Blocker / next step |
|---:|---|---|---|
| A1 | IslamHouse | `RESEARCH` | Guessed book and API paths 404; the public API's documented URLs embed a shared key, which may not be shipped |
| A2 | Internet Archive — Arabic texts | `RESEARCH` | `licenseurl` is uploader-asserted and unreliable (see evidence); not started, per instructions |
| A3 | Leiden University Digital Collections | `BLOCKED` | See above |
| A4 | Staatsbibliothek zu Berlin — Oriental manuscripts | `RESEARCH` | IIIF manifest carries no licence; per-item rights must come from METS |
| A5 | DigiVatLib (Vatican Library) | `BLOCKED` | Manifest: "Images Copyright Biblioteca Apostolica Vaticana", no licence → free to view only; `/search` disallowed |
| A6 | OPenn — Manuscripts of the Muslim World | `BLOCKED` | See above |
| A7 | Bloom Library | `BLOCKED` | API needs partner/Enterprise credentials; keys cannot ship in an adapter |
| A8 | Bibliotheca Alexandrina DAR | `RESEARCH` | Mixed: free full text beside preview-only copyrighted books; needs a machine-readable free flag |
| A9 | Qatar National Library repository | `RESEARCH` | Rights statement per item not checked |
| A10 | StoryWeaver | `RESEARCH` | Search API returned 500; download sign-in not checked |
| A11 | Al-Maktaba al-Shamela | `RESEARCH` | Likely text-only (`OUT_OF_SCOPE`), formats not checked |
| A12 | vHMML Reading Room | `RESEARCH` | Account requirement not checked |
| A13 | Cambridge Digital Library — Islamic | `BLOCKED` | 403 to this client, robots.txt included |
| A14 | Harvard — Islamic Heritage Project | `BLOCKED` | 429 on the first request, robots.txt included; retry later |
| A15 | King Fahd Glorious Qur'an Printing Complex | `RESEARCH` | Download formats and terms not checked |
| A16 | Quran.com API | `OUT_OF_SCOPE` | JSON text; no EPUB, PDF or page images |
| A17 | AUC FOUNT | `RESEARCH` | Institutional repository, mostly theses; per-item licences |
| A18 | AUB ScholarWorks | `RESEARCH` | As above |
| A19 | MSU Open Books — *Elementary Arabic* | `BLOCKED` | 403 to this client, robots.txt included |
| A20 | 3asafeer | `RESEARCH` | Freemium; free stories must be separable by machine-readable evidence |
| A21 | Library of Arabic Literature | `BLOCKED` | robots.txt disallows `/books/` for all agents |
| A22 | Waqfeya | `BLOCKED` | Unreachable; rights doubtful (scans of in-copyright books) |
| A23 | Noor Book | `BLOCKED` | Unreachable; rights doubtful |
| A24 | Institut du monde arabe digital library | `BLOCKED` | Unreachable |

### International

| # | Source | Status | Blocker / next step |
|---:|---|---|---|
| I1 | Internet Archive | `RESEARCH` | As A2 |
| I2 | Europe PMC | `RESEARCH` | Articles fit Core's `paper` type (as arXiv); PDF render path and its robots rule not checked |
| I3 | Language Science Press | `VERIFIED_CANDIDATE` | CC BY 4.0 on the book page; PDF on Zenodo `/records/…/files/` (allowed; Zenodo's `/api/` is not) |
| I4 | Book Dash | `BLOCKED` | See above |
| I5 | Free Kids Books | `RESEARCH` | Licence varies per book |
| I6 | Saylor Academy textbooks | `RESEARCH` | Book list rendered without static PDF or licence links |
| I7 | Milne Open Textbooks | `RESEARCH` | Site CC BY 4.0; per-book licences and file hosts not checked |
| I8 | xkcd | `VERIFIED_CANDIDATE` → built | `oneshelf.xkcd` |
| I9 | Open Research Library | `RESEARCH` | File hosts not checked |
| I10 | Manchester Hive | `RESEARCH` | Mixed paid/OA; needs an OA flag |
| I11 | Stockholm University Press | `BLOCKED` | 403 to this client, robots.txt included |
| I12 | Helsinki University Press | `BLOCKED` | 403 to this client, robots.txt included |
| I13 | Ubiquity partner presses | `RESEARCH` | Directory reachable; the presses' own sites 403 (I11, I12) |
| I14 | Pressbooks networks (Open Oregon) | `BLOCKED` | 403 to this client, robots.txt included |
| I15 | Wormworld Saga | `RESEARCH` | Free to read; no open licence found yet → reader not allowed without one |
| I16 | Freefall | `RESEARCH` | http only; free to read, licence not found |
| I17 | Unite for Literacy | `RESEARCH` | robots.txt redirects; licence not checked |
| I18 | Let's Read (The Asia Foundation) | `RESEARCH` | robots.txt returns HTML; CC licence per book not checked |
| I19 | International Children's Digital Library | `RESEARCH` | http only; robots.txt unreachable |
| I20 | Room to Read Literacy Cloud | `RESEARCH` | Sign-in requirement not checked |
| I21 | Europeana | `BLOCKED` | API returns 401 without a personal key |
| I22 | DPLA | `BLOCKED` | API returns 403 without a personal `api_key` |
| I23 | Open Library | `BLOCKED` | robots.txt disallows `search.json` |
| I24 | Zenodo (as a source) | `BLOCKED` | robots.txt disallows `/api/` |
| I25 | HAL | `BLOCKED` | robots.txt disallows the search API path |
| I26 | Springer Nature OA books | `BLOCKED` | robots.txt disallows `/search` |
| I27 | De Gruyter Brill OA | `BLOCKED` | robots.txt disallows `/search` |
| I28 | Digital Comic Museum | `BLOCKED` | 403 with a bot challenge |
| I29 | Feedbooks public domain | `REJECTED` | Closed March 2024; domain redirects to Cantook |

## Details

Each entry uses the same fields. Evidence links are the pages that state a claim, fetched on the
*Last Verified* date.

### xkcd — `VERIFIED_CANDIDATE`, built as `oneshelf.xkcd`

- **URL:** https://xkcd.com/
- **Content Types:** comic (one image per comic; some interactive comics have none)
- **Languages:** en
- **Discovery Method:** archive page `https://xkcd.com/archive/`, every comic in one response
- **Metadata Method:** official JSON interface `https://xkcd.com/{n}/info.0.json`
- **Reader Method:** the JSON's `img` (images on imgs.xkcd.com)
- **Download Method:** none (no book file; the reader's CBZ is the local copy)
- **Authentication:** none
- **Rate Limit:** none published; adapter uses 20/min, concurrency 1. `Cache-Control: max-age=300`
- **Robots Status:** allowed — only `/personal/` disallowed for `*`
- **Access Scope:** whole_source · **Access Type:** open_license
- **License:** CC BY-NC 2.5 · **Rights Granularity:** source
- **Redistribution:** with attribution, non-commercial · **Commercial Use:** not allowed
- **Stable ID:** comic number · **Canonical URL:** `https://xkcd.com/{n}/`
- **Pagination:** none (single response) · **Incremental Sync:** archive is newest-first; `info.0.json` gives the latest number
- **Blocker:** none. Limits: interactive comics (1608, 1663…) have no image file; 1190's image redirects via c.xkcd.com to plain http and is refused
- **Evidence:** licence https://xkcd.com/license.html · JSON interface https://xkcd.com/json.html · robots https://xkcd.com/robots.txt
- **Last Verified:** 2026-09-29

### Book Dash — `BLOCKED`

- **URL:** https://bookdash.org/books/
- **Content Types:** picture books · **Languages:** 11 South African languages plus SASL and wordless (ISO 639-3 taxonomy slugs: eng, afr, xho, zul, nso, sot, tsn, ssw, ven, tso, nbl…)
- **Discovery Method:** WordPress REST `https://bookdash.org/wp-json/wp/v2/books` (id, slug, title, `languages` term ids); listing pages `/books/page/N/`
- **Metadata Method:** WordPress REST; book page JSON-LD (inLanguage)
- **Reader Method:** none complete — the book page's gallery shows a selection of pages (for *The Window Seat*: pages 4–15 and 17), not the book
- **Download Method:** `/book-source-files/?book={slug}&folder=/e-book/{lang}` lists `?view-file=` and `?download=` links for a PDF. Both redirect to `d3qawc7yl9x4zs.cloudfront.net`, which returns **403** to a plain request. The page's download form loads Google reCAPTCHA (`recaptcha/api.js`) and offers "Skip sharing details and proceed with download"; the working path evidently depends on that browser flow (a signed or cookie-scoped CloudFront URL)
- **Authentication:** none for viewing; downloads via a reCAPTCHA-scripted flow
- **Rate Limit:** not published · **Robots Status:** allowed (`Disallow:` empty, Yoast block)
- **Access Scope:** whole_source · **Access Type:** open_license · **License:** CC BY 4.0 (site-wide statement) · **Rights Granularity:** source
- **Redistribution:** allowed with attribution per the crediting guidelines · **Commercial Use:** allowed by CC BY 4.0
- **Stable ID:** WordPress post id / slug · **Canonical URL:** `https://bookdash.org/books/{slug}/`
- **Pagination:** REST `page`/`per_page` (totals only in `X-WP-Total` headers, which recipes cannot read)
- **Incremental Sync:** REST `modified_after` (not checked)
- **Current Status:** `BLOCKED`
- **Blocker:** no complete book is reachable by an honest client without executing the site's reCAPTCHA download flow; forging a Referer, cookies or signed URLs would bypass an access control. The partial gallery is not the book. **Unblock:** a public, stable file URL (the source-files host without signing), an OPDS/API from Book Dash, or the same books from a partner platform with public files.
- **Evidence:** licence https://bookdash.org/who-we-are/open-content-partners/ ("Creative Commons CC BY 4.0 license") · crediting https://bookdash.org/book-dash-crediting-requirements_and-identity-guidelines/ · REST https://bookdash.org/wp-json/wp/v2/books?per_page=1&slug=the-window-seat · file listing https://bookdash.org/book-source-files/?book=the-window-seat&folder=/e-book/en_english · 403 https://bookdash.org/book-source-files/?view-file=the-window-seat/e-book/en_english/the-window-seat_en.pdf · robots https://bookdash.org/robots.txt
- **Last Verified:** 2026-09-29

### OPenn — Manuscripts of the Muslim World — `BLOCKED`

- **URL:** https://openn.library.upenn.edu/html/muslimworld_contents.html
- **Content Types:** manuscripts (page images) · **Languages:** ar, fa, tr and others (per TEI)
- **Discovery / Metadata / Reader / Download:** per the site's own documentation, static HTML contents pages, TEI P5 XML per object, and plain image files; *not checked live*
- **Authentication:** none (documented) · **Rate Limit / Robots Status:** not checked — robots.txt unreachable
- **Access Type / License:** documented as CC0 or CC BY per collection; *not checked live*
- **Current Status:** `BLOCKED`
- **Blocker:** `openn.library.upenn.edu` did not answer from this environment: TCP connect timeout with curl (20 s) and with Core's HTTP client, in two sessions, and WebFetch did not complete within 300 s. No fixture can be taken and no live check run. **Unblock:** retry from another network; if reachable, build from the TEI (rights) and image files (reader).
- **Evidence:** read-me https://openn.library.upenn.edu/ReadMe.html (search-engine snippet, not fetched) · Penn announcement https://almanac.upenn.edu/articles/penn-libraries-openn-service-a-digital-platform-for-viewing-ancient-manuscripts
- **Last Verified:** 2026-09-29 (unreachable)

### Leiden University Digital Collections — `BLOCKED`

- **URL:** https://digitalcollections.universiteitleiden.nl/
- **Content Types:** manuscripts, printed books, maps · **Languages:** ar, fa, tr, nl, la, …
- **Discovery Method:** the portal's search — robots.txt disallows `/search/` and `/?q=search/`
- **Metadata / Reader Method:** IIIF Presentation 3. `…/iiif_manifest/item:{n}/manifest` redirects (via `iiif-endpoint.universiteitleiden.nl`) to `https://catalogue.leidenuniv.nl/view/iiif/presentation/31UKB_LEU/{alma id}/manifest?iiifVersion=3`; images on `eu-img02.ext.exlibrisgroup.com`
- **Rights in the manifest:** per item — e.g. Or. 298: `rights: https://creativecommons.org/publicdomain/mark/1.0/`, metadata "Rights: Full access." — good machine-readable evidence
- **Authentication:** none · **Rate Limit:** portal robots.txt `Crawl-delay: 10`
- **Robots Status:** `catalogue.leidenuniv.nl/robots.txt` is `User-agent: *` / `Disallow: /` — **every manifest is disallowed**
- **Anti-bot:** the portal intermittently answers with an F5 "TSPD" JavaScript challenge page ("Toegang geblokkeerd / Access Blocked"), robots.txt included
- **Access Scope:** per_item · **Access Type:** mixed (PDM on the sampled item) · **Rights Granularity:** item
- **Stable ID:** handle `hdl.handle.net/1887.1/item:{n}` · **Canonical URL:** `https://digitalcollections.universiteitleiden.nl/view/item/{n}`
- **Current Status:** `BLOCKED`
- **Blocker:** the only manifest host disallows all agents; the portal is behind a bot challenge that must not be solved. **Unblock:** Leiden allowing `/view/iiif/` in catalogue.leidenuniv.nl's robots.txt, or an alternative public IIIF endpoint (the old `iiif_manifest` path returned 404 "No manifest available" for a non-existent id and redirects for real ones).
- **Evidence:** manifest redirect https://digitalcollections.universiteitleiden.nl/iiif_manifest/item:2000455/manifest · manifest https://catalogue.leidenuniv.nl/view/iiif/presentation/31UKB_LEU/12505879300002711/manifest?iiifVersion=3 · robots https://catalogue.leidenuniv.nl/robots.txt · portal robots https://digitalcollections.universiteitleiden.nl/robots.txt · item https://digitalcollections.universiteitleiden.nl/view/item/2000455
- **Last Verified:** 2026-09-29

### Language Science Press — `VERIFIED_CANDIDATE`

- **URL:** https://langsci-press.org/catalog · **Content Types:** book (linguistics monographs) · **Languages:** mostly en
- **Discovery Method:** OMP catalog pages (an OMP OAI-PMH endpoint is likely; not checked)
- **Metadata Method:** `citation_*` meta tags on each book page
- **Download Method:** PDF on Zenodo, e.g. `https://zenodo.org/record/6907848/files/350.pdf?download=1` — Zenodo's robots.txt allows `/record(s)/…/files/`, disallows `/api/`
- **Authentication:** none · **Robots Status:** allowed (langsci-press.org and the Zenodo file path)
- **Access Type:** open_license · **License:** CC BY 4.0 (linked on the book page) · **Rights Granularity:** item (the book page links its licence; one page checked)
- **Commercial Use / Redistribution:** allowed (CC BY) · **Stable ID:** OMP book id (`/catalog/book/{n}`)
- **Current Status:** `VERIFIED_CANDIDATE`
- **Blocker:** none found. Next: confirm the Zenodo redirect chain and that every book page links a CC licence (gate on it)
- **Evidence:** book page https://langsci-press.org/catalog/book/350 · Zenodo robots https://zenodo.org/robots.txt
- **Last Verified:** 2026-09-29

### Internet Archive (Arabic texts and public-domain texts) — `RESEARCH`

- **URL:** https://archive.org/ · **Discovery Method:** `advancedsearch.php` (allowed; JSON) · **Metadata Method:** `/metadata/{id}` (allowed)
- **Rights evidence:** `licenseurl` is set by the uploader. A sample of 15 Arabic `texts` items returned 4 with the Public Domain Mark — one of them `AcroRd32_20181107` — and one `access-restricted-item: true` (lending library); another is a `waqfeya_` mirror. A licence-field filter alone is **not** robust gating
- **Current Status:** `RESEARCH` — not started, as instructed
- **Next:** restrict to curated collections with institutional rights statements (e.g. a library's own PD scans), exclude `access-restricted-item`, and prove with fixtures
- **Evidence:** https://archive.org/advancedsearch.php?q=language%3Aara+AND+mediatype%3Atexts&fl%5B%5D=identifier&fl%5B%5D=licenseurl&fl%5B%5D=access-restricted-item&rows=15&output=json · https://archive.org/metadata/ArIslamicbooks · https://archive.org/robots.txt
- **Last Verified:** 2026-09-29

### Staatsbibliothek zu Berlin — `RESEARCH`

- **URL:** https://digital.staatsbibliothek-berlin.de/suche?category=Orientalische+Handschriften
- **Metadata / Reader Method:** IIIF Presentation 2, `https://content.staatsbibliothek-berlin.de/dc/{PPN}/manifest` (reachable; robots.txt present)
- **Rights:** the library states PDM 1.0 for works published before 1920, "in exceptional cases" other licences — but the sampled manifest has no `license`/`attribution`, so per-item evidence must come from METS
- **Robots Status:** digital.staatsbibliothek-berlin.de robots.txt 404 (no rules); content host has robots.txt
- **Blocker:** per-item machine-readable rights not yet located
- **Evidence:** policy https://lab.sbb.berlin/dc/?lang=en · manifest https://content.staatsbibliothek-berlin.de/dc/PPN867445300/manifest
- **Last Verified:** 2026-09-29

### DigiVatLib — `BLOCKED`

- **URL:** https://digi.vatlib.it/ · **Metadata / Reader Method:** IIIF Presentation 2 (e.g. Vat.ar.1, 634 canvases)
- **Rights:** manifest `attribution: "Images Copyright Biblioteca Apostolica Vaticana"`, no `license` → **free_to_read**; a reader (which saves a CBZ) is not permitted
- **Robots Status:** `/search`, `/*/search`, `/*/detail/*`, `/about` disallowed
- **Blocker:** rights. **Unblock:** a licence or written permission for local copies
- **Evidence:** https://digi.vatlib.it/iiif/MSS_Vat.ar.1/manifest.json · https://digi.vatlib.it/robots.txt
- **Last Verified:** 2026-09-29

### Bloom Library — `BLOCKED`

- **URL:** https://bloomlibrary.org/ · **Discovery Method:** OPDS `https://api.bloomlibrary.org/v1/opds`
- **Authentication:** "We will set up your account and provide you with the credentials" — key format `key=ACCOUNT:KEY`, granted with a Bloom Enterprise subscription or a content-sharing partnership
- **Formats:** PDF, ePUB, bloomPUB per entry; licence in `dcterms:license` (cc-by-sa, cc-by-nc-nd, …) — good per-item evidence
- **Blocker:** personal/partner credentials cannot ship in an adapter. **Unblock:** a keyless public feed, or a Core per-user credential setting
- **Evidence:** https://docs.bloomlibrary.org/opds/
- **Last Verified:** 2026-09-29

### Europeana, DPLA — `BLOCKED`

- **Authentication:** Europeana Search API requires a personal key (`wskey`, moving to a header; keys from a Europeana account) — 401 without one. DPLA requires a 32-character `api_key` issued by email — 403 without one
- **Blocker:** personal keys cannot ship. **Unblock:** Core per-user credentials
- **Evidence:** https://pro.europeana.eu/page/get-api · https://europeana.atlassian.net/wiki/spaces/EF/pages/2462351393/Accessing+the+APIs · https://pro.dp.la/developers/api-basics · https://api.europeana.eu/record/v2/search.json?query=arabic (401) · https://api.dp.la/v2/items?q=arabic (403)
- **Last Verified:** 2026-09-29

### Feedbooks — `REJECTED`

- Closed on 2024-03-15; feedbooks.com redirects to Cantook (FR/BE/CH/LU only); `/publicdomain` returned 403 with a challenge page
- **Evidence:** https://blog.the-ebook-reader.com/2024/03/01/feedbooks-closing-download-your-ebooks-before-theyre-gone/ · https://en.wikipedia.org/wiki/Feedbooks
- **Last Verified:** 2026-09-29

### Robots-disallowed APIs — `BLOCKED`

Checked with the RFC 9309 matcher on 2026-09-29:

| Source | Path needed | Verdict | Evidence |
|---|---|---|---|
| Open Library | `/search.json` | disallowed | https://openlibrary.org/robots.txt |
| Zenodo | `/api/records` | disallowed | https://zenodo.org/robots.txt |
| HAL | `api.archives-ouvertes.fr/search/` | disallowed | https://api.archives-ouvertes.fr/robots.txt |
| Springer Nature | `link.springer.com/search` | disallowed | https://link.springer.com/robots.txt |
| De Gruyter Brill | `/search` | disallowed | https://www.degruyterbrill.com/robots.txt |
| Library of Arabic Literature | `/books/` | disallowed | https://www.libraryofarabicliterature.org/robots.txt |

### First-contact refusals — `BLOCKED`

The host refused this client before any page was read (robots.txt included), so nothing about the source
can be verified from here. Retrying from another network, or asking the operator, is the path forward — not
changing the User-Agent.

| Source | URL | Response |
|---|---|---|
| Cambridge Digital Library | https://cudl.lib.cam.ac.uk/collections/islamic/1 | 403 |
| Harvard Islamic Heritage Project | https://curiosity.lib.harvard.edu/islamic-heritage-project | 429 |
| MSU Open Books | https://openbooks.lib.msu.edu/arb101/ | 403 |
| Stockholm University Press | https://www.stockholmuniversitypress.se/ | 403 |
| Helsinki University Press | https://hup.fi/ | 403 |
| Open Oregon (Pressbooks) | https://openoregon.pressbooks.pub/ | 403 |
| Digital Comic Museum | https://digitalcomicmuseum.com/ | 403, challenge page |
| Waqfeya | https://waqfeya.com/ | no connection |
| Noor Book | https://www.noor-book.com/ | no connection |
| Institut du monde arabe | https://bibliotheque-numerique.imarabe.org/ | no connection |

### Remaining `RESEARCH` and `OUT_OF_SCOPE` rows

Reachability and robots only; rights, formats and interfaces are the next step for each.

| Source | URL | robots.txt for that path | Page status | Note |
|---|---|---|---|---|
| IslamHouse | https://islamhouse.com/ | allowed | 404 on `/ar/books/` | Find the real listing path; API URLs embed a shared key |
| Bibliotheca Alexandrina DAR | https://dar.bibalex.org/ | none (404) | 302 | Mixed free/preview |
| QNL repository | https://ediscovery.qnl.qa/ar/islandora | allowed | 200 | Islandora; rights per item |
| StoryWeaver | https://storyweaver.org.in/ | allowed | 200 (search API 500) | CC BY 4.0 claimed; download sign-in |
| Shamela | https://shamela.ws/ | none (404) | 200 | Probably text only |
| vHMML | https://www.vhmml.org/readingRoom/ | allowed | 200 | Account model |
| King Fahd Complex | https://qurancomplex.gov.sa/ | allowed | 200 | Mushaf PDFs? terms? |
| Quran.com API (`OUT_OF_SCOPE`) | https://api.quran.com/api/v4/chapters | none (404) | 200 JSON | Text only |
| AUC FOUNT | https://fount.aucegypt.edu/ | allowed | 200 | Repository (theses) |
| AUB ScholarWorks | https://scholarworks.aub.edu.lb/ | allowed | 200 | Repository (theses) |
| 3asafeer | https://3asafeer.com/ | allowed | 200 | Freemium |
| Europe PMC | https://www.ebi.ac.uk/europepmc/webservices/rest/search | allowed | 200 JSON, no key | `paper` content type; PDF path |
| Free Kids Books | https://freekidsbooks.org/ | allowed | 200 | Per-book licence |
| Saylor Academy | https://saylor.org/books/ | none (404) | 200 | No static PDF/licence links |
| Milne Open Textbooks | https://milneopentextbooks.org/ | allowed | 200 | CC BY 4.0 site statement |
| Open Research Library | https://openresearchlibrary.org/ | allowed | 200 | File hosts |
| Manchester Hive | https://www.manchesterhive.com/ | allowed | 200 | Mixed OA/paid |
| Ubiquity partner presses | https://ubiquity.pub/partner-presses/ | none (404) | 200 | Presses 403 |
| Wormworld Saga | https://www.wormworldsaga.com/ | none (404) | 200 | Free to read; no licence found |
| Freefall | http://freefall.purrsia.com/ | unreachable | 200 (http) | http only; free to read |
| Unite for Literacy | https://www.uniteforliteracy.com/ | redirect | 200 | Licence |
| Let's Read | https://www.letsreadasia.org/ | returns HTML | 200 | Licence per book |
| ICDL | http://en.childrenslibrary.org/ | unreachable | 200 (http) | http only |
| Room to Read Literacy Cloud | https://literacycloud.org/ | allowed | 200 | Sign-in |
