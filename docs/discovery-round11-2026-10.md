# Discovery round 11: Arabic journals in Yemen, Syria, Libya, Algeria, Sudan and Palestine — 2026-10-10

Continues round 10 ([discovery-round10-2026-10.md](discovery-round10-2026-10.md)) by the same rules:
- **Scope:** Arabic open-access sources not investigated before. Every domain and journal path was checked against rounds 3–10, `candidate-sources.md`, `source-matrix.md` and every adapter's `source.yaml`.
- **Access:** OneShelf's own User-Agent, robots.txt first, about one request per 1.2–1.5 s. Nothing was bypassed.
- **Rights:** unchanged ([round 8 rights decision](discovery-round8-2026-10.md#rights-decision-2026-10-09-journal-wide-statements-are-not-enough)). Only a versioned Creative Commons URL in the article's own DC.Rights counts. A footer or sidebar `rel=license` is never taken as the article's licence.

This round is discovery only: **nothing was built.**

**Outcomes (15 sources):** ELIGIBLE NOT BUILT 8, RIGHTS NEED REVIEW 6, TECHNICALLY BLOCKED 1.

**One politeness slip.** M'sila's robots.txt sets `Crawl-delay: 5`. The first probe of its second journal (OLDA, row 6) made four requests about 1.2 s apart before the delay was applied; every later M'sila request was 5.5 s apart. The adapter built in round 10 for the same host (`oneshelf.msila-japl`) is limited to 10 requests a minute.

## Recommended for the next build round

Six journals fit the round-7/8 adapter shape unchanged. The table samples five or six articles per issue with the shipped gate's regex.

| Candidate | Newer issue | Older issue | `citation_pdf_url` |
|---|---|---|---|
| Thamar Education (row 1) | 6/6 pass (2026) | 6/6 pass (2016); a 2006 article also passes | 12/12 |
| Thamar Arts (row 2) | 6/6 pass (2026) | 6/6 pass (2023) | 12/12 |
| Latakia Arts and Humanities (row 3) | 4/5 pass (2024); the fifth item has no licence and no PDF | a 2005 article passes | 5/6 |
| Zawia Arts (row 4) | 6/6 pass (2026); 5/5 (2025) | 5/5 pass (2023); 0/5 in a 2024 issue | 21/21 |
| Elmergib Humanities (row 5) | 6/6 pass (2026) | 6/6 pass (2024); a 2023 article has no licence | 13/13 |
| M'sila OLDA (row 6) | 6/6 pass (2026) | 6/6 pass (2020); a 2017 article also passes | 13/13 |

Build notes:
- **Thamar (Dhamar) University** runs both journals on `journal.tu.edu.ye`. That is one host with two adapters, like the Kufa journals.
- **Latakia** (Tishreen University's new name) answered slowly: several requests timed out after 40 s, and an archive page did not answer. An adapter needs a modest `rate_limit`, and live checks should be repeated before publishing.
- **Zawia and Elmergib:** part of each archive opens. Articles without an item licence stay listed with no file (Zawia's 2024 issue 148, Elmergib's 2023 issue).
- **M'sila OLDA:**
  - Its `issue/current` page lists no articles, so its pasted-address examples should use a numbered issue.
  - Its articles are Arabic, English and French, so the per-article language matters.
  - Same host and robots rules as `oneshelf.msila-japl`: one request per 5 s, no locale switch.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Outcome | Adapter / blocker |
|---|---|---|---|---|---|---|---|
| 1 | [Thamar University — مجلة كلية التربية (Journal of the Faculty of Education)](https://journal.tu.edu.ye/index.php/edu) | education, humanities, Islamic studies | ar | per article DC.Rights `https://creativecommons.org/licenses/by/4.0` plus `rel=license`; 12 of 12 sampled (2016, 2026) plus a 2006 article | only `/cache/` | ELIGIBLE NOT BUILT | **Recommended** |
| 2 | [Thamar University — مجلة كلية الآداب (Arts)](https://journal.tu.edu.ye/index.php/artsmain) | arts, humanities | ar | per article `https://creativecommons.org/licenses/by/4.0`; 12 of 12 sampled (2023, 2026) | only `/cache/` | ELIGIBLE NOT BUILT | **Recommended** |
| 3 | [Latakia (formerly Tishreen) University Journal — Arts and Humanities Sciences Series](https://journal.latakia-univ.edu.sy/index.php/humlitr) | Arabic literature, history, philosophy, education | ar (some en) | per article `https://creativecommons.org/licenses/by-nc-sa/4.0` plus `rel=license`; 4 of 5 (2024) and a 2005 article | only `/cache/` | ELIGIBLE NOT BUILT | **Recommended.** Slow host |
| 4 | [University of Zawia — مجلة كلية الآداب (UZFAJ)](https://journals.zu.edu.ly/index.php/UZFAJ) | humanities, history, Islamic studies, linguistics | ar (some en) | per article `https://creativecommons.org/licenses/by-nc/4.0`; 16 of 16 in 2023, 2025 and 2026; 0 of 5 in a 2024 issue | only `/cache/` | ELIGIBLE NOT BUILT | **Recommended.** Part of the archive opens |
| 5 | [Elmergib University — مجلة العلوم الإنسانية المرقب (Elmergib Journal of Human Science)](https://ehsj.elmergib.edu.ly/index.php/ejhs) | humanities | ar | per article `https://creativecommons.org/licenses/by-nc/4.0`; 12 of 12 (2024, 2026); a 2023 article has none | only `/cache/` | ELIGIBLE NOT BUILT | **Recommended.** Six issues since 2023. Not the round-9 Elmergib JHAS journal (login only) |
| 6 | [University of M'sila — El Omda in Linguistics and Discourse Analysis (OLDA)](https://journals.univ-msila.dz/index.php/OLDA) | linguistics, discourse analysis | ar, en, fr | per article `https://creativecommons.org/licenses/by-nc/4.0`; 12 of 12 (2020, 2026) plus a 2017 article | Crawl-delay 5; disallows `setLocale`, `search`, `browse` | ELIGIBLE NOT BUILT | **Recommended.** See the politeness note above |
| 7 | [Al-Saeed University — مجلة جامعة السعيد للعلوم الانسانية](https://journal.alsaeeduni.edu.ye/index.php/sjhas) | humanities, applied sciences | ar | per article `https://creativecommons.org/licenses/by/4.0` in 2026 (6/6); 2023 (6/6) and 2017 have none (an empty second DC.Rights) | only `/cache/` | ELIGIBLE NOT BUILT | Only the newest issue opens; low priority |
| 8 | [Taiz University (Turba) — مجلة العلوم التربوية و الدراسات الإنسانية](https://hesj.org/ojs/index.php/hesj) | education, humanities | ar | per article CC BY 4.0 on only 1 of 6 (2026) and 0 of 6 (2025); the others have just the sidebar `rel=license` | no rules | ELIGIBLE NOT BUILT | Too few articles carry an item licence; not recommended |
| 9 | [Sirte University — مجلة جامعة سرت للعلوم الانسانية](https://journal.su.edu.ly/index.php/humanities) | humanities | ar | DC.Rights only "الحقوق الفكرية (c) 2026 مجلة جامعة سرت للعلوم الانسانية" (2026 and 2001) | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 10 | [Hadhramout University Journal of Humanities](https://hu.edu.ye/hu-publications/journals/index.php/hujh) | humanities | ar, en | DC.Rights only a copyright line (2026 and 2014) | only WordPress paths | RIGHTS NEED REVIEW | No licence to gate on |
| 11 | [Maghnia University Centre — مجلة إحالات (IHALAT)](https://ojs.cu-maghnia.dz/index.php/ihalat) | linguistics, literature, criticism | ar, en, fr, es | 2025: no DC.Rights; 2018: only "Copyright (c) 2025 مجلة إحالات" | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 12 | [Omdurman Islamic University Journal](https://journal.oiu.edu.sd/index.php/oiuj) | Islamic studies, law | ar, en | DC.Rights only a copyright line and an empty value (2026 and 2014) | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 13 | [Islamic University of Gaza — IUG Journal of Humanities Research](https://journals.iugaza.edu.ps/index.php/IUGJHR) | humanities | ar, en | DC.Rights only a copyright line and an empty value (2026 and 2001) | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 14 | [University of Aden — Journal of Social Sciences & Humanities](https://journals.aden-univ.net/index.php/UAJSH) | social sciences, humanities | en (sampled) | DC.Rights only "Copyright (c) 2026 University of Aden Journal of Social Sciences & Humanities" | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 15 | [Damascus University Journal of Arts and Humanities](https://journal.damascusuniversity.edu.sy/index.php/humj) | arts, humanities | ar | — | robots.txt timed out | TECHNICALLY BLOCKED | Every request timed out after 40 s |

Also seen but not counted:
- **Not Arab-world sources:** Indonesian Arabic-studies journals (Walisongo, UIN Jakarta *Insaniyat*).
- **Already decided:** EKB-hosted Al-Azhar journals in Egypt.
- **No OJS host found:** the University of Science and Technology (Yemen) journal is in a DSpace repository.

## Notes for maintainers

- **Empty second DC.Rights.** Al-Saeed, Omdurman and IUG write a second DC.Rights meta tag with an empty value. The gate's xpath only takes a value that starts with the Creative Commons URL, so an empty value is refused like a missing one.
- **Sidebar licences.** Taiz (Turba) shows a CC BY `rel=license` in the sidebar of every article page, including articles whose own DC.Rights has only a copyright line. Under the round-8 decision this is not item-level evidence, which is why row 8 is not recommended.
- **Pinned Core.** No Core change is needed for rows 1–6.
