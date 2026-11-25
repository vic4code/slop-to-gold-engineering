"""Check one CLI journey against either revision or demonstrate both."""

from argparse import ArgumentParser
from pathlib import Path
from subprocess import run
from sys import executable
from tempfile import TemporaryDirectory


IMPORTER = Path(__file__).with_name("importer.py")
EXPECTED_IDS = ["batch-1", "batch-2"]


def drive(revision, database):
    command = [executable, str(IMPORTER), str(database), revision]
    for import_id in ("batch-1", "batch-1", "batch-2"):
        run([*command, "import", import_id], check=True)
    return run([*command, "list"], check=True, capture_output=True, text=True).stdout.splitlines()


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--revision", choices=("before", "after"))
    args = parser.parse_args()

    with TemporaryDirectory() as directory:
        if args.revision:
            observed = drive(args.revision, Path(directory) / "imports.db")
            require_unique_imports(observed)
            print(f"Verified {args.revision}: {observed!r}")
            return

        before = drive("before", Path(directory) / "before.db")
        after = drive("after", Path(directory) / "after.db")

    print(f"Before: {before!r}")
    print(f"After:  {after!r}")
    if before != ["batch-1", *EXPECTED_IDS]:
        raise SystemExit("The baseline did not reproduce the expected duplicate.")
    require_unique_imports(after)
    print("Verified: a replay creates one row, and a distinct import still creates its own row.")


def require_unique_imports(observed):
    if observed != EXPECTED_IDS:
        raise SystemExit(
            f"Expected {EXPECTED_IDS!r}, got {observed!r}. Keep one row per import ID "
            "with a UNIQUE or PRIMARY KEY constraint and handle replay with "
            "ON CONFLICT (import_id) DO NOTHING at the import entry point."
        )


if __name__ == "__main__":
    main()
