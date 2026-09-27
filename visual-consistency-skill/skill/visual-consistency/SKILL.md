---
name: visual-consistency
description: Compare two or more supplied campaign, storyboard, product, character, or generated images for visual continuity; identify unintended differences, distinguish deliberate variation, and write targeted correction instructions. Use for visual consistency audits, image-series continuity reports, and controlled revision prompts. Do not invoke for a single-image critique or image-to-prompt extraction.
---

# Visual Consistency

1. Establish the comparison set and assign stable IDs (01, 02, …) in supplied order. Identify the reference image or infer the most repeated traits as a provisional baseline. State that inference. If only one image exists, request or locate the missing comparator; offer a single-image checklist only if useful.
2. Record invariants from the user's brief and visibly repeated evidence: identity, product geometry, logo/text, wardrobe, palette, materials, lighting, location, camera, and graphic system. Separate intentional variables (shot, pose, time, format) from invariants. Do not assume every difference is an error.
3. Inspect every image at sufficient resolution, including crops for small details when available. For each finding, name the image ID, region/object, observable difference, baseline evidence, severity (critical/major/minor), and confidence (high/medium/low). Distinguish observed facts from uncertain interpretations. Never claim an unreadable logo is misspelled.
4. Prioritize errors that impair identity, product accuracy, branding, or sequential continuity. A change supported only by aesthetics is a suggestion, not a defect. If images, resolution, or a brand reference are insufficient, mark the finding unverified and say what reference would settle it.
5. Return a compact report: invariant/variable assumptions; a table of findings; coherent elements; top fixes in order; one correction instruction per affected image. Preserve all unaffected content in each prompt and name the specific changes. Include a short global lock list for subsequent generation. Avoid proposing exact pixel-level matches unsupported by the input.
6. If the user requests actual image edits, apply the relevant image-editing tool after the audit and verify the result against the same invariants. Do not treat the audit as authorization to modify the source files.

Use the language of the request. Ask only for a missing reference that prevents a useful comparison; otherwise proceed with labeled assumptions. Do not invent measurements, brand rules, or visual details that cannot be seen.
