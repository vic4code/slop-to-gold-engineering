# Slop to Gold

**Make recurring code review feedback executable.**

Slop to Gold is an open-source playbook and installable skill for coding agents. Use it to turn a repeated review comment into a code constraint or test, then prove the change through the same entry point your users rely on.

[Quickstart](#quickstart) · [Install](#install-the-skill) · [Guidelines](skills/slop-to-gold-engineering/references/engineering-standard.md) · [Architecture](docs/architecture.md) · [Contributing](CONTRIBUTING.md)

- **Enforce the supported path.** Put the rule in the API, type system, database, or linter where it can catch the mistake.
- **Verify the actual behavior.** Reproduce the failure, rerun it after the fix, and check that a valid case still works.
- **Use the tools you already have.** Run the skill with your project's test and build commands. [pstack](https://github.com/cursor/plugins/tree/main/pstack) adds optional workflows.

## Quickstart

Clone the repository and run the demo with Python 3.10 or later. It uses Python's standard library and SQLite.

```sh
git clone https://github.com/vic4code/slop-to-gold-engineering.git
cd slop-to-gold-engineering
python3 examples/verify.py
```

```text
Before: ['batch-1', 'batch-1', 'batch-2']
After:  ['batch-1', 'batch-2']
Verified: a replay creates one row, and a distinct import still creates its own row.
```

The demo submits the same batch ID twice and a different ID once. A database constraint makes retries safe in the fixed importer. The verifier drives the CLI and reads back the saved rows. Add `--revision before` to see the failing check and its suggested repair. See the [feature map](examples/feature-map.md) for the scenarios covered.

## Install the skill

Run this from the project where you want to use the skill with the [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add vic4code/slop-to-gold-engineering --skill slop-to-gold-engineering
```

You can also copy the complete [skill folder](skills/slop-to-gold-engineering/) into your agent's skill directory or register it as a local skill in OpenBot.

Try it on a recurring review comment in your project:

> Use slop-to-gold-engineering. We keep catching imports from a private adapter. Find the affected callers, enforce the public API boundary, and show one forbidden import failing and one supported import passing. Leave the command I can rerun.

## Repository layout

| Path | Purpose |
| --- | --- |
| [`skills/`](skills/slop-to-gold-engineering/) | Installable workflow and bundled engineering guidelines |
| [`examples/`](examples/) | Runnable CLI demo, verifier, and feature map |
| [`tests/`](tests/) | Checks for the demo's failure message, replay behavior, and documented quickstart |
| [`docs/`](docs/) | Architecture and design notes |
| [`.github/workflows/`](.github/workflows/) | The same demo and tests on pushes and pull requests |

## Contributing

Have a review comment your team keeps writing? Open an issue with the behavior you want to preserve and what would prove the fix. See [CONTRIBUTING.md](CONTRIBUTING.md) for the local checks. If the workflow earns a place in your repo, give this project a **star**.

## Credits and license

An independent adaptation inspired by Lauren Tan's *All Code Is Slop (Except Mine)*. [Original talk and slides](https://ai.engineer/talks/O_zcc6Xl12g-all-code-is-slop-except-mine) · [Design notes and related work](docs/design-notes.md)

The repository's original work is released under the [MIT license](LICENSE).
