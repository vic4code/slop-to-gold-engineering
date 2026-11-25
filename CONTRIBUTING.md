# Contributing

Report a problem with the observed behavior, the expected result, and the command or prompt that reproduces it. Identify your agent and version if the report concerns skill installation or use.

See the [architecture guide](docs/architecture.md) for where a change belongs. For a change to the example, use the existing CLI entry point. Run these commands from the repository root:

```sh
python3 examples/verify.py
python3 -m unittest discover -s tests
```

If the demo output changes, update the Quickstart transcript in the README. The tests compare it against the CLI output.

For a change to the skill, keep its folder name, frontmatter name, and installation instructions in sync. If you add a new workflow, include a prompt and describe what evidence a successful run should leave. Verify the instructions with and without optional integrations where the change affects both paths.

Use synthetic fixtures. Link source material and describe how the change applies it. In a pull request, include the trigger, the expected and observed results, and any cases you did not verify.
