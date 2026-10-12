# Discovery round 14: manga, comics and books in Arabic or English — 2026-10-12

Continues round 13 ([discovery-round13-2026-10.md](discovery-round13-2026-10.md)) by the same rules: OneShelf's
own User-Agent, robots.txt first (Crawl-delay honoured), about one request per 1.5 s, nothing bypassed, and a
copy only on a licence, grant or public-domain statement the source makes for the content copied. Every domain
was checked against the 1,234 recorded in earlier rounds and adapters.

New this round: main now pins a Core with **plugin API 1.2**, whose reader can return sanitised **text**
units, so HTML-only book sites can be read without a PDF or EPUB.

**Outcomes (17 sources):** IMPLEMENTED 1, RIGHTS NEED REVIEW 1, TECHNICALLY BLOCKED 7, NOT ELIGIBLE 8.

**Manga and Arabic:** no new eligible source. The Arabic text libraries found (Arabic Collections Online,
Shamela, Al-Warraq, Bibliotheca Alexandrina, Ketab Online) are recorded already or reserve all rights.

## Implemented — one adapter (VERIFIED live, pinned Core 86c8b402, API 1.2)

| Adapter | Label | Rights evidence | Live check (2026-10-12) |
|---|---|---|---|
| `oneshelf.authorama` | `Authorama · Books · EN` | Each book's own footer: "This complete text of … is in the public domain" (also "belongs to the public domain", "is public domain", "is copyright-free"); 25 of 25 sampled books carry one | PASS on 5 books: *Flatland*, *The Secret Garden*, *The Nibelungenlied* (750 KB page), *Famous Affinities of History IV* ("copyright-free"), *Cambridge Sketches* |

Build notes:
- **Shape:** a book is one `one_shot` unit, read as text from its complete-book page (`/book/<slug>.html`);
  its content block holds the heading, the text and the footer, and the advertisement column is outside it.
  178 books are listed on the home page; a book is opened by pasting any of its addresses.
- **Gate:** the unit and the text exist only while the page's own footer states public-domain (or
  copyright-free) status; a SYNTHETIC fixture without it gives neither.
- **robots.txt** has one rule, `Disallow: text`, without a leading slash; it matches none of the paths
  requested.

## Every source

| # | Source | Content | Lang | Rights | robots.txt | Outcome | Adapter / blocker |
|---|---|---|---|---|---|---|---|
| 1 | [Authorama](https://www.authorama.com/) | public-domain books (HTML) | en | per book footer: public domain | `Disallow: text` only | IMPLEMENTED | `oneshelf.authorama` |
| 2 | [Christian Classics Ethereal Library](https://www.ccel.org/about/copyright.html) | Christian classics (HTML, PDF) | en | "These books may be used for personal, educational, or non-profit purposes", after describing both public-domain books and books used by permission; no rights field on the work page | Crawl-delay 10 | RIGHTS NEED REVIEW | The grant's scope is ambiguous and not per item |
| 3 | [Loyal Books](https://www.loyalbooks.com/) | public-domain audiobooks and e-books | en | site-wide "public domain" | Crawl-delay 60; `/search/` disallowed | TECHNICALLY BLOCKED | One request a minute |
| 4 | [American Literature](https://americanliterature.com/) | short stories, novels | en | — | blocks AI crawlers | TECHNICALLY BLOCKED | HTTP 403 to OneShelf's User-Agent |
| 5 | [Online-Literature](https://www.online-literature.com/) | classics | en | — | 403 | TECHNICALLY BLOCKED | HTTP 403 |
| 6 | [Lit2Go (USF)](https://etc.usf.edu/lit2go/) | classics with audio | en | — | system paths | TECHNICALLY BLOCKED | HTTP 500 on every page tried |
| 7 | [OpenLearn (Open University)](https://www.open.edu/openlearn/) | free courses (EPUB, PDF) | en | CC BY-NC-SA (reported) | 403 | TECHNICALLY BLOCKED | HTTP 403, robots.txt included |
| 8 | [Irregular Webcomic!](https://www.irregularwebcomic.net/) | webcomic | en | — | 403 | TECHNICALLY BLOCKED | HTTP 403 |
| 9 | [Classic Shorts](https://www.classicshorts.com/) | classic short stories | en | site © "except, naturally, the stories"; no grant | system paths | NOT ELIGIBLE | No public-domain statement per story |
| 10 | [Read Book Online](https://www.readbookonline.net/) | literature incl. modern works | en | site copyright only | no rules | NOT ELIGIBLE | Includes in-copyright works; no per-item status |
| 11 | [Full Text Archive](https://www.fulltextarchive.com/) | classics | en | "All non-literary content … © Full Text Archive"; no per-item status | `/collection/`, `/language/` disallowed | NOT ELIGIBLE | No statement for the texts themselves |
| 12 | [Freeditorial](https://freeditorial.com/en) | free e-books | en | "© 2026 Freeditorial. All rights reserved." | WordPress defaults | NOT ELIGIBLE | No grant |
| 13 | [Ketab Online — جامع الكتب الإسلامية](https://ketabonline.com/ar) | Arabic Islamic books | ar | "جميع الحقوق محفوظة" | no robots.txt | NOT ELIGIBLE | All rights reserved |
| 14 | [Smashwords](https://www.smashwords.com/) | self-published e-books | en | per book, mostly all rights reserved | `/books/download/` disallowed | NOT ELIGIBLE | Downloads are a disallowed path |
| 15 | [Darths & Droids](https://www.darthsanddroids.net/) | webcomic | en | no licence on the site | no rules | NOT ELIGIBLE | No licence found |
| 16 | [Electric Sheep Comix](http://www.electricsheepcomix.com/) | webcomic | en | no licence on the front page | Crawl-delay 10 | NOT ELIGIBLE | No licence found |
| 17 | [Hackles](http://hackles.org/) | webcomic | en | — | — | TECHNICALLY BLOCKED | HTTP 522 (origin down) |
