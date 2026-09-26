# Brand profile schema

Use this schema in the profile template. Keep the epistemic class separate from the kind of direction and from later audit status.

## Epistemic class

| Class | Meaning | What it can support |
|---|---|---|
| `EXPLICIT` | A source directly states a requirement, prohibition, permission, or preference. Preserve whether it says *must*, *must not*, *may*, *prefer*, or similar. | A hard violation only when the source clearly prohibits or requires something, the rule applies, and the asset contradicts it. A soft preference may support a qualified warning, never an invented ban. |
| `INFERRED` | A principle is reasonably synthesized from explicit statements or multiple examples, but is not stated as a direct rule. | A clearly labeled observation or qualified warning. Never a violation. State the inference and its evidence. |
| `PATTERN` | A feature recurring across at least two supplied examples, without evidence that it is required. | Descriptive context, such as “different from the examples reviewed.” One example is an isolated example, not a pattern. Never a violation by itself. |
| `UNKNOWN` | Evidence is absent, inaccessible, contradictory, ambiguous, or insufficient. | A limitation or question. Never a violation and never a pass. |

An explicit statement can be permissive or aspirational rather than mandatory. Do not use `EXPLICIT` as shorthand for “enforceable prohibition.” Store modality separately.

## Fields for each item

- `id`: stable short identifier.
- `topic`: e.g. logo, color, typography, tone, claims, photography.
- `class`: one of the four epistemic classes above.
- `statement`: concise, faithful restatement; retain modality and exceptions.
- `direction`: `REQUIREMENT`, `PROHIBITION`, `PERMISSION`, `PREFERENCE`, `PRINCIPLE`, `OBSERVATION`, or `UNKNOWN`.
- `evidence`: exact short quotation or concrete description of the evidence. Do not invent quotations.
- `source`: document/file name and visible version/date/status, if available.
- `locator`: page, section, slide, timestamp, image/frame, or `NOT PROVIDED`.
- `scope`: explicit values for brand, market, channel, format, audience, product/campaign; use `UNKNOWN` for unspecified dimensions.
- `validity`: stated effective date, end date, or `UNKNOWN`; do not derive an effective date from file metadata alone.
- `supersedes_or_exception`: exact relationship stated by a source, or `NONE STATED`.
- `confidence`: `HIGH`, `MEDIUM`, or `LOW` for extraction quality, with a short reason; this measures evidence quality, not compliance.

## Source inventory and profile state

At profile level, record brand, scope, build date, profile version, source inventory, inaccessible/partial material, unresolved conflicts, known exceptions, open questions, and reviewer/validation state. The default state is `DRAFT — HUMAN REVIEW REQUIRED`.

## Isolated examples

Keep a useful single example in a separate non-normative inventory with its source and exact campaign/scope. This is a source note, not a fifth epistemic class. If the example does not establish a general rule, record the broader policy as `UNKNOWN`; do not place one example in the `PATTERN` table.

## Classification examples

- “Never use gradients in approved static assets.” → `EXPLICIT` / `PROHIBITION`, with its named scope.
- “Prefer short, direct headlines.” → `EXPLICIT` / `PREFERENCE`; this does not mean long headlines are forbidden.
- A brand book calls the brand “warm and direct,” and examples often use first person. A conclusion that first person supports warmth is `INFERRED`, with both sources named.
- Seven of eight supplied campaigns use centered product photography → `PATTERN`, limited to those examples.
- One approved campaign uses a blue background → record that single example with its source; it is not a `PATTERN`, and the general color rule remains `UNKNOWN`.
- No supplied source discusses green → `UNKNOWN` for green use; do not infer a palette ban or approval.
