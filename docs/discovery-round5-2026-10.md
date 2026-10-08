# Discovery round 5: new sources — 2026-10-07

47 sources investigated in this round, none investigated before (checked against the 797 domains already in
the docs and manifests). Screened with `./tools/inspect-source` (robots.txt first); rights read on each
source's own pages. Nothing bypassed: no challenge, CAPTCHA, interstitial, login or robots rule was worked
around, and no terms were accepted on a user's behalf.

**Outcomes:** IMPLEMENTED 11, READY FOR ELIGIBILITY REVIEW 5, RIGHTS NEED REVIEW 4, TECHNICALLY BLOCKED 26, RIGHTS/TERMS BLOCKED 1.

## Implemented — eleven adapters (VERIFIED live, local Core)

| Adapter | Source | Language / type | Rights gate | Live checks |
|---|---|---|---|---|
| `oneshelf.nasa-ntrs` | ntrs.nasa.gov (API) | en, reports (PDF) | determinationType public-use, no third-party material | 6 PASS (Apollo 11 mission report 359 pp, lunar sample petrology, Mars 2020 overview …); GOV_PERMITTED and MAY_INCLUDE_COPYRIGHT_MATERIAL records refused |
| `oneshelf.govinfo` | govinfo.gov (MODS) | en, federal publications (PDF) | Government-authored collections only | 5 PASS (Economic Report of the President 2024 487 pp, US Reports 576 1,130 pp, Budget 2025, a public law, a committee report); a hearing refused |
| `oneshelf.erudit` | erudit.org | fr, articles (text) | the article's Creative Commons licence | 5 PASS (Enjeux et société, two issues, 40–77 KB each); a "Tous droits réservés" article with its body on the page refused |
| `oneshelf.cyberleninka` | cyberleninka.ru | ru, articles (text) | the CC BY badge | 5 PASS (15–52 KB each) |
| `oneshelf.elejandria` | elejandria.com | es, books (EPUB, PDF) | site statement (public domain / open; free in Spain) | 6 PASS (Don Quijote, Crimen y castigo, Ariel, two Montgomery translations, Gómez Carrillo) |
| `oneshelf.brogo` | icculus.org | en, webcomic (images) | CC BY-SA 4.0 / GFDL (creator) | 6 PASS (2005–2025; a month with 31 strips) |
| `oneshelf.jall-ferdowsi` | jall.um.ac.ir | ar, fa, articles (PDF) | CC BY 4.0 link on the page | 5 PASS (two issues, 13–33 pp) |
| `oneshelf.rctall-atu` | rctall.atu.ac.ir | fa, ar, articles (PDF) | CC BY-NC 4.0 link on the page | 5 PASS (first and latest issue) |
| `oneshelf.jalit-ut` | jalit.ut.ac.ir | ar, fa, articles (PDF) | CC BY-NC 4.0 link on the page | 5 PASS |
| `oneshelf.ibn-almuqaffa-ut` | jal-lq.ut.ac.ir | ar, articles (PDF) | CC BY-NC 4.0 (journal-wide, source level) | 5 PASS |
| `oneshelf.chitanka` | chitanka.info | bg, books (text) | every rights mark public domain or CC | 5 PASS (Под игото 88 parts incl. part 40, Botev, Aleko Konstantinov, Yovkov); fully copyrighted texts (a modern novel, an Elin Pelin edition) refused |

Text adapters (Érudit, CyberLeninka, Chitanka) and Brogo (`{key:segments}`) need plugin API 1.2, which the
pinned Core does not have.

## Follow-up — 2026-10-08: two more Arabic journals (VERIFIED live, pinned Core)

The two Sinaweb journals left at READY FOR ELIGIBILITY REVIEW (rows 21 and 22) are implemented. Both use
API 1.0 and pass `check-adapter` on the pinned Core.

| Adapter | Source | Language / type | Rights gate | Live checks |
|---|---|---|---|---|
| `oneshelf.lasem-semnan` | lasem.semnan.ac.ir | ar, articles (PDF) | CC BY 4.0 link on the page | 5 PASS (first issue 2010 and latest issue 2026, two articles each; 2011; 22–38 pp) |
| `oneshelf.rall-ui` | rall.ui.ac.ir | ar, articles (PDF) | CC BY-NC-ND 4.0 (journal-wide, source level) | 5 PASS (first issue 2009, the three 2026 issues, two articles of the latest; 14–22 pp) |

- **Semnan** has the same issue page as `oneshelf.jalit-ut` (`h2.list-article-title`, bookmark-icon heading)
  and links CC BY 4.0 on every page, so catalog and downloads check the licence on each page as jalit-ut does.
  Its issue list is `browse?_action=issue` (the round-5 note "different site layout" is about the homepage, not
  the issue pages).
- **Isfahan** lists articles as `h5.list-article-title` and has no bookmark icon; the issue heading is the span
  after "المجلد والعدد". The licence (CC BY-NC-ND 4.0) is on the about page only, not on issue or article
  pages, so the licence applies to the whole source, as for `oneshelf.ibn-almuqaffa-ut`. No derivatives: the
  PDF is stored unaltered.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Discovery | Item resolution | Format | Core supports | Outcome | Adapter | Blocker / notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [NASA Technical Reports Server](https://ntrs.nasa.gov/) | reports, papers (PDF) | en | PUBLIC_DOMAIN / FREE_OFFICIAL (per record) | allows all | public JSON API `/api/citations/search` | `/api/citations/<id>` | PDF | yes | IMPLEMENTED | `oneshelf.nasa-ntrs` | gate: copyright.determinationType GOV_PUBLIC_USE_PERMITTED or PUBLIC_USE_PERMITTED, no third-party material |
| 2 | [GovInfo (GPO)](https://www.govinfo.gov/) | US federal publications (PDF) | en | PUBLIC_DOMAIN (17 U.S.C. § 105) | search disallowed | pasted package address (API needs a key) | `/metadata/pkg/<id>/mods.xml` | PDF | yes | IMPLEMENTED | `oneshelf.govinfo` | only Government-authored collections (ERP, BUDGET, GAOREPORTS, GOVMAN, CRPT, USREPORTS, PLAW, STATUTE); hearings refused |
| 3 | [Érudit](https://www.erudit.org/) | journal articles (text) | fr (en) | OPEN_LICENSED (per article) | no rules | pasted issue address; issue page lists articles | article page `section#corps` | text units (api 1.2) | yes | IMPLEMENTED | `oneshelf.erudit` | gate: the article's own p.licence Creative Commons link; PDF-only CC articles have no text (see Core) |
| 4 | [CyberLeninka](https://cyberleninka.ru/) | journal articles (text) | ru | OPEN_LICENSED (per article) | search, API, PDFs disallowed; article pages allowed | pasted article address | article page `div.ocr` | text units (api 1.2) | yes | IMPLEMENTED | `oneshelf.cyberleninka` | gate: the 'CC BY' badge (div.label-cc); exclusion tested on a constructed page |
| 5 | [Elejandría](https://www.elejandria.com/) | books (EPUB, PDF) | es | PUBLIC_DOMAIN (site statement; free in Spain) | search disallowed | pasted book address | book page download buttons → `/libro/link_descarga_libro/<book>/<file>` | EPUB, PDF | yes | IMPLEMENTED | `oneshelf.elejandria` | MOBI not offered; jurisdiction note (free in Spain) |
| 6 | [Brogo](https://icculus.org/mwm/brogo/home.html) | webcomic (images) | en | CREATOR_AUTHORIZED (CC BY-SA 4.0 / GFDL) | allows all but one forum path | year archive pages | month pages | images | yes (api 1.2: segments) | IMPLEMENTED | `oneshelf.brogo` | — |
| 7 | [Journal of Arabic Language and Literature (Ferdowsi)](https://jall.um.ac.ir/) | journal articles (PDF) | ar, fa | OPEN_LICENSED (CC BY 4.0, journal-wide) | allows all | pasted issue address; issue page lists articles | article page citation_pdf_url | PDF | yes | IMPLEMENTED | `oneshelf.jall-ferdowsi` | Sinaweb platform |
| 8 | [Translation Researches in Arabic Language and Literature (ATU)](https://rctall.atu.ac.ir/) | journal articles (PDF) | fa, ar | OPEN_LICENSED (CC BY-NC 4.0) | allows all | pasted issue address | article page citation_pdf_url | PDF | yes | IMPLEMENTED | `oneshelf.rctall-atu` | Sinaweb |
| 9 | [Arabic Literature / ادب عربی (University of Tehran)](https://jalit.ut.ac.ir/) | journal articles (PDF) | ar, fa | OPEN_LICENSED (CC BY-NC 4.0) | allows all | pasted issue address | article page citation_pdf_url | PDF | yes | IMPLEMENTED | `oneshelf.jalit-ut` | Sinaweb; newest issue has no PDFs yet |
| 10 | [Ibn al-Muqaffa' in Narrative and Poetry (University of Tehran)](https://jal-lq.ut.ac.ir/) | journal articles (PDF) | ar | OPEN_LICENSED (CC BY-NC 4.0, about page) | allows all | pasted issue address | article page citation_pdf_url | PDF | yes | IMPLEMENTED | `oneshelf.ibn-almuqaffa-ut` | licence stated journal-wide only (source-level) |
| 11 | [Chitanka (Моята библиотека)](https://chitanka.info/) | books (text) | bg | PUBLIC_DOMAIN / OPEN_LICENSED (per text) | file downloads (.epub, .fb2.zip, .txt.zip …) disallowed | Chitanka search | reading pages `/text/<id>/<part>` (`div#textstart`) | text units (api 1.2) | yes | IMPLEMENTED | `oneshelf.chitanka` | gate: every rel=license mark public domain or CC; 'Пълни авторски права' refused |
| 12 | [OSTI.GOV (DOE)](https://www.osti.gov/) | reports, accepted manuscripts | en | RIGHTS_UNCLEAR | /search/ disallowed; API allowed | JSON API `/api/v1/records` | `/servlets/purl/<id>` | PDF | yes | RIGHTS NEED REVIEW | — | no per-record rights; journal items are publisher-copyrighted accepted manuscripts; acceptable-use policy discourages automated downloading |
| 13 | [ERIC](https://eric.ed.gov/) | education research (PDF) | en | RIGHTS_UNCLEAR | allows all | API api.ies.ed.gov/eric | files.eric.ed.gov | PDF | yes | RIGHTS NEED REVIEW | — | authors/publishers keep copyright, ERIC holds full text by permission; API does not mark U.S.-Government works |
| 14 | [Redalyc](https://www.redalyc.org/) | journal articles (HTML, PDF) | es, pt | RIGHTS_UNCLEAR | allows articles (CCBot disallowed) | journal and article pages | article `/html/` page | text or PDF | yes | RIGHTS NEED REVIEW | — | no licence on article pages; journal pages are client-rendered |
| 15 | [Manifold presses (University of Hawai'i Press, South Carolina, Cincinnati)](https://manifold.uhpress.hawaii.edu/) | books (HTML sections) | en | RIGHTS_UNCLEAR | no robots.txt | Manifold API projects/texts | `/api/v1/texts/<id>/relationships/text_sections/<id>` (body HTML) | text units | partly (no catalog titles: JSON items unreadable in templates) | RIGHTS NEED REVIEW | — | licence only in a text's metadata.rights; the one read says 'All rights reserved' |
| 16 | [HAL](https://hal.science/) | papers (PDF) | fr, en | OPEN_LICENSED (per deposit) | robots.txt names anthropic-ai: Disallow / | — | — | — | — | RIGHTS/TERMS BLOCKED | — | AI agents disallowed by name; requests stopped (held for a maintainer, like e-codices) |
| 17 | [Government of Canada Publications](https://publications.gc.ca/) | government publications (PDF) | en, fr | FREE_OFFICIAL (non-commercial reproduction permitted) | search disallowed | pasted record address | record page → `/collections/…pdf` | PDF | no | TECHNICALLY BLOCKED | — | every PDF redirects to an 'Information Archived on the Web' interstitial whose link points back to itself; adapter drafted, not committed |
| 18 | [Emory Open Books (Manifold)](https://openbooks.fchi.emory.edu/) | books | en | RIGHTS_UNCLEAR | — | Manifold | — | — | — | TECHNICALLY BLOCKED | — | manifold.ecds.emory.edu answers HTTP 202 with an empty body (bot gateway) |
| 19 | [Princeton Digital Library (DPUL)](https://dpul.princeton.edu/) | manuscripts, early Arabic books | ar, fa, … | PUBLIC_DOMAIN (likely) | query URLs disallowed; Crawl-delay 10 | collection pages | item pages | IIIF images | — | TECHNICALLY BLOCKED | — | item pages answer 'Verifying connection' (bot challenge) |
| 20 | [Egyptian Knowledge Bank journals](https://journals.ekb.eg/) | journal articles | ar, en | OPEN_LICENSED (per journal) | — | Sinaweb | — | PDF | yes | TECHNICALLY BLOCKED | — | every connection reset from this environment |
| 21 | [Studies on Arabic Language and Literature (Semnan)](https://lasem.semnan.ac.ir/) | journal articles | ar, fa | OPEN_LICENSED (CC BY 4.0, per search result) | allows all | different site layout | — | PDF | likely | IMPLEMENTED (2026-10-08) | `oneshelf.lasem-semnan` | issue pages are the jalit-ut layout; issues listed at browse?_action=issue |
| 22 | [Research in Arabic Language (Isfahan)](https://rall.ui.ac.ir/) | journal articles | ar | OPEN_LICENSED (CC BY-NC-ND 4.0, footer) | allows all | Sinaweb variant | — | PDF | likely | IMPLEMENTED (2026-10-08) | `oneshelf.rall-ui` | h5 article titles; heading after "المجلد والعدد"; licence on about page only (source level) |
| 23 | [Lisan Mobin, Al-Jamea, Arabic Language Studies (Iranian journals)](https://lisanmobin.ikiu.ac.ir/) | journal articles | ar | — | — | — | — | — | — | TECHNICALLY BLOCKED | — | DNS failure from this environment (three hosts) |
| 24 | [Chronicling America (LOC)](https://chroniclingamerica.loc.gov/) | newspapers | en | PUBLIC_DOMAIN | — | loc.gov JSON API | — | images, OCR | yes | TECHNICALLY BLOCKED | — | redirects to www.loc.gov, which this environment's egress policy refuses — eligible, untestable here |
| 25 | [UN ESCWA publications](https://www.unescwa.org/publications) | reports | ar, en | FREE_OFFICIAL | — | — | — | PDF | — | TECHNICALLY BLOCKED | — | archive.unescwa.org refused by the egress policy |
| 26 | [Manchester Open Hive](https://www.manchesteropenhive.com/) | books | en | OPEN_LICENSED (OA titles) | — | — | — | — | — | TECHNICALLY BLOCKED | — | redirects to www.manchesterhive.com, refused by the egress policy |
| 27 | [Trove (NLA)](https://trove.nla.gov.au/) | newspapers, books | en | PUBLIC_DOMAIN (old newspapers) | /api/search/* and renditions disallowed | API (key required) | — | — | — | TECHNICALLY BLOCKED | — | search API robots-disallowed and keyed |
| 28 | [CORE](https://core.ac.uk/) | papers | multilingual | mixed | /search disallowed | API (key required) | — | PDF | — | TECHNICALLY BLOCKED | — | search disallowed; API needs a key |
| 29 | [J-STAGE](https://www.jstage.jst.go.jp/) | journal articles | ja, en | mixed (per article) | PDFs (`/*_pdf`) disallowed | — | — | PDF | — | TECHNICALLY BLOCKED | — | the article files are robots-disallowed |
| 30 | [Scaife Viewer (Perseus)](https://scaife.perseus.org/) | Greek/Latin texts | grc, la | OPEN_LICENSED | Disallow: / | — | — | — | — | TECHNICALLY BLOCKED | — | robots.txt disallows everything |
| 31 | [California Digital Newspaper Collection](https://cdnc.ucr.edu/) | newspapers | en | PUBLIC_DOMAIN | Disallow: / | — | — | — | — | TECHNICALLY BLOCKED | — | robots.txt disallows everything |
| 32 | [Hemeroteca Digital (BNE)](https://hemerotecadigital.bne.es/) | newspapers | es | PUBLIC_DOMAIN | Disallow: / | — | — | — | — | TECHNICALLY BLOCKED | — | robots.txt disallows everything |
| 33 | [Biblioteca Digital Hispánica (BNE)](https://bdh-rd.bne.es/) | books, manuscripts | es | PUBLIC_DOMAIN | — | — | — | — | — | TECHNICALLY BLOCKED | — | HTTP 403 to the client |
| 34 | [e-newspaperarchives.ch](https://www.e-newspaperarchives.ch/) | newspapers | de, fr, it | PUBLIC_DOMAIN (old) | — | — | — | — | — | TECHNICALLY BLOCKED | — | HTTP 403 to the client |
| 35 | [Hoosier State Chronicles](https://newspapers.library.in.gov/) | newspapers | en | PUBLIC_DOMAIN (old) | — | Veridian | — | — | — | TECHNICALLY BLOCKED | — | HTTP 403 to the client |
| 36 | [Harvard Library IIIF (Islamic Heritage Project)](https://iiif.lib.harvard.edu/) | manuscripts | ar, fa, ota | PUBLIC_DOMAIN | — | — | IIIF manifests | images | yes | TECHNICALLY BLOCKED | — | manifests answer HTTP 403 to the client |
| 37 | [OER Commons](https://oercommons.org/) | open educational resources | en | OPEN_LICENSED | — | — | — | — | — | TECHNICALLY BLOCKED | — | HTTP 403 to the client |
| 38 | [Ubiquity Press](https://www.ubiquitypress.com/) | books, journals | en | OPEN_LICENSED | — | — | — | — | — | TECHNICALLY BLOCKED | — | HTTP 403 to the client |
| 39 | [Luminos (UC Press)](https://www.luminosoa.org/) | books | en | OPEN_LICENSED | — | — | — | — | — | TECHNICALLY BLOCKED | — | HTTP 403 to the client |
| 40 | [ASJP (Algerian Scientific Journal Platform)](https://www.asjp.cerist.dz/) | journal articles | ar, fr | OPEN_LICENSED (per journal) | — | — | — | PDF | — | TECHNICALLY BLOCKED | — | TLS certificate verification fails |
| 41 | [Arab Journals Platform (AARU)](https://digitalcommons.aaru.edu.jo/) | journal articles | ar, en | OPEN_LICENSED (per journal) | — | — | — | PDF | — | TECHNICALLY BLOCKED | — | DNS failure from this environment |
| 42 | [Doha Institute publications](https://www.dohainstitute.org/ar/) | research, journals | ar | RIGHTS_UNCLEAR | — | — | — | — | — | TECHNICALLY BLOCKED | — | connection fails |
| 43 | [King Saud University e-books](https://ebook.ksu.edu.sa/) | books | ar | RIGHTS_UNCLEAR | — | — | — | — | — | TECHNICALLY BLOCKED | — | DNS failure |
| 44 | [Kotobati](https://www.kotobati.com/) | books | ar | RIGHTS_UNCLEAR | — | — | — | — | — | TECHNICALLY BLOCKED | — | connection fails; rights of its uploads unclear |
| 45 | [UN Digital Library](https://digitallibrary.un.org/) | UN documents | 6 UN languages | FREE_OFFICIAL | allowed | client-rendered search | record pages | PDF | unknown | READY FOR ELIGIBILITY REVIEW | — | home page renders no server text; record pages and files not yet examined |
| 46 | [Smithsonian Libraries digital library](https://library.si.edu/digital-library) | books | en | PUBLIC_DOMAIN (mostly) | allowed | Drupal pages | — | PDF/IIIF (BHL, Internet Archive) | unknown | READY FOR ELIGIBILITY REVIEW | — | items appear hosted on BHL/Internet Archive; not examined further |
| 47 | [ManyBooks](https://manybooks.net/) | ebooks | en | mixed | allowed | Drupal pages | — | EPUB/PDF | unknown | READY FOR ELIGIBILITY REVIEW | — | free and commercial titles mixed; download path not examined |

## Core limitations seen (not built this round)

| Limitation | Evidence | Sources it would unlock (estimate) |
|---|---|---|
| **Bug: `regex_replace` mangles non-ASCII replacement text** (UTF-8 read as Latin-1: replacement `é—` → `Ã©â€”`). | `oneshelf.jall-ferdowsi` issue titles; worked around with a template. No shipped adapter uses a non-ASCII replacement. | 0 blocked, but every Arabic/Persian/Cyrillic recipe that rewrites text is exposed. Small fix. |
| **A text unit cannot fall back to the article's PDF.** Text and file units are separate kinds per adapter. | Érudit CC articles published as PDF only (aporia, Imaginations, CJHE, Intersections sampled) give no text. | Érudit's PDF-only CC articles (most CC journals sampled); similar mixes on OpenEdition and journals platforms: ~2–4 sources more complete. |
| **JSON list items are not readable in templates** (a template sees `{item}` only when it is a scalar). | Manifold catalogs could not carry section titles together with a gate; NTRS search cannot be gated by licence. | Manifold presses (3 instances, once rights are clear), search-time gating for NTRS-like APIs: ~3–5. |
| **A URL pattern yields one group** (from round 4). | ANNO addresses split the key across two parameters. | ANNO direct addresses, other two-parameter catalogues: ~2. |
| **Plain text / ZIP units** (from round 4). | Projekti Lönnrot. | ~1–2. |

Also seen (not Core): sources that answer automated clients with 403, bot challenges or interstitials (Canada,
DPUL, Emory, Harvard IIIF, OER Commons, Ubiquity, Luminos, BDH, e-newspaperarchives, Hoosier) — 10 sources
— are not Core limitations and are not worked around.

## Best candidates for the next round

- ~~**Sinaweb Arabic journals with other templates**~~ — implemented 2026-10-08 (`oneshelf.lasem-semnan`,
  `oneshelf.rall-ui`; see the follow-up above).
- **UN Digital Library** (6 UN languages including Arabic, free official) — record pages and files not yet examined.
- **Chronicling America** — public domain, keyless JSON API; blocked only by this environment's egress policy.
- **Manifold presses** — would work as text units once a text's licence is confirmed (ask the presses / read their
  open-access statements per book).
- **ManyBooks, Smithsonian Libraries** — examine the download path and overlap with already-covered hosts.
