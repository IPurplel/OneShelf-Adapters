# Discovery round 4: new sources — 2026-10-07

38 sites not investigated before (checked against the 415 domains in earlier docs and manifests). Screened with
`./tools/inspect-source` (robots.txt first); rights read on each site's own pages. Nothing bypassed: no
challenge, CAPTCHA, login or robots rule was worked around.

**Grades:** A 4, B 5, C 8, D 3, F 18. **Rights:** OPEN_LICENSED 15, PUBLIC_DOMAIN 6, CREATOR_AUTHORIZED 1, PUBLISHER_AUTHORIZED 3, FREE_OFFICIAL 1, RIGHTS_UNCLEAR 8, RESTRICTED 4.
**Access:** Allowed 20, Partial 5, Disallowed 3, Unavailable 10. **Decision:** IMPLEMENTED 8, QUEUED 9, HELD 1, BLOCKED 20.

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
| 9 | [Tanzil](https://tanzil.net/docs/download) | Quran text | ar | OPEN_LICENSED | CC BY 3.0, verbatim copies only | Allowed | no rule against downloads | C | whole-Quran text files only (one file per text type) | QUEUED | — | one whole-text file; units would need splitting by sura, which recipes cannot do |
| 10 | [Representative Poetry Online](https://rpo.library.utoronto.ca/) | poetry (text) | en | RIGHTS_UNCLEAR | footer: everything except the poetry © the Editors; per-poem status not stated | Allowed | allowed | D | HTML poem pages | QUEUED (rights research) | — | no per-poem rights statement to gate on |
| 11 | [National Library of Wales](https://www.library.wales/) | manuscripts, books (images) | cy, en | RIGHTS_UNCLEAR | viewer links a copyright policy; the manifest it names returned 404 | Allowed | allowed | C | viewer.library.wales/<id>; IIIF manifests on iiif.llyfrgell.cymru | QUEUED | — | discovery is a JS catalogue; the manifest named by the viewer returned 404 |
| 12 | [ANNO (Austrian Newspapers Online)](https://anno.onb.ac.at/) | newspapers (images) | de | PUBLIC_DOMAIN | historic newspapers, ÖNB | Allowed | allowed | C | HTML title/year/issue pages | QUEUED | — | daily issues exceed list caps; needs a year-per-work design |
| 13 | [EU Publications Office](https://op.europa.eu/en/web/general-publications/publications) | official publications (PDF) | 24 EU languages | FREE_OFFICIAL | EU reuse decision 2011/833/EU | Allowed | portal pages allowed | C | Liferay portal; SPARQL endpoint for metadata | QUEUED | — | search only through SPARQL or a JS portal |
| 14 | [World Bank Open Knowledge Repository](https://openknowledge.worldbank.org/) | reports (PDF) | en, fr, es … | OPEN_LICENSED | CC BY 3.0 IGO on most items | Partial | /search and /server/api disallowed except bitstreams | C | DSpace 7 | QUEUED | — | search and metadata API disallowed |
| 15 | [WHO IRIS](https://iris.who.int/) | reports (PDF) | multilingual | OPEN_LICENSED | CC BY-NC-SA 3.0 IGO | Partial | /search and API disallowed except bitstreams | C | DSpace 7 | QUEUED | — | search and metadata API disallowed |
| 16 | [FAO Open Knowledge](https://openknowledge.fao.org/) | reports (PDF) | multilingual | OPEN_LICENSED | CC BY-NC-SA 3.0 IGO | Partial | /search and API disallowed except bitstreams | C | DSpace 7 | QUEUED | — | search and metadata API disallowed |
| 17 | [Projekti Lönnrot](https://www.lonnrot.net/) | books (text in ZIP) | fi, sv | PUBLIC_DOMAIN | public-domain texts | Allowed | allowed | C | ZIP of plain text per book | QUEUED | — | ZIP text is no supported unit; most titles are also on Project Gutenberg |
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
