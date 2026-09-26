# Brand Guardian Skills

Two composable Skills turn supplied brand sources into a reviewable profile and a traceable creative audit:

- `brand-profile-builder` extracts explicit rules, inferred principles, recurring patterns, isolated examples, conflicts, and unknowns.
- `brand-guardian` audits copy or creative assets against that profile, cites its evidence, and proposes the smallest supported correction.

## Install

For Codex, copy both folders under [`skills/`](skills/) to the Skills directory in your environment (for example, `$CODEX_HOME/skills/`). Each Skill folder is self-contained. For another agent that supports the Agent Skills format, use that agent's discovery mechanism.

## Use

1. Run `brand-profile-builder` with the available brand documents and the intended scope.
2. Review and validate the resulting profile with the brand owner.
3. Run `brand-guardian` with that profile, the asset, the channel and audience, and the creative objective.

`UNKNOWN` means the supplied evidence does not support a decision; it is never a violation or a pass. A recurring pattern is descriptive, not a rule. Unresolved conflicts stay visible, corrections preserve the creative intent, and the audit has no aggregate score.

## Tests

The adversarial suite has 15 scenarios in `tests/brand-guardian/`. The blind replay by a distinct Codex model is documented in [`model-evaluation-run-2026-09-26.md`](tests/brand-guardian/model-evaluation-run-2026-09-26.md). Run the deterministic package checks from this directory:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The blind replay follows the Skills directly; it is not a substitute for a full replay in another deployed runtime.

## Contents

- `skills/brand-profile-builder/` — profile extraction Skill, schema, evidence guide, and template.
- `skills/brand-guardian/` — audit Skill, verdict model, conflict rules, correction guide, and report template.
- `examples/` — fictional profile and audit showing scoped evidence and a limited correction.
- `tests/` — behavioral fixtures, expected results, and dependency-free package checks.
