# Evidence classes and audit outcomes

Keep two questions separate: **what kind of brand evidence is this?** and **what can be concluded about the asset?**

## Evidence class

- `EXPLICIT`: the source directly states a direction. Preserve modality: requirement, prohibition, permission, or preference. Only an applicable, clearly mandatory direction can support a violation.
- `INFERRED`: a reasoned principle synthesized from supplied text or examples. It can support a labeled observation or qualified warning, never a violation.
- `PATTERN`: a recurrence in supplied examples. It can describe similarity or departure, never a violation.
- `UNKNOWN`: unavailable, unreadable, ambiguous, out of scope, or contradictory evidence. It never supports a violation and is not equivalent to pass.

## Audit outcome

- `VIOLATION`: confirmed mismatch with an applicable explicit requirement/prohibition.
- `WARNING`: a relevant deviation from an explicit soft preference or a useful inferred direction; state clearly that it is not a confirmed rule violation. Do not force a warning where it adds no value.
- `PASS`: a checked, applicable explicit requirement is met, or an explicitly permitted option is used within its stated scope. For a permission, say “permitted”; do not imply that the option is required. Do not use “fully compliant” if other relevant areas remain unknown.
- `UNKNOWN`: there is not enough evidence to decide, including unresolved applicable conflict or unreadable asset evidence.
- `OBSERVATION`: optional neutral note about a pattern, novelty, or creative departure when there is no explicit requirement to pass or fail on that point. It is not a compliance finding or a pass/fail claim.

An explicit qualitative principle without phrase-level criteria does not, by itself, justify a warning about a particular word. Use `UNKNOWN` for a requested compliance decision, or a neutral `OBSERVATION` only if it adds useful context. Do not infer a violation or negative warning from word association alone.

An asset-level summary may count confirmed violations and list unresolved areas, but never reduce the audit to a global score. Do not assign arbitrary severity or confidence labels. If the user requests prioritization, explain practical impact in plain language or apply their supplied severity scale.

## Evidence required for a violation

Every violation includes:

1. The explicit rule, preserving its force and any exception.
2. Source document, version/date if known, and page/section/other locator from the profile.
3. A short factual description or quotation of what conflicts in the asset.
4. Why the rule applies to this asset's scope.
5. A minimal correction that preserves intent.

If any of these are missing, downgrade to `UNKNOWN`, `WARNING`, or an observation as appropriate. Do not fill gaps with common brand practice.
