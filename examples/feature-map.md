# Feature map · import a batch

- **User action** — Run the import command with a batch ID. Retry with that same ID if the first response is lost.
- **Entry point** — `python3 examples/importer.py DATABASE after import BATCH_ID`. The example's `before` revision deliberately allows replay to create a duplicate. Use separate empty databases for each revision.
- **Expected outcome** — Listing the batches shows the retried ID once. A different batch ID creates a separate row.
- **Run and observe** — From the repository root, run `python3 examples/verify.py`. It executes both revisions as child processes and reads the persisted results through their list commands. The output shows both lists and fails if the baseline cannot reproduce the bug or the fix rejects a valid case.
- **Coverage** — The demo checks sequential replay against a fresh SQLite database. The test suite also submits eight overlapping CLI imports after schema initialization and checks the saved rows. Database migrations and network retries are outside this example.
