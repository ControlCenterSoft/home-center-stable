from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/promote-qualified-stable-v10.yml"

class StablePromotionV10ContractTests(unittest.TestCase):
    def test_guarded_promotion_contract(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        required = (
            "cancel-in-progress: false",
            "PROMOTION_NOT_CREATED_FROM_MAIN",
            "SOURCE_RELEASE_DRAFT",
            "SOURCE_RELEASE_PRERELEASE",
            "SOURCE_RUNTIME_ASSET_MISSING",
            "SOURCE_RUNTIME_SIDECAR_MISSING",
            "SOURCE_VERSION_MISMATCH",
            "SOURCE_NOT_DESCENDANT_OF_APPROVED_BASE",
            "Qualify promotion tooling contract before candidate sanitization",
            "tests/test_stable_promotion_v10_contract.py",
            "promotion_contract_test.unlink()",
            "verify-source --source-root .",
            "security_gate_public_release.py",
            "HOME_CENTER_PUBLIC_EXPORT=PASS",
        )
        for marker in required:
            self.assertIn(marker, text)

if __name__ == "__main__":
    unittest.main()
