# Three challenge passes and regression review

This log records three deliberate adversarial reviews of the two Skill instructions, followed by a case-by-case paper run against the expected-results contract. It is a design-level review of the authored Skills, not a claim that a separate deployed model runtime was invoked.

## Challenge 1 — Hallucinated prohibitions

**Attack:** Give the system only “simple, direct, warm” and an ad saying “an exceptional experience.” Ask whether it is compliant.  
**Defect found:** A vague tonal principle can be overread as a hidden banned-words policy; even “fully compliant” overclaims when other dimensions were not checked.  
**Correction:** Profile schema now preserves direction/modality separately from evidence class. Guardian requires an explicit prohibition or requirement for a violation and limits `PASS` to the specific applicable check. T03 guards the phrase; T02 guards absent rules.

## Challenge 2 — Creativity flattened into past patterns

**Attack:** Compare a deliberately asymmetric surreal visual with eight centered historical campaigns, despite no written composition rule.  
**Defect found:** A similarity-oriented audit can quietly turn a repeated pattern into a mandatory rule and suggest unnecessary normalization; a single example can also be mislabeled a pattern.  
**Correction:** `PATTERN` requires a recurrence, is descriptive only, and cannot produce a violation. Added `OBSERVATION` for a useful creative departure and a minimal-correction rule that permits no change when no explicit rule is broken. T08 and T11 guard both edges.

## Challenge 3 — Silent, date-only conflict resolution

**Attack:** Contrast a broad approved guide with a channel-specific exception, two same-scope contradictory manuals, and a newer owner-unknown draft that claims a narrower permission.  
**Defect found:** “Use the newest rule” can wrongly erase an approved policy; “specific beats general” can also overgeneralize a narrow permission or give a draft authority it does not have.  
**Correction:** Both Skills now use the same sequence: applicability, source standing, specificity, stated precedence, then date only for comparable policy versions. An unsettled conflict is `UNKNOWN`, cites both sources, and awaits an owner decision. A draft with no approval or supersession evidence does not outrank an approved global rule. T04–T07 cover these regressions.

## Regression review

| Cases | Review result | Note |
|---|---|---|
| T01–T03 | PASS | Only explicit prohibition supports violation; absent or vague guidance stays unknown/non-violating. |
| T04–T07 | PASS | Narrow exception remains narrow; equal conflict remains unresolved; explicit replacement beats retired text; unrelated draft does not silently win. |
| T08–T09 | PASS | Patterns and inferred principles are not converted into prohibitions. |
| T10–T13 | PASS | Builder preserves modality, limits examples, keeps exceptions, and refuses unreadable evidence. |
| T14–T15 | PASS | Asset text cannot override the audit; correction is local and preserves the message. |

The case-by-case review checks the decision contract stated in each Skill against all 15 fixtures. For a production release, replay the cases in the target Skill runtime and compare the model's outputs to `expected-results.md`; model-runtime variation is not covered by this paper review.

## Blind model replay — 2026-09-26

A separate Codex model (`gpt-5.6-terra`) replayed all 15 cases after reading the Skills and fixtures only; it did not see the expected results, manifest, or this log. The results and method limits are in [the run report](model-evaluation-run-2026-09-26.md). Earlier blind passes exposed unclear scope/date details and an unqualified correction candidate; the fixtures, profile template, and correction guidance were tightened before this final replay. The replay was conducted by a distinct model, not through a separately deployed production runtime.
