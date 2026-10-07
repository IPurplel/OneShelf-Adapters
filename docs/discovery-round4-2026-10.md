# Discovery round 4: new sources — 2026-10-07

38 sites not investigated before (checked against the 415 domains in earlier docs and manifests). Screened with
`./tools/inspect-source` (robots.txt first); rights read on each site's own pages. Nothing bypassed: no
challenge, CAPTCHA, login or robots rule was worked around.

**Grades:** A 4, B 10, C 1, D 2, F 21. **Rights:** OPEN_LICENSED 15, PUBLIC_DOMAIN 7, CREATOR_AUTHORIZED 1, PUBLISHER_AUTHORIZED 3, FREE_OFFICIAL 1, RIGHTS_UNCLEAR 7, RESTRICTED 4.
**Access:** Allowed 17, Partial 7, Disallowed 3, Unavailable 11. **Decision:** IMPLEMENTED 13, QUEUED 1, HELD 1, BLOCKED 23.

Grades: A — documented API, clean gate; B — stable HTML, gate on the page; C — eligible but a design or
Core gap stands in the way; D — rights unclear; F — blocked (rights, robots or access).

## Implemented (VERIFIED live, local Core)

| Adapter | Source | Language / type | Rights gate | Live works |
|---|---|---|---|---|
| `oneshelf.wolne-lektury` | wolnelektury.pl API v2 | pl, books (EPUB) | site: all PD or free licence; preview books excluded | 8 PASS |
| `oneshelf.ganjoor` | api.ganjoor.net | fa, poetry (text units, rtl) | poets who died ≥70 years ago only | 6 PASS (Hafez, Saadi, Rumi, Khayyam, Shahnameh, Iqbal); Shahriar refused |
| `oneshelf.litteraturbanken` | litteraturbanken.se API | sv, books (EPUB) | epub_license cc-0 only (863/1,643) | 7 PASS; lb262922 refused |
| `oneshelf.bokselskap` | bokselskap.no | no, books (text units) | site grant: private non-commercial use | 7 books + 2 mid-book chapters PASS |
| `oneshelf.mek` | mek.oszk.hu | hu, books (PDF/EPUB) | MEK statement: personal non-commercial copies; single-file docs only | 7 PASS; 07990 (multi-file), 06080 (no files) refused |
| `oneshelf.folger-shakespeare` | folger.edu | en, plays (PDF) | "free to use for all non-commercial purposes" | 6 PASS (Hamlet 144 pp, Julius Caesar, Sonnets, Venus and Adonis, King Lear, The Tempest); 42 units |
| `oneshelf.textgrid-digitale-bibliothek` | textgridlab.org search + html aggregator | de, books (text units) | edition metadata: Digitale Bibliothek project and CC BY 3.0 DE | 5 PASS (Faust 36 parts, Effi Briest 37, Woyzeck, Buch der Lieder, Der Schimmelreiter); work record 11d4c.0 refused |
| `oneshelf.siyavula` | siyavula.com/read | en, af, textbooks (PDF/EPUB) | each file's link: CC-BY / CC-BY-ND; closed-copyright books excluded | 5 PASS (Grade 10 Maths learner PDF 535 pp, its CC BY EPUB 49 MB, Natural Sciences Gr 7A PDF 268 pp, Physical Sciences Gr 9 Afrikaans EPUB 66 MB, Grade 10 Maths teacher guide Afrikaans PDF 749 pp); 146 units; IT book refused |
| `oneshelf.rpo` | rpo.library.utoronto.ca | en, poetry (text units) | poet's death year ≤ 1955 (catalog: poet page; reader: the poem's own poet line, one poet only) | 6 PASS (Yeats 42 poems, Keats 25, Dickinson 23, Shakespeare 200, Chaucer 17 — General Prologue 276 KB, Christina Rossetti 16); Frost (d. 1963) refused |
| `oneshelf.anno` | iiif.onb.ac.at (ONB Labs IIIF) | de, newspapers (images) | each manifest's Public Domain Mark | 6 PASS (Wiener Zeitung 1800-01-01 38 pp, Neue Freie Presse 1865-01-01, Die Presse 1850-01-05, Kikeriki 1880-01-04, Pester Lloyd 1900-01-05, Prager Tagblatt 1900-01-05) |
| `oneshelf.world-bank-okr` | openknowledge.worldbank.org (DSpace 7) | en, reports (PDF) | the item page's Creative Commons licence link | 6 PASS (PDFs 22–92 pp, re-checked after the content-endpoint fix); a page served without its metadata gives no unit (fails closed) |
| `oneshelf.who-iris` | iris.who.int (DSpace 7) | multilingual, reports (PDF) | the same | 5 PASS (World health statistics 2023 136 pp, Global tuberculosis report 2023, World malaria report 2023 356 pp, physical-activity guidelines 2020, a Russian hypertension guide — language ru); a 1970s article without a licence refused |
| `oneshelf.fao-knowledge` | openknowledge.fao.org (DSpace 7) | multilingual, reports (PDF) | the item page's Creative Commons licence badge | 5 PASS (SOFA 2023 en and es, SOFI 2023 316 pp — its citation tag names an EPUB, SOFIA 2024 264 pp, SOFO 2024); a 1940s letter without a licence refused |

## Core (feature/text-reading-units, not pushed, not the pin)

- 270e815 `{key:segments}` encoder (keys that are short paths; `..`/empty refused).
- 2267bc8 form values no longer double-encoded (found on MEK: non-ASCII title searches returned nothing).

Tooling: 8bc67e4 — `live-check --unit-key` reads that unit with the unit's own address from the catalog.

## Every candidate

| # | Source | Content | Lang | Rights | Evidence | Access | robots.txt | Grade | Mechanism / endpoints | Result | Adapter | Block or wait reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Wolne Lektury](https://wolnelektury.pl/) | books (EPUB) | pl | OPEN_LICENSED | site: every book public domain or CC BY-SA 3.0; API `preview` flag marks embargoed books | Allowed | only /admin, /accounts-like paths | A | JSON API v2 `/api/2/books/?search=`, `/api/2/books/<slug>/` | IMPLEMENTED — VERIFIED (8 works) | `oneshelf.wolne-lektury` | — |
| 2 | [Ganjoor](https://ganjoor.net/) | poetry (text, rtl) | fa | PUBLIC_DOMAIN | per poet: death year (AH) in the API; gate ≤ 1374 AH | Allowed | api.ganjoor.net: no rules against these paths | A | JSON API `poems/search`, `ganjoor/cat`, `ganjoor/poem/<id>` | IMPLEMENTED — VERIFIED (6 works; Shahriar refused) | `oneshelf.ganjoor` | — |
| 3 | [Litteraturbanken](https://litteraturbanken.se/) | books (EPUB) | sv | OPEN_LICENSED | per work: `epub_license` cc-0 (863 of 1,643); bank licences excluded | Allowed | no rules | A | JSON API `list_all/etext`, `get_work_info`, `/api/epub/…` | IMPLEMENTED — VERIFIED (7 works; lb262922 refused) | `oneshelf.litteraturbanken` | — |
| 4 | [Bokselskap](https://www.bokselskap.no/) | books (text) | no | PUBLISHER_AUTHORIZED | help page: free private non-commercial use | Allowed | no rule against search or book pages | B | HTML: `/?s=`, book page `#innhold_liste`, chapter `#text_inner` | IMPLEMENTED — VERIFIED (7 books, 2 mid-book chapters) | `oneshelf.bokselskap` | — |
| 5 | [Magyar Elektronikus Könyvtár (MEK)](https://mek.oszk.hu/) | books (PDF/EPUB) | hu | PUBLISHER_AUTHORIZED | copyright.htm: personal, non-commercial copies allowed | Allowed | no rule against search or documents | B | HTML: POST `/hu/search/elfull/`, document folder `/<nnnnn>/<nnnnn>/` | IMPLEMENTED — VERIFIED (7 works; multi-file and file-less refused) | `oneshelf.mek` | — |
| 6 | [Folger Shakespeare](https://www.folger.edu/explore/shakespeares-works/) | plays (PDF) | en | PUBLISHER_AUTHORIZED | download page: "free to use for all non-commercial purposes" | Allowed | only /admin/*; flgr.sh none | B | HTML download page; `flgr.sh/txtfss<code>pdf` → Folger S3 bucket | IMPLEMENTED — VERIFIED (6 of 42 plays) | `oneshelf.folger-shakespeare` | — |
| 7 | [TextGrid Digitale Bibliothek](https://textgridrep.org/) | books (text) | de | OPEN_LICENSED | per edition metadata: CC BY 3.0 DE (by-Nennung TextGrid) | Partial | zip/teicorpus/epub aggregators disallowed; search and html aggregator allowed | A | XML `tgsearch-public/search`, `…/info/<uri>/metadata`; `aggregator/html/<uri>` | IMPLEMENTED — VERIFIED (5 editions; work record refused) | `oneshelf.textgrid-digitale-bibliothek` | — |
| 8 | [Siyavula open textbooks](https://www.siyavula.com/read) | textbooks (PDF/EPUB) | en, af | OPEN_LICENSED | per file link: CC-BY / CC-BY-ND; IT and CAT books "Closed copyright" | Allowed | account/order/practice pages only | B | HTML `/read`; files `/downloads/books/<subject>/<file>` | IMPLEMENTED — VERIFIED (5 files) | `oneshelf.siyavula` | — |
| 9 | [Tanzil](https://tanzil.net/docs/download) | Quran text | ar | OPEN_LICENSED | terms: verbatim copies with attribution | Allowed | /res/ disallowed; /pub/download/ allowed | F | download form `/pub/download/index.php` (Download button enabled only after ticking "I agree with Terms of Use") | BLOCKED (follow-up) | — | a terms checkbox gates the file (not ticked on a user's behalf); one whole-Quran file that recipes cannot split by sura |
| 10 | [Representative Poetry Online](https://rpo.library.utoronto.ca/) | poetry (text) | en | PUBLIC_DOMAIN | copyright page: most poems public domain, no claim by RPO; in-copyright poems by permission | Allowed | /search/ disallowed; /poets, /content/ allowed | B | HTML `/poets?combine=`, poet page (death date, poem index), poem page (`field--name-field-poem-body`) | IMPLEMENTED — VERIFIED (6 poets; Frost refused) | `oneshelf.rpo` | — |
| 11 | [National Library of Wales](https://www.library.wales/) | manuscripts, books (images) | cy, en | RIGHTS_UNCLEAR | viewer links a copyright policy; the manifest it names returned 404 | Unavailable | archives.library.wales: Cloudflare challenge | F | viewer.library.wales/<id>; IIIF manifests on iiif.llyfrgell.cymru (404) | BLOCKED (follow-up) | — | archives catalogue behind a Cloudflare challenge, search host 404, the manifest the viewer names 404: no item can be found or read |
| 12 | [ANNO (Austrian Newspapers Online)](https://iiif.onb.ac.at/api/) | newspapers (images) | de | PUBLIC_DOMAIN | each manifest: Public Domain Mark; API licence NoC-NC; issues older than 1906 only | Partial | anno.onb.ac.at: Cloudflare Turnstile; iiif.onb.ac.at: no robots.txt (400) | B | ONB Labs IIIF `/presentation/ANNO/<id>/manifest/`, images `/images/ANNO/<id>/<page>/full/!2048,2048/0/default.jpg` | IMPLEMENTED — VERIFIED (6 issues) | `oneshelf.anno` | no issue listing: an issue is opened by its IIIF address |
| 13 | [EU Publications Office](https://op.europa.eu/en/web/general-publications/publications) | official publications (PDF) | 24 EU languages | FREE_OFFICIAL | EU reuse decision 2011/833/EU | Partial | search results and download actions need `p_p_id=` portlet URLs, disallowed | F | Liferay portal; Cellar `publications.europa.eu/resource/cellar/<uuid>` | BLOCKED (follow-up) | — | search and file actions robots-disallowed; Cellar redirects to plain http, which OneShelf refuses |
| 14 | [World Bank Open Knowledge Repository](https://openknowledge.worldbank.org/) | reports (PDF) | en, fr, es … | OPEN_LICENSED | per item rel="license": CC BY 3.0 IGO (12 of 13 sampled), CC BY-NC 3.0 IGO | Partial | /search and /server/api disallowed except bitstreams; item pages allowed; Crawl-delay 10 | B | DSpace 7 item page (rel=license, rel=item PDF links); files from `/server/api/core/bitstreams/<id>/content` | IMPLEMENTED — VERIFIED (6 items) | `oneshelf.world-bank-okr` | no search (robots) |
| 15 | [WHO IRIS](https://iris.who.int/) | reports (PDF) | multilingual | OPEN_LICENSED | per item rel="license": recent publications CC BY-NC-SA 3.0 IGO; older documents none (1 of 12 sampled) | Partial | /search and API disallowed except bitstreams; Crawl-delay 10 | B | DSpace 7 item page (rel=license, rel=item PDF links); files from `/server/api/core/bitstreams/<id>/content` | IMPLEMENTED — VERIFIED (5 items; unlicensed item refused) | `oneshelf.who-iris` | no search (robots) |
| 16 | [FAO Open Knowledge](https://openknowledge.fao.org/) | reports (PDF) | en, fr, es, zh, ar, ru | OPEN_LICENSED | per item licence badge: flagship publications CC BY-NC-SA 3.0 IGO / CC BY 4.0; meeting documents none (0 of 7 sampled) | Partial | /search and API disallowed except bitstreams; Crawl-delay 10 | B | DSpace 7 item page (licence badge, "Download PDF" links); files from `/server/api/core/bitstreams/<id>/content` | IMPLEMENTED — VERIFIED (5 items; unlicensed item refused) | `oneshelf.fao-knowledge` | no search (robots) |
| 17 | [Projekti Lönnrot](https://www.lonnrot.net/) | books (text in ZIP) | fi, sv | PUBLIC_DOMAIN | each file's header: public domain in and outside the EU | Allowed | no robots.txt (404) | C | `/valmiit.html` lists 3,700+ `/kirjat/<n>_<name>.zip`, each one plain-text file | QUEUED (Core gap) | — | plain text inside a ZIP: Core reads neither; titles mostly on Project Gutenberg (`oneshelf.gutenberg`) |
| 18 | [David Revoy (MiniFantasyTheater)](https://www.davidrevoy.com/) | webcomics (images) | en | OPEN_LICENSED | CC BY 4.0 per artwork (footer) | Allowed | AI-agent list present but commented out | B | blog posts with images, tag pages | HELD | — | AI-agent list in robots.txt; left to a maintainer, as e-codices |
| 19 | [Deutsches Textarchiv](https://www.deutschestextarchiv.de/) | books (text) | de | OPEN_LICENSED | CC BY-SA 4.0 | Disallowed | download and search paths disallowed; AI agents incl. anthropic-ai disallowed | F | — | BLOCKED | — | robots.txt disallows downloads/search and AI agents; JS cookie check |
| 20 | [DBNL](https://www.dbnl.org/) | books (text) | nl | PUBLIC_DOMAIN | many texts public domain | Disallowed | Disallow: / | F | — | BLOCKED | — | robots.txt disallows everything |
| 21 | [UNESDOC](https://unesdoc.unesco.org/) | documents (PDF) | multilingual | OPEN_LICENSED | CC BY-SA 3.0 IGO on many | Disallowed | Disallow: / | F | — | BLOCKED | — | robots.txt disallows everything |
| 22 | [Walt Whitman Archive](https://whitmanarchive.org/) | texts, manuscripts | en | OPEN_LICENSED | CC BY-NC-SA | Unavailable | not reached | F | — | BLOCKED | — | Cloudflare challenge |
| 23 | [National Library of Israel](https://www.nli.org.il/en) | books, manuscripts | he, ar, … | RIGHTS_UNCLEAR | per item, not read | Unavailable | not reached | F | — | BLOCKED | — | browser check (403) |
| 24 | [Trinity College Dublin Digital Collections](https://digitalcollections.tcd.ie/) | manuscripts (images) | en, ga, la | RIGHTS_UNCLEAR | not reached | Unavailable | not reached | F | — | BLOCKED | — | reCAPTCHA page on every request |
| 25 | [Papers Past](https://paperspast.natlib.govt.nz/) | newspapers | en, mi | PUBLIC_DOMAIN | historic newspapers (copyright page not readable) | Unavailable | not reached | F | — | BLOCKED | — | Incapsula bot protection |
| 26 | [LiberLiber](https://liberliber.it/) | books (EPUB/PDF) | it | OPEN_LICENSED | public domain and Creative Commons texts | Partial | pages allowed | F | — | BLOCKED | — | file downloads behind a Cloudflare-challenge interstitial |
| 27 | [Dorar](https://dorar.net/) | Islamic texts | ar | RESTRICTED | all rights reserved | Allowed | allowed | F | — | BLOCKED | — | all rights reserved |
| 28 | [al-Diwan](https://www.aldiwan.net/) | Arabic poetry | ar | RESTRICTED | © Diwan Foundation | Allowed | allowed | F | — | BLOCKED | — | site copyright, no reuse grant |
| 29 | [Usul.ai](https://usul.ai/) | Arabic books (text) | ar | RIGHTS_UNCLEAR | site all rights reserved; texts from Shamela/OpenITI with mixed provenance | Allowed | allowed | D | — | BLOCKED (rights) | — | rights unclear |
| 30 | [Turath](https://turath.io/) | Arabic books (text) | ar | RIGHTS_UNCLEAR | scanned/Shamela editions; no licence | Allowed | allowed | D | JS application | BLOCKED (rights) | — | rights unclear; SPA |
| 31 | [Planet eBook](https://www.planetebook.com/) | books (PDF/EPUB) | en | RESTRICTED | "© Copyright 2025 Planet eBook. All Rights Reserved." | Allowed | allowed | F | — | BLOCKED | — | all rights reserved on its editions |
| 32 | [MIT Internet Classics Archive](https://classics.mit.edu/) | texts | en | RESTRICTED | "All rights reserved … including the right of reproduction" | Allowed | allowed | F | — | BLOCKED | — | reproduction reserved |
| 33 | [al-Islam.org](https://www.al-islam.org/) | books (text) | en, ar | RIGHTS_UNCLEAR | not reached | Unavailable | not reached | F | — | BLOCKED | — | connection reset |
| 34 | [Oxford Text Archive](https://ota.bodleian.ox.ac.uk/) | texts (TEI) | multilingual | OPEN_LICENSED | per item (varies) | Unavailable | not reached | F | — | BLOCKED | — | timeouts |
| 35 | [e-manuscripta](https://www.e-manuscripta.ch/) | manuscripts (images) | de, la | PUBLIC_DOMAIN | mostly public domain | Unavailable | not reached | F | — | BLOCKED | — | timeouts |
| 36 | [King Fahd National Library publications](https://eservices.kfnl.gov.sa:8060/kfnlpuplications/) | books (PDF) | ar | OPEN_LICENSED | reported CC BY-SA 4.0 (search result; not read on site) | Unavailable | not reached | F | — | BLOCKED | — | port 8060 refused by the egress policy |
| 37 | [Syrian General Book Authority](https://syrbook.gov.sy/) | books (PDF) | ar | RIGHTS_UNCLEAR | free downloads reported; terms not read | Unavailable | not reached | F | — | BLOCKED | — | self-signed TLS certificate (http refused) |
| 38 | [Bizarre Cathedral](https://bizarrecathedral.com/) | webcomic | en | CREATOR_AUTHORIZED | creator's CC BY-NC-SA (historical) | Unavailable | robots 404 | F | — | BLOCKED | — | comic gone; domain now frames unrelated apps |

## Notes

- Ganjoor's text units are right-to-left: Core derives direction from the language (fa). Verified in live
  reads (Hafez ghazal 495).
- Litteraturbanken's refusal shows as an incomplete catalog with no units, not as an error.
- MEK search matches titles only; its EPUBs are often broken (spine), so PDF is offered first.
- Folger's eleven plays with `_pdf` file codes (JC_, Lr_ …) keep the underscore in their key.
- TextGrid's html aggregator is served with an XML declaration; Core's parser already strips it. Page
  markers ("[9]") stay in the text, as in OpenEdition.
- Siyavula's files are large (EPUBs up to ~49 MB); one work holds all 146 open files, named by file name,
  because a recipe cannot pick one book's links by key.

## Follow-up: the queued sources (2026-10-07)

The nine sources queued above were taken up again. Five became adapters (RPO, ANNO through the ONB's IIIF
service, and the three DSpace 7 repositories), three are blocked (Tanzil, National Library of Wales, EU
Publications Office) and one waits on Core (Projekti Lönnrot). Their rows in the table above now carry the
outcome; the earlier queue reasons are kept below.

| Source | Earlier queue reason | Outcome |
|---|---|---|
| Tanzil | one whole-text file | BLOCKED: the download form's button is enabled only by ticking "I agree with Terms of Use" (not ticked on a user's behalf); still one whole-Quran file |
| Representative Poetry Online | no per-poem rights statement | IMPLEMENTED: RPO's copyright page says most poems are public domain and copyrighted ones are there by permission; the adapter keeps only poets who died in 1955 or earlier and re-checks on each poem page |
| National Library of Wales | JS discovery; manifest 404 | BLOCKED: archives catalogue behind a Cloudflare challenge, search host 404, manifests 404 |
| ANNO | daily issues exceed list caps | IMPLEMENTED one issue per work through ONB Labs IIIF (anno.onb.ac.at now asks a Turnstile check); no issue listing exists, so an issue is opened by its IIIF address |
| EU Publications Office | SPARQL only | BLOCKED: search and downloads need disallowed portlet URLs; Cellar redirects to plain http |
| World Bank, WHO IRIS, FAO | search and API disallowed | IMPLEMENTED without search: a pasted item page names its licence and PDF (server-rendered DSpace 7); downloads use the allowed /bitstreams/ path at 6 requests a minute (Crawl-delay 10) |
| Projekti Lönnrot | ZIP text | QUEUED (Core gap): one plain-text file per ZIP; Core reads neither ZIP nor plain-text units |

**Quran.com** (listed `OUT_OF_SCOPE` in candidate-sources.md because it served text only) was re-read now that
text units exist: its API (api.quran.com/api/v4, no robots.txt) serves each sura verse by verse, which would
fit, but its terms allow personal non-commercial copies of content while forbidding use of "any proprietary
information or interfaces of the Service … for any reason" without written consent. `HELD` as RIGHTS_UNCLEAR
until Quran.com (or the Quran Foundation's API terms) permits it.

DSpace notes: an item page's `citation_pdf_url` can name an EPUB (FAO's *State of Food Security and Nutrition
2023*), so the adapters take the files the page declares as PDF (signposting `rel="item"` with type
application/pdf, or FAO's "Download PDF" links). `/bitstreams/<id>/download` is a route of the web
application: on some requests it answers with the application's HTML page instead of the file, so files are read
from the REST content endpoint, which each robots.txt allows explicitly.

Core gaps seen here: a URL pattern yields one group, so an address whose key is split across two query
parameters (ANNO's `aid` and `datum`) cannot be opened; plain text (and text inside a ZIP) is no unit format;
and a recipe cannot select a page's elements by a key (Siyavula's per-book links).
