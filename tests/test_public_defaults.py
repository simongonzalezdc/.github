from __future__ import annotations

import py_compile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PublicDefaultsTests(unittest.TestCase):
    def test_required_public_docs_exist(self) -> None:
        required = [
            "README.md",
            "CONTRIBUTING.md",
            "LICENSE",
            "AGENTS.md",
            "CLAUDE.md",
            "docs/agent-law/empower-orchestrator.md",
            "profile/README.md",
        ]
        for path in required:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file(), path)

    def test_agent_law_markers_are_present(self) -> None:
        for path in ["AGENTS.md", "CLAUDE.md", ".github/pull_request_template.md"]:
            with self.subTest(path=path):
                text = (ROOT / path).read_text(encoding="utf-8")
                self.assertIn("EMPOWER_ORCHESTRATOR:START", text)
                self.assertIn("EMPOWER_ORCHESTRATOR:END", text)

    def test_provisioner_script_compiles(self) -> None:
        py_compile.compile(str(ROOT / "scripts/provision-agent-law.py"), doraise=True)


if __name__ == "__main__":
    unittest.main()

