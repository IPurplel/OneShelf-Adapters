# When an adapter stops working

History is not erased, and nothing here can delete a reader's content: OneShelf keeps downloaded works,
progress and the library regardless of what the Registry says.

| Situation | What we do |
|---|---|
| Broken upstream (layout change) | Fix it with a version bump; until then open an issue labelled `broken`. |
| Temporarily unavailable site | Nothing in the Registry; OneShelf's source health shows it. |
| Domain moved | New version with the new domain — installations review the new permission. The id stays. |
| Source gone for good / deprecated | Remove the adapter directory in a PR explaining why; the next publication drops it from the index. Installed copies keep working locally as far as the site allows. |
| Security removal | Remove it and publish promptly; describe the issue in a security advisory. |

The Registry schema (`oneshelf.registry/1`) has no deprecation field today. If one becomes necessary it will
be added to OneShelf Core first, compatibly, rather than invented here.
