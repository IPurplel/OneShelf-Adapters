# Trust levels

| Tier directory | Registry label | OneShelf shows it as |
|---|---|---|
| `adapters/official/` | `official` | **Official** |
| `adapters/verified-community/` | `verified_community` | **Verified Community** |
| `adapters/community/` | `community` | **Community** |

**The tier is decided by the directory, and the directory by maintainers.** The Registry build derives the
label from the tier; nothing inside an adapter can set it, and CI rejects the same id in two tiers.

OneShelf trusts these labels because this is its **first-party Registry** (owner decision, 2026-09-21): an
installation believes the tiers only while its `ONESHELF_REGISTRY_URL` is exactly its configured
`ONESHELF_FIRST_PARTY_REGISTRY_URL` — by default `https://raw.githubusercontent.com/IPurplel/OneShelf-Adapters/registry/index.json`. A label never travels on its own: a Registry anywhere
else that claims `official` is shown as Community unless a key the installation trusts has signed the package.

Signing is optional here. If packages are signed with the project key and an installation trusts that public
key, OneShelf shows *Official · Signed* — stronger evidence that does not depend on GitHub. An invalid signature
from a trusted key is always refused.

## Promotion

```
PR → adapters/community/<id>      (merged: published as Community)
maintainer review + live evidence → a separate PR moving it to adapters/verified-community/<id>
published again → signed → Verified Community
```

Official means the OneShelf project maintains or has adopted the adapter. A contributor asking for
promotion does not promote; a maintainer-authored move does. Moving tiers does not change the id, so
every installation keeps one plugin with one history.
