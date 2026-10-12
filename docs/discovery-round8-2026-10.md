# Discovery round 8: more Arabic journals in Iraq, and two in Jordan and Palestine — 2026-10-09

Continues round 7 ([discovery-round7-2026-10.md](discovery-round7-2026-10.md)) on the same day and by the same
rules:
- **Scope:** Arabic open-access journals not investigated before. Every domain was checked against the docs of rounds 1–7.
- **Access:** every source was read with OneShelf's own User-Agent, robots.txt first. Nothing was bypassed.
- **Rights:** a licence counts only when the article's own page states it. A journal-wide statement is never taken as an article's licence.

**Outcomes (9 sources):** IMPLEMENTED 4 (Tikrit, Babylon, Wasit and Diyala universities), RIGHTS NEED REVIEW 2,
TECHNICALLY BLOCKED 1, NOT EXAMINED FURTHER 2.

## Implemented — four adapters (VERIFIED live, pinned Core, API 1.0)

The four adapters follow the round-7 pattern:
- **Structure:** one Open Journal Systems journal per adapter. Every article of an issue is listed, and an article's PDF is offered only while its own DC.Rights meta tag is a Creative Commons licence.
- **Language:** the file's language is the article's own `citation_language`.
- **Checks:** all four pass `check-adapter` on the pinned Core (`475c145f`). Each has a SYNTHETIC refusal test.
- **Mutation check:** the gate has two layers, the licence value and the licence suffix in the URL regex. Either one alone refuses the SYNTHETIC page. With both removed, every refusal test fails.

| Adapter | Source | Language / type | Rights gate | Live checks |
|---|---|---|---|---|
| `oneshelf.tikrit-jtuh` | jtuh.org — مجلة جامعة تكريت للعلوم الإنسانية (Journal of Tikrit University for Humanities) | ar, articles (PDF) | the article's DC.Rights Creative Commons licence (CC BY 4.0) | 2 PASS: issue 143 (2026) and issue 114 (2025, 13 pp) |
| `oneshelf.babylon-jubh` | journalofbabylon.com — مجلة جامعة بابل للعلوم الانسانية (Journal of University of Babylon for Humanities) | ar, en, articles (PDF) | as above. The licence is written `http://creativecommons.org/licenses/by/4.0` | 2 PASS: issue 226 (2026, English article) and issue 172 (2024, 21 pp). Refused live: article 4292 (2022); see notes |
| `oneshelf.wasit-lark` | lark.uowasit.edu.iq — مجلة لارك للفلسفة واللسانيات والعلوم الاجتماعية (Lark Journal) | ar, articles (PDF) | as above (CC BY 4.0) | 2 PASS: issue 94 (2026, 81 articles) and the oldest listed issue 70 (17 pp) |
| `oneshelf.diyala-djhr` | djhr.uodiyala.edu.iq — مجلة ديالى للبحوث الانسانية (Diyala Journal for Human Research) | ar, articles (PDF) | as above (CC BY-NC 4.0) | 2 PASS: issue 150 (2026) and issue 91 (45 pp) |

- **Themes.**
  - **Lark and Diyala:** default OJS theme, the same selectors as round 7.
  - **Tikrit and Babylon:** OJS Bootstrap 3 theme. Their catalogs read `div.article-summary h3.media-heading a`, and the issue heading comes from the breadcrumb's last item.
- **Babylon's host names.**
  - **The site's links:** the site writes its issue and article links on `mail.journalofbabylon.com`.
  - **What the adapter requests:** everything on `www.`. The catalog keys articles by id only. On `www.`, `citation_pdf_url` names `www.`, and the cover image is rewritten to `www.`.
  - **Pasted addresses:** an issue address on either host opens the work.
  - **robots.txt:** `www.` has only commented content-signal lines and no rules. `mail.` has no robots.txt and is never requested.
- **Diyala's journal path** is `DJHR2022`; `index.php/DJHR` answers 404.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Outcome | Adapter / blocker |
|---|---|---|---|---|---|---|---|
| 1 | [Tikrit University — Journal of Tikrit University for Humanities](https://jtuh.org/index.php/jtuh) | humanities | ar | per article DC.Rights `https://creativecommons.org/licenses/by/4.0` (6 of 6 sampled, 2025–2026) | only `/cache/` | IMPLEMENTED | `oneshelf.tikrit-jtuh` |
| 2 | [University of Babylon — مجلة جامعة بابل للعلوم الانسانية](https://www.journalofbabylon.com/index.php/JUBH) | humanities | ar, en | per article `http://creativecommons.org/licenses/by/4.0` (2024–2026). The 2022 article 4292 names only the journal's copyright page | no rules | IMPLEMENTED | `oneshelf.babylon-jubh` |
| 3 | [Wasit University — Lark Journal](https://lark.uowasit.edu.iq/index.php/lark) | philosophy, linguistics, social sciences | ar | per article CC BY 4.0 | only `/cache/` | IMPLEMENTED | `oneshelf.wasit-lark` |
| 4 | [University of Diyala — مجلة ديالى للبحوث الانسانية](https://djhr.uodiyala.edu.iq/index.php/DJHR2022) | humanities | ar | per article `https://creativecommons.org/licenses/by-nc/4.0` | allows everything | IMPLEMENTED | `oneshelf.diyala-djhr` |
| 5 | [Al al-Bayt University — Al-Manarah series](https://journals.aabu.edu.jo/) (`Art`, `law`, `Edu`, `Bus`) | humanities, law, education | ar, en | DC.Rights only "Copyright (c) 2026 سلسلة …" and an empty second value (9 of 9 sampled) | only `/cache/` | RIGHTS NEED REVIEW | No licence to gate on |
| 6 | [An-Najah University Journal for Research — B (Humanities)](https://journals.najah.edu/journal/anujr-b/) | humanities, social sciences | ar, en | one journal-wide CC BY-NC 4.0 notice above the footer of every page ("… © 1986 by An-Najah National University is licensed under CC BY-NC 4.0"); no per-article licence | no robots.txt (404) | RIGHTS NEED REVIEW | Journal-level only. Own platform (not OJS); pages carry `citation_pdf_url` |
| 7 | [University of Jordan — journal archive](https://archives.ju.edu.jo/) (Dirasat) | humanities, social sciences, law, education | ar, en | — | robots.txt itself answers "Request Rejected" (a web application firewall) | TECHNICALLY BLOCKED | Firewall refuses OneShelf's User-Agent; not worked around |
| 8 | [Tikrit University — Journal of Legal Sciences](https://jls.tu.edu.iq/) | law | ar | — | allows `*` except system paths; refuses several AI crawlers; `Content-Signal: ai-train=no` | NOT EXAMINED FURTHER | Not OJS; no metadata read |
| 9 | [University of Al-Qadisiyah — humanities journals](https://journalofhumanities.qu.edu.iq/) | humanities | ar | — | robots.txt answers an HTML page | NOT EXAMINED FURTHER | Another platform; not examined |

Hosts tried that did not answer and may not be the journals' real addresses are not counted. They were candidate
addresses for journals of Al-Mustansiriyah, Anbar, Mosul (Adab Al-Rafidayn) and Basrah universities.

## Notes for maintainers

- **Babylon article 4292 (2022)** is a third journal-wide case, after the round-7 notes on kjlps and Al-Adab.
  - **The article's own claim:** its DC.Rights is "الحقوق الفكرية (c) 2022 جامعة بابل" plus a link to the journal's own `CopyrightandLicensing` page.
  - **The journal's claim:** the sidebar of the same page says the journal "is licensed under a Creative Commons Attribution 4.0 International License".
  - **What the adapter does:** it refuses the file, as round 7 did. Test 4 keeps the refusal as a regression case. The sidebar statement is not accepted (see the rights decision below).
- **An-Najah** is the same question at journal level. Its pages state CC BY-NC 4.0 for the journal and nothing per article, so it stays RIGHTS NEED REVIEW and is not built.
- **Pinned Core.** No Core change was needed.

## Rights decision (2026-10-09): journal-wide statements are not enough

This is the current policy decision, applied to every adapter of rounds 7 and 8:
- **The rule:** a file is exposed only when the individual article's own page gives deterministic licence evidence. Here that is a versioned Creative Commons licence URL in its DC.Rights meta tag.
- **What does not count:** a journal-wide or archive-wide statement alone (footer, sidebar, policy text or a journal-level notice). It is not enough to expose an article, historical or current, whose own page has no licence evidence.

Applied:
- **Babylon article 4292 (2022) remains refused.** Test 4 of `oneshelf.babylon-jubh` and a live check confirm it. The same page with an item-level licence added gives the PDF, so the refusal is a rights decision and not a parser failure.
- **Older kjlps and Al-Adab articles** without an item-level licence remain listed with no file (round 7).
- **An-Najah remains not built.**
- **No journal-wide licence fallback** was added to any adapter. Core's rights semantics are unchanged.
- **Accepted licence values:** the gate accepts any versioned `creativecommons.org/licenses/<type>/<version>` URL, over http or https, with or without a trailing slash. This is the same gate as the IMIST and QU Press adapters already on `main`, and every such licence allows the unaltered private copy OneShelf keeps.
  - **Observed values:** Tikrit, Babylon and Wasit state CC BY 4.0; Diyala states CC BY-NC 4.0.
  - **Refused:** a public-domain dedication URL (`publicdomain/zero`), an unversioned `licenses/` URL, any other host and copyright lines.

The rule can be reconsidered later, but only as a dedicated rights-policy decision.

## Best candidates for the next round

- **Other University of Babylon journals** on the same host (`JUBPAS`, `JUBES`, `JUB`) and **other Tikrit, Wasit and Diyala journals**: the same gate. Most are English sciences.
- **Ibn al-Haitham Journal** (round 7, row 14): still eligible and not built.
- **An-Najah, Babylon's 2022 archive, kjlps and Al-Adab:** not planned. Only a dedicated rights-policy decision could change the rule below.
