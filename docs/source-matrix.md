# Open-access source matrix

Every candidate source for the open-access Registry expansion, investigated against
[source-discovery.md](source-discovery.md#4-open-access-eligibility): whether it is really free in full, whether
robots.txt and the terms allow the requests, which machine-readable interface it has, and what OneShelf can
actually read from it. Statuses:

| Status | Meaning |
|---|---|
| `EXISTING_VERIFIED` | Already an adapter; audited and live-verified in this pass |
| `EXISTING_NEEDS_FIX` | Already an adapter; a defect was found and is not fixed yet |
| `VERIFIED` | New adapter: packaged tests pass and every declared capability passed `./tools/live-check` |
| `IMPLEMENTED_NOT_LIVE_VERIFIED` | New adapter whose packaged tests pass but whose live check could not run |
| `BLOCKED` | Not implementable now; the blocker, the evidence and what would unblock it are recorded |
| `INVESTIGATING` | Not decided yet |

The matrix is being filled in; rows marked `INVESTIGATING` have not been decided.
