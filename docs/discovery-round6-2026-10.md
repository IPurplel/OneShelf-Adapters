# Discovery round 6: Arabic sources — 2026-10-08

Priority: the UN Digital Library and its Arabic collection, then other Arabic open-access sources not
investigated before (checked against the domains already in the docs and manifests). Rights were read on
each source's own pages and, where a page and a PDF could disagree, in the PDFs' own imprints. Nothing
bypassed: no challenge, CAPTCHA, anti-bot form, login or robots rule was worked around, and no terms were
accepted on a user's behalf. A publicly downloadable PDF was never taken as openly licensed.

**Outcomes (52 sources):** IMPLEMENTED 11 (WIPO, 2 QU Press journals, 8 IMIST journals), ELIGIBLE NOT BUILT 2,
RIGHTS NEED REVIEW 15, RIGHTS BLOCKED 2, TECHNICALLY BLOCKED 22, NOT EXAMINED FURTHER 0. (ILO and UNHCR were examined
in a follow-up the same day: rows 21–23. QScience, a Refworld re-check and the Yarmouk journals followed on 2026-10-09:
rows 22, 24 and 25–26.) **Final total: 52 sources** (11 + 2 + 15 + 2 + 22 + 0). This supersedes the "48" stated
in the first version of this document, which was a miscount: its own table summed to 49 before the Yarmouk row was
split into rows 25–26.

## Implemented — eleven adapters (VERIFIED live, pinned Core, API 1.0)

All eleven pass `check-adapter` on the pinned Core (`475c145f`). Every licence condition is covered by a
refusal test, and a mutation check (the licence condition removed from the recipe) makes that test fail.

| Adapter | Source | Language / type | Rights gate | Live checks |
|---|---|---|---|---|
| `oneshelf.wipo-publications-ar` | wipo.int | ar, publications (PDF) | the publication page's own `License:` Creative Commons link | 8 PASS (CC BY 4.0, CC BY 3.0 IGO, CC BY-NC-SA 3.0 IGO; 2017–2026; 16–342 pp); 2 refused live (317 Berne Convention, 4829 PCT — no licence: no unit, no file); search 75 results complete |
| `oneshelf.tajseer-qu` | journals.qu.edu.qa | ar, articles (PDF) | the article's DC.Rights Creative Commons licence | 5 PASS (2019, 2022, 2026; 5–25 pp) |
| `oneshelf.sharia-qu` | journals.qu.edu.qa | ar, en, articles (PDF) | the article's DC.Rights Creative Commons licence | 5 PASS (2005, 2018, 2026; 12–68 pp) |
| `oneshelf.imist-prometheus` | journals.imist.ma | ar, articles (PDF) | DC.Rights (CC BY 4.0 sampled) | 2 PASS (first and latest issue) |
| `oneshelf.imist-insaf` | journals.imist.ma | ar, articles (PDF) | DC.Rights (CC BY-NC-ND 4.0) | 2 PASS (2014 — 136 pp — and 2026) |
| `oneshelf.imist-didase` | journals.imist.ma | ar, articles (PDF) | DC.Rights (CC BY 4.0) | 2 PASS (2022, 2026) |
| `oneshelf.imist-tribunejuridique` | journals.imist.ma | ar, articles (PDF) | DC.Rights (CC BY-NC-ND 4.0) | 2 PASS (2025, 2026; a galley addressed `…/download/<id>/DOI`) |
| `oneshelf.imist-chariaa` | journals.imist.ma | ar, articles (PDF) | DC.Rights (CC BY 4.0) | 1 PASS (the archive holds one issue) |
| `oneshelf.imist-dafatir-barlamania` | journals.imist.ma | ar, articles (PDF) | DC.Rights (CC BY-NC-ND 4.0) | 2 PASS (2022, 2026) |
| `oneshelf.imist-joussour` | revues.imist.ma | ar, articles (PDF) | DC.Rights (CC BY-NC 4.0) | 2 PASS (2022, 2024) |
| `oneshelf.imist-lixus` | revues.imist.ma | ar, articles (PDF) | DC.Rights (CC BY-NC-ND 4.0) | 1 PASS (2026); 1 refused live (a 2020 article stating only "الحقوق الفكرية (c) 2022" — listed, no file) |

- **WIPO.** WIPO's [terms of use](https://www.wipo.int/en/web/terms-of-use): "Except for some content published
  under more restrictive terms, new WIPO online publications … are issued under … CC BY 4.0". Of the 226
  Arabic publications (all fetched): 94 CC BY 4.0, 81 CC BY 3.0 IGO, 2 CC BY-NC-SA 3.0 IGO, 49 no licence
  (treaty texts and most items before 2017) — refused. 13 Arabic PDFs sampled against their page: 10 carry the
  same licence in the imprint, 2 state none (one image-only), none contradicts it. WIPO's search ignores its
  own offset when a query is given (every "next" page repeats results 1–50), so the adapter asks for up to 250
  results in one response; all of WIPO's Arabic publications fit. Revisit if they pass 250.
- **QU Press and IMIST (Open Journal Systems).** Each article page carries its licence as a DC.Rights meta tag.
  Issue pages do not, so catalogs list every article and the downloads recipe decides per article
  (`visibility: all_listed_items`, `local_copy: eligible_items_only`, as for Érudit). Each adapter has a
  SYNTHETIC fixture (a real article page with its licence removed) that must give no file. One adapter per
  journal: see Core findings.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Outcome | Adapter / blocker |
|---|---|---|---|---|---|---|---|
| 1 | [UN Digital Library](https://digitallibrary.un.org/) | UN documents, Arabic among six languages | ar, en, fr, es, ru, zh | Official documents (UN symbol) are public domain ([ST/AI/189/Add.9/Rev.2](https://en.wikisource.org/wiki/ST/AI/189/Add.9/Rev.2), 1987, in force 2014). The Library's [2018 terms](https://www.un.org/sites/un2.un.org/files/2020/06/library_content_terms_of_use_2018.pdf): non-commercial use with credit. Current terms (`/pages/?page=tos`) answer 403; a search summary reports "Web scraping and/or automated downloads … not permitted without approval by the Library" — **not verified on the site** | `/search` disallowed; Crawl-Delay 5; a malformed line meant to disallow `/record/*/export/*` | TECHNICALLY BLOCKED | Every record, export and sitemap address answers an AWS WAF challenge (`x-amzn-waf-action: challenge`, empty 202). `/api/v1/search` answers 403 (API key). |
| 2 | [UN Official Document System](https://documents.un.org/) (docs.un.org, undocs.org) | Arabic texts of UN documents (PDF) | ar + 5 | as row 1 | documents.un.org disallows `/doc`, `/access`, `/api` | TECHNICALLY BLOCKED | The viewer pages (docs.un.org/ar/…) are allowed, but every file is served from `documents.un.org/api/symbol/access`, which robots.txt disallows. |
| 3 | [IOM Publications Platform](https://publications.iom.int/) | IOM reports and guides (PDF) | ar among many | [Terms](https://publications.iom.int/terms-and-conditions): "From 2021 IOM publications … are copyrighted under the Creative Commons 3.0 BY-NC-ND IGO license". **Contradicted by the PDFs:** *Contributions and Counting* (PUB2021/061/R, Arabic) "جميع الحقوق محفوظة … إلا بإذن كتابي"; the AAP framework (2021) and MENA regional strategy (2021) all rights reserved. Five 2023+ Arabic PDFs: CC BY-NC-ND 3.0 IGO | `/search/` disallowed; the search form is protected by an anti-bot module | RIGHTS NEED REVIEW | No licence on the publication page; the year is no safe proxy; recipes cannot read a PDF imprint. 36 Arabic items, 17 from 2021 on. Ask IOM for a machine-readable licence field. |
| 4 | [WIPO Publications](https://www.wipo.int/publications/) | IP guides, reports, treaties (PDF) | ar among 10 | per item, `License:` on the page | `/publications/`, `/edocs/pubdocs/` allowed | IMPLEMENTED | `oneshelf.wipo-publications-ar` |
| 5 | [QU Press — Tajseer](https://journals.qu.edu.qa/index.php/tajseer) | humanities articles (PDF) | ar | per article DC.Rights: CC BY 4.0 (2019–21), CC BY-NC 4.0 | only `/cache/` | IMPLEMENTED | `oneshelf.tajseer-qu` |
| 6 | [QU Press — Journal of College of Sharia and Islamic Studies](https://journals.qu.edu.qa/index.php/sharia) | Islamic studies articles (PDF) | ar, en | per article: CC BY-NC 4.0 (back to 2005) | only `/cache/` | IMPLEMENTED | `oneshelf.sharia-qu` |
| 7 | IMIST — 8 Arabic journals ([journals](https://journals.imist.ma/) / [revues](https://revues.imist.ma/)) | articles (PDF) | ar | per article DC.Rights CC | editorial, login, user, gateway, search paths only | IMPLEMENTED | `oneshelf.imist-{prometheus, insaf, didase, tribunejuridique, chariaa, dafatir-barlamania, joussour, lixus}` |
| 8 | IMIST — LegalSciences, MOGADOR, takwine, ibnkhaldoun, REEJD, connaissances-pedagogiques, Istinad, MASSALEK, Istichraf | articles | ar | article pages state no Creative Commons licence (DC.Rights a copyright line, or none) | as row 7 | RIGHTS NEED REVIEW (9) | No licence to gate on; journal-level statements not checked. |
| 9 | IMIST — RAPGS, REMEJE, korasat | articles | ar / en | — | as row 7 | TECHNICALLY BLOCKED (3) | RAPGS: current issue in English, no PDF; REMEJE: no articles listed; korasat: article page timed out. |
| 10 | [An-Najah University Journal for Research – B (Humanities)](https://journals.najah.edu/journal/anujr-b/) | articles (PDF) | ar (older), en (recent) | every article page: "… © 1986 by An-Najah University … is licensed under CC BY-NC 4.0" (`rel="license"`); [terms](https://journals.najah.edu/terms-and-conditions/): all articles CC BY-NC 4.0 | none (404) | ELIGIBLE NOT BUILT | Feasible: issue key `anujr-b-v40-i10`, `/article/<id>/`, `citation_pdf_url`. Not built: no per-article language metadata; 4 of 4 sampled 2020 PDFs Arabic, 4 of 4 2026 PDFs English — the adapter would mislabel languages. The archive page lists no issues in its HTML. |
| 11 | [ALECSO publications library](https://www.alecso.org/publications/) | reports, magazines (PDF) | ar | "© 2026 مكتبة الإصدارات - جميع الحقوق محفوظة" | `/images/` and system paths | RIGHTS BLOCKED | All rights reserved. |
| 12 | [Arab Human Development Report 2022](https://hdr.undp.org/content/arab-human-development-report-2022) (UNDP) | report (PDF) | ar, en, fr | Arabic summary imprint: "جميع الحقوق محفوظة. ولا يجوز إعادة إنتاج …" | allows all | RIGHTS BLOCKED | All rights reserved. |
| 13 | [OECD](https://www.oecd.org/) | reports | multilingual | — | `/content/dam/oecd/` (the PDFs) disallowed | TECHNICALLY BLOCKED | Files robots-disallowed. |
| 14 | [UNDP Arab States](https://www.undp.org/arab-states/publications) | reports | ar, en | — | — | TECHNICALLY BLOCKED | 403 (CloudFront). |
| 15 | [AJSRP](https://journals.ajsrp.com/) | Arabic journal family | ar | — | (challenge) | TECHNICALLY BLOCKED | Cloudflare managed challenge on every path, robots.txt included. |
| 16 | [NAUSS journals](https://journals.nauss.edu.sa/) | security studies | ar | — | — | TECHNICALLY BLOCKED | 403. |
| 17 | [Al-Quds Open University journals](https://journals.qou.edu/) | articles | ar | — | — | TECHNICALLY BLOCKED | Cloudflare challenge. |
| 18 | [QSpace (Qatar University)](https://qspace.qu.edu.qa/) | theses, articles | ar, en | per item | search, browse, `/full` disallowed; Crawl-delay 10 | TECHNICALLY BLOCKED | 500 on every request (2026-10-08); retry later. |
| 19 | SQU, Hashemite University, Yarmouk (jjar), University of Bahrain journals | articles | ar | — | — | TECHNICALLY BLOCKED (4) | Timeout (journals.squ.edu.om) or DNS failure. |
| 20 | University of Jordan *Dirasat*, IASJ (Iraq), IU Gaza | articles | ar | — | — | TECHNICALLY BLOCKED (3) | Timeout, connection reset, DNS failure. |
| 21 | [ILO publications](https://www.ilo.org/ar/publications) | reports, guides (PDF) | ar among many | [Rights and permissions](https://www.ilo.org/rights-and-permissions): "As of 3 May 2023, unless otherwise indicated, ILO publications are licensed under … CC BY 4.0"; earlier ones "do not automatically benefit from a Creative Commons licence"; co-publications may differ — "check the copyright page of each work". **No licence on any of the 906 Arabic publication pages** (all fetched via the sitemap); 131 dated on or after 2023-05-03 (`article:published_time`). 23 of those PDFs read: ~10 state CC BY 4.0 (Arabic imprint "هذا العمل مرخص بموجب ترخيص المشاع الإبداعي نسب المصنف 4.0"), ~10 state nothing (fact sheets, summaries, annual reports), 1 page-dated 2023-05-17 (wcms_882437) carries the old Protocol 2 copyright notice, 1 co-publication only "حقوق النشر محفوظة" | `/search`, taxonomy disallowed; publication pages and files allowed | RIGHTS NEED REVIEW | The page date is not the production date the policy speaks of, and the licence is only in the PDF, which recipes cannot read. The publication date is no safe gate. Needs a licence field on the page (or ILO's repository metadata). |
| 22 | UNHCR — [unhcr.org](https://www.unhcr.org/ar), [Refworld](https://www.refworld.org/), [Global Focus](https://reporting.unhcr.org/) | publications, legal documents | ar among others | — | (challenge) | TECHNICALLY BLOCKED (3) | Cloudflare managed challenge on every path, robots.txt included (it answered 200 earlier the same day). **Refworld re-checked twice on 2026-10-09** (about 13:10Z and 14:16Z, OneShelf's own User-Agent): robots.txt, the home page, a search (`/search?keywords=لاجئ`) and a document page (`/legal/agreements/unga/1951/en/39821`) all answer 403 `cf-mitigated: challenge` ("Just a moment..."). Still blocked; not worked around. |
| 23 | [UNHCR Operational Data Portal](https://data.unhcr.org/) | situation reports, documents (PDF) | ar among others | [Disclaimer](https://data.unhcr.org/en/disclaimer/): "Except where otherwise indicated, the **datasets** made available by UNHCR on the Operational Data Portal are licensed under … CC BY 4.0" — documents are not covered, and many are uploaded by partner organisations | none (404) | RIGHTS NEED REVIEW | The licence covers datasets, not the PDF documents; the document listing and search answer 503 (only detail pages and the home page load). |
| 24 | [QScience](https://www.qscience.com/) (HBKU Press) | journal articles (PDF) | ar, en | **Per item, machine-readable:** the public metadata API (`/qscience/qscience/published/rest/content/v1/<uri>.xml/metadata/`, JSON) gives `contentMetadata.licenses[]` with `type: open-access` and markup "This is an open access article distributed under the terms of the Creative Commons Attribution license CC BY 4.0 …" — with a `creativecommons.org/licenses/by/4.0/` link on 82 of the Arabic-titled items and the licence named in text only on 322; `languages` (e.g. `["ar"]`) and `copyright` ("© 2020 The Author(s), licensee HBKU Press.") per item. Sitemap (197 article sitemaps; every QScience request — sitemaps, metadata, probes — was spaced at least 5 s apart, as Crawl-delay 5 asks): 6,857 article pages; **405 with Arabic titles** (ajsr 88, jist 76, qproc 74, rels 59, irl 28, connect 22, qfarc 18, difi 14, qfarf 13, rolacc 10, jlghs 2, qjph 1), of which 154 have `languages: ar`. Metadata fetched for all 405: 404 CC BY 4.0, 1 answered 502 | allows all; Crawl-delay 5 | TECHNICALLY BLOCKED | Rights eligibility looks good, but **no readable content can be retrieved anonymously**. With OneShelf's User-Agent every article page (`/view/journals/…/article-N.xml`), its `.pdf` and `citation_pdf_url` (`/downloadpdf/view/…pdf`) return only the empty JavaScript shell (633–1,452 bytes; server-rendered HTML appears only for some other user agents; no other User-Agent was impersonated for this assessment or would be by a recipe). The REST routes answer **401** without a login session: `…/download/` (for the `.xml` and the `.pdf` uri), `…/xml/` (JATS — the `citation_xml_url`), `pdf-watermark/…/watermark-pdf/`; `…/fulltext/html` 404. OAI-PMH (`rest/content-interchange/v1/oaipmh`, `oai_dc`/`marc21`/`ifp`, 7,458 records) is public but carries no rights field and no file link — only the JavaScript `/view/` address. The metadata JSON holds abstract, figures and references, not the text. Tested on qmj/2025/4/article-100 (en), ajsr/2020/1/article-2 and connect/2024/1/article-3 (ar). Not worked around (no login emulation); a metadata-only adapter is not a OneShelf capability. |
| 25 | [Jordan Journal of Educational Sciences — المجلة الأردنية في العلوم التربوية](https://jjes.yu.edu.jo/index.php/jjes) (Yarmouk University; OJS 3.3.0.13, default theme) | education articles (PDF) | ar (most), en | Per article, DC.Rights: `https://creativecommons.org/licenses/by-nc/4.0` (with `rel="license"` link) on article 1199 and others. [Submission policy](https://jjes.yu.edu.jo/index.php/jjes/about/submissions): "Published articles are licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license" — **but of 451 article pages surveyed (46 issues: 2–40, 80–90; 41–43 not reached) only 10 carry it** (issue 90: 1199, 1234, 1256, 1263, 1277, 1286, 1392, 1407; 89: 1080; 88: 444); the other 441 state only "Copyright (c) 2023/2024/2025 …" with an empty second DC.Rights. `citation_language` ar on 72, en on 379 (the older issues' metadata says en) | only `/cache/` | ELIGIBLE NOT BUILT | Fits the IMIST/QU per-article gate exactly (`citation_pdf_url` → `/article/download/1199/915`, 200 `application/pdf`, 1.36 MB, checked with OneShelf's User-Agent). Generated (catalog `div.obj_article_summary h3.title a`, gate on DC.Rights, SYNTHETIC no-licence fixture) but **not committed — the unfinished adapter was removed from the tree: the journal server stopped answering at about 14:20Z** (timeouts, then connection resets, on jjes.yu.edu.jo and ayhss.yu.edu.jo; www.yu.edu.jo still up) before fixtures could be fetched — possibly rate limiting after the survey (~470 requests, 1 s apart). Polled gently until 15:33Z; not worked around. Retry later; low yield (10 eligible articles) until the journal adds the licence to older pages. |
| 26 | Yarmouk — [Abhath Al-Yarmouk, Humanities and Social Sciences](https://ayhss.yu.edu.jo/index.php/ayhss), [Jordan Journal of the Arts](https://jja.yu.edu.jo/index.php/jja), [Jordan Journal of Modern Languages and Literatures](https://jjmll.yu.edu.jo/index.php/jjmll) | articles (PDF) | ar; jjmll en/fr/ar | Latest-issue article pages: DC.Rights only "الحقوق الفكرية (c) 2026 …" / "Copyright (c) 2026 …", second DC.Rights empty; no Creative Commons link on article or `/about` pages; footer "All Rights Reserved, Yarmouk University" | only `/cache/` | RIGHTS NEED REVIEW (3) | No licence to gate on. Yarmouk's English-language science journals (aybse, jjms, jjp, jjc) were not examined (outside this Arabic round). The legacy portal journals.yu.edu.jo only links to these sites (robots.txt 404). |

## Core findings (not changed; no Core work done)

| Finding | Evidence | Consequence |
|---|---|---|
| **`{…:path}` percent-encodes `/` on API 1.0** (`quote(v, safe="")`, `oneshelf/plugins/templates.py` of the pinned Core). | A key such as `chariaa/441` would request `chariaa%2F441`. | A platform adapter covering many OJS journals needs API 1.2 `{…:segments}`, which the pinned Core lacks. This round therefore builds one adapter per journal (10 adapters for 2 platforms). With a newer pin, one IMIST adapter and one QU Press adapter could replace them. |
| WIPO search ignores `start` when a query is given. | `start=0` and `start=50` return the same 50 ids (two sorts tried). | Worked around (one response of up to 250). |
| Anti-bot gates (AWS WAF, Cloudflare managed challenge, Drupal antibot). | UN Digital Library, AJSRP, Al-Quds Open University, IOM search. | Not worked around (policy). |

## Best candidates for the next round

- **An-Najah Humanities (row 10)** — rights and access are fine. It needs either a language field from the
  site or one adapter per period (Arabic volumes) with a stated cutoff.
- **IOM (row 3)** — only if IOM exposes a licence per publication, or confirms in writing which 2021–2022
  items are CC.
- **The nine IMIST journals without article licences (row 8)** — read each journal's own policy page; some
  may state a licence journal-wide (source-level, as `oneshelf.ibn-almuqaffa-ut`).
- **ILO (row 21)** — 128 Arabic PDFs dated after 3 May 2023; buildable only if a per-item licence becomes
  machine-readable (ILO's research repository, researchrepository.ilo.org, is a JavaScript application: not
  examined), or ILO confirms which post-policy items are CC BY 4.0.
- **UNHCR (rows 22–23)** — Refworld was still challenged on two re-checks the next day; retry only if UNHCR lifts the challenge; the data
  portal needs a statement that covers its documents, not only its datasets.
- **JJES, Yarmouk (row 25)** — build when the server answers again: the generator draft is ready; only fixtures
  and live checks are missing. Survey at most a few issues per session.
- **QScience (row 24)** — 404 Arabic-titled items with a per-item CC BY 4.0 in public metadata; buildable only
  if HBKU Press offers an anonymous file route (the PDF and JATS endpoints answer 401 without a session).
- **UN Digital Library** — only with the Library's approval (its terms reportedly require it for automated
  downloads) and an access path without the WAF challenge.
