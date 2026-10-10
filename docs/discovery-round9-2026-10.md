# Discovery round 9: Arabic journals in Libya, Mosul, Baghdad, Jordan, Palestine and Sudan — 2026-10-10

Continues round 8 ([discovery-round8-2026-10.md](discovery-round8-2026-10.md)) by the same rules:
- **Scope:** Arabic open-access sources not investigated before. Every domain and journal path was checked against the docs of rounds 3–8, `candidate-sources.md`, `source-matrix.md` and every adapter's `source.yaml`.
- **Access:** every source was read with OneShelf's own User-Agent, robots.txt first, at about one request per second. Nothing was bypassed.
- **Rights:** unchanged ([round 8 rights decision](discovery-round8-2026-10.md#rights-decision-2026-10-09-journal-wide-statements-are-not-enough)). A licence counts only when the article's own page states it as a versioned Creative Commons licence URL in DC.Rights. A footer, sidebar or site-metadata licence is never taken as an article's licence.

Rows 1–4 were implemented on 2026-10-10 after review (see the build notes and live checks below); the others were not built. The candidates below await a decision.

**Outcomes (12 sources):** IMPLEMENTED 4, ELIGIBLE NOT BUILT 2, RIGHTS NEED REVIEW 2, TECHNICALLY BLOCKED 3, NOT EXAMINED FURTHER 1.

## Implemented — four adapters (VERIFIED live, pinned Core, API 1.0)

Four journals fit the round-7/8 adapter shape unchanged:
- one OJS journal per adapter;
- the DC.Rights gate with the versioned-CC regex;
- `citation_pdf_url` for the file;
- the article's own `citation_language`.

The sampling below takes six articles from the newest issue and six from a mid-archive issue, using the same regex the shipped gate uses.

| Candidate | Newest issue | Mid-archive issue | PDF |
|---|---|---|---|
| Misurata Arts (row 1) | 6/6 pass (2026) | 6/6 pass (2018) | `application/pdf`, `%PDF-`, no redirect; 2026 and 2021 checked |
| Mosul JEH (row 2) | 6/6 pass (2026, CC BY-NC) | 6/6 pass (2026); a 2025 English article also passes | `application/pdf`, `%PDF-`; one same-host locale redirect (`…/ar/article/download/…`) |
| Baghdad JRASHC (row 3) | 6/6 pass (2026) | 0/6 (2023): no item licence, so listed with no file | `application/pdf`, `%PDF-`, no redirect |
| Mosul BERJ (row 4) | 6/6 pass (2026) | 0/6 (2024): no item licence, so listed with no file | `application/pdf`, `%PDF-`; same-host locale redirect |

Build notes:
- **Misurata Arts issue IDs:** older issues use slugs (`issue/view/issue11-2018`, `issue20-2025`) and the newest a number (`issue/view/26`). Neither contains `/`, so the API 1.0 path parameter carries them. The catalog id pattern must allow `[A-Za-z0-9-]+`.
- **Mosul hosts.** Each journal has its own host: `jeh.`, `berj.`, `radab.uomosul.edu.iq`. The shared aliases redirect to it: `ojs.`, `moss.`, `jcis.`, `edusj.uomosul.edu.iq`.
  - The adapter's `network.domains` must name the journal's own host.
  - Pages and PDFs redirect once to a locale path (`/ar/`) on the same host.
- **BERJ's `citation_language`:** it reads `en` on 2024 articles whose titles are Arabic, so the 2024 file language would be wrong. The 2024 articles carry no item licence and get no file anyway, so this only affects listed metadata.
- **JRASHC and BERJ:** like kjlps and Al-Adab in round 7, only part of the archive opens. Older articles stay listed with no file, and no journal-wide fallback is used.

All of them:
- **Checks:** pass `check-adapter` on the pinned Core (`475c145f`).
- **Gate:** the round-8 DC.Rights Creative Commons gate. Each has a SYNTHETIC refusal test; adapters with an older unlicensed archive also have a real refusal test.
- **Mutation check:** with the licence condition removed from the downloads recipe, every refusal test fails.
- **Licence matrix:** any versioned CC licence URL (http or https, with or without a trailing slash) gives the file. Refused: `publicdomain/zero`, an unversioned `licenses/` URL, a lookalike or other host, a copyright line or copyright page, and a journal-wide notice alone.
- **Fixtures:** the fixtures' line-end whitespace was normalised outside attribute values. Parse trees are unchanged and raw `git diff --check` is clean.

| Adapter | Live checks (2026-10-10) |
|---|---|
| `oneshelf.misurata-arts` | 2 PASS: issue 26 (2026, 19 articles, 24 pp) and issue `issue11-2018` (14 articles, 35 pp) |
| `oneshelf.mosul-jeh` | 2 PASS: issue 2968 (2026, 50 articles) and issue 2753 (2025, an English article, 22 pp) |
| `oneshelf.baghdad-jrashc` | 2 PASS: issue 91 (2026) and issue 83 (22 pp). Refused live: article 627 (2020) |
| `oneshelf.mosul-berj` | 2 PASS: issue 2981 (2026) and issue 2927 (19 pp). Refused live: article 38819 (2022) |

Notes from the build:
- **Misurata Arts:** older issues have word-style IDs, so the source pattern and the catalog accept `[A-Za-z0-9-]+` for issues and articles. The site's pages are English by default, so the issue lists the English titles the journal gives its articles. Files and `citation_language` are Arabic.
- **Mosul JEH issue 2867 (2026)** has licensed articles but publishes no PDFs at all. The adapter lists them with no file, which is correct.
- **Mosul hosts:** both Mosul adapters use the University of Mosul Bootstrap 5 theme. Their catalogs read `div.article-card h6.card-title a`, and the issue heading comes from the breadcrumb.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Outcome | Adapter / blocker |
|---|---|---|---|---|---|---|---|
| 1 | [Misurata University — مجلة كلية الآداب (Faculty of Arts Journal)](https://hit.misuratau.edu.ly/ojs/index.php/arts) | humanities, social sciences | ar (some en) | per article DC.Rights `https://creativecommons.org/licenses/by/4.0` plus `rel=license`; 12 of 12 sampled, 2018 and 2026; also article 229 (2021) | no robots.txt (404) | IMPLEMENTED | `oneshelf.misurata-arts`. 22 issues on archive page 1; the journal dates its archive from 2014 |
| 2 | [University of Mosul — مجلة التربية للعلوم الانسانية (Journal of Education for the Humanities)](https://jeh.uomosul.edu.iq/index.php/jeh) | humanities, education | ar, en | per article `https://creativecommons.org/licenses/by-nc/4.0`; 12 of 12 sampled, plus a 2025 article | only `/cache/` | IMPLEMENTED | `oneshelf.mosul-jeh`. About 50 articles per issue |
| 3 | [University of Baghdad — مجلة التراث العلمي العربي (Journal of Arabic Scientific Heritage)](https://jrashc.uobaghdad.edu.iq/index.php/jrashc) | Arabic heritage, history of science, linguistics | ar | per article `https://creativecommons.org/licenses/by/4.0` in 2026 (6/6). 2023 (6/6) and 2020 have no DC.Rights licence, only the journal sidebar `rel=license` | only `/cache/` | IMPLEMENTED | `oneshelf.baghdad-jrashc`. The gate refuses the older articles |
| 4 | [University of Mosul — مجلة ابحاث كلية التربية الاساسية (College of Basic Education Research Journal)](https://berj.uomosul.edu.iq/index.php/berj) | education, humanities | ar, en | per article `https://creativecommons.org/licenses/by/4.0` in 2026 (6/6). 2024 (6/6) and 2022 have none; the site footer's CC BY-NC-SA covers "this OJS site and its metadata" and is not counted | only `/cache/` | IMPLEMENTED | `oneshelf.mosul-berj`. Only recent issues open |
| 5 | [University of Mosul — آداب الرافدين (Adab Al-Rafidayn)](https://radab.uomosul.edu.iq/index.php/radab) | humanities | ar | per article `https://creativecommons.org/licenses/by/4.0/deed.en` (2026, 6/6). Older issues 1837 and 1801: none | only `/cache/` | ELIGIBLE NOT BUILT | **Needs a recipe variant:** the shipped regex refuses the `/deed.en` suffix; pages have no `citation_*` tags (no `citation_pdf_url`); `DC.Language` says `en` on Arabic articles. Round 8 could not reach this host |
| 6 | [Palestine Ahliya University — Journal for Research and Studies](https://journal.paluniv.edu.ps/index.php/journal) | humanities, law, social sciences | en (18 of 18 sampled) | per article `https://creativecommons.org/licenses/by/4.0`, 2022–2026 | only `/cache/` | ELIGIBLE NOT BUILT | Fits the gate, but every sampled article is English; outside this round's Arabic focus |
| 7 | [University of Sirte — مجلة أبحاث (Abhat, Faculty of Arts)](https://journal.su.edu.ly/index.php/abhat) | humanities | ar | DC.Rights only "الحقوق الفكرية (c) 2026 Abhat Journal"; no `rel=license` | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 8 | [Mutah University — Jordanian Journal of Arabic Language and Literature](https://dsr.mutah.edu.jo/index.php/jjall) | Arabic language and literature | ar | 2026 article: no DC.Rights. 2017 article: only "Copyright (c) 2022 JORDANIAN JOURNAL OF ARABIC LANGUAGE AND LITERATURE" | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 9 | [Misurata University — Scientific Journal of the Faculty of Education](https://journals.misuratau.edu.ly/edu/ojs/index.php/eduction) | education, Islamic studies, Arabic | ar, en | — (search snippet claims CC BY 4.0; not verified) | no robots.txt (404) | TECHNICALLY BLOCKED | Every page answered HTTP 508 (Loop Detected) |
| 10 | [University of Benghazi — مجلة كلية الآداب (JOFOA)](https://journals.uob.edu.ly/JOFOA) | humanities | ar | — | only `/cache/` | TECHNICALLY BLOCKED | Issue pages answered HTTP 522 (origin timeout) |
| 11 | [Elmergib University — Journal of Human and Applied Sciences](https://khsj.elmergib.edu.ly/index.php/jhas) | humanities, applied sciences | ar | — | only `/cache/` | TECHNICALLY BLOCKED | Issue pages redirect to the login form; not worked around |
| 12 | [Sudan University of Science and Technology — Journal of Humanities](http://scientific-journal.sustech.edu/Human-and-Economics-Sciences/index.php) | humanities, economics | ar | — | allows everything | NOT EXAMINED FURTHER | The published OJS address answers 404 for `issue/current` and `issue/archive` |

Also seen but not counted as new sources:
- **Already covered:** Hindawi books (`oneshelf.hindawi`, safahat.org), OpenITI, Al-Quds Open University (`journals.qou.edu`), Arab Journals Platform (`digitalcommons.aaru.edu.jo`), ASJP and EKB.
- **Corpus, not a library:** the Gothenburg "Arabic E-Book Corpus" (CC BY 4.0) is a single 143 MB XML dataset of Hindawi books, not per-item downloads.
- **Not Arab-world sources:** Semnan's *Studies on Arabic Language and Literature*, Kalam Arabi and *Anaquel de Estudios Árabes* are Arabic-studies journals outside the Arab world. They are left for a non-Arabic round.

## Notes for maintainers

- **Adab Al-Rafidayn and `deed.<lang>`.** Accepting `…/licenses/by/4.0/deed.en` is still item-level, versioned CC evidence. But it widens the shipped regex, so it should be decided on its own and not slipped into an adapter. The missing `citation_pdf_url` also needs a galley-link extraction, which no round-7/8 adapter uses.
- **Site-footer licences.** Several hosts (Mosul BERJ, Adab Al-Rafidayn) carry an OJS footer: "This OJS site and its metadata are licensed under CC BY-NC-SA 4.0". It is a statement about the site, not the article, and the DC.Rights gate ignores it. A refusal fixture should keep that footer, to prove it is not read.
- **Pinned Core.** No Core change is needed for rows 1–4.
