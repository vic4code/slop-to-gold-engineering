# Slop to Gold Guidelines

Use this standard for substantial features, bug fixes, refactors, performance work, and code reviews.

## Define the behavior and the evidence

Restate the user's goal, the affected entry point, and what would prove success. Read the repository instructions and identify the revision and affected callers. For a bug, capture the original failure. For performance, measure the named scenario under conditions you can repeat. For a review, record each finding's trigger and consequence.

## Make the correct path the default

Link actual occurrences before calling a problem recurring. A single confirmed bug can still merit a regression check. Work down the table and choose the smallest effective guard. Pair a constraint with a behavior check when the resulting user experience matters.

| Layer | Use it to | Evidence |
| --- | --- | --- |
| Architecture and API | Give state one owner and expose a supported way to change it. | Existing callers still work and cannot bypass the invariant through an old path. |
| Types and data constraints | Reject invalid states at the boundary that owns them. | Valid input works and the boundary rejects invalid input. |
| Lint and CI | Catch a pattern the code still permits. Point the diagnostic at the replacement or repair. | The same check catches a known bad example and accepts a valid neighbor. |
| Behavior tests | Check the result and side effects through the normal entry point. | The same journey fails for the original reason before the fix and succeeds after it. |
| Documentation and skills | Record decisions that require judgment, including why exceptions exist. | A maintainer can identify when the decision applies and when to revisit it. |

When a timer, retry, or manual sync obscures a problem, trace where ownership or ordering went wrong. Remove obsolete copies of the workaround once callers are migrated. Existing code teaches agents which patterns to repeat. Before adding a data constraint, check for existing violations and define how the rollout will handle them. Check for side effects of the guard itself. Keep comments that explain constraints a reader cannot infer from the code, such as an external API limitation.

## Verify what the user does

Write a small feature map when the path is hard to discover. Include the user action, the entry point, test state, and expected visible and persisted results. Reuse the repository's existing driver. Make the local edit, run, and debug loop reliable before automating review, merging, or release. Capture the action and its result with a command transcript, screenshot, or recording as appropriate. Use isolated data.

For race conditions, retry ordering, or state transitions that ordinary examples cannot cover, state the invariant and assess property tests or model checking. Report the tested cases, bounds, and assumptions. Show that each new guard can fail on a known historical case or an isolated faulty fixture. Leave the rerun command. Repeat timing-dependent scenarios and report how often the failure reproduced.

## Optional pstack integration

| Task | Reference |
| --- | --- |
| Confirm the goal | `in-your-own-words` |
| Plan the work | The matching `poteto-mode` playbook, such as bug fix, feature, refactoring, or performance |
| Review a diff | `interrogate` for findings backed by runs and `no-comments` for comment review. Apply each within the authorized review scope. |
| Prevent recurring corrections | `correct` |
| Identify affected callers and data paths | `blast-radius` |
| Make an app journey repeatable | `create-verification-skill` |
| Check an important invariant beyond ordinary examples | `create-formal-verification-skill`. Use `statechart` when a reader needs to see allowed transitions or a counterexample. |

Use the project's tools and the local pstack reference when it is available. With pstack unavailable, restate the goal, list the affected callers, choose a guard from the table, and verify it through the normal entry point with the project’s tools. Report the revision, rerun command or artifact, observed result, and anything still unverified.

## Worked example

A synthetic batch importer creates a second record when a caller retries with the same ID. Make that ID unique at the database layer and handle the conflict at the import entry point. Send the same ID twice and a different ID once, then list what was saved. The example covers sequential replay against a fresh SQLite database. The repository also exercises concurrent CLI clients against a fresh database with an initialized schema. Migration and network retries need separate checks in a real product.

## Sources

- Lauren Tan’s talk covers enforceable architecture, actionable lint diagnostics, runtime evidence, and formal verification. [Original talk and slide viewer](https://ai.engineer/talks/O_zcc6Xl12g-all-code-is-slop-except-mine) · [Organizer transcript](https://ai.engineer/api/code/reading-download/transcripts/lauren-tan.md)
- The workflow names come from [pstack](https://github.com/cursor/plugins/tree/main/pstack). This repository supplies its own standard, feature map, and runnable example.
