# Security

## Reporting

Please report vulnerabilities privately through GitHub's **Report a vulnerability** (Security tab) on this
repository, not in a public issue. Include the adapter id, what an attacker gains, and how to reproduce.

Relevant here: an adapter or fixture that leaks secrets; a way for a contribution to gain trust it was not
given; a package that escapes OneShelf's validation; a problem in the Registry build or signing process;
a workflow that exposes secrets or runs untrusted code with privileges.

Vulnerabilities in OneShelf itself belong to the OneShelf repository's security policy.

## What protects a OneShelf installation

1. **Declarative only.** Packages contain data files; OneShelf rejects code, symlinks, unsafe names and
   oversized content.
2. **Validation and packaged tests** run in CI, at Registry build time, and again inside OneShelf.
3. **Hashes.** Every Registry entry carries the package's sha256; OneShelf refuses a mismatch, and an install
   is bound to the exact bytes the owner reviewed.
4. **Signatures.** Official and Verified Community require an Ed25519 signature from a key the installation
   trusts. Keys are configured locally in OneShelf and never taken from the Registry.
5. **Permissions.** The owner approves every domain and capability; new permissions in an update wait for
   review.
6. **Network policy.** OneShelf fetches only from approved public domains, re-checking every redirect and
   DNS answer, and never from private networks.

## Signing keys

The project's private signing key never enters this repository, its workflows, its artifacts or logs. Only
public keys are committed (`registry-trust/trusted-keys.txt`). Signing happens on the owner's machine.
