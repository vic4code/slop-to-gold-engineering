# Design notes

Slop to Gold is an independent adaptation of Lauren Tan’s talk. This page connects the original ideas to the workflows and example in this repository.

## pstack workflow mapping

pstack already covers the workflow practiced here. Each link points to the upstream skill that addresses that part of the process.

- [`correct`](https://github.com/cursor/plugins/blob/ca782ed8b3c2c521cead8e1720d55c3a5dbf2347/pstack/skills/correct/SKILL.md) turns repeat mistakes into enforceable rules and proves that each new check catches a known counterexample.
- [`interrogate`](https://github.com/cursor/plugins/blob/ca782ed8b3c2c521cead8e1720d55c3a5dbf2347/pstack/skills/interrogate/SKILL.md) stress-tests a change and backs review findings with reproducible runs.
- [`create-verification-skill`](https://github.com/cursor/plugins/blob/ca782ed8b3c2c521cead8e1720d55c3a5dbf2347/pstack/skills/create-verification-skill/SKILL.md) helps a project build a verification workflow around the entry point its users actually use.

The local example demonstrates that approach at a SQLite write boundary. The [CLI verifier](../examples/verify.py) drives the original and corrected versions and reads back the saved data. The [feature map](../examples/feature-map.md) describes the scenario and its coverage.

## Grok Bot's project-specific implementation

The talk describes a broader engineering system. Grok Bot puts constraints in its Electron framework, Dune. Its feature map and CLI let agents exercise the running app. The team also describes experiments with formal verification and an automated release workflow that tests new builds and opens fixes. pstack supplies reusable workflows for some of these practices. The project's own architecture and verification tools carry them out in Grok Bot. [Original talk and slides](https://ai.engineer/talks/O_zcc6Xl12g-all-code-is-slop-except-mine)

## From the talk to the repo

| Talk segment | Implementation here |
| --- | --- |
| [Trust pyramid and codebase quality](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=123s) | Use code structure and executable rules first. Reserve prose for decisions that need judgment. |
| [Dune and enforceable boundaries](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=300s) | Tan illustrates module boundaries in Dune. This repository applies the same principle at a different boundary, using SQLite to enforce one record per batch ID. |
| [Timer workarounds and lint diagnostics](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=416s) | Trace repeated corrections to their cause. The runnable behavior check names the failed invariant, the observed rows, and the repair. |
| [Runtime verification and feature maps](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=580s) | Record the public entry point, drive it, and check the persisted result. |
| [Code as memory](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=264s) | Retire obsolete workaround paths once callers have migrated. |
| [Formal verification](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=650s) | Consider bounded property or model checks for important cases ordinary tests cannot cover. |
| [Release automation](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=911s) | Verify the local edit, run, and debug loop before automating release. |

[Original talk and slide viewer](https://ai.engineer/talks/O_zcc6Xl12g-all-code-is-slop-except-mine) · [Trust pyramid slide frame](https://ai.engineer/api/talk-essay-media/c094802d6073e6ab31aad6a7406c807a88afd34efea9b445be9196cc365761dc) · [Feature map slide frame](https://ai.engineer/api/talk-essay-media/0a57dd9b23616685acb085340c05e2583095347dc8f0ddb0fea3b4f5943aa210)

[Karpathy’s LLM Wiki idea file](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and [llm-code-wiki](https://github.com/dylannalex/llm-code-wiki) are precedents for turning a public explanation into a task-specific tool. Related implementations of Lauren Tan’s talk include [All Code Is Slop · Agent Skills](https://github.com/wilsonwangdev/all-code-is-slop-skills) and [Trust Pyramid](https://github.com/Tim-rppl/trust-pyramid).
