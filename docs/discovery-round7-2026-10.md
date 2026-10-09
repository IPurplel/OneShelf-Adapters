# Discovery round 7: Arabic journals in Iraq and Jordan — 2026-10-09

Priority: Arabic open-access sources not investigated before (every domain checked against the docs and
manifests of rounds 1–6), then any other source found on the way. Leads came from web searches (DOAJ's Arabic
journal listings among them) and from the round-6 backlog. Every source was read with OneShelf's own
User-Agent, robots.txt first. Rights were read on each article's or book's own page. Nothing bypassed: no
challenge, CAPTCHA, login or robots rule was worked around. A journal-wide statement was never taken as an
article's licence when the article's own page says otherwise or says nothing.

**Outcomes (20 sources):** IMPLEMENTED 7 (5 University of Kufa journals, Al-Adab Journal of the University of
Baghdad, JJES of Yarmouk University), VERIFIED BUT HELD 1 (Language Science Press, row 8), ELIGIBLE NOT BUILT 1,
RIGHTS NEED REVIEW 5, TECHNICALLY BLOCKED 4, NOT EXAMINED FURTHER 2.

## Implemented — seven adapters (VERIFIED live, pinned Core, API 1.0)

All seven pass `check-adapter` on the pinned Core (`475c145f`). Every licence condition is covered by a
refusal test. In a mutation check, the test fails once the licence condition is removed from the recipe.

| Adapter | Source | Language / type | Rights gate | Live checks |
|---|---|---|---|---|
| `oneshelf.kufa-jall` | journal.uokufa.edu.iq/…/jall — مجلة اللغة العربية وآدابها | ar, articles (PDF) | the article's DC.Rights Creative Commons licence (CC BY 4.0) | 2 PASS: issue 1088 (2026, 64 pp) and oldest listed issue 36 (2021, 30 pp) |
| `oneshelf.kufa-fqhj` | …/fqhj — مجلة كلية الفقه | ar, articles (PDF) | as above | 1 PASS: issue 1094 (2026, 34 pp). 1 refused live: article 8282, issue 569 (2022). It states only "Copyright (c) 2022 مجلة كلية الفقه", so it is listed with no file |
| `oneshelf.kufa-arts` | …/kufa_arts — مجلة آداب الكوفة | ar, en, articles (PDF) | as above; the file's language is the article's own `citation_language` | 2 PASS: issue 1000 (2026, ar, 26 pp) and issue 54 with the English article 12156 (`language: en`, 24 pp) |
| `oneshelf.kufa-kjlps` | …/kjlps — مجلة الكوفة للعلوم القانونية والسياسية | ar, articles (PDF) | as above | 2 PASS: issues 1047 (2024, 29 pp) and 1055 (6.6 MB, 29 pp). Refused live: article 9483 (oldest listed issue 661), which has only a copyright line; see notes |
| `oneshelf.kufa-ewjh` | …/ewjh — مجلة كلية التربية للبنات للعلوم الإنسانية | ar, articles (PDF) | as above | 2 PASS: issues 1093 (2025, 24 pp) and 814 (26 pp). Oldest listed issue 635: article 9185 is CC but has no PDF galley, so there is no file |
| `oneshelf.baghdad-aladab` | aladabj.uobaghdad.edu.iq — مجلة الآداب (Al-Adab Journal) | ar, articles (PDF) | as above. The journal writes the licence as `http://creativecommons.org/licenses/by/4.0`, and the gate accepts http and https | 2 PASS: issues 179 (2026, 20 pp) and 166 (76 pp). Refused live: article 1633 (oldest listed issue 23, 2020), which has no DC.Rights; see notes |
| `oneshelf.yarmouk-jjes` | jjes.yu.edu.jo — المجلة الأردنية في العلوم التربوية (JJES) | ar, en, articles (PDF) | as above (CC BY-NC 4.0) | 1 PASS: issue 90 (2026, 14 pp). 1 refused live: article 295 (issue 89), with only "Copyright (c) 2026 المجلة الأردنية في العلوم التربوية" |

- **Kufa, Baghdad and Yarmouk (Open Journal Systems).** These follow the IMIST and QU Press pattern of round 6:
  - **Rights:** each article page carries its own licence as a DC.Rights meta tag. Catalogs list every article, and the downloads recipe decides per article (`visibility: all_listed_items`, `local_copy: eligible_items_only`).
  - **Tests:** each adapter has a SYNTHETIC fixture, a real article page with its licence removed, which must give no file. fqhj and JJES also have a real article without a licence.
  - **Structure:** there is one adapter per journal, because API 1.0 percent-encodes `/` (round 6 Core finding).
  - **New in this round:** the downloads recipe reads the article's `citation_language` into the file's `language`, so آداب الكوفة's English articles are labelled `en`. This answers the round-6 An-Najah concern for journals whose pages state a language.
- **Rate.** Kufa answers every request, 200s included, with `Retry-After: 3600`. That is not a rate limit, but the adapters stay at 20 requests a minute, one at a time. Surveys were kept to a few issues per journal, two seconds apart.
- **JJES** was ELIGIBLE NOT BUILT in round 6 (row 25), because the server stopped answering. It answered again on 2026-10-09 at 20:01Z. Yield is still low: only the newest issues carry the licence.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Outcome | Adapter / blocker |
|---|---|---|---|---|---|---|---|
| 1 | [University of Kufa — مجلة اللغة العربية وآدابها](https://journal.uokufa.edu.iq/index.php/jall) | Arabic language and literature | ar | per article DC.Rights `https://creativecommons.org/licenses/by/4.0` (back to 2021) | `/cache/`, system paths, `/index.php/*/login` | IMPLEMENTED | `oneshelf.kufa-jall` |
| 2 | [Kufa — مجلة كلية الفقه](https://journal.uokufa.edu.iq/index.php/fqhj) | Islamic jurisprudence | ar | per article CC BY 4.0 (2023–2026 sampled); 2022 article 8282 only a copyright line | as row 1 | IMPLEMENTED | `oneshelf.kufa-fqhj` |
| 3 | [Kufa — مجلة آداب الكوفة](https://journal.uokufa.edu.iq/index.php/kufa_arts) | arts, humanities | ar, en | per article CC BY 4.0 | as row 1 | IMPLEMENTED | `oneshelf.kufa-arts` |
| 4 | [Kufa — مجلة الكوفة للعلوم القانونية والسياسية](https://journal.uokufa.edu.iq/index.php/kjlps) | law, political science | ar | per article CC BY 4.0 (2023–2024 sampled). The site footer licenses the whole journal under CC BY 4.0, but the oldest listed article (9483, 2012) states only a copyright line | as row 1 | IMPLEMENTED | `oneshelf.kufa-kjlps` |
| 5 | [Kufa — مجلة كلية التربية للبنات للعلوم الإنسانية](https://journal.uokufa.edu.iq/index.php/ewjh) | humanities | ar | per article CC BY 4.0 + `rel="license"` | as row 1 | IMPLEMENTED | `oneshelf.kufa-ewjh` |
| 6 | [University of Baghdad — مجلة الآداب](https://aladabj.uobaghdad.edu.iq/index.php/aladabjournal) | arts, humanities | ar | per article DC.Rights `http://creativecommons.org/licenses/by/4.0` (2026 and mid-archive: 7 of 7). The 2020 article 1633 has no DC.Rights; its page shows the journal's policy, which says articles are CC BY 4.0 | only `/cache/` | IMPLEMENTED | `oneshelf.baghdad-aladab` |
| 7 | [Yarmouk — JJES](https://jjes.yu.edu.jo/index.php/jjes) | education | ar, en | per article CC BY-NC 4.0 on the newest issues only (round 6: 10 of 451) | only `/cache/` | IMPLEMENTED | `oneshelf.yarmouk-jjes` |
| 8 | [Language Science Press](https://langsci-press.org/) | linguistics books | en (also de, zh, pt, es) | per book DC.Rights CC BY 4.0 (7 of 7 sampled, 2016–2025) | only `cache/`; Zenodo allows `/records/*/files/`, Crawl-delay 10 | VERIFIED BUT HELD | An adapter (`oneshelf.langsci-press`) was built and verified, but it is not an Arabic source and is kept out of this change for a separate review |
| 9 | [Kufa Review](https://journal.uokufa.edu.iq/index.php/Kufa_Review) | humanities | en | DC.Rights only "الحقوق الفكرية (c) … Kufa Review" | as row 1 | RIGHTS NEED REVIEW | No licence to gate on |
| 10 | [Kufa — `kjps`](https://journal.uokufa.edu.iq/index.php/kjps) | — | en | no DC.Rights licence on the current issue's articles | as row 1 | RIGHTS NEED REVIEW | No licence to gate on |
| 11 | [Baghdad — Journal of the College of Education for Women](https://jcoeduw.uobaghdad.edu.iq/index.php/journal) | education | ar | DC.Rights only "Copyright (c) 2026 مجلة كلية التربية للبنات" | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 12 | [Journal of Arabic and Islamic Studies](https://journals.uio.no/JAIS) (Oslo) | Arabic and Islamic studies | en (some ar) | DC.Rights only "Copyright (c) 2026 Journal of Arabic and Islamic Studies" | only `/cache/` | RIGHTS NEED REVIEW | No licence on the article page |
| 13 | [WAC Clearinghouse](https://wac.colostate.edu/books/) | writing-studies books | en | no licence link on the sampled book page | WordPress defaults | RIGHTS NEED REVIEW | Per-book licences not machine-readable on the page sampled |
| 14 | [Ibn al-Haitham Journal for Pure and Applied Sciences](https://jih.uobaghdad.edu.iq/index.php/j) (Baghdad) | science | en | per article CC BY 4.0 | only `/cache/` | ELIGIBLE NOT BUILT | Fits the same pattern; English science, outside this round's Arabic focus |
| 15 | Baghdad — [Journal of the College of Languages](https://jcolang.uobaghdad.edu.iq/index.php/jcolang), [Alustath](https://alustath.uobaghdad.edu.iq/index.php/alustath), [Journal of the College of Islamic Sciences](https://jcois.uobaghdad.edu.iq/index.php/jcois) | humanities | ar | — | only `/cache/` | TECHNICALLY BLOCKED (3) | `issue/current` lists no article links (another theme or no current issue); not examined further |
| 16 | [al-ʿUṣūr al-Wusṭā](https://journals.library.columbia.edu/index.php/alusur) (Columbia) | medieval Middle East | en, ar | CC BY-NC-ND 4.0 on the archive page | only `/cache/` | TECHNICALLY BLOCKED | `issue/current` lists no article links |
| 17 | [Kohl: a Journal for Body and Gender Research](https://kohljournal.press/) | gender studies | ar, en, fr | no licence found in the static home page | Crawl-delay 10 | NOT EXAMINED FURTHER | — |
| 18 | [Arab Council for the Social Sciences](https://theacss.org/) | publications | ar, en | no licence found | WordPress defaults | NOT EXAMINED FURTHER | — |
| 19 | Ifpo Arabic books on [OpenEdition Books](https://books.openedition.org/ifpo/) | books | ar, fr | per book | as the existing adapter | — (no new adapter) | `oneshelf.openedition-books` reads each book's `citation_language`, so a CC-licensed Ifpo book in Arabic already opens there (API 1.2) |

Rows 15 and 16 count as four technically blocked sources. Row 19 is not counted.

## Notes for maintainers

- **Journal-wide statements (kjlps, Al-Adab).**
  - **kjlps:** the site footer says the whole journal "مرخصة بموجب ترخيص المشاع الإبداعي" (CC BY 4.0), but article 9483 states only "الحقوق الفكرية (c) 2022".
  - **Al-Adab:** each article page repeats the policy "Articles are licensed under an open access Creative Commons CC BY 4.0", even on 2020 articles that carry no DC.Rights.
  - **What the adapters do:** they gate on the article's own DC.Rights, the conservative reading used since round 6. If a maintainer accepts the journal statement as covering the whole archive, the gate could move to source level (as `oneshelf.ibn-almuqaffa-ut`), which would unlock the older articles. **Decided 2026-10-09: not accepted.** Item-level evidence stays required; see the rights decision in [round 8](discovery-round8-2026-10.md#rights-decision-2026-10-09-journal-wide-statements-are-not-enough).
- **Pinned Core.** No Core change was needed.
  - **`check-all`:** it reports the 19 existing API 1.2 adapters as needing a newer Core, as before. The repository policy tests pass.
  - **`regex_replace` bug (round 5):** it does not affect these adapters, whose replacements are ASCII.

## Best candidates for the next round

- **Ibn al-Haitham Journal (row 14)** (still open after [round 8](discovery-round8-2026-10.md), which built four more Arabic journals) and other English-language University of Baghdad journals: they use the same OJS gate, so each is a few minutes' work with the generator approach used here.
- **Other Kufa journals** (`kufa.edu.iq` hosts 25): only five were confirmed Arabic with CC per article. The rest are mostly English sciences.
- **Older kjlps / Al-Adab articles**: not planned. Journal-wide statements were not accepted (see notes); only a dedicated rights-policy decision could change that.
- **Kohl, ACSS (rows 17–18)**: read their licence pages, and look for a machine-readable rights field.
