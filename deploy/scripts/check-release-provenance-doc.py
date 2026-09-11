#!/usr/bin/env python3
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
provenance = json.loads((ROOT / "APPROVED-SOURCE.json").read_text(encoding="utf-8"))
release_md = (ROOT / "RELEASE.md").read_text(encoding="utf-8")

errors = []
if provenance.get("version") != version:
    errors.append("APPROVED_SOURCE_VERSION_MISMATCH")

approved_revision = provenance.get("approved_revision", "")
boundary_revision = provenance.get("stable_release_boundary_revision", "")
approved_manifest = provenance.get("approved_manifest_sha256", "")

for name, value, pattern in (
    ("APPROVED_REVISION", approved_revision, r"[0-9a-f]{40}"),
    ("STABLE_BOUNDARY", boundary_revision, r"[0-9a-f]{40}"),
    ("APPROVED_MANIFEST", approved_manifest, r"[0-9a-f]{64}"),
):
    if not re.fullmatch(pattern, value):
        errors.append(f"{name}_INVALID")
    elif value not in release_md:
        errors.append(f"{name}_MISSING_FROM_RELEASE_MD")

if f"Release {version}" not in release_md and f"v{version}" not in release_md:
    errors.append("VERSION_MISSING_FROM_RELEASE_MD")

# RELEASE.md is part of the commit tree, so it must never hard-code the final
# public tag commit SHA: that identity is only knowable after the commit exists.
# The only 40-hex commit identities permitted in the checked-in prose are the
# canonical approved revision and the pre-existing stable release boundary.
found_commit_shas = set(re.findall(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", release_md))
allowed_commit_shas = {approved_revision, boundary_revision}
unexpected = sorted(found_commit_shas - allowed_commit_shas)
missing = sorted(allowed_commit_shas - found_commit_shas)
if unexpected:
    errors.append("UNEXPECTED_RELEASE_MD_COMMIT_SHA=" + ",".join(unexpected))
if missing:
    errors.append("REQUIRED_RELEASE_MD_COMMIT_SHA_MISSING=" + ",".join(missing))

if errors:
    print("RELEASE_PROVENANCE_DOC=FAIL", file=sys.stderr)
    for error in errors:
        print(error, file=sys.stderr)
    raise SystemExit(66)

print(
    "RELEASE_PROVENANCE_DOC=PASS"
    f" version={version}"
    f" approved_revision={approved_revision}"
    f" stable_boundary={boundary_revision}"
)
