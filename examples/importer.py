"""An isolated example of the same import command before and after a guardrail."""

import argparse
import sqlite3
from contextlib import closing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("database")
    parser.add_argument("revision", choices=("before", "after"))
    parser.add_argument("operation", choices=("import", "list"))
    parser.add_argument("import_id", nargs="?")
    args = parser.parse_args()

    if (args.operation == "import") != (args.import_id is not None):
        parser.error("Provide an import ID for import only.")

    with closing(sqlite3.connect(args.database)) as db, db:
        if args.revision == "before":
            db.execute("CREATE TABLE IF NOT EXISTS imports (import_id TEXT NOT NULL)")
        else:
            db.execute("CREATE TABLE IF NOT EXISTS imports (import_id TEXT PRIMARY KEY NOT NULL)")

        if args.operation == "list":
            for (import_id,) in db.execute("SELECT import_id FROM imports ORDER BY import_id"):
                print(import_id)
        elif args.revision == "before":
            db.execute("INSERT INTO imports (import_id) VALUES (?)", (args.import_id,))
        else:
            db.execute(
                "INSERT INTO imports (import_id) VALUES (?) ON CONFLICT (import_id) DO NOTHING",
                (args.import_id,),
            )


if __name__ == "__main__":
    main()
