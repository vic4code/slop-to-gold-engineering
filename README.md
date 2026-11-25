# Slop to Gold

**A runnable example of turning repeat code review feedback into a regression check.**

Slop to Gold is an independent teaching project inspired by Lauren Tan's *All Code Is Slop (Except Mine)*. It includes a Python and SQLite example, a short engineering guide, and a companion Agent Skill.

[Quickstart](#quickstart) · [Install the companion skill](#install-the-companion-skill) · [Design notes](docs/design-notes.md) · [Architecture](docs/architecture.md)

## How this relates to pstack

The talk describes how Grok Bot's team applied these ideas in its own codebase, including the Dune framework, app-specific verification tools, and release automation. [pstack](https://github.com/cursor/plugins/tree/main/pstack) is Lauren Tan's collection of reusable agent skills. It already covers the core workflow of preventing recurring mistakes, reviewing changes with evidence, and verifying real user flows. If you already use pstack, use its workflows directly. [See the workflow mapping](docs/design-notes.md#pstack-workflow-mapping).

This repository adds a small, runnable example. The same CLI check shows a duplicate write in the original implementation and verifies that a database constraint fixes it while allowing a different ID. The demo runs with the Python standard library. The companion skill can run on its own and refers to pstack workflows when they are available.

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

## Install the companion skill

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
