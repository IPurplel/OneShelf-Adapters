# Trust levels

| Tier directory | Registry label | Signature | OneShelf shows |
|---|---|---|---|
| `adapters/official/` | `official` | required (project key) | Official — only if the signature verifies against a key the installation trusts |
| `adapters/verified-community/` | `verified_community` | required (project key) | Verified Community — same rule |
| `adapters/community/` | `community` | none | Community |

**The tier is decided by the directory, and the directory by maintainers.** The Registry build derives the
label from the tier; nothing inside an adapter can set it, and CI rejects the same id in two tiers.
OneShelf never believes a label on its own: an unsigned or unknown-key `official` entry is treated as
Community, and a bad signature from a trusted key is refused outright.

## Promotion

```
PR → adapters/community/<id>      (merged: published as Community)
maintainer review + live evidence → a separate PR moving it to adapters/verified-community/<id>
published again → signed → Verified Community
```

Official means the OneShelf project maintains or has adopted the adapter. A contributor asking for
promotion does not promote; a maintainer-authored move does. Moving tiers does not change the id, so
every installation keeps one plugin with one history.
