# Discovery round 4: new sources — 2026-10-07

38 sites not investigated before (checked against the 415 domains in earlier docs and manifests). Screened with
`./tools/inspect-source` (robots.txt first); rights read on each site's own pages. Nothing bypassed.

**Grades:** A 3, B 6, C 12, D 0, F 17. **Rights:** OPEN_LICENSED 13, PUBLIC_DOMAIN 7, PUBLISHER_AUTHORIZED 4,
FREE_OFFICIAL 1, CREATOR_AUTHORIZED 1, RIGHTS_UNCLEAR 5, RESTRICTED 7. **Access:** Allowed 25, Partial 3,
Disallowed 3, Unavailable 7. **Decision:** IMPLEMENTED 6, QUEUED 9, HELD 1, BLOCKED 22.

## Implemented (VERIFIED live, local Core)

| Adapter | Source | Language / type | Rights gate | Live works |
|---|---|---|---|---|
| `oneshelf.wolne-lektury` | wolnelektury.pl API v2 | pl, books (EPUB) | site: all PD or free licence; preview books excluded | 8 PASS |
| `oneshelf.ganjoor` | api.ganjoor.net | fa, poetry (text units, rtl) | poets who died ≥70 years ago only | 6 PASS; Shahriar refused |
| `oneshelf.litteraturbanken` | litteraturbanken.se API | sv, books (EPUB) | epub_license cc-0 only (863/1,643) | 7 PASS; lb-assv refused |
| `oneshelf.bokselskap` | bokselskap.no | no, books (text units) | site grant: private non-commercial use | 7 books + 2 mid-book chapters PASS |
| `oneshelf.mek` | mek.oszk.hu | hu, books (PDF/EPUB) | MEK statement: personal non-commercial copies; single-file docs only | 7 PASS; multi-file and file-less refused |
| `oneshelf.folger-shakespeare` | folger.edu | en, plays (PDF) | "free to use for all non-commercial purposes" | 6 PASS (42 units) |

## Core (feature/text-reading-units, not pushed, not the pin)

- 270e815 `{key:segments}` encoder (keys that are short paths; `..`/empty refused).
- 2267bc8 form values no longer double-encoded (found on MEK).

## Queued (eligible, not built)

TextGrid Digitale Bibliothek (CC BY 3.0 DE; search filter `project.id:TGPR-372fe6dc…&format:text/xml` works; reader via
`textgridlab.org/1.0/aggregator/html/` — aggregator HTML carries an XML declaration that needs handling; epub/zip
aggregators robots-disallowed) · Siyavula (CC BY/BY-ND PDFs, mixed languages on one page) · Tanzil (Quran CC BY, whole-file
only) · Representative Poetry Online (per-poem rights) · National Library of Wales (IIIF, discovery is a JS Primo app) ·
ANNO (daily issues exceed list caps) · EU Publications Office (SPARQL only) · World Bank / WHO IRIS / FAO (DSpace;
/search and API disallowed except bitstreams) · Projekti Lönnrot (ZIP text; mostly on Gutenberg).

## Held

David Revoy / MiniFantasyTheater — robots.txt lists AI agents (commented out); left to a maintainer.

## Blocked (reason)

Deutsches Textarchiv (downloads/search robots-disallowed, AI agents disallowed, JS cookie check) · DBNL (robots `/`) ·
UNESDOC (robots `/`) · Walt Whitman Archive (Cloudflare) · National Library of Israel (browser check) · Trinity College
Dublin (reCAPTCHA) · Papers Past (Incapsula) · LiberLiber (download behind Cloudflare-challenge interstitial) · Dorar
(all rights reserved) · al-Diwan (© Diwan Foundation) · Usul.ai, Turath (rights unclear: Shamela/scanned editions) ·
Planet eBook (all rights reserved) · MIT Internet Classics Archive (reproduction reserved) · King Fahd National Library
publications (port 8060 refused by egress policy) · Syrian General Book Authority (self-signed TLS) · Bizarre Cathedral
(comic gone) · al-Islam.org, Oxford Text Archive, e-manuscripta (connection reset / timeouts).
