# Discovery round 13: manga, comics and books in Arabic or English — 2026-10-12

Scope: **manga, comics and books whose content is Arabic or English.** Every domain was checked first against
the comics round, rounds 3–12, `candidate-sources.md`, `source-matrix.md` and every adapter's `source.yaml`
(1,225 recorded domains). Most well-known open sources were already there (StoryWeaver, Global Storybooks,
3asafeer, Let's Read Asia, Literacy Cloud, Diesel Sweeties, Cat and Girl, Ozy and Millie, Samandal, TokTok,
Manga Arabia, KFNL, Dar BibAlex, Waqfeya, Shamela, Kotobati, Craphound and others).

- **Access:** OneShelf's own User-Agent, robots.txt first, about one request per 1.5 s. Nothing was bypassed.
- **Rights:** unchanged ([rights-model.md](rights-model.md)). A copy is offered only on a licence or grant the
  creator states for the content copied. Free to read is not free to copy.
- **"Works" means checked live:** every file the new adapters list was fetched (first bytes, with a range
  request) and has the right signature: 25 PDFs (Peter Watts), 23 EPUBs (English Literature Ebooks) and 59
  EPUBs (Megamouse Books).

**Outcomes (15 sources):** IMPLEMENTED 3, RIGHTS NEED REVIEW 3, TECHNICALLY BLOCKED 4, NOT ELIGIBLE 5.

**Manga:** no new eligible source. *Ubunchu!* is CC BY-NC, but its files are fan translations on third-party
hosts (and it is on MangaDex, which OneShelf already covers). No CC-licensed OEL manga was found.

**Arabic:** no new eligible source. The Arabic comics magazines (Samandal, TokTok, Garage, Skefkef, Lab619,
Majid) are commercial or on Issuu; Arabic open-licence book publishers state contradictory terms (Darah, like
KFNL in earlier rounds).

## Implemented — three adapters (VERIFIED live, pinned Core, API 1.0)

| Adapter | Label | Rights evidence | Live check (2026-10-12) |
|---|---|---|---|
| `oneshelf.peter-watts` | `Peter Watts (rifters.com) · Books · EN` | The backlist page: "These documents are available under a Creative Commons License", `rel="license"` CC BY-NC-SA 2.5; each novel ends with the licence text | PASS: 25 units (4 novels, stories, essays); *Starfish* PDF (1.4 MB) and *Home* PDF validated; all 25 PDFs present |
| `oneshelf.englishliteratureebooks` | `English Literature Ebooks (Emma Laybourn) · Books · EN` | Home page: "You are welcome to share or copy the ebooks on this site for any non-commercial purpose. They may not be sold." | PASS: poetry (11 books) and abridged novels (12); EPUBs validated; all 23 present |
| `oneshelf.megamouse-books` | `Megamouse Books (Emma Laybourn) · Children's books · EN` | Book list: "You may share or copy the free books as much as you like, so long as you do not sell them." | PASS: 59 books; EPUBs validated; all 59 present |

Build notes:
- **Gates:** each downloads recipe reads the page that states the licence or grant and gives a file only
  while it is there (a SYNTHETIC fixture without it gives none). A unit's key must be a plain file name of the
  author's own files; anything else gives nothing.
- **Peter Watts:** the novels' pages are 1–1.5 MB (over the fixture limit), so their PDFs are named from the
  backlist's links to them (`STARFISH.htm` → `shorts/PeterWatts_Starfish.pdf`); all four were fetched live.
  *The Things* photo-book (designed by someone else) and links to other sites are not units. *Echopraxia*
  (not under CC) is not offered.
- **Emma Laybourn's sites:** only EPUBs are offered, because the PDFs' names do not always match the EPUBs'
  (`grannysmall.epub`, `granny-small.pdf`). Megamouse books hosted on Smashwords are not units.
- **Fixtures:** line-end whitespace was normalised outside attribute values. Raw `git diff --check` reports 8
  trailing-whitespace lines, all inside multi-line `<meta content="…">` values of the Emma Laybourn fixtures,
  kept verbatim for source fidelity.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Outcome | Adapter / blocker |
|---|---|---|---|---|---|---|---|
| 1 | [Peter Watts — The Backlist](https://www.rifters.com/real/shorts.htm) | SF novels, stories, essays | en | CC BY-NC-SA 2.5 stated for "these documents" (`rel="license"`); full licence text in each novel | no robots.txt (404) | IMPLEMENTED | `oneshelf.peter-watts` |
| 2 | [English Literature Ebooks](https://www.englishliteratureebooks.com/) | public-domain poetry anthologies, abridged classic novels | en | the editor's own permission: share or copy for any non-commercial purpose | nothing disallowed | IMPLEMENTED | `oneshelf.englishliteratureebooks` |
| 3 | [Megamouse Books](https://www.megamousebooks.com/) | children's stories, abridged children's classics | en | the author's own permission: share or copy, not sell | nothing disallowed | IMPLEMENTED | `oneshelf.megamouse-books` |
| 4 | [Ubunchu! (Aerial Line)](https://seotch.wordpress.com/ubunchu/) | manga | ja, en (fan) | CC BY-NC 3.0 | WordPress defaults | NOT ELIGIBLE | Files are fan translations on third-party hosts; the series is on MangaDex |
| 5 | [King Abdulaziz Foundation (Darah)](https://darah.gov.sa/) | Arabic books | ar | CC BY-ND announced, but the store's terms forbid copying and storing | — | RIGHTS NEED REVIEW | Contradictory terms, as with KFNL |
| 6 | [ALECSO publications and OER network](https://alecso.org/nsite/ar/) | Arabic reports, education | ar | no licence on the items sampled | — | RIGHTS NEED REVIEW | `alecso.org/publications/` was recorded before; no item licence |
| 7 | [OpenArabic.org](https://openarabic.org/arabic-short-stories/) | guide to Arabic graded readers | ar, en | points to Global Storybooks, StoryWeaver, 3asafeer | `User-agent: *` | NOT ELIGIBLE | A guide, not a library; its sources are already recorded |
| 8 | [Comics English](https://www.comicsenglish.com/) | comic strips for English learners | en | a CC BY-NC 4.0 notice was reported; the live site shows none | no rules | RIGHTS NEED REVIEW | No licence on the current site |
| 9 | [Obooko](https://www.obooko.com/) | free e-books | en | "legally licensed", no open licence or copying grant found | — | NOT ELIGIBLE | Free to read and keep is not a grant to copy |
| 10 | [Karl Schroeder — Ventus](https://www.kschroeder.com/) | SF novel | en | CC BY-NC-ND (reported) | AI crawlers blocked | TECHNICALLY BLOCKED | The book page answers 404 |
| 11 | [RAMP Jordan](https://www.rampjo.org/) | Arabic early-grade readers | ar | — | — | TECHNICALLY BLOCKED | The domain no longer resolves |
| 12 | [ubunchu.net](http://ubunchu.net/) | manga | ja | — | — | TECHNICALLY BLOCKED | The domain no longer resolves |
| 13 | [Lab619, Skefkef, Garage](https://arablit.org/2015/08/31/garage/) | Arabic comics magazines | ar | no licence; a single free first issue reported for Lab619 | — | NOT ELIGIBLE | Commercial magazines |
| 14 | [AUB guide: online Arabic comics](https://aub.edu.lb.libguides.com/c.php?g=276541&p=1842965) | list of Arabic comics sites | ar | each listed site is commercial, on Issuu or Facebook | — | NOT ELIGIBLE | No open-licence source in the list |
| 15 | [Syrian General Book Authority](https://www.enabbaladi.net/372828/) | Arabic books (600+ PDFs reported) | ar | no licence found | — | TECHNICALLY BLOCKED | No official site reached from the reports |
