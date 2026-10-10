# Adapter labels

OneShelf's Registry screen shows each adapter by its manifest `name` (with its id and trust tier), so the
name is what someone reads when choosing what to install. Every adapter's name therefore says three things:

```
Source · Category · LANG
```

| Example | Source | Category | Language |
|---|---|---|---|
| `3asq (Al-Aasheq) · Manga · AR` | 3asq | Manga | Arabic |
| `مجلة آداب الكوفة (University of Kufa, Iraq) · Journal · AR` | the journal and its university | Journal | Arabic |
| `Translation Researches in Arabic Language and Literature (ATU) · Journal · FA/AR` | | Journal | Persian and Arabic |
| `OAPEN Library · Academic books · Multi` | | Academic books | several |

The full list, grouped by category and by language, is [adapter-catalogue.md](adapter-catalogue.md).

## The rule

- **Three parts**, joined by ` · ` (space, middle dot U+00B7, space). The whole name is at most 80
  characters (OneShelf Core's limit), so a long journal title keeps its university and country but may
  shorten them, e.g. `(Kufa, Iraq)`.
- **Source:** the site, publisher or journal as its readers know it. An Arabic journal keeps its Arabic
  title, followed by its institution and country in English.
- **Category:** exactly one of the list below.
- **LANG:** the language of the content, as upper-case ISO 639 codes: `AR`, or up to four joined by `/`
  (`FA/AR`), main language first. `Multi` for a source in many languages. Egyptian Arabic (`arz`) is
  labelled `AR`.

The label must agree with the manifest's `defaults`: its languages include `defaults.language` (unless
`Multi`), and the category fits `defaults.content_type`. The description still says everything else.

## Categories

| Category | For | `defaults.content_type` |
|---|---|---|
| Manga | Japanese-style comics and scanlations | `manga` |
| Webtoons | vertical-scroll web comics (WEBTOON, Tapas) | `comic`, `manhwa`, `manhua` |
| Comics | comics, comic strips, web comics | `comic` |
| Books | general books and literature | `book`, `novel` |
| Children's books | picture and story books for children | `book` |
| Academic books | university and scholarly presses, open-access monographs | `book` |
| Textbooks | open course textbooks | `book` |
| Poetry | poetry collections | `book` |
| Religious texts | scripture and religious literature | `book` |
| Journal | one academic journal (its issues and articles) | `paper` |
| Papers | preprint servers and article platforms holding many journals | `paper` |
| Reports | reports and official publications of institutions | `paper`, `book` |
| Manuscripts | digitised manuscripts | `book`, `other` |
| Newspapers | historical newspapers | `other` |
| Digital library | mixed collections of a library or archive | `book`, `other` |

An unset `content_type` fits every category. A new category is a change to
`tools/lib/adapter_labels.py` and this page in the same Pull Request.

## Tools and checks

- `./tools/new-adapter <slug> --name "…" --category … --language …` writes a labelled name.
- `./tools/adapter-catalogue` rewrites the catalogue after a name changes; `--check` changes nothing.
- `tests/test_labels.py`, run by `./tools/check-all` and CI, fails on a name that breaks the rule or a stale
  catalogue.

Renaming a published adapter changes its package, so it needs a version bump like any other change.

## Why the name

The Core manifest schema accepts no extra keys (no `category` or `tags`), and the Registry index carries
only `id`, `name`, `version`, `api`, `file`, `sha256` and `trust_label`. The name is the only field the
install screen shows that an adapter controls, so the label lives there without any Core change.
Filtering by category or language in OneShelf itself would need a Core change, and this format can be read
by a machine (`tools/lib/adapter_labels.py` parses it) if Core ever adds one.
