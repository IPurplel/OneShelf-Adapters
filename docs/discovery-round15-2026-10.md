# Discovery round 15: manga in Arabic or English — 2026-10-13

Manga only, by the rules of rounds 13–14: OneShelf's own User-Agent, robots.txt first, about one request per
1.5 s, nothing bypassed, and a copy only on a licence, grant or public-domain statement the source makes for
the content copied. Earlier rounds already record the official free-to-read platforms (MANGA Plus, K MANGA,
Manga Arabia and others), MangaDex, 3asq, Manga Library Z and the CC-licensed *Ubunchu!* and *Mikako-san*.

This round tried new angles: author free-use releases, Japanese government manga (the Government of Japan
Standard Terms of Use v2.0 are compatible with CC BY 4.0), and Arabic manga publishers.

**Outcomes (5 sources):** IMPLEMENTED 1, TECHNICALLY BLOCKED 2, NOT ELIGIBLE 2.

## Implemented — one adapter (VERIFIED live, pinned Core 86c8b402, API 1.0)

| Adapter | Label | Rights evidence | Live check (2026-10-13) |
|---|---|---|---|
| `oneshelf.mod-japan-manga` | `Manga-Style Defense of Japan (Japan MOD) · Manga · EN` | The ministry's own [Terms of Use](https://www.mod.go.jp/en/notice.html): content "may be freely used, copied, publicly transmitted, translated or otherwise modified", commercial use included, compatible with CC BY 4.0; logos and organisational character designs excluded | PASS: 3 booklets (2019, 2018, 2017); 2019 PDF validated (32 pages); all three PDFs present |

Build notes:
- The terms exclude the ministry's logo and character designs that represent the organisation. The booklets'
  characters are ordinary people (the 2019 colophon credits the drawings to Manga Designers Lab, publisher the
  Ministry of Defense); the logo on a cover stays only as part of the unaltered booklet.
- The main site's terms page is `/en/notice.html` ("Terms of Use" in the English site's footer); it was missed
  at first because the Japanese home page answered with a short stub.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Outcome | Adapter / blocker |
|---|---|---|---|---|---|---|---|
| 1 | [Japan Ministry of Defense — Manga-Style Defense of Japan (English)](https://www.mod.go.jp/j/kids/comic/e/index.html) | government explainer manga, 2017–2019 | en | the ministry's Terms of Use (Standard Terms of Use 2.0): free reuse incl. commercial, CC BY 4.0 compatible | `/a/`, `/sp/j/` only | IMPLEMENTED | `oneshelf.mod-japan-manga`. Main site terms: [mod.go.jp/en/notice.html](https://www.mod.go.jp/en/notice.html) |
| 2 | *Give My Regards to Black Jack* (Shuho Sato) — English episodes on [Smashwords](https://www.smashwords.com/books/byseries/8764/title) | medical drama manga | en | the author has allowed free secondary use since 15 September 2012 | Smashwords disallows `/books/download/` | TECHNICALLY BLOCKED | Downloads are a disallowed path; the author's own site (mangaonweb.com) is gone |
| 3 | Black Jack free English app (iOS, third party) | as above | en | relies on the author's free-use release | — | TECHNICALLY BLOCKED | An app, not a website |
| 4 | [مانجا العربية (Manga Arabia / Manga for Kids)](https://aawsat.com/node/3172571) | Arabic manga magazines | ar | free to read in the app; no licence | — | NOT ELIGIBLE | Free to read is not free to copy; app-only |
| 5 | Search for CC-licensed OEL manga | — | en | none found | — | NOT ELIGIBLE | Results were commercial titles and fan-translation aggregators |
