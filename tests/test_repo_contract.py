"""Contract tests for the how-to-human overhaul.

These encode the MVP UX: front door first, library second, donate last.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LIB_FILES = (
    "lib/body/sleep-protocols.md",
    "lib/body/thermal-regulation.md",
    "lib/body/hardware-tuning.md",
    "lib/mind/regulation-scripts.md",
    "lib/mind/input-management.md",
    "lib/social/identity-protocols.md",
)

CANONICAL = (
    "README.md",
    "manifesto.md",
    "main().md",
    "docs/core-guide.md",
    "docs/donate.md",
    "docs/profile/README.md",
    "docs/profile/BIO.md",
    ".github/FUNDING.yml",
    "tasks.md",
)

OLD_TO_NEW = (
    ("Sleep-Protocols.md", "lib/body/sleep-protocols.md"),
    ("Thermal-Regulation.md", "lib/body/thermal-regulation.md"),
    ("Hardware-Tuning.md", "lib/body/hardware-tuning.md"),
    ("Regulation-Scripts.md", "lib/mind/regulation-scripts.md"),
    ("Input-Management.md", "lib/mind/input-management.md"),
    ("Identity-Protocols.md", "lib/social/identity-protocols.md"),
    ("The-Core-Guide.md", "docs/core-guide.md"),
)

BTC = "bc1q3rfg8nxtqtmqvqk9yted68j3ny9v3xzlh2tqen"
SOL = "Eh8yq5CWVVJu5dM73XxQzTnptaRwpKGeXMNqnTKPqqkw"
ETH_BURN = "0x0000000000000000000000000000000000000000"


def _read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def _unlabeled_opening_fences(text: str) -> list[int]:
    """Return 1-based line numbers of opening fences with no language hint."""
    unlabeled: list[int] = []
    in_fence = False
    for index, line in enumerate(text.splitlines(), 1):
        if not line.startswith("```"):
            continue
        if in_fence:
            in_fence = False
            continue
        lang = line[3:].strip()
        if not lang:
            unlabeled.append(index)
        in_fence = True
    return unlabeled


class TestCanonicalLayout(unittest.TestCase):
    def test_lib_modules_exist(self) -> None:
        missing = [path for path in LIB_FILES if not (ROOT / path).is_file()]
        self.assertEqual(missing, [], f"missing lib modules: {missing}")

    def test_canonical_docs_exist(self) -> None:
        missing = [path for path in CANONICAL if not (ROOT / path).is_file()]
        self.assertEqual(missing, [], f"missing canonical files: {missing}")

    def test_old_root_modules_are_stubs_or_gone(self) -> None:
        for old, new in OLD_TO_NEW:
            path = ROOT / old
            if path.is_file():
                text = path.read_text(encoding="utf-8")
                self.assertIn(new, text, f"{old} must point at {new}")
                self.assertLess(
                    len(text.splitlines()),
                    12,
                    f"{old} should be a stub, not a duplicate manual",
                )


class TestReadmeIsFrontDoor(unittest.TestCase):
    def setUp(self) -> None:
        self.readme = _read("README.md")

    def test_no_base64_images(self) -> None:
        self.assertNotIn("data:image", self.readme)

    def test_no_eth_burn_address(self) -> None:
        self.assertNotIn(ETH_BURN, self.readme)

    def test_informational_hook_present(self) -> None:
        self.assertRegex(
            self.readme,
            r"(?i)(instruction manual|git gud|firmware|RTFM|bootloader)",
        )

    def test_visual_banner_referenced(self) -> None:
        self.assertRegex(
            self.readme,
            r"!\[.+\]\(assets/.+\.(png|svg|webp)\)|<img [^>]*src=\"assets/.+\.(png|svg|webp)\"",
        )
        banners = list((ROOT / "assets").rglob("*.png")) + list(
            (ROOT / "assets").rglob("*.svg")
        )
        self.assertTrue(banners, "expected at least one banner under assets/")

    def test_quick_start_before_donate(self) -> None:
        lower = self.readme.lower()
        quick = lower.find("quick start")
        donate = min(
            i
            for i in (lower.find("## fuel"), lower.find("support this"), lower.find("donate"))
            if i != -1
        )
        self.assertGreater(quick, -1, "Quick Start missing")
        self.assertGreater(donate, quick, "donate/support must come after Quick Start")

    def test_opening_is_not_a_tip_jar(self) -> None:
        opening = "\n".join(self.readme.splitlines()[:28])
        self.assertNotRegex(opening, r"(?i)bitcoin|ethereum|solana|donate crypto|bc1q")

    def test_donate_is_collapsed_details(self) -> None:
        self.assertRegex(self.readme, r"(?i)<details")
        self.assertRegex(self.readme, r"(?i)<summary>.*(fuel|support|donate|coffee)")

    def test_links_into_lib(self) -> None:
        self.assertIn("lib/mind/regulation-scripts.md", self.readme)
        self.assertIn("lib/body/sleep-protocols.md", self.readme)
        self.assertIn("docs/core-guide.md", self.readme)
        self.assertIn("manifesto.md", self.readme)

    def test_fenced_code_has_language(self) -> None:
        self.assertEqual(_unlabeled_opening_fences(self.readme), [])

    def test_does_not_paste_full_manifesto(self) -> None:
        self.assertNotIn("Hogwarts with only your Physics 101", self.readme)


class TestDonateSurface(unittest.TestCase):
    def setUp(self) -> None:
        self.donate = _read("docs/donate.md")
        self.funding = _read(".github/FUNDING.yml")

    def test_btc_and_sol_present(self) -> None:
        self.assertIn(BTC, self.donate)
        self.assertIn(SOL, self.donate)

    def test_no_placeholder_eth(self) -> None:
        self.assertNotIn(ETH_BURN, self.donate)

    def test_no_base64(self) -> None:
        self.assertNotIn("data:image", self.donate)

    def test_no_privacy_rotation_fiction(self) -> None:
        self.assertNotRegex(self.donate, r"(?i)addresses may rotate")

    def test_funding_yml_points_at_donate_doc(self) -> None:
        self.assertIn("custom:", self.funding)
        self.assertRegex(self.funding, r"donate")

    def test_donate_fences_labeled(self) -> None:
        self.assertEqual(_unlabeled_opening_fences(self.donate), [])


class TestNoPhantomDevkitTest(unittest.TestCase):
    def test_acceptance_readme_removed(self) -> None:
        self.assertFalse(
            (ROOT / ".github/ACCEPTANCE_TEST_README.md").exists(),
            "phantom neuro-spicy-devkit acceptance test must be removed",
        )


class TestCanonicalContent(unittest.TestCase):
    def test_manifesto_is_the_source(self) -> None:
        manifesto = _read("manifesto.md")
        self.assertIn("Hogwarts", manifesto)
        self.assertIn("RTFM", manifesto)

    def test_main_is_a_bootloader_not_a_dump(self) -> None:
        main = _read("main().md")
        self.assertNotIn("content omitted for brevity", main)
        self.assertLess(len(main.splitlines()), 80)
        self.assertRegex(main, r"(?i)definite move|main\(\)|bootloader")

    def test_identity_protocols_are_not_gatekeeping(self) -> None:
        text = _read("lib/social/identity-protocols.md").lower()
        self.assertNotIn("normies", text)

    def test_core_guide_links_lib(self) -> None:
        guide = _read("docs/core-guide.md")
        self.assertIn("lib/body/sleep-protocols.md", guide)
        self.assertIn("Module 01", guide)


class TestProfileProposal(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = _read("docs/profile/README.md")
        self.bio = _read("docs/profile/BIO.md").strip()

    def test_hook_and_featured_work(self) -> None:
        self.assertRegex(self.profile, r"(?i)(firmware|glitch|zenos|how-to-human|rtfm)")
        self.assertIn("how-to-human", self.profile)
        self.assertIn("zenOS", self.profile)

    def test_visual_hook(self) -> None:
        self.assertRegex(self.profile, r"!\[.+\]\(|<img ")

    def test_donate_collapsed_and_not_in_opening(self) -> None:
        self.assertRegex(self.profile, r"(?i)<details")
        opening = "\n".join(self.profile.splitlines()[:20])
        self.assertNotRegex(opening, r"(?i)bitcoin|solana|bc1q")

    def test_bio_fits_github_limit(self) -> None:
        first_line = next(
            (line.strip() for line in self.bio.splitlines() if line.strip() and not line.startswith("#")),
            "",
        )
        self.assertLessEqual(len(first_line), 160)
        self.assertGreater(len(first_line), 20)

    def test_profile_fences_labeled(self) -> None:
        self.assertEqual(_unlabeled_opening_fences(self.profile), [])


if __name__ == "__main__":
    unittest.main()
