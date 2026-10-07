# Discovery round: manga, manhwa, manhua, comics and books

A discovery and qualification round — **no adapter was built from it**. It maps the wider ecosystem of reading
sites whose shape suits OneShelf (work → chapters → ordered pages) and keeps two questions apart: **technical
fit** and **rights**. A source with fit A and `RIGHTS_UNCLEAR` is interesting and *not* ready. Nothing here
changes an adapter, the Registry or Core. Earlier rounds: [source-matrix.md](source-matrix.md) (60 candidates)
and [candidate-sources.md](candidate-sources.md) (follow-up backlog); none of their sources is repeated here.

## How the sources were screened — 2026-09-30

- **Found through** web search in English, Japanese, Korean, Chinese, Arabic, French, Spanish, Portuguese,
  Indonesian and Vietnamese; publisher lists; webcomic hosting and collective directories (ComicFury forums,
  SpiderForest, Hiveworks, ComicControl usage lists); Tachiyomi/Mihon extension listings (discovery only);
  library and digital-humanities guides (AUB Arabic comics guide, national libraries).
- **Screened by machine, uniformly:** for every site, one request for robots.txt evaluated with this
  repository's RFC 9309 matcher for OneShelf's own User-Agent (`OneShelf/0.1 (+self-hosted personal
  library)`), one request for the front page, and an engine fingerprint read with **Scrapling's parser**
  (`scrapling.parser.Selector`): generator tags, WordPress/Madara/MangaStream/Comic Easel/ComicPress/Toocheke/
  ComicControl/Giga Viewer/Comici/Next.js/Nuxt/Drupal/Visual Library/Kitodo signatures, feeds, JSON-LD types,
  image hosts, and whether the page carries text without script. Scrapling's fetchers were not used — they
  impersonate browsers ([source-discovery.md](source-discovery.md#2-toolsinspect-source)).
- **Inspected by hand** where the fingerprint was promising: `./tools/inspect-source` (Core's HTTP client,
  robots first) on series, archive, chapter and page URLs, IIIF manifests and APIs; exact robots.txt rules
  for the paths an adapter would need.
- Nothing was solved, bypassed or retried around a refusal. A 403/429/challenge is recorded as what an
  ordinary permitted client meets. No cookies, tokens or keys were used or stored.

**robots.txt** is `allowed` (rules allow the front page and every probed reading path, or no robots.txt —
RFC 9309 treats a 4xx robots.txt, and an HTML page served in its place, as no rules), `partially_allowed`
(front page allowed, some reading paths — search, /api/, /viewer/, /archive/ … — disallowed), `disallowed`
(the front page itself; often `User-agent: *` listed with AI crawlers and `Disallow: /`), or `unavailable`
(401/403/429/5xx/challenge/no connection — the site refused or did not answer this client).

**Technical fit** is strictly OneShelf integration: A excellent · B good · C difficult but plausible · D poor
· F unusable · — not applicable (a directory or an excluded site). A trailing `p` marks a **provisional** grade
from the front-page fingerprint only; grades without it come from an inspected series → chapter → page chain
or API. **Rights** use the task's vocabulary; `FREE_OFFICIAL` means the rights holder lets people read for
free — it is not a grant to keep copies ([rights-model.md](rights-model.md)).

## Summary

```text
NEW SOURCE DISCOVERY SUMMARY

New websites investigated: 204

Manga: 50
Manhwa: 7
Manhua: 7
Comics/Webcomics: 78
Books: 51
Mixed: 11

Technical fit:
A: 9
B: 39
C: 47
D/F: 101
n/a (directories, excluded sites): 8

Rights:
OPEN_LICENSED: 17
PUBLIC_DOMAIN: 33
CREATOR_AUTHORIZED: 66
PUBLISHER_AUTHORIZED: 6
FREE_OFFICIAL: 58
RIGHTS_UNCLEAR: 19
RESTRICTED: 5
UNSUITABLE: 0

robots:
Allowed: 147
Partial: 28
Disallowed: 7
Unavailable: 22

READY FOR ELIGIBILITY REVIEW: 6
RIGHTS NEED REVIEW: 15
TECHNICALLY BLOCKED (shortlisted): 18

Potential reusable source families discovered: 6 (plus 2 documented and not recommended)
```

Discovery was stopped when further searches returned mostly the same publisher lists, sites already
screened, unauthorized aggregators, or sites that refuse this client. The count is what credible searching
produced, not a quota: 204 sites, of which 1 turned out to duplicate an existing adapter.

## Top OneShelf candidates

Chosen for architecture — stable ids, public access, a stable reader, few domains, good metadata, bounded
pagination — not popularity.

### READY FOR ELIGIBILITY REVIEW

Technically promising (fit A/B; a `p` grade still needs its series → page chain inspected), robots.txt allows
the paths, and the source itself states an open licence (per item where marked). Next step: confirm the
structure, the rights-model review (`rights.yaml`), then an implementation task.

| Source | URL | Content | Rights | robots.txt | Fit | Why |
|---|---|---|---|---|---|---|
| NIJL Kokusho Database | https://kokusho.nijl.ac.jp/ | Books | `OPEN_LICENSED` | allowed | A | Per-item licence in the manifest: CC BY-SA 4.0 (verified, 91 canvases). Early Japanese books incl. illustrated kibyōshi |
| Acomics | https://acomics.ru/ | Webcomic | `OPEN_LICENSED` | allowed | A | Russian webcomic host. /~<slug>/<n> sequential pages, images under /upload/!c/<author>/<slug>/; each comic's /about page has a licence field (e.g. CC BY-NC-SA 4.0 — verified). Licences vary per comic: only comics whose /about names an open licence would qualify (a declarative per-comic gate) |
| Sandra and Woo | https://www.sandraandwoo.com/ | Webcomic | `OPEN_LICENSED` | allowed | B | CC BY-NC-ND 3.0 linked on every page (verified); /archive/; images under /comics/ |
| Grise Bouille | https://grisebouille.net/ | Webcomic | `OPEN_LICENSED` | allowed | Bp | Gee; CC BY-SA 4.0 linked on every page (verified). Mixes comics and illustrated text |
| Unglue.it | https://unglue.it/ | Books | `OPEN_LICENSED` | allowed | B | CC-licensed ebooks (verified link shapes). File hosts not yet checked — if downloads resolve to arbitrary publisher hosts it is an aggregator (the DOAB blocker) |
| GDL content API | https://content.digitallibrary.io/api/ | Children's Books | `OPEN_LICENSED` | allowed | Bp | API page reachable; book endpoints not yet exercised |

### RIGHTS NEED REVIEW

Clean structure, but the rights question is open: creator-hosted comics free to read with no stated licence
(a reader saves a copy — [rights-model.md](rights-model.md) needs a grant for that), public domain only in one
jurisdiction (Faded Page: Canada; PG Australia: Australia), publisher-authorized free reading, or per-item
public-domain status that must be read from metadata (NDL).

| Source | URL | Content | Rights | robots.txt | Fit | Why |
|---|---|---|---|---|---|---|
| SMBC | https://www.smbc-comics.com/ | Webcomic | `CREATOR_AUTHORIZED` | allowed | A | /comic/archive lists all 7,926 pages in one <select>; /comic/<slug> has #cc-comic image and title text (verified) |
| Paranatural | https://www.paranatural.net/ | Webcomic | `CREATOR_AUTHORIZED` | allowed | A | /comic/archive lists 921 pages in one response (verified) |
| El Goonish Shive | https://www.egscomics.com/ | Webcomic | `CREATOR_AUTHORIZED` | allowed | Ap | ComicControl family |
| Awkward Zombie | https://www.awkwardzombie.com/ | Webcomic | `CREATOR_AUTHORIZED` | allowed | Ap | ComicControl family |
| Octopus Pie | https://www.octopuspie.com/ | Webcomic | `CREATOR_AUTHORIZED` | allowed | B | Complete comic |
| Kill Six Billion Demons | https://killsixbilliondemons.com/ | Webcomic | `CREATOR_AUTHORIZED` | allowed | B | /comic/<slug>/ with #comic img (verified) |
| ComicFury | https://comicfury.com/ | Webcomic | `CREATOR_AUTHORIZED` | allowed | B | Creator-hosted (thousands of comics). /comicprofile.php?url=<slug>, /read/<slug>/archive, /read/<slug>/comics/<numeric id>, images on img.comicfury.com (verified). Licence per comic, rarely stated |
| The Duck Webcomics | https://www.theduckwebcomics.com/ | Webcomic | `CREATOR_AUTHORIZED` | allowed | Bp | /<ComicName>/ slugs; media under /media/users/ (verified on front page) |
| Mimi & Eunice | https://mimiandeunice.com/ | Webcomic | `CREATOR_AUTHORIZED` | allowed | Bp | Nina Paley; links copyheart.org ('copying is an act of love') — not a standard licence (verified link) |
| Manga Library Z | https://www.mangaz.com/ | Manga | `PUBLISHER_AUTHORIZED` | allowed | Cp | Out-of-print manga republished with authors' permission; /series/detail/<id>, /book/detail/<id> (verified); viewer host vw.mangaz.com allowed by robots; viewer images not yet inspected |
| NDL Digital Collections | https://dl.ndl.go.jp/ | Mixed | `PUBLIC_DOMAIN` | partially_allowed (blocks /search /api/) | A | Manifest verified (28 canvases); licence field points to NDL's general IIIF terms, so per-item PD status must come from item metadata |
| Faded Page | https://www.fadedpage.com/ | Books | `PUBLIC_DOMAIN` | allowed | A | EPUB and PDF via link.php?file=<pid>.epub (verified). Public domain in CANADA — may be in copyright elsewhere |
| Project Gutenberg Australia | https://gutenberg.net.au/ | Books | `PUBLIC_DOMAIN` | allowed | A | 522 EPUBs on its own host from one list page (verified). Public domain in AUSTRALIA — may be in copyright elsewhere |
| Dongman Manhua | https://www.dongmanmanhua.cn/ | Manhua | `FREE_OFFICIAL` | allowed (robots.txt answers with an HTML page (no rules)) | Bp | Naver's Chinese WEBTOON; likely reuses the WEBTOON adapter's pattern |
| AlphaPolis Manga | https://www.alphapolis.co.jp/manga/official | Manga | `FREE_OFFICIAL` | allowed | Cp | Publisher-run; 全話無料 series exist — a free-in-full filter may be possible; viewer not inspected |

### TECHNICALLY PROMISING BUT BLOCKED

Good structure or important content, blocked by something an adapter must not work around: robots.txt rules,
scrambled or session-bound images, a binary API, a text-only format Core cannot read, or app-only reading.

| Source | URL | Content | Rights | robots.txt | Fit | Why |
|---|---|---|---|---|---|---|
| Shonen Jump+ | https://shonenjumpplus.com/ | Manga | `FREE_OFFICIAL` | allowed (no robots.txt (404)) | F | Giga Viewer: /series/<id>, /episode/<id>, embedded #episode-json with ordered pages; per-series RSS/Atom (free_only=1). Pages tile-scrambled (choJuGiga "baku") and 403 to a plain client even with Referer (verified on Shonen Jump+) |
| MANGA Plus | https://mangaplus.shueisha.co.jp/ | Manga | `FREE_OFFICIAL` | allowed | F | Shueisha; Arabic among 10 languages. API is protobuf, which recipes cannot parse; page images are reported encrypted. Robots allow the API. |
| Champion Cross | https://championcross.jp/ | Manga | `FREE_OFFICIAL` | partially_allowed (blocks /search /api/ /viewer/) | D | Comici engine; reader paths robots-disallowed |
| Big Comics (Comici) | https://bigcomics.jp/ | Manga | `FREE_OFFICIAL` | partially_allowed (blocks /api/ /viewer/) | D | Comici engine; reader paths robots-disallowed |
| Comic Growl | https://comic-growl.com/ | Manga | `FREE_OFFICIAL` | partially_allowed (blocks /api/ /viewer/) | D | Comici engine; reader paths robots-disallowed |
| ComicWalker (Kadocomi) | https://comic-walker.com/ | Manga | `FREE_OFFICIAL` | partially_allowed (blocks /api/) | Dp | KADOKAWA; its API path is robots-disallowed |
| VIZ Shonen Jump | https://www.viz.com/shonenjump | Manga | `FREE_OFFICIAL` | partially_allowed (blocks /search /manga/) | D | Reader paths robots-disallowed |
| KakaoPage | https://page.kakao.com/ | Manhwa | `FREE_OFFICIAL` | partially_allowed (blocks /viewer/) | D | Reader path robots-disallowed |
| CCC Creative Comic | https://www.creative-comic.tw/zh/ | Manhua | `FREE_OFFICIAL` | disallowed (blocks /search /api/ /manga/ /comic/) | D | Taiwan government-backed; robots.txt Disallow for all other agents |
| Dumbing of Age | https://www.dumbingofage.com/ | Webcomic | `CREATOR_AUTHORIZED` | disallowed (blocks /search /api/ /manga/ /comic/) | B | robots.txt lists * with AI crawlers and disallows all (verified) — blocked |
| Lackadaisy | https://www.lackadaisy.com/ | Webcomic | `CREATOR_AUTHORIZED` | disallowed (blocks /search /api/ /manga/ /comic/) | Bp | robots.txt disallows all for * (verified) — blocked |
| e-rara | https://www.e-rara.ch/ | Books | `PUBLIC_DOMAIN` | disallowed (blocks /search /api/ /manga/ /comic/) | B | robots.txt: Disallow / for * (Google/Bing allowed) — blocked |
| Delpher | https://www.delpher.nl/ | Mixed | `PUBLIC_DOMAIN` | disallowed (blocks /search /api/ /manga/ /comic/) | C | robots.txt: Disallow / for * — blocked |
| Archive of Our Own | https://archiveofourown.org/ | Books | `CREATOR_AUTHORIZED` | allowed | D | EPUB exists but its path is robots-disallowed; fan works (derivative) need rights review |
| Shosetsuka ni Naro (Syosetu) | https://syosetu.com/ | Books | `CREATOR_AUTHORIZED` | allowed | D | Web novels; text only (Core has no text format) |
| Royal Road | https://www.royalroad.com/ | Books | `CREATOR_AUTHORIZED` | allowed | D | Web novels; text only; chapter paths allowed |
| Kakuyomu | https://kakuyomu.jp/ | Books | `CREATOR_AUTHORIZED` | allowed | D | Web novels; text only |
| Manga Arabia | https://www.mangaarabia.com/en | Manga | `PUBLISHER_AUTHORIZED` | allowed | F | Saudi official Arabic manga; the website is a landing page (title anchors are in-page #s_titles) — reading is in the apps |

### SOURCE-FAMILY OPPORTUNITIES

See the next section. The two that pay off now are **ComicControl** (a single-response archive and one image
per page on every site — the xkcd pattern) and the **webcomic hosting platforms** (ComicFury, Acomics, The
Duck: one adapter reaches thousands of creator comics).

## Potential reusable source engines

OneShelf has no source-family concept: each site stays its own adapter and identity. A family means one
recipe design, copied per site with its own domains and fixtures — or, where noted, a Core primitive that
several sites would use.

| Engine / Pattern | Candidate Sites | Common Search | Common Work Page | Common Reader | Possible Shared Adapter Primitive |
|---|---:|---|---|---|---|
| **ComicControl** (Hiveworks CMS; ~210 sites per usage trackers) | 4 screened: SMBC, El Goonish Shive, Paranatural, Awkward Zombie | none | `/comic/archive` — every page in one `<select name=comic>` (7,926 on SMBC, 921 on Paranatural; verified) | `/comic/<slug>`: one `#cc-comic` image with title text; `/comic/rss` | None needed — today's recipe primitives cover it (catalog `single_response`, reader one image). A shared recipe template per site |
| **Webcomic hosting platforms** | 3: ComicFury, Acomics, The Duck | platform search (ComicFury `/search.php?query=`) | ComicFury `/comicprofile.php?url=<slug>`; Acomics `/~<slug>`; The Duck `/<Name>/` | ComicFury `/read/<slug>/comics/<id>` (img.comicfury.com); Acomics `/~<slug>/<n>` (/upload/…) | One adapter per platform covers every comic on it. Acomics exposes a per-comic licence field, so a per-item rights gate is declarative |
| **WordPress webcomic plugins** (ComicPress / Comic Easel / Toocheke / Webcomic) | 12 screened: Sandra and Woo, Digger, Buttersafe, KSBD, O Human Star, Octopus Pie, Dumbing of Age, Wondermark, Schlock Mercenary, Dresden Codak, Narbonic, Poorly Drawn Lines | WP search (often robots-disallowed) | `/comic/<slug>/`; Toocheke exposes REST post type `comic` (verified on Octopus Pie); Comic Easel/Webcomic do not | `#comic img` (verified on KSBD, Sandra and Woo, Digger) | A WordPress REST catalog would need the page count, which WP gives only in the `X-WP-Total` header — recipes cannot read headers. A Core primitive to page until an empty page (or read `X-WP-Total`) would serve these and Book Dash-style WP sites |
| **Giga Viewer** (Hatena) | 14: Shonen Jump+, Tonari no Young Jump, Comic DAYS, Kurage Bunch, Comic Gardo, Comic Action, Comic Border, Magcomi, Comic Zenon, Ichijin Plus, Comic Trail, Sunday Webry, Comic Earth Star (+ Magazine Pocket formerly) | publisher search | `/series/<id>` + per-series RSS/Atom with `?free_only=1` | `/episode/<id>`: `#episode-json` with ordered pages and RTL direction (verified) | **None acceptable.** Pages are tile-scrambled (`choJuGiga: baku`) and 403 to a plain client even with Referer. Unscrambling publisher images would be circumvention; excluded |
| **Comici** | 6: Comici, Heros Web, Big Comics, Champion Cross, Manga Cross, Comic Growl | `/search` (disallowed on some) | `/series/<id>` | `/episodes/<id>` viewer | **None** — `/viewer/` and `/api/` are robots-disallowed on three of the six |
| **IIIF Presentation** (institutional) | 7: NIJL Kokusho, NDL, Kyoto RMDA, GDZ, Tübingen, e-rara, Smithsonian | varies (NDL search disallowed) | manifest `label`, `metadata`, `license` | canvases → image service | Already used by Wellcome, MDZ, Gallica, Bodleian, Manchester adapters. NIJL puts a per-item licence in the manifest, so the existing licence-gate pattern applies unchanged |
| Madara (WordPress manga theme) | 1 found: Mangalik | — | — | — | **Not recommended.** The only site found on it republishes commercial series without authorization; no legitimate Madara site turned up |
| Web-novel platforms (Syosetu API, Kakuyomu, Royal Road, Scribble Hub, AO3) | 5 | APIs/search | `/works/<id>`, `/fiction/<id>` | HTML text chapters | Blocked on Core, not on the sites: a Core **HTML/plain-text book format** would also unblock Wikisource, Aozora Bunko, OpenITI and Global Storybooks from the earlier rounds |

## Unauthorized aggregators — recorded, not pursued

Four Arabic manga/webtoon readers (Mangatek, Kawaii Manga, ToonArab, Mangalik) list fan translations of
commercially published Korean and Chinese series (for example *Return of the Mount Hua Sect*, *Magic
Emperor*, *Shadow Slave* — seen on their own front pages, 2026-09-30) with no sign of authorization. Their
rights status is not unclear, so they are `RESTRICTED`, and their reader structure is deliberately not
documented. Other scanlation aggregators surfaced by searches were not screened for the same reason.

Arabic findings in short: the legitimate Arabic comics scene (Manga Arabia, Manga Productions, Samandal,
TokTok, Majid, Rusumat) is app-first or print-first — no free web reader was found. The best Arabic comics
prospect is GlobalComix's Arabic section (mixed free/paid per issue; rights need review). MANGA Plus has
official Arabic chapters but a protobuf API.

## All candidates

| # | Source | URL | Content | Languages | Rights Status | Access | Engine/CMS | API/Structured Data | Reader Type | robots.txt | Technical Fit | Existing/Duplicate? | Key Notes |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MANGA Plus | https://mangaplus.shueisha.co.jp/ | Manga | en,es,fr,id,pt,ru,th,vi,de,ar | `FREE_OFFICIAL` | Public (latest/first chapters free) | custom / not identified | Protobuf API (jumpg-webapi.tokyo-cdn.com, application/x-protobuf — verified) | Image pages | allowed | F | new | Shueisha; Arabic among 10 languages. API is protobuf, which recipes cannot parse; page images are reported encrypted. Robots allow the API. |
| 2 | Shonen Jump+ | https://shonenjumpplus.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited free episodes) | Giga Viewer | Embedded JSON + RSS/Atom | Image pages | allowed (no robots.txt (404)) | F | new | Giga Viewer: /series/<id>, /episode/<id>, embedded #episode-json with ordered pages; per-series RSS/Atom (free_only=1). Pages tile-scrambled (choJuGiga "baku") and 403 to a plain client even with Referer (verified on Shonen Jump+) |
| 3 | Tonari no Young Jump | https://tonarinoyj.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer | Giga Viewer | Image pages | allowed (no robots.txt (404)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 4 | Magazine Pocket | https://pocket.shonenmagazine.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Nuxt | Nuxt payload | Image pages | allowed | Dp | new | Kodansha; Nuxt SPA; viewer not inspected |
| 5 | Comic DAYS | https://comic-days.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer, Next.js | Giga Viewer | Image pages | allowed (no robots.txt (404)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 6 | Kurage Bunch | https://kuragebunch.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer | Giga Viewer | Image pages | allowed (no robots.txt (404)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 7 | Comic Gardo | https://comic-gardo.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer, Next.js | Giga Viewer | Image pages | allowed (no robots.txt (404)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 8 | Comic Action | https://comic-action.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer, Next.js | Giga Viewer | Image pages | allowed | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 9 | Comic Border | https://comicborder.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer | Giga Viewer | Image pages | allowed (no robots.txt (404)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 10 | Magcomi | https://magcomi.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer, Next.js | Giga Viewer | Image pages | allowed (no robots.txt (404)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 11 | Heros Web | https://viewer.heros-web.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Comici, Next.js | Comici viewer | Image pages | allowed (robots.txt answers with an HTML page (no rules)) | Dp | new | Comici engine; robots.txt answers HTML |
| 12 | Comic Zenon | https://comic-zenon.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer | Giga Viewer | Image pages | allowed (no robots.txt (404)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 13 | Ichijin Plus | https://ichijin-plus.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer, Next.js | Giga Viewer | Image pages | allowed (robots.txt answers with an HTML page (no rules)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 14 | Comic Trail | https://comic-trail.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer | Giga Viewer | Image pages | allowed (no robots.txt (404)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 15 | ComicWalker (Kadocomi) | https://comic-walker.com/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Next.js | Next.js; /api/ disallowed | Image pages | partially_allowed (blocks /api/) | Dp | new | KADOKAWA; its API path is robots-disallowed |
| 16 | Young Ace UP | https://web-ace.jp/youngaceup/ | Manga | ja | `FREE_OFFICIAL` | Public | custom / not identified | HTML | Image pages | allowed | Cp | new | KADOKAWA; viewer not inspected |
| 17 | Manga UP! | https://global.manga-up.com/ | Manga | en | `FREE_OFFICIAL` | Public (partial free) | Next.js | Next.js | Image pages | allowed (no robots.txt (404)) | Dp | new | Square Enix global; viewer not inspected |
| 18 | Gangan Online | https://www.ganganonline.com/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Next.js | Next.js | Image pages | allowed (no robots.txt (404)) | Dp | new | Square Enix JP |
| 19 | Sunday Webry | https://www.sunday-webry.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer | Giga Viewer | Image pages | allowed (no robots.txt (404)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 20 | Ura Sunday | https://urasunday.com/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Next.js | Next.js | Image pages | allowed (no robots.txt (404)) | Dp | new | Shogakukan |
| 21 | GANMA! | https://ganma.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Next.js | Next.js | Image pages | allowed | Dp | new | Independent publisher |
| 22 | Zebrack | https://zebrack-comic.shueisha.co.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (23-hour free reads) | React SPA | React SPA | Image pages | allowed | Dp | new | Shueisha e-book store; wait-free model |
| 23 | Yanmaga Web | https://yanmaga.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | custom / not identified | HTML | Image pages | allowed | Cp | new | Kodansha |
| 24 | AlphaPolis Manga | https://www.alphapolis.co.jp/manga/official | Manga | ja | `FREE_OFFICIAL` | Public (many series free in full) | custom / not identified | HTML | Image pages | allowed | Cp | new | Publisher-run; 全話無料 series exist — a free-in-full filter may be possible; viewer not inspected |
| 25 | Comic Earth Star | https://comic-earthstar.com/ | Manga | ja | `FREE_OFFICIAL` | Public (time-limited) | Giga Viewer, Next.js | Giga Viewer | Image pages | allowed (no robots.txt (404)) | D | new | Giga Viewer (fingerprint); same family as Shonen Jump+ — scrambled, session-scoped pages expected |
| 26 | Comic Meteor | https://comic-meteor.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | custom / not identified | HTML | Image pages | allowed | Cp | new | Viewer not inspected |
| 27 | Comici | https://comici.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Comici | Comici | Image pages | allowed | Dp | new | Platform behind the Comici family |
| 28 | Big Comics (Comici) | https://bigcomics.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Next.js | Comici; /viewer/ and /api/ disallowed | Image pages | partially_allowed (blocks /api/ /viewer/) | D | new | Comici engine; reader paths robots-disallowed |
| 29 | Manga Park | https://manga-park.com/ | Manga | ja | `FREE_OFFICIAL` | Unreachable | custom / not identified | — | Image pages | unavailable (robots.txt answered 000) | F | new | No connection (twice) |
| 30 | Champion Cross | https://championcross.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Comici, Next.js | Comici; /viewer/, /api/, search disallowed | Image pages | partially_allowed (blocks /search /api/ /viewer/) | D | new | Comici engine; reader paths robots-disallowed |
| 31 | Manga Cross | https://mangacross.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Comici, Next.js | Comici | Image pages | allowed (robots.txt answers with an HTML page (no rules)) | Dp | new | Comici engine; robots.txt answers HTML |
| 32 | Pixiv Comic | https://comic.pixiv.net/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Next.js | Next.js | Image pages | allowed | Dp | new | Publisher serials on pixiv |
| 33 | Comic FUZ | https://comic-fuz.com/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Next.js | Next.js | Image pages | allowed (no robots.txt (404)) | Dp | new | Houbunsha; reported protobuf API |
| 34 | Cycomi | https://cycomi.com/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Next.js | Next.js | Image pages | allowed | Dp | new |  |
| 35 | Comic Growl | https://comic-growl.com/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Comici, Next.js | Comici; /viewer/, /api/ disallowed | Image pages | partially_allowed (blocks /api/ /viewer/) | D | new | Comici engine; reader paths robots-disallowed |
| 36 | Niconico Manga | https://manga.nicovideo.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | WordPress | HTML | Image pages | allowed | Cp | new | Mix of publisher and user-posted manga |
| 37 | Comic Newtype | https://comic.webnewtype.com/ | Manga | ja | `FREE_OFFICIAL` | Gone (404) | custom / not identified | — | Image pages | allowed (no robots.txt (404)) | F | new | Front page 404 |
| 38 | Manga Library Z | https://www.mangaz.com/ | Manga | ja | `PUBLISHER_AUTHORIZED` | Public (全巻無料 — whole volumes free) | custom / not identified | HTML detail pages; viewer on vw.mangaz.com | Image pages | allowed | Cp | new | Out-of-print manga republished with authors' permission; /series/detail/<id>, /book/detail/<id> (verified); viewer host vw.mangaz.com allowed by robots; viewer images not yet inspected |
| 39 | K MANGA | https://kmanga.kodansha.com/ | Manga | en | `FREE_OFFICIAL` | Public (partial free) | custom / not identified | SPA | Image pages | allowed (robots.txt answers with an HTML page (no rules)) | Dp | new | Kodansha EN; robots.txt answers HTML |
| 40 | VIZ Shonen Jump | https://www.viz.com/shonenjump | Manga | en | `FREE_OFFICIAL` | Public (first/latest chapters) | custom / not identified | HTML; /manga/ and search disallowed | Image pages | partially_allowed (blocks /search /manga/) | D | new | Reader paths robots-disallowed |
| 41 | Comikey | https://comikey.com/ | Manga | en,es,pt | `FREE_OFFICIAL` | Public (partial free) | custom / not identified | HTML | Image pages | allowed | Cp | new | Licensed EN/ES/PT |
| 42 | INKR | https://comics.inkr.com/ | Mixed | en | `FREE_OFFICIAL` | Public (partial free) | Next.js | Next.js | Image pages | allowed | Dp | new |  |
| 43 | pixiv | https://www.pixiv.net/ | Manga | ja | `CREATOR_AUTHORIZED` | Public; originals need login | Next.js | Next.js + ajax JSON | Image pages | allowed | Cp | new | Creator-posted manga and doujinshi; per-work terms; full-size images Referer-bound (reported) |
| 44 | Naver Webtoon | https://comic.naver.com/ | Manhwa | ko | `FREE_OFFICIAL` | Public (most episodes free) | React SPA | React SPA; search disallowed | Long strip | partially_allowed (blocks /search) | Cp | Related: WEBTOON adapter covers the global site | Korean-language Naver site |
| 45 | Kakao Webtoon | https://webtoon.kakao.com/ | Manhwa | ko | `FREE_OFFICIAL` | Public (wait-or-pay) | Next.js | Next.js | Long strip | allowed | Dp | new | Many episodes pay-gated |
| 46 | KakaoPage | https://page.kakao.com/ | Manhwa | ko | `FREE_OFFICIAL` | Wait-or-pay | Next.js | Next.js; /viewer/ disallowed | Long strip | partially_allowed (blocks /viewer/) | D | new | Reader path robots-disallowed |
| 47 | Postype | https://www.postype.com/ | Manhwa | ko | `CREATOR_AUTHORIZED` | Public (creator paywalls) | Next.js | Next.js; /api/ disallowed | Long strip | partially_allowed (blocks /api/) | Dp | new | Creator platform; per-post paywalls |
| 48 | DillyHub | https://www.dillyhub.com/ | Manhwa | ko | `CREATOR_AUTHORIZED` | Unreachable | custom / not identified | — | Long strip | unavailable (robots.txt answered 000) | F | new | No connection (twice) |
| 49 | Anytoon | https://www.anytoon.co.kr/webtoon/main | Manhwa | ko | `RESTRICTED` | Mostly paid | Next.js | Next.js | Long strip | allowed | Dp | new | Commercial webtoon store |
| 50 | comico JP | https://www.comico.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (partial free) | Nuxt | Nuxt | Long strip | allowed | Dp | new |  |
| 51 | Dongman Manhua | https://www.dongmanmanhua.cn/ | Manhua | zh | `FREE_OFFICIAL` | Public (most episodes free) | custom / not identified | HTML (WEBTOON engine) | Long strip | allowed (robots.txt answers with an HTML page (no rules)) | Bp | Related: WEBTOON adapter (same company, separate host) | Naver's Chinese WEBTOON; likely reuses the WEBTOON adapter's pattern |
| 52 | Bilibili Manga | https://manga.bilibili.com/ | Manhua | zh | `FREE_OFFICIAL` | Public (partial free) | custom / not identified | JSON API; image tokens (reported) | Image pages | allowed (no robots.txt (404)) | Dp | new | Page images need a per-request token (reported) |
| 53 | Tencent AC | https://ac.qq.com/ | Manhua | zh | `FREE_OFFICIAL` | Public (partial free) | custom / not identified | HTML; obfuscated chapter data (reported) | Image pages | allowed | Dp | new |  |
| 54 | Kuaikan Manhua | https://www.kuaikanmanhua.com/ | Manhua | zh | `FREE_OFFICIAL` | Public (partial free) | Nuxt | Nuxt; search disallowed | Long strip | partially_allowed (blocks /search) | Dp | new |  |
| 55 | CCC Creative Comic | https://www.creative-comic.tw/zh/ | Manhua | zh-Hant | `FREE_OFFICIAL` | Public | custom / not identified | robots.txt allows named search engines only | Image pages | disallowed (blocks /search /api/ /manga/ /comic/) | D | new | Taiwan government-backed; robots.txt Disallow for all other agents |
| 56 | MangaToon | https://mangatoon.mobi/ | Mixed | en,id,es,pt,vi,th | `FREE_OFFICIAL` | Public (partial free) | custom / not identified | HTML; /api/ disallowed | Long strip | partially_allowed (blocks /api/) | Dp | new | App-first |
| 57 | U17 | https://www.u17.com/ | Manhua | zh | `FREE_OFFICIAL` | Unreachable | custom / not identified | — | Image pages | unavailable (robots.txt answered 000) | F | new | No connection (twice) |
| 58 | ComicFury | https://comicfury.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | ComicFury | HTML; RSS per comic | Image pages | allowed | B | new | Creator-hosted (thousands of comics). /comicprofile.php?url=<slug>, /read/<slug>/archive, /read/<slug>/comics/<numeric id>, images on img.comicfury.com (verified). Licence per comic, rarely stated |
| 59 | The Duck Webcomics | https://www.theduckwebcomics.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed | Bp | new | /<ComicName>/ slugs; media under /media/users/ (verified on front page) |
| 60 | Comic Genesis | https://www.comicgenesis.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Unreachable | custom / not identified | — | Image pages | unavailable (robots.txt answered 000) | F | new | No connection (twice) |
| 61 | Hiveworks | https://hiveworkscomics.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | Hugo/Jekyll static | Static hub linking member sites | Image pages | allowed (robots.txt answers with an HTML page (no rules)) | — | new | Directory of creator-owned comics (many on ComicControl); not a reader itself |
| 62 | SpiderForest | https://www.spiderforest.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | Static hub | Image pages | allowed | — | new | Collective of 100+ comics on their own sites; directory only |
| 63 | Acomics | https://acomics.ru/ | Webcomic | ru | `OPEN_LICENSED` | Public | custom / not identified | HTML; RSS per comic | Image pages | allowed | A | new | Russian webcomic host. /~<slug>/<n> sequential pages, images under /upload/!c/<author>/<slug>/; each comic's /about page has a licence field (e.g. CC BY-NC-SA 4.0 — verified). Licences vary per comic: only comics whose /about names an open licence would qualify (a declarative per-comic gate) |
| 64 | GlobalComix | https://globalcomix.com/ | Comics | en,ar,es,pt,fr | `CREATOR_AUTHORIZED` | Public (mixed free/paid per issue) | custom / not identified | HTML /c/<slug> | Image pages | allowed | Cp | new | Has an Arabic section (/browse/ar/comics); free/paid mixed per issue |
| 65 | Comic Rocket | https://www.comic-rocket.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | Aggregator; /read/, search, /api/ disallowed | Image pages | partially_allowed (blocks /search /api/ /read/) | F | new | Frames creators' sites; reader robots-disallowed |
| 66 | Piperka | https://piperka.net/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | Aggregator index | Image pages | allowed | F | new | Index of archive pages on third-party sites (unbounded hosts) |
| 67 | Keenspot | https://www.keenspot.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | Hub | Image pages | allowed | — | new | Publisher hub linking comic sites |
| 68 | Kwikku | https://www.kwikku.com/ | Mixed | id | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Mixed | allowed (no robots.txt (404)) | Cp | new | Indonesian creator platform (novels, comics) |
| 69 | Ciayo Comics | https://www.ciayo.com/ | Comics | id | `CREATOR_AUTHORIZED` | Empty page | custom / not identified | — | Long strip | allowed | F | new | Front page has no content (service closed?) |
| 70 | Sandra and Woo | https://www.sandraandwoo.com/ | Webcomic | en,de | `OPEN_LICENSED` | Public | ComicPress (WP) | WordPress (ComicPress) | Image pages | allowed | B | new | CC BY-NC-ND 3.0 linked on every page (verified); /archive/; images under /comics/ |
| 71 | Geek&Poke | https://geek-and-poke.com/ | Webcomic | en | `OPEN_LICENSED` | Public | custom / not identified | — | Image pages | disallowed (blocks /search /api/ /manga/ /comic/) | D | new | Historically CC BY-SA; robots.txt groups * with AI crawlers and disallows all; front page 404 |
| 72 | Morevna Project | https://morevnaproject.org/ | Comics | en,ru | `OPEN_LICENSED` | Public | WordPress | WordPress | Image pages | allowed | Cp | new | CC BY(-SA) animation/comics project; comics section not found at /comics/ (404) |
| 73 | Mimi & Eunice | https://mimiandeunice.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | WordPress | WordPress | Image pages | allowed | Bp | new | Nina Paley; links copyheart.org ('copying is an act of love') — not a standard licence (verified link) |
| 74 | CommitStrip | https://www.commitstrip.com/en/ | Webcomic | en,fr | `RIGHTS_UNCLEAR` | Public | WordPress | WordPress | Image pages | allowed | Bp | new | No licence link on the page |
| 75 | MonkeyUser | https://www.monkeyuser.com/ | Webcomic | en | `RIGHTS_UNCLEAR` | Public | Hugo/Jekyll static | Static (Hugo/Jekyll) | Image pages | allowed (no robots.txt (404)) | Bp | new |  |
| 76 | turnoff.us | https://turnoff.us/ | Webcomic | en | `RIGHTS_UNCLEAR` | Public | custom / not identified | Static HTML | Image pages | allowed | Bp | new |  |
| 77 | SMBC | https://www.smbc-comics.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | ComicControl | ComicControl; RSS | Image pages | allowed | A | new | /comic/archive lists all 7,926 pages in one <select>; /comic/<slug> has #cc-comic image and title text (verified) |
| 78 | Girl Genius | https://www.girlgeniusonline.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed (no robots.txt (404)) | Bp | new |  |
| 79 | Stand Still Stay Silent | https://www.sssscomic.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed (no robots.txt (404)) | Bp | new | Complete comic |
| 80 | Gunnerkrigg Court | https://www.gunnerkrigg.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed | Bp | new | Numbered pages (?p=n) |
| 81 | Questionable Content | https://questionablecontent.net/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed | Bp | new | Numbered strips |
| 82 | Dinosaur Comics | https://www.qwantz.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML; RSS | Image pages | allowed | Bp | new | Numbered strips |
| 83 | Order of the Stick | https://www.giantitp.com/comics/oots.html | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed | Bp | new | Numbered strips |
| 84 | Schlock Mercenary | https://www.schlockmercenary.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | WordPress | WordPress | Image pages | allowed (no robots.txt (404)) | Bp | new | Complete (2000–2020) |
| 85 | El Goonish Shive | https://www.egscomics.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | ComicControl | ComicControl | Image pages | allowed | Ap | new | ComicControl family |
| 86 | Dumbing of Age | https://www.dumbingofage.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | Toocheke (WP) | WordPress (Toocheke) | Image pages | disallowed (blocks /search /api/ /manga/ /comic/) | B | new | robots.txt lists * with AI crawlers and disallows all (verified) — blocked |
| 87 | Lackadaisy | https://www.lackadaisy.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | disallowed (blocks /search /api/ /manga/ /comic/) | Bp | new | robots.txt disallows all for * (verified) — blocked |
| 88 | Kill Six Billion Demons | https://killsixbilliondemons.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | Comic Easel (WP) | WordPress (Comic Easel); no REST comic type | Image pages | allowed | B | new | /comic/<slug>/ with #comic img (verified) |
| 89 | Unsounded | https://www.casualvillain.com/Unsounded/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML (script-built) | Image pages | allowed (no robots.txt (404)) | Cp | new | Front page renders by script |
| 90 | Paranatural | https://www.paranatural.net/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | ComicControl | ComicControl | Image pages | allowed | A | new | /comic/archive lists 921 pages in one response (verified) |
| 91 | Existential Comics | https://existentialcomics.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed (no robots.txt (404)) | Bp | new | Numbered comics |
| 92 | Cyanide & Happiness | https://explosm.net/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | Next.js, WordPress | Next.js + WordPress | Image pages | allowed (no robots.txt (404)) | Cp | new |  |
| 93 | Penny Arcade | https://www.penny-arcade.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed | Bp | new | Dated strips |
| 94 | Megatokyo | https://megatokyo.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed | Bp | new | Numbered strips |
| 95 | Homestuck | https://www.homestuck.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML; search disallowed | Mixed | partially_allowed (blocks /search) | Cp | new | Mixed media (Flash-era animations) |
| 96 | Dresden Codak | https://dresdencodak.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | WordPress | WordPress | Image pages | allowed | Bp | new |  |
| 97 | Octopus Pie | https://www.octopuspie.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | Toocheke (WP) | WordPress (Toocheke) — REST post type `comic` (verified) | Image pages | allowed | B | new | Complete comic |
| 98 | Digger | https://diggercomic.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | ComicPress (WP) | WordPress (ComicPress) | Image pages | allowed | Bp | new | Complete; no licence link found on the front page |
| 99 | Narbonic | https://www.narbonic.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | WordPress | WordPress | Image pages | allowed | Bp | new | Complete |
| 100 | Wondermark | https://wondermark.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | Webcomic (WP plugin) | WordPress (Webcomic plugin); no REST comic type | Image pages | allowed | Bp | new |  |
| 101 | Poorly Drawn Lines | https://poorlydrawnlines.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | WordPress | WordPress | Image pages | allowed | Bp | new |  |
| 102 | Strong Female Protagonist | https://strongfemaleprotagonist.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | WordPress | WordPress; search disallowed | Image pages | partially_allowed (blocks /search) | Bp | new |  |
| 103 | Ava's Demon | https://www.avasdemon.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed | Bp | new |  |
| 104 | Sluggy Freelance | https://sluggy.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | Drupal | Image pages | allowed | Cp | new |  |
| 105 | Abstruse Goose | https://abstrusegoose.com/ | Webcomic | en | `OPEN_LICENSED` | Unreachable | custom / not identified | — | Image pages | unavailable (robots.txt answered 000) | F | new | Was CC BY-NC 3.0 (reported); no connection (twice) |
| 106 | Cat and Girl | https://catandgirl.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | WordPress | WordPress; /archive/ disallowed | Image pages | partially_allowed (blocks /archive/) | Cp | new | Archive path robots-disallowed |
| 107 | Nedroid | https://nedroid.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed | Cp | new | Little text on the front page |
| 108 | Hark! A Vagrant | https://www.harkavagrant.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Unreachable | custom / not identified | — | Image pages | unavailable (robots.txt answered 000) | F | new | No connection (twice) |
| 109 | Buttersafe | https://www.buttersafe.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | ComicPress (WP) | WordPress (ComicPress) | Image pages | allowed | Bp | new |  |
| 110 | Awkward Zombie | https://www.awkwardzombie.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | ComicControl | ComicControl | Image pages | allowed | Ap | new | ComicControl family |
| 111 | O Human Star | https://ohumanstar.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | Comic Easel (WP), ComicPress (WP) | WordPress (Comic Easel) | Image pages | allowed | Bp | new | No licence link found |
| 112 | Scary Go Round / Bad Machinery | https://scarygoround.com/ | Webcomic | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed (robots.txt answers with an HTML page (no rules)) | Cp | new | robots.txt answers HTML |
| 113 | Barnacle Press | https://www.barnaclepress.com/ | Comics | en | `PUBLIC_DOMAIN` | Public | WordPress | WordPress (posts) | Image pages | allowed | Cp | new | Early newspaper strips as blog posts; strip-level structure not inspected |
| 114 | Golden Age Comics (UK) | https://goldenagecomics.co.uk/ | Comics | en | `PUBLIC_DOMAIN` | Public | custom / not identified | — | Mixed | allowed | — | DUPLICATE: redirects to comicbookplus.com (oneshelf.comic-book-plus) |  |
| 115 | The Comic Strip Library | https://www.comicstriplibrary.org/ | Comics | en | `PUBLIC_DOMAIN` | Public | React SPA | React SPA | Image pages | allowed (no robots.txt (404)) | Cp | new | Needs the SPA's data endpoint |
| 116 | Grand Comics Database | https://www.comics.org/ | Comics | many | `OPEN_LICENSED` | Refused this client (403) | custom / not identified | Metadata API (reported) | — | unavailable (robots.txt answered 403) | F | new | Metadata only (CC BY-SA data); 403 challenge incl. robots.txt |
| 117 | NYPL Digital Collections | https://digitalcollections.nypl.org/ | Mixed | many | `PUBLIC_DOMAIN` | Public | custom / not identified | SPA; API needs a personal token | Image pages | allowed | Dp | new | Hokusai manga etc.; API key cannot ship |
| 118 | Smithsonian Libraries Digital Library | https://library.si.edu/digital-library | Books | many | `PUBLIC_DOMAIN` | Public | Drupal | Drupal; IIIF (reported) | Image pages | allowed | Cp | new | Hokusai manga volumes (CC0 per Smithsonian Open Access) |
| 119 | NDL Digital Collections | https://dl.ndl.go.jp/ | Mixed | ja | `PUBLIC_DOMAIN` | Public (per item) | React SPA | IIIF Presentation (/api/iiif/<pid>/manifest.json — allowed by an Allow rule); search disallowed | Image pages | partially_allowed (blocks /search /api/) | A | new | Manifest verified (28 canvases); licence field points to NDL's general IIIF terms, so per-item PD status must come from item metadata |
| 120 | NIJL Kokusho Database | https://kokusho.nijl.ac.jp/ | Books | ja | `OPEN_LICENSED` | Public | custom / not identified | IIIF Presentation (/biblio/<id>/manifest) | Image pages | allowed | A | new | Per-item licence in the manifest: CC BY-SA 4.0 (verified, 91 canvases). Early Japanese books incl. illustrated kibyōshi |
| 121 | ARC Ritsumeikan Early Japanese Books | https://www.dh-jac.net/db1/books/ | Books | ja | `RIGHTS_UNCLEAR` | Public | custom / not identified | HTML DB | Image pages | allowed | Cp | new | Front page renders by script |
| 122 | Kyoto University Rare Materials | https://rmda.kulib.kyoto-u.ac.jp/ | Books | ja | `PUBLIC_DOMAIN` | Public | Drupal | IIIF; search disallowed | Image pages | partially_allowed (blocks /search) | Bp | new | Drupal + IIIF fingerprint |
| 123 | Waseda Kotenseki Sogo Database | https://www.wul.waseda.ac.jp/kotenseki/ | Books | ja | `PUBLIC_DOMAIN` | Public | custom / not identified | HTML + PDF | PDF | allowed (no robots.txt (404)) | Cp | new |  |
| 124 | Heidelberg Digital Library | https://digi.ub.uni-heidelberg.de/ | Mixed | de,ar,la | `OPEN_LICENSED` | Unreachable | custom / not identified | IIIF (reported) | Image pages | unavailable (robots.txt answered 000) | F | new | No connection (twice) from here |
| 125 | SLUB Dresden Digital Collections | https://digital.slub-dresden.de/ | Mixed | de | `PUBLIC_DOMAIN` | Refused this client (403) | custom / not identified | Kitodo + IIIF (reported) | Image pages | unavailable (robots.txt answered 403) | F | new | 403 incl. robots.txt |
| 126 | e-rara | https://www.e-rara.ch/ | Books | de,fr,la,it | `PUBLIC_DOMAIN` | Public | Visual Library (semantics) | Visual Library; IIIF | Image pages | disallowed (blocks /search /api/ /manga/ /comic/) | B | new | robots.txt: Disallow / for * (Google/Bing allowed) — blocked |
| 127 | Polona | https://polona.pl/ | Mixed | pl | `PUBLIC_DOMAIN` | Public | custom / not identified | SPA; JSON API (reported) | Image pages | allowed (robots.txt answers with an HTML page (no rules)) | Cp | new | robots.txt answers HTML |
| 128 | Delpher | https://www.delpher.nl/ | Mixed | nl | `PUBLIC_DOMAIN` | Public | custom / not identified | — | Image pages | disallowed (blocks /search /api/ /manga/ /comic/) | C | new | robots.txt: Disallow / for * — blocked |
| 129 | BNE Digital (Biblioteca Digital Hispánica) | https://bdh.bne.es/bnesearch/Search.do | Mixed | es | `PUBLIC_DOMAIN` | Refused this client (403) | custom / not identified | IIIF (reported) | Image pages | unavailable (robots.txt answered 403) | F | new | 403 incl. robots.txt |
| 130 | Hemeroteca Digital Brasileira | https://bndigital.bn.gov.br/hemeroteca-digital/ | Comics | pt | `PUBLIC_DOMAIN` | Refused this client (403 challenge) | custom / not identified | DocReader | Image pages | allowed | F | new | O Tico-Tico; page answers a challenge |
| 131 | Pepines (UNAM) | https://pepines.iib.unam.mx/inicio | Comics | es | `PUBLIC_DOMAIN` | Public | custom / not identified | HTML | Image pages | allowed (no robots.txt (404)) | Cp | new | Mexican historietas catalogue; digital pages not located on the front page |
| 132 | Archivo Cultural | https://archivocultural.org/ | Books | es | `RIGHTS_UNCLEAR` | Unreachable | custom / not identified | — | — | unavailable (robots.txt answered 000) | F | new |  |
| 133 | Refaiya Leipzig | https://www.refaiya.uni-leipzig.de/ | Books | ar | `OPEN_LICENSED` | Unreachable | custom / not identified | — | Image pages | unavailable (robots.txt answered 000) | F | new | No connection (twice) |
| 134 | Tübingen Digital Collections | https://idb.ub.uni-tuebingen.de/ | Books | ar,de,la | `PUBLIC_DOMAIN` | Public | custom / not identified | Redirects to opendigi.ub.uni-tuebingen.de; IIIF (reported) | Image pages | allowed | Cp | new | Needs a second host declared |
| 135 | ULB Halle Digital Collections | https://digitale.bibliothek.uni-halle.de/ | Books | de,ar | `PUBLIC_DOMAIN` | Public | WordPress | WordPress front; Visual Library behind (reported) | Image pages | allowed (robots.txt answers with an HTML page (no rules)) | Cp | new | robots.txt answers HTML |
| 136 | Göttingen GDZ | https://gdz.sub.uni-goettingen.de/ | Books | de | `PUBLIC_DOMAIN` | Public | custom / not identified | IIIF | Image pages | allowed | Bp | new | IIIF fingerprint; item manifests not yet located |
| 137 | Global Grey Ebooks | https://www.globalgreyebooks.com/ | Books | en | `PUBLIC_DOMAIN` | Public | custom / not identified | Static HTML | EPUB | allowed (no robots.txt (404)) | Bp | new | One-person curated PD library; EPUB/PDF (listing page path not found yet) |
| 138 | Faded Page | https://www.fadedpage.com/ | Books | en | `PUBLIC_DOMAIN` | Public | custom / not identified | HTML; stable pid | EPUB | allowed | A | new | EPUB and PDF via link.php?file=<pid>.epub (verified). Public domain in CANADA — may be in copyright elsewhere |
| 139 | Project Gutenberg Australia | https://gutenberg.net.au/ | Books | en | `PUBLIC_DOMAIN` | Public | custom / not identified | Static lists | EPUB | allowed | A | new | 522 EPUBs on its own host from one list page (verified). Public domain in AUSTRALIA — may be in copyright elsewhere |
| 140 | epubBooks | https://www.epubbooks.com/ | Books | en | `PUBLIC_DOMAIN` | Public (login for downloads, reported) | custom / not identified | HTML | EPUB | allowed (robots.txt answers with an HTML page (no rules)) | Cp | Mirrors PG/Standard Ebooks titles | Aggregates Gutenberg projects |
| 141 | Bibebook | https://www.bibebook.com/ | Books | fr | `PUBLIC_DOMAIN` | Public | custom / not identified | HTML | EPUB | allowed | Cp | new | French PD; download links not on the front page |
| 142 | Bibliothèque numérique romande | https://ebooks-bnr.com/ | Books | fr | `PUBLIC_DOMAIN` | Public | WordPress | WordPress | EPUB | allowed | Cp | new | French PD editions; script-rendered front page |
| 143 | Ebooks libres et gratuits | https://www.ebooksgratuits.com/ | Books | fr | `PUBLIC_DOMAIN` | Public | custom / not identified | HTML | EPUB | allowed | Cp | new | French PD |
| 144 | Baen Free Library | https://www.baen.com/allbooks/category/index/id/2012 | Books | en | `PUBLISHER_AUTHORIZED` | Public (downloads via account section) | custom / not identified | HTML | EPUB | allowed | Cp | new | Publisher's own free library; download link on the page points to /customer/account/… |
| 145 | Unglue.it | https://unglue.it/ | Books | en | `OPEN_LICENSED` | Public | custom / not identified | HTML; /work/<id>/download/ | EPUB | allowed | B | new | CC-licensed ebooks (verified link shapes). File hosts not yet checked — if downloads resolve to arbitrary publisher hosts it is an aggregator (the DOAB blocker) |
| 146 | Craphound (Cory Doctorow) | https://craphound.com/ | Books | en | `OPEN_LICENSED` | Public | WordPress | WordPress | EPUB | allowed | Cp | new | Author's CC novels (per the author); file links not on the category page |
| 147 | Green Tea Press | https://greenteapress.com/ | Books | en | `OPEN_LICENSED` | Public | WordPress | WordPress | PDF | allowed | Cp | new | CC textbooks (per the publisher); PDF links not on the front page |
| 148 | Mises Institute Library | https://mises.org/library/books | Books | en | `PUBLISHER_AUTHORIZED` | Refused this client (403 challenge) | custom / not identified | — | PDF | partially_allowed (blocks /search) | F | new |  |
| 149 | Public Domain Library | https://publicdomainlibrary.org/en/ | Books | en | `PUBLIC_DOMAIN` | Public | Hugo/Jekyll static | Static | EPUB | allowed | Bp | new |  |
| 150 | Domínio Público | http://www.dominiopublico.gov.br/ | Books | pt | `PUBLIC_DOMAIN` | Refused this client (403 challenge) | custom / not identified | — | PDF | unavailable (robots.txt answered 403) | F | new | Brazil government library |
| 151 | Biblioteca Virtual Miguel de Cervantes | https://www.cervantesvirtual.com/ | Books | es | `PUBLIC_DOMAIN` | Public | custom / not identified | HTML | Mixed | allowed | Cp | new | Mostly HTML text editions |
| 152 | Zeno.org | http://www.zeno.org/ | Books | de | `PUBLIC_DOMAIN` | Public (robots.txt unreachable) | custom / not identified | HTML | HTML text | unavailable (robots.txt answered 000) | D | new | HTML text only |
| 153 | Projekt Gutenberg-DE | https://www.projekt-gutenberg.org/ | Books | de | `PUBLIC_DOMAIN` | Public | WordPress | HTML | HTML text | allowed (robots.txt answers with an HTML page (no rules)) | D | new | HTML text only; robots.txt answers HTML |
| 154 | Shosetsuka ni Naro (Syosetu) | https://syosetu.com/ | Books | ja | `CREATOR_AUTHORIZED` | Public | custom / not identified | Official JSON API (api.syosetu.com — verified) | HTML text | allowed | D | new | Web novels; text only (Core has no text format) |
| 155 | Kakuyomu | https://kakuyomu.jp/ | Books | ja | `CREATOR_AUTHORIZED` | Public | Next.js | Next.js; /works/<id> | HTML text | allowed | D | new | Web novels; text only |
| 156 | Royal Road | https://www.royalroad.com/ | Books | en | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML /fiction/<id>/…/chapter/<id> | HTML text | allowed | D | new | Web novels; text only; chapter paths allowed |
| 157 | Archive of Our Own | https://archiveofourown.org/ | Books | many | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML; /downloads/ and search disallowed (verified) | HTML text | allowed | D | new | EPUB exists but its path is robots-disallowed; fan works (derivative) need rights review |
| 158 | Scribble Hub | https://www.scribblehub.com/ | Books | en | `CREATOR_AUTHORIZED` | Public | WordPress | WordPress | HTML text | allowed | D | new | Web novels; text only |
| 159 | Wattpad | https://www.wattpad.com/ | Books | many | `CREATOR_AUTHORIZED` | Refused this client (challenge) | custom / not identified | — | HTML text | unavailable (robots.txt answered challenge) | F | new | robots.txt answered a challenge |
| 160 | Sacred Texts Archive | https://sacred-texts.com/ | Books | en | `PUBLIC_DOMAIN` | Public | custom / not identified | HTML | HTML text | allowed | D | new | HTML text only |
| 161 | Marxists Internet Archive | https://www.marxists.org/ | Books | many | `RIGHTS_UNCLEAR` | Public | custom / not identified | HTML | Mixed | allowed | D | new | Mixed HTML/PDF, mixed rights |
| 162 | Perseus Digital Library | https://www.perseus.tufts.edu/hopper/ | Books | grc,la,en | `OPEN_LICENSED` | Public | custom / not identified | XML texts | HTML text | disallowed (blocks /search /api/ /manga/ /comic/) | D | new | robots.txt disallows all for * — blocked; text only |
| 163 | Monkey Pen | https://monkeypen.com/ | Children's Books | en | `RIGHTS_UNCLEAR` | Public (store) | Shopify | Shopify | PDF | partially_allowed (blocks /search) | Dp | new | Shopify store; free PDFs mixed with paid |
| 164 | Storyberries | https://www.storyberries.com/ | Children's Books | en | `RIGHTS_UNCLEAR` | Public | WordPress | WordPress | HTML text | allowed | Dp | new | Illustrated stories as web pages |
| 165 | We Love Reading | https://welovereading.org/ | Children's Books | ar,en | `RIGHTS_UNCLEAR` | Public | WordPress | WordPress | PDF | allowed | Dp | new | Jordanian literacy NGO; site PDFs are catalogues and reports, not the stories (verified) |
| 166 | Global Digital Library | https://digitallibrary.io/ | Children's Books | many | `OPEN_LICENSED` | Public | Next.js, WordPress | Next.js front; separate content API | EPUB | allowed (robots.txt answers with an HTML page (no rules)) | Cp | new | CC-licensed children's books |
| 167 | Al-Mostafa Library | https://www.al-mostafa.com/ | Books | ar | `RIGHTS_UNCLEAR` | Unreachable | custom / not identified | — | PDF | unavailable (robots.txt answered 000) | F | new |  |
| 168 | Alwaraq | https://alwaraq.net/ | Books | ar | `PUBLIC_DOMAIN` | Public | custom / not identified | HTML | HTML text | allowed (robots.txt answers with an HTML page (no rules)) | D | new | Classical Arabic texts as HTML; robots.txt answers HTML |
| 169 | Abjjad | https://www.abjjad.com/ | Books | ar | `RIGHTS_UNCLEAR` | Public | custom / not identified | HTML; search disallowed | Mixed | partially_allowed (blocks /search) | Dp | new | Arabic reading community and store |
| 170 | Manga Arabia | https://www.mangaarabia.com/en | Manga | ar,en | `PUBLISHER_AUTHORIZED` | App-first | Drupal | Drupal landing page | Image pages | allowed | F | new | Saudi official Arabic manga; the website is a landing page (title anchors are in-page #s_titles) — reading is in the apps |
| 171 | Manga Productions | https://manga.com.sa/ | Manga | ar,en | `PUBLISHER_AUTHORIZED` | Public | WordPress | WordPress; search disallowed | Mixed | partially_allowed (blocks /search) | Dp | new | Saudi studio site; no web reader found |
| 172 | Samandal Comics | https://samandal-comics.org/ | Comics | ar,en,fr | `CREATOR_AUTHORIZED` | Public | WordPress | WordPress | — | allowed | F | new | Lebanese anthology; publications page, no online reader or PDFs found |
| 173 | TokTok | https://toktokmag.com/ | Comics | ar | `CREATOR_AUTHORIZED` | Gone (404) | React SPA | — | — | allowed (no robots.txt (404)) | F | new | Egyptian magazine; front page 404 |
| 174 | Majid | https://www.majid.ae/ | Comics | ar | `FREE_OFFICIAL` | Public | Next.js | Next.js | Mixed | allowed (robots.txt answers with an HTML page (no rules)) | Dp | new | Emirati children's magazine; digital reading not located |
| 175 | Rusumat | https://rusumat.com/ | Comics | ar | `CREATOR_AUTHORIZED` | Unreachable | custom / not identified | — | Image pages | unavailable (robots.txt answered 000) | F | new | Arab comics app/platform |
| 176 | Mangatek | https://mangatek.com/ | Manga | ar | `RESTRICTED` | Public | custom / not identified | custom | Long strip | partially_allowed (blocks /api/) | — | new | Unauthorized Arabic translations of commercially published series (e.g. Return of the Mount Hua Sect, Magic Emperor — verified listing). Not pursued |
| 177 | Kawaii Manga | https://kawaiimanga.org/ | Manga | ar | `RESTRICTED` | Public | Next.js | Next.js | Long strip | partially_allowed (blocks /api/) | — | new | Arabic fan-translation reader; no authorization found. Not pursued |
| 178 | ToonArab | https://toonarab.com/ | Manhwa | ar | `RESTRICTED` | Public | custom / not identified | custom | Long strip | partially_allowed (blocks /search) | — | new | Unauthorized Arabic translations of commercial webtoons/novels (e.g. Shadow Slave — verified listing). Not pursued |
| 179 | Mangalik | https://mangalik.net/ | Manga | ar | `RESTRICTED` | Public | Madara (WP manga theme) | WordPress (Madara) | Long strip | unavailable (robots.txt answered 403) | — | new | Madara manga theme; fan translations of commercial series. Not pursued |
| 180 | Grise Bouille | https://grisebouille.net/ | Webcomic | fr | `OPEN_LICENSED` | Public | custom / not identified | Static HTML | Mixed | allowed | Bp | new | Gee; CC BY-SA 4.0 linked on every page (verified). Mixes comics and illustrated text |
| 181 | Bouletcorp | https://bouletcorp.com/ | Webcomic | fr,en | `CREATOR_AUTHORIZED` | Public | Nuxt | Nuxt | Long strip | allowed | Cp | new | French; Nuxt SPA |
| 182 | Tus Comics | https://tuscomics.com/ | Webcomic | es | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML; /api/ disallowed | Image pages | partially_allowed (blocks /api/) | Cp | new | Spanish webcomic host |
| 183 | Sinergia sin control | https://sinergiasincontrol.blogspot.com/ | Webcomic | es | `OPEN_LICENSED` | Public | custom / not identified | Blogger (Atom feed) | Image pages | allowed | Cp | new | CC BY-NC-SA 2.5 ES (per its own blog); Blogger posts — unit = post |
| 184 | re:ON Comics | https://www.reoncomics.com/ | Comics | id | `PUBLISHER_AUTHORIZED` | Unreachable | custom / not identified | — | Image pages | unavailable (robots.txt answered 000) | F | new | Indonesian publisher (320+ free comics per press); no connection (twice) |
| 185 | POPS Comics | https://pops.vn/comics | Comics | vi | `FREE_OFFICIAL` | Public (partial free) | Next.js, WordPress | Next.js/WordPress; search disallowed | Image pages | partially_allowed (blocks /search) | Dp | new | Vietnamese licensed platform |
| 186 | Katakeeb | https://www.katakeeb.com/ | Children's Books | ar | `RIGHTS_UNCLEAR` | Public | React SPA | React SPA | Mixed | allowed | Dp | new | Arabic children's stories (audio/illustrated) |
| 187 | Alroqey children's ebooks | https://www.alroqey.com/ebooks/children | Children's Books | ar | `RIGHTS_UNCLEAR` | Public | custom / not identified | HTML; /books/ and search disallowed | PDF | partially_allowed (blocks /search /books/) | D | new | Arabic PDFs; book path robots-disallowed; rights of the PDFs unknown |
| 188 | Tarbiyaa stories | https://tarbiyaa.com/stories/ | Children's Books | ar | `RIGHTS_UNCLEAR` | Public | WordPress, Drupal | WordPress/Drupal | HTML text | allowed | Dp | new | Arabic illustrated stories as pages |
| 189 | Rawiaty | https://rawiaty.com/ | Children's Books | ar | `RIGHTS_UNCLEAR` | Public | WordPress | WordPress | PDF | allowed | Cp | new | Arabic printable picture stories |
| 190 | 4MyKidz Arabic stories | https://4mykidz.com/ | Children's Books | ar | `RIGHTS_UNCLEAR` | Public | WordPress | WordPress | HTML text | allowed | Dp | new |  |
| 191 | GDL content API | https://content.digitallibrary.io/api/ | Children's Books | many | `OPEN_LICENSED` | Public (no credentials, per its docs) | WordPress | Documented REST API (content.digitallibrary.io/api) | EPUB | allowed | Bp | new | API page reachable; book endpoints not yet exercised |
| 192 | Um Sábado Qualquer | https://www.umsabadoqualquer.com/ | Webcomic | pt | `CREATOR_AUTHORIZED` | Unreachable | custom / not identified | — | Image pages | unavailable (robots.txt answered 000) | F | new | No connection (twice) |
| 193 | izneo free comics | https://www.izneo.com/fr/bd/free | Comics | fr | `FREE_OFFICIAL` | Unreachable | custom / not identified | — | Image pages | allowed | F | new | Commercial store's free shelf; no connection |
| 194 | Ookbee Comics | https://www.ookbee.com/comics | Comics | th | `CREATOR_AUTHORIZED` | Gone (404) | Next.js | Next.js; /api/ disallowed | Image pages | partially_allowed (blocks /api/) | F | new | Thai; path 404 |
| 195 | Webcomic-Verzeichnis | https://www.webcomic-verzeichnis.de/ | Webcomic | de | `CREATOR_AUTHORIZED` | Unreachable | custom / not identified | Directory | — | unavailable (robots.txt answered 000) | F | new | German webcomic directory; no connection |
| 196 | Lapin | https://www.lapin.org/ | Comics | fr | `CREATOR_AUTHORIZED` | Public | WordPress | WordPress | Image pages | allowed | Cp | new | French comics collective |
| 197 | Tira Ecol | https://www.tiraecol.net/ | Webcomic | es | `RIGHTS_UNCLEAR` | Public | WordPress | WordPress | Image pages | allowed (robots.txt answers with an HTML page (no rules)) | Cp | new | Spanish strip |
| 198 | Nichtlustig (Joscha Sauer) | https://joscha.com/ | Webcomic | de | `CREATOR_AUTHORIZED` | Public | custom / not identified | HTML | Image pages | allowed | Cp | new | German |
| 199 | Jeem | https://jeem.tv/ | Children's Books | ar | `RIGHTS_UNCLEAR` | Unreachable (522) | custom / not identified | — | — | unavailable (robots.txt answered 522) | F | new | Al Jazeera children's; origin down |
| 200 | Mkzhan (Zhiyin Manke) | https://www.mkzhan.com/ | Manhua | zh | `FREE_OFFICIAL` | Public (partial free) | custom / not identified | HTML | Image pages | allowed (no robots.txt (404)) | Cp | new | Official Zhiyin Manke platform; viewer not inspected |
| 201 | LINE Manga | https://manga.line.me/ | Manga | ja | `FREE_OFFICIAL` | Refused this client (412) | custom / not identified | /api/ disallowed | Image pages | partially_allowed (blocks /api/) | F | new |  |
| 202 | BOOK WALKER free | https://bookwalker.jp/ | Manga | ja | `FREE_OFFICIAL` | Public (free first volumes) | custom / not identified | HTML store | Image pages | allowed | Dp | new | Store; free samples/first volumes in a DRM viewer |
| 203 | Ohio State University Libraries Digital Collections | https://library.osu.edu/dc/ | Comics | en | `RIGHTS_UNCLEAR` | Public | custom / not identified | Hub | Image pages | allowed | Cp | new | Billy Ireland collections are mostly catalogue-only |
| 204 | Smithsonian Open Access | https://www.si.edu/openaccess | Mixed | many | `PUBLIC_DOMAIN` | Refused this client (403) | custom / not identified | API needs api.data.gov key | Image pages | allowed | F | new | Personal key; 403 on front page |

## Evidence

- Each site's robots.txt is at `https://<host>/robots.txt`; the verdicts above were computed on 2026-09-30 with
  `tools/lib/inspect_source.py`'s `Robots` (RFC 9309). Specific rules quoted: AO3 disallows `/downloads/` and
  `/works/search`; NDL allows `/api/iiif/…` and disallows search; Dumbing of Age, Geek&Poke, CCC, e-rara,
  Delpher and Perseus put `User-agent: *` in a `Disallow: /` group (with AI crawlers, or with only search
  engines allowed).
- Structures marked *verified* were read with `./tools/inspect-source` on: `https://www.smbc-comics.com/comic/archive`,
  `https://www.smbc-comics.com/comic/2002-09-05`, `https://www.paranatural.net/comic/archive`,
  `https://shonenjumpplus.com/episode/9253191256784141807` (and one of its page images: 403),
  `https://comicfury.com/comicprofile.php?url=charcoal-heart`, `https://comicfury.com/read/charcoal-heart/comics/first`,
  `https://acomics.ru/~tails-n-ears-revolution/1` and `/about`, `https://www.sandraandwoo.com/`,
  `https://grisebouille.net/`, `https://www.octopuspie.com/wp-json/wp/v2/types`,
  `https://killsixbilliondemons.com/comic/kill-six-billion-demons-chapter-1/`, `https://www.mangaz.com/book/detail/207783`,
  `https://www.fadedpage.com/showbook.php?pid=20190101`, `https://gutenberg.net.au/plusfifty-a-m.html`,
  `https://unglue.it/free/`, `https://dl.ndl.go.jp/api/iiif/1288355/manifest.json`,
  `https://kokusho.nijl.ac.jp/biblio/100249537/manifest`, `https://api.syosetu.com/novelapi/api/?out=json&lim=1`,
  `https://jumpg-webapi.tokyo-cdn.com/api/title_detailV3?title_id=100020` (application/x-protobuf).
- Claims marked *reported* come from public documentation or community sources and were not verified here.
- Discovery leads: publisher lists (loomic.io, Comics Beat), Hatena's GigaViewer adopter releases, ComicControl
  usage statistics (ful.io), SpiderForest and Hiveworks directories, AUB Libraries' Arabic comics guide,
  Indonesian, Vietnamese, Korean and Chinese legal-reading lists, Wikipedia's list of CC-licensed works.

## Round 2 — checkpoints

| Date | Task | Result | Commit | Next |
|---|---|---|---|---|
| 2026-09-30 | NIJL Kokusho Database | `VERIFIED` as `oneshelf.nijl-kokusho` (search, work, catalog, reader; per-item CC/PDM gate, All-Rights-Reserved excluded) | d924457 | Acomics eligibility |
| 2026-09-30 | Acomics | `VERIFIED` as `oneshelf.acomics` (search, work, catalog, reader; per-comic CC/PDM/CC0 gate on each page, translations and unlicensed comics excluded) | e03fb2e | ComicControl feasibility review |
| 2026-09-30 | Feasibility reviews (ComicControl, WordPress/Toocheke, HTML/text reader) | written up in [architecture-reviews-2026-09.md](architecture-reviews-2026-09.md) | a1275e1 | secondary candidates |
| 2026-09-30 | Sandra and Woo | `VERIFIED` as `oneshelf.sandra-and-woo` (work, catalog, reader; CC BY-NC-ND 3.0) | 15909a7 | GDL, Unglue.it, Grise Bouille recorded in the architecture reviews |
| 2026-09-30 | Full regression | `./tools/bootstrap` (Core 475c145), `./tools/check-all`: 34 adapters, 83 repository tests, published versions reproducible, Registry built and verified; the three new adapters reviewed and installed through Core main's Registry API | a8e8003 | next batch: HTML/text format task (Core), GDL once search language or per-book EPUB exists |
| 2026-10-06 | HTML/text format (Core, Review C) | plugin API 1.2 text reading units on Core `feature/text-reading-units` (eae9b3d, 537115c, e4d7498): sanitiser (nh3), `.ostext` storage + migration 0016, Download Missing, Book Reader; Core 1,351 backend + 338 frontend tests and the reader browser check pass | Core branch | merge to Core main, then move the tooling pin |
| 2026-10-06 | English and Arabic Wikisource | `VERIFIED` as `oneshelf.wikisource-en` and `oneshelf.wikisource-ar` (search, work, catalog, reader as text; live-checked on 7 works) against local Core (`ONESHELF_CORE_PATH`) | this commit | GDL; images in text units (Grise Bouille); other Wikisource languages |
| 2026-10-07 | Discovery round 3 | 35 new sites investigated; 7 adapters `VERIFIED` (eBible.org, Project Runeberg, OpenEdition Books, Tuwhera, meson press, Amherst College Press, University of Michigan Press), 21 blocked, 5 queued, 1 held — [discovery-round3-2026-10.md](discovery-round3-2026-10.md) | this commit | Sefaria (needs Core), e-codices (maintainer), merge Core and move the pin |
