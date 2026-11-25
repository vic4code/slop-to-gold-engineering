---
name: slop-to-gold-engineering
description: "Use for substantial development, bug fixes, refactors, performance work, and PR reviews when you need to prevent recurring mistakes and prove user-facing behavior. Use pstack when available, enforce correct defaults, and capture reproducible evidence."
license: MIT
metadata:
  example-prompt: "Use slop-to-gold-engineering to fix this recurring issue. Reproduce it, add an effective guard, and show me how to rerun the check."
---

# Slop to Gold

Use [the guidelines](references/engineering-standard.md) for examples and the enforcement decision table. Follow repository instructions and the authorization for the current task.

1. In one or two sentences, restate the intended user outcome, the observable failure or change, and what would prove success. Inspect the active revision, existing entry points, and affected callers. Reproduce a bug before editing. For performance, measure the named scenario before and after under comparable conditions.
2. Choose the smallest effective check or code constraint using the guidelines. For a PR diff, trace the changed code to its callers, report findings with evidence, and review comments for information the code cannot express. When pstack is available, use its relevant workflows from the guidelines. Adapt them to the current tools and authorized scope.
3. Fix the root cause within scope. For a recurring correction, identify actual occurrences and prefer the smallest effective guard in architecture or an API, then types or data constraints, then lint or a repeatable test. Explain what to use in the check's failure message when possible. Pair a constraint with a behavior check. Check how existing data and callers will behave, and remove obsolete workaround paths once their callers can use the supported path. Use prose for decisions that require judgment. In review-only requests, report findings and checks without editing.
4. Verify via the normal entry point. Use the same failing input after the fix and include a valid neighboring case when the rule could reject it. Demonstrate that a new check can fail using a historical failure or isolated fixture. Leave the rerun command or fixture. Capture expected versus observed behavior, including the guard’s side effects. Repeat timing-dependent checks and report how often they reproduce the failure. Prefer the repo's existing harness. If none exists and scope permits, script the entry point, the inputs, and the expected outcome with the project's tools. For important concurrency or state invariants that ordinary cases cannot cover, assess property tests or model checking and state the bounds and assumptions.
5. Return the outcome, revision, rerun command or artifact, observed result, and pending checks. For a review, give each finding's trigger, impact, and minimal repair. A static read, unit test, or sandbox run proves only what was exercised.

The bundled guidelines include a worked example. The repository README links to the runnable version. Avoid triggering builds, writes to production, PR changes, or releases outside the user-authorized task.
