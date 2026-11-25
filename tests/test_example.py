import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


class ExampleTest(unittest.TestCase):
    def test_readme_quickstart_matches_executable_output(self):
        readme = (EXAMPLES.parent / "README.md").read_text(encoding="utf-8")
        quickstart = readme.split("## Quickstart\n", 1)[1].split("\n## ", 1)[0]
        documented = quickstart.split("```text\n", 1)[1].split("\n```", 1)[0]

        result = subprocess.run(
            [sys.executable, str(EXAMPLES / "verify.py")],
            check=True,
            capture_output=True,
            text=True,
            timeout=15,
        )

        self.assertEqual(result.stdout.rstrip("\n"), documented)

    def test_documented_baseline_fails_with_repair_guidance(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(EXAMPLES / "verify.py"), "--revision", "before"],
                cwd=directory,
                capture_output=True,
                text=True,
                timeout=15,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("['batch-1', 'batch-1', 'batch-2']", result.stderr)
        self.assertIn("UNIQUE or PRIMARY KEY", result.stderr)

    def test_parallel_cli_replays_keep_one_row_per_id(self):
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "imports.db"
            command = [sys.executable, str(EXAMPLES / "importer.py"), str(database), "after"]

            # Initialize the schema before exercising concurrent clients.
            subprocess.run([*command, "list"], check=True, timeout=15)
            ids = ["batch-1"] * 6 + ["batch-2"] * 2
            with ThreadPoolExecutor(max_workers=len(ids)) as workers:
                imports = [
                    workers.submit(
                        subprocess.run, [*command, "import", batch_id], check=True, timeout=15
                    )
                    for batch_id in ids
                ]
                for result in imports:
                    result.result()

            listed = subprocess.run(
                [*command, "list"], check=True, capture_output=True, text=True, timeout=15
            )

        self.assertEqual(listed.stdout.splitlines(), ["batch-1", "batch-2"])
