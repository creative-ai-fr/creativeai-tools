# Promptoscope camera variants

Use this workflow only when the user asks to vary the point of view, camera position, or viewing angle of an analyzed image.

## Keep the original analysis intact

- Return the original Promptoscope v1.0 analysis object unchanged. It continues to describe the view that is actually visible in the source image.
- Put each requested alternate view in its own JSON sidecar following `camera-variant-schema.json`. Never add camera-variant keys to the source object.
- Each sidecar must contain exactly six keys: `variant_schema_version`, `variant_id`, `source_analysis_id`, `camera`, `preserve`, and `prompt`. The field is `prompt`, never `instruction`.
- The MCP companion UI is optional. If available, call its `promptoscope.camera_variants` tool with the source analysis and the variant sidecars you composed. The tool validates and renders them; it does not analyze the image or write the prompts.
- If the UI tool is unavailable, return the sidecar JSON in the conversation using the same schema.

## Camera coordinates

- `azimuth_deg`: horizontal orbit around the subject relative to the source view. `0` keeps the source direction, negative angles move toward the subject's left, positive angles toward the subject's right, and `-90` / `90` approximate left / right profile views. Keep the value between `-180` and `180`.
- `elevation_deg`: vertical position relative to the source view. `0` is level with it, positive angles look down, and negative angles look up. Keep the value between `-90` and `90`.
- `distance`: a qualitative framing distance: `close`, `medium`, or `wide`. Do not invent physical distances or lens measurements.
- If the user specifies an angle or distance, use it exactly. Otherwise use the default set below.
- Before writing sidecars, extract the user's requested values into a small internal table keyed by `variant_id`. After composing the JSON, compare each sidecar's `camera` object to that table field by field. An explicit request always wins over the defaults; do not silently normalize, round, or substitute coordinates. Regenerate any sidecar that fails this equality check.

## Default set

Create three variants when the user asks for a set but does not specify individual viewpoints:

| ID | View | Azimuth | Elevation | Distance |
| --- | --- | ---: | ---: | --- |
| A | Source / face-on view | 0° | 0° | medium |
| B | Three-quarter from the subject's left | -45° | 0° | medium |
| C | Elevated view | 0° | +45° | medium |

These are defaults, not mandatory choices when the user asks for different angles.

## Write each variant prompt

- Write each `prompt` in English, as a complete image-generation prompt that describes the requested viewpoint and preserves the source's visual identity.
- Preserve the subject, setting, lighting, style, and color palette. Adjust composition only as needed to express the new viewpoint while retaining approximate subject scale and framing where possible.
- Keep known details consistent. Do not invent details hidden from the source view. When a requested viewpoint reveals an unseen surface, say briefly in the accompanying explanation that its appearance must be inferred.
- Do not claim camera motion, 3D reconstruction, exact geometry, or photorealistic consistency unless the source and user provide that information.
- Assign a short analysis ID such as `A-01` for the UI session if needed. It belongs only in each sidecar's `source_analysis_id`; never add it to the source analysis JSON.

## Response

Present the source Promptoscope JSON and each camera sidecar as separate JSON objects. If the companion panel is available, use it to display the source JSON beside selectable variants and their sidecar JSON. Do not replace the source object with a variant.

Before sending, parse each object and verify `additionalProperties: false`, the required key order, and the scalar/array types defined by the two schemas. Repair any mismatch internally and only then return the JSON.
