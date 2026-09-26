"""Dependency-free checks for the packaged skills and evaluation contract."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
TESTS = ROOT / "tests"
MANIFEST = TESTS / "brand_guardian_cases.json"
EXPECTED_IDS = [f"T{i:02}" for i in range(1, 16)]


def parse_skill_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError(f"Missing YAML frontmatter: {path}")
    fields = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if not separator or key in fields:
            raise AssertionError(f"Malformed or duplicate frontmatter field: {line}")
        fields[key.strip()] = value.strip()
    return fields, text[match.end():]


class SkillPackageTests(unittest.TestCase):
    def test_each_skill_has_valid_minimal_manifest(self):
        for name in ("brand-profile-builder", "brand-guardian"):
            with self.subTest(skill=name):
                folder = SKILLS / name
                fields, body = parse_skill_frontmatter(folder / "SKILL.md")
                self.assertEqual(set(fields), {"name", "description"})
                self.assertEqual(fields["name"], name)
                self.assertTrue(fields["description"])
                self.assertLessEqual(len(fields["description"]), 1024)
                self.assertNotIn("[TODO:", body)
                self.assertTrue(list((folder / "references").glob("*.md")))
                self.assertTrue(list((folder / "assets").glob("*.md")))

    def test_relative_markdown_links_resolve(self):
        link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for markdown in ROOT.rglob("*.md"):
            for target in link_pattern.findall(markdown.read_text(encoding="utf-8")):
                if target.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                local_target = target.split("#", 1)[0]
                self.assertTrue((markdown.parent / local_target).exists(), f"{markdown}: {target}")

    def test_core_decision_contract_is_present(self):
        all_instructions = "\n".join(p.read_text(encoding="utf-8") for p in SKILLS.rglob("*.md"))
        for required in ("EXPLICIT", "INFERRED", "PATTERN", "UNKNOWN", "VIOLATION"):
            self.assertIn(required, all_instructions)
        self.assertRegex(all_instructions, r"(?i)unknown[^\n]{0,100}(never|not)[^\n]{0,100}violation")
        self.assertRegex(all_instructions, r"(?i)(no|without)[^\n]{0,40}(global|overall)[^\n]{0,30}score|do not[^\n]{0,30}score")


class EvaluationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.cases = cls.manifest["cases"]
        cls.by_id = {case["id"]: case for case in cls.cases}

    def test_manifest_has_exactly_fifteen_complete_cases(self):
        self.assertEqual(self.manifest["schema_version"], 1)
        self.assertEqual(list(self.by_id), EXPECTED_IDS)
        for case in self.cases:
            with self.subTest(case=case["id"]):
                self.assertIn(case["skill"], {"brand-profile-builder", "brand-guardian"})
                for field in ("prompt", "profile", "asset", "scope"):
                    self.assertTrue(case[field])
                expected = case["expected"]
                self.assertIn(expected["decision"], {"VIOLATION", "WARNING", "PASS", "UNKNOWN", "OBSERVATION", "PROFILE_ENTRY"})
                self.assertTrue(expected["must"])
                self.assertTrue(expected["must_not"])

    def test_markdown_cases_and_expected_results_cover_manifest(self):
        cases_md = (TESTS / "brand-guardian/test-cases.md").read_text(encoding="utf-8")
        expected_md = (TESTS / "brand-guardian/expected-results.md").read_text(encoding="utf-8")
        for case_id in EXPECTED_IDS:
            with self.subTest(case=case_id):
                self.assertEqual(cases_md.count(f"## {case_id} —"), 1)
                self.assertEqual(expected_md.count(f"| {case_id} |"), 1)

    def test_markdown_expected_decisions_match_machine_readable_manifest(self):
        expected_md = (TESTS / "brand-guardian/expected-results.md").read_text(encoding="utf-8")
        rows = {
            parts[1].strip(): parts[2].strip()
            for line in expected_md.splitlines()
            if line.startswith("| T")
            for parts in [line.split("|")]
        }
        for case in self.cases:
            with self.subTest(case=case["id"]):
                expected = case["expected"]
                token = expected["class"] if expected["decision"] == "PROFILE_ENTRY" else expected["decision"]
                formatted_values = re.findall(r"`([^`]+)`", rows[case["id"]])
                self.assertTrue(any(token in value for value in formatted_values), rows[case["id"]])

    def test_unknown_and_non_rule_evidence_cannot_become_violations(self):
        for case_id in ("T02", "T03", "T05"):
            with self.subTest(case=case_id):
                self.assertEqual(self.by_id[case_id]["expected"]["decision"], "UNKNOWN")
        self.assertEqual(self.by_id["T11"]["expected"]["decision"], "PROFILE_ENTRY")
        self.assertEqual(self.by_id["T11"]["expected"]["class"], "UNKNOWN")
        self.assertIn(self.by_id["T13"]["expected"]["decision"], self.by_id["T13"]["expected"]["acceptable_decisions"])
        self.assertEqual(self.by_id["T13"]["expected"]["class"], "UNKNOWN")
        self.assertEqual(self.by_id["T08"]["expected"]["decision"], "OBSERVATION")
        self.assertEqual(self.by_id["T08"]["expected"]["class"], "PATTERN")
        self.assertEqual(self.by_id["T09"]["expected"]["decision"], "WARNING")
        self.assertEqual(self.by_id["T09"]["expected"]["acceptable_decisions"], ["WARNING", "OBSERVATION"])
        self.assertEqual(self.by_id["T09"]["expected"]["class"], "INFERRED")

    def test_confirmed_violations_require_explicit_evidence(self):
        for case_id in ("T01", "T07", "T14", "T15"):
            with self.subTest(case=case_id):
                self.assertEqual(self.by_id[case_id]["expected"]["decision"], "VIOLATION")
                self.assertEqual(self.by_id[case_id]["expected"]["class"], "EXPLICIT")

    def test_adversarial_fixtures_include_the_evidence_they_expect_models_to_use(self):
        t03 = self.by_id["T03"]
        self.assertIn("EXPLICIT / PRINCIPLE", t03["profile"])
        self.assertIn("No phrase-level criteria", t03["profile"])
        self.assertEqual(t03["expected"]["acceptable_decisions"], ["UNKNOWN", "OBSERVATION"])

        t01 = self.by_id["T01"]
        self.assertIn("do not imply the candidate is approved by the supplied profile", t01["expected"]["must"])

        t11 = self.by_id["T11"]
        self.assertIn("One approved campaign", t11["profile"])
        self.assertEqual(t11["expected"]["class"], "UNKNOWN")
        self.assertIn("call one use a recurring pattern", t11["expected"]["must_not"])
        template = (SKILLS / "brand-profile-builder/assets/brand-profile-template.md").read_text(encoding="utf-8")
        self.assertIn("Isolated examples (non-normative)", template)

        t12 = self.by_id["T12"]
        self.assertIn("(2024)", t12["profile"])
        self.assertIn("2026-08-14", t12["profile"])
        self.assertIn("Signed campaign brief", t12["profile"])

        t14 = self.by_id["T14"]
        self.assertIn("consumer-facing ad", t14["asset"])
        self.assertIn("no source note", t14["asset"])


if __name__ == "__main__":
    unittest.main()
