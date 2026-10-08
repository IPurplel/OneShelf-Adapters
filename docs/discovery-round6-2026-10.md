# Discovery round 6: Arabic sources — 2026-10-08

Priority: the UN Digital Library and its Arabic collection, then other Arabic open-access sources not
investigated before (checked against the domains already in the docs and manifests). Rights were read on
each source's own pages and, where a page and a PDF could disagree, in the PDFs' own imprints. Nothing
bypassed: no challenge, CAPTCHA, anti-bot form, login or robots rule was worked around, and no terms were
accepted on a user's behalf. A publicly downloadable PDF was never taken as openly licensed.

**Outcomes (46 sources):** IMPLEMENTED 11 (WIPO, 2 QU Press journals, 8 IMIST journals), ELIGIBLE NOT BUILT 1,
RIGHTS NEED REVIEW 10, RIGHTS BLOCKED 2, TECHNICALLY BLOCKED 18, NOT EXAMINED FURTHER 4.

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
| 21 | ILO, UNHCR, QScience, journals.yu.edu.jo | reports, articles | ar among others | — | ILO, UNHCR: Drupal defaults; QScience: allows all, Crawl-delay 5 | NOT EXAMINED FURTHER (4) | Reachable; not examined this round. |

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
- **ILO and UNHCR** — Arabic editions exist; check per-item licences (ILO states CC BY 4.0 for recent
  publications).
- **UN Digital Library** — only with the Library's approval (its terms reportedly require it for automated
  downloads) and an access path without the WAF challenge.
