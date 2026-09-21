# Compatibility

Adapters declare the OneShelf plugin API they target in `manifest.yaml` (`api: '1.0'`). A OneShelf
installation runs adapters whose API has the same major version and a minor version no newer than its own;
the Source Registry shows anything else as **Requires a newer OneShelf** and never installs it.

This repository validates against one pinned OneShelf Core revision, recorded in
`tooling/oneshelf-core-ref.txt`. That pin is authoritative for CI and for `./tools/bootstrap`. A separate,
**advisory** workflow also checks against OneShelf's latest `main` and does not block merges.

Contributors cannot extend the plugin API from here. A new capability, field or transform is a OneShelf
Core change with Core's own review; once released, the pin here is moved forward in its own Pull Request.
