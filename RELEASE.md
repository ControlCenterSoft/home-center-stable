# Release 0.42.0

The release set contains the Linux runtime archive, source archive, canonical
SPDX 2.3 document, acceptance record, release manifest, and `SHA256SUMS`. Both
archives contain `VERSION`, `REVISION`, and an internal `MANIFEST.sha256`.
Verify the complete set before installation and require the published
`v0.42.0` tag and release artifacts to agree with the release manifest.

This promotion incorporates the approved Home Center development source at
canonical revision `980e9d84736b64a6e1558bae524e4da2a1c8115a` (`v0.42.0`).
The checked-in `APPROVED-SOURCE.json` records that canonical revision, approved
manifest digest `f82f1d80515fab27f320a69341e1cd137154faf6ad0281c2bd5349bd5c002958`,
the stable release-boundary revision
`c9a9c2ab5c5ccd76369409aed5d0b906bafb77b7`, and the per-file disposition
(`identical`, `adapted`, or `excluded`).

The final public tag commit is deliberately not hard-coded into this checked-in
file. A commit cannot reliably contain its own final commit identity. The
actual annotated-tag resolution is verified after publication and belongs in
post-publication release evidence (release manifest / acceptance metadata /
GitHub Release metadata). Commit equality between canonical and public
repositories is not a release requirement; the version, approved source
mapping, manifests, checksums, SBOM, acceptance evidence, and actual tag
resolution are the authoritative link.

The immutable `v0.42.0` tag contains stale prose provenance identifiers carried
forward from 0.41.0. See `docs/release-errata/0.42.0.md`; the tag and release
assets remain immutable and must not be rewritten.

For subsequent stable releases, `VERSION` is the canonical publication
identity. The release branch must be exactly `release/<VERSION>`, the annotated
tag is `v<VERSION>`, and `VERSION`, Python package metadata, and the runtime
version must agree. Publication is permitted only through the stable release
procedure; documentation corrections do not mutate an already published tag
or GitHub Release.
