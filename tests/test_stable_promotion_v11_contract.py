from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/promote-qualified-stable-v11.yml"


class StablePromotionV11ContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.text = WORKFLOW.read_text(encoding="utf-8")

    def test_promotion_is_created_from_exact_current_main(self) -> None:
        self.assertIn("cancel-in-progress: false", self.text)
        self.assertIn("startsWith(github.ref_name, 'promote11/')", self.text)
        self.assertIn("PROMOTION_NOT_CREATED_FROM_MAIN", self.text)
        self.assertIn("git ls-remote --exit-code origin refs/heads/main", self.text)

    def test_source_release_assets_and_version_are_fail_closed(self) -> None:
        self.assertIn("SOURCE_RELEASE_MISSING", self.text)
        self.assertIn("SOURCE_RELEASE_DRAFT", self.text)
        self.assertIn("SOURCE_RELEASE_PRERELEASE", self.text)
        self.assertIn('runtime_name="home-center-${version}-linux-amd64.tar.gz"', self.text)
        self.assertIn("SOURCE_RUNTIME_ASSET_MISSING", self.text)
        self.assertIn("SOURCE_RUNTIME_SIDECAR_MISSING", self.text)
        self.assertIn("SOURCE_VERSION_MISMATCH", self.text)

    def test_exact_source_ancestry_is_required(self) -> None:
        self.assertIn("APPROVED_REVISION_UNAVAILABLE", self.text)
        self.assertIn("SOURCE_NOT_DESCENDANT_OF_APPROVED_BASE", self.text)
        self.assertIn('refs/tags/v$version:refs/tags/source-v$version', self.text)
        self.assertIn("approved_revision", self.text)

    def test_permanent_promoter_survives_generated_candidate(self) -> None:
        self.assertIn("PERMANENT_PROMOTION_TOOLING_MISSING", self.text)
        self.assertIn("promote-qualified-stable-v11.yml", self.text)
        self.assertIn("test_stable_promotion_v11_contract.py", self.text)
        self.assertNotIn("permanent_workflow.unlink()", self.text)
        self.assertNotIn("permanent_contract.unlink()", self.text)

    def test_candidate_is_requalified_before_push(self) -> None:
        self.assertIn("python3 deploy/scripts/build-release.py verify-source --source-root .", self.text)
        self.assertIn("python3 tests/security_gate_public_release.py", self.text)
        self.assertIn("python3 -m unittest discover -v -s tests -p 'test_*.py'", self.text)
        self.assertIn("HOME_CENTER_PUBLIC_EXPORT=PASS", self.text)


if __name__ == "__main__":
    unittest.main()
