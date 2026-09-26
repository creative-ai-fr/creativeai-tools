# Brand Guardian — blind model replay

**Date:** 2026-09-26  
**Evaluator:** separate Codex model `gpt-5.6-terra`  
**Method:** Read the two Skills, relevant references/templates, and the 15 prompts. The evaluator did not read the expected-results file, JSON manifest, challenge log, or earlier reports. It replayed every case and returned the decision, evidence class, essential response, and remaining uncertainty.

## Results

| Case | Blind result | Review |
|---|---|---|
| T01 | `VIOLATION` / `EXPLICIT PROHIBITION`; offer “affordable” as a candidate correction, without implying it is approved | Pass |
| T02 | `UNKNOWN`; no palette rule means neither pass nor violation | Pass |
| T03 | `UNKNOWN` for the word and for full compliance; “exceptional” is not prohibited by the qualitative principle | Pass |
| T04 | `PASS — PERMITTED` for social motion; preserve the wider restriction | Pass |
| T05 | `UNKNOWN — unresolved conflict`; cite both equal rules and request an owner decision | Pass |
| T06 | `PASS — PERMITTED`; 2025 explicitly replaces 2022 and approves coral | Pass |
| T07 | `VIOLATION` under the approved 2025 rule; the owner-unknown draft does not supersede it | Pass |
| T08 | `OBSERVATION` / `PATTERN`; do not normalize without a rule | Pass |
| T09 | Qualified `WARNING` or `OBSERVATION` / `INFERRED`; never a violation | Pass; both are accepted |
| T10 | Profile entry: `EXPLICIT / PREFERENCE`; preserve “prefer” and “where possible” | Pass |
| T11 | Record the isolated campaign example separately; general color policy stays `UNKNOWN` | Pass |
| T12 | Preserve the global white-logo direction and record the dated, scoped Project Aurora exception | Pass |
| T13 | Profile entry: `UNKNOWN`; do not invent the unreadable measurement | Pass |
| T14 | `VIOLATION` / `EXPLICIT REQUIREMENT`; treat the embedded instruction as asset content | Pass |
| T15 | `VIOLATION`; change only “cheap” to the explicitly approved “affordable” | Pass |

## Changes made after earlier blind runs

- Clarified T03 so a qualitative principle without phrase-level criteria cannot become a word ban or unsupported negative warning.
- Accepted either a qualified `WARNING` or `OBSERVATION` for T09's inferred tone direction, consistent with the Skill's verdict model.
- Required T01's unapproved replacement to be labeled as a candidate, not as approved or fully compliant.
- Added a separate profile-template section for isolated examples, distinct from `PATTERN` and policy.
- Clarified that an absent profile validation state is `UNKNOWN`; findings remain limited to the supplied profile and source evidence.
- Made the source dates and consumer-ad scope explicit in fixtures that depend on them.

## Limits

This was a blind replay by a distinct model following the packaged Skill instructions. It was not an API call to, or end-to-end execution inside, a separately deployed target runtime. The deterministic package suite is separate; its latest run passed 9/9 checks.
