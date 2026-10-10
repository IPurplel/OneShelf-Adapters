# Discovery round 10: Arabic journals in Libya, Algeria, Iraq, Tunisia and Saudi Arabia — 2026-10-10

Continues round 9 ([discovery-round9-2026-10.md](discovery-round9-2026-10.md)) on the same day and by the same rules:
- **Scope:** Arabic open-access sources not investigated before. Every domain and journal path was checked against rounds 3–9, `candidate-sources.md`, `source-matrix.md` and every adapter's `source.yaml`.
- **Access:** OneShelf's own User-Agent, robots.txt first, about one request per second. M'sila's Crawl-delay of 5 s was honoured at 5.5 s. Nothing was bypassed.
- **Rights:** unchanged ([round 8 rights decision](discovery-round8-2026-10.md#rights-decision-2026-10-09-journal-wide-statements-are-not-enough)). Only a versioned Creative Commons URL in the article's own DC.Rights counts.

This round is discovery only: **nothing was built.**

**Outcomes (11 sources):** ELIGIBLE NOT BUILT 5, RIGHTS NEED REVIEW 2, TECHNICALLY BLOCKED 3, NOT EXAMINED FURTHER 1.

## Recommended for the next build round

Three journals fit the round-7/8 adapter shape unchanged, sampled six articles from the newest issue and six from a
mid-archive issue with the shipped gate's regex:

| Candidate | Newest issue | Mid-archive issue | `citation_pdf_url` |
|---|---|---|---|
| Tripoli Delalat (row 1) | 6/6 pass (2026) | 6/6 pass (2023); a 2021 article also passes | 12/12; PDF `application/pdf`, no redirect |
| Kufa Studies Center (row 2) | 6/6 pass (2026) | 6/6 pass (2025); a 2024 article also passes | 12/12; PDF `application/pdf`, no redirect |
| M'sila JAPL (row 3) | 6/6 pass (2023, CC BY-NC) | 6/6 pass (2022) | 12/12; PDF `application/pdf`, no redirect |

Build notes:
- **Kufa Studies Center** is on `journal.uokufa.edu.iq`, the host of the five round-7 Kufa adapters. It would be a sixth adapter on that host, with the same robots rules.
- **M'sila's robots.txt.** It sets `Crawl-delay: 5` and disallows `setLocale`, `search` and `browse`.
  - The adapter's `rate_limit` must be at most one request per 5 s.
  - Its recipes must never request a locale switch.
  - Its newest issue (173) holds articles dated 2021 and 2023, so issue order is not date order.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Outcome | Adapter / blocker |
|---|---|---|---|---|---|---|---|
| 1 | [University of Tripoli — مجلة دلالات للعلوم الإنسانية والتربوية (Delalat Journal of Humanities and Educational Sciences)](https://j.tu.edu.ly/delalat/index.php/delalat) | humanities, education, Islamic studies | ar | per article DC.Rights `https://creativecommons.org/licenses/by/4.0` plus `rel=license`; 12 of 12 sampled (2023, 2026) plus a 2021 article | no robots.txt (404) | ELIGIBLE NOT BUILT | **Recommended.** 17 issues |
| 2 | [University of Kufa — مجلة مركز دراسات الكوفة (Journal of Kufa Studies Center)](https://journal.uokufa.edu.iq/index.php/ksc) | humanities, social sciences, economics | ar | per article `https://creativecommons.org/licenses/by/4.0`; 12 of 12 sampled (2025, 2026) plus a 2024 article | system paths and `/cache/` only | ELIGIBLE NOT BUILT | **Recommended** |
| 3 | [University of M'sila — مجلة دفاتر مخبر الشعرية الجزائرية (JAPL)](https://journals.univ-msila.dz/index.php/JAPL) | Arabic literature, poetics, criticism | ar | per article `https://creativecommons.org/licenses/by-nc/4.0`; 12 of 12 sampled (2022, 2023) plus two more (2021, 2023) | Crawl-delay 5; disallows `setLocale`, `search`, `browse` | ELIGIBLE NOT BUILT | **Recommended.** Its own OJS host, not ASJP |
| 4 | [Al-Mustansiriyah University — مجلة آداب المستنصرية](https://amm.uomustansiriyah.edu.iq/index.php/mustansiriyah) | humanities | ar, fr | per article CC: `https://…/by/4.0` (2023 article) and `http://…/by-sa/4.0` (2024 article); the gate accepts both | only `/cache/` | ELIGIBLE NOT BUILT | Both issue pages examined (113, 127) list **one** article each, although the journal has many. Its catalog structure needs examining before an adapter |
| 5 | [Tunis University — Joussour](https://joussour.utunis.rnu.tn/index.php/JHASES) | humanities, social sciences | fr (sampled) | per article DC.Rights `https://creativecommons.org/licenses/by/4.0` (plus "Creative Commons CC BY" text) | only `/cache/` | ELIGIBLE NOT BUILT | One issue of five articles so far; sampled article is French. Not the IMIST `joussour` journal of round 3–6 |
| 6 | [Al-Mustansiriyah University — Mustansiriyah Journal of Humanities](https://mjh.uomustansiriyah.edu.iq/index.php/mjh) | humanities, education | ar | no DC.Rights at all (2026 and 2023 articles) | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 7 | [King Abdulaziz University — Journal of Arts and Humanities](https://journals.kau.edu.sa/index.php/ART) | humanities | ar, en | DC.Rights only "الحقوق الفكرية (c) 2026 مجلة جامعة الملك عبدالعزيز: الآداب والعلوم الانسانية" | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 8 | [Al-Mustansiriyah University — Al-Mostansiriyah Journal for Arab and International Studies](https://mjais.uomustansiriyah.edu.iq/index.php/mjais) | politics, law, international studies | ar | per article `https://creativecommons.org/licenses/by/4.0` (2024, 6/6); a 2019 article has none | only `/cache/` | TECHNICALLY BLOCKED | Licensed 2024 articles have no `citation_pdf_url` and no PDF galley link (6/6), so there is no file to offer |
| 9 | [University of Al-Qadisiyah — Al-Qadisiyah Journal for Humanities Sciences](https://journalart.qu.edu.iq/index.php/QJHS) | humanities | ar | — | only `/cache/` | TECHNICALLY BLOCKED | Issue page lists 83 articles, but article pages answered HTTP 500 |
| 10 | [University of Thi-Qar — Journal of the College of Education for Humanities](https://jedh.utq.edu.iq/index.php/main) | humanities, education | ar | — | no robots.txt (404) | TECHNICALLY BLOCKED | HTTP 503 on issue pages |
| 11 | [Larbi Tebessi University — journal platform](https://tsjp.univ-tebessa.dz/) | humanities, social sciences | ar, en, fr | — | only `/cache/` | NOT EXAMINED FURTHER | The site index redirects to a login form; the individual journal paths were not identified |

Also seen but not counted:
- **Already covered or decided:** EKB-hosted Egyptian faculty journals (Cairo and Alexandria arts) and the Arab Journals Platform.
- **Not Arab-world sources:** Granada's *MEAH*, a Malang-hosted Moroccan article, and the Oujda journal on DOAJ (no OJS host found).

## Notes for maintainers

- **Multiple DC.Rights values.** Joussour writes three DC.Rights values: text, a copyright line and the URL. The shipped xpath takes the first value that *starts with* the CC URL, so the order does not matter. A fixture with this shape is still a cheap regression test.
- **Al-Mustansiriyah** runs at least three OJS journals with three different outcomes: licensed, licensed but without PDFs, and unlicensed. Round 8 tried candidate addresses for this university that did not answer; these journal-specific hosts (`amm.`, `mjais.`, `mjh.uomustansiriyah.edu.iq`) are the real ones. Each needs its own verdict, as with the Mosul hosts in round 9.
- **Pinned Core.** No Core change is needed for rows 1–3.
