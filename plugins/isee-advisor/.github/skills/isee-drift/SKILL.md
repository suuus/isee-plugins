---
name: isee-drift
description: |
  Re-assess a repo and compare against a prior ISEE report to detect improvements, regressions, and new signals. Read-only scan.

  USE FOR: detect drift, compare assessments, track improvements, regressions, periodic review.

  DO NOT USE FOR: initial assessments, modifying files, configuring tools.
user-invocable: false
---

# ISEE Drift Detection

Compare the current repo state against `.github/isee-report.md` to surface what changed across all four ISEE layers — improvements, regressions, new signals, and unchanged gaps.

## Procedure

1. Find `.github/isee-report.md`; if missing, use the `ask_user` template in [`references/rubric.md`](references/rubric.md).
2. Insert drift todos into SQL — use INSERT template from the rubric.
3. Re-scan all four layers (same signals as assess skills, lighter analysis), including ADRP/ASRP/AERP lifecycle and fingerprint changes.
4. For each prior finding, determine status: ✅ Improved · ✅ Maintained · ⚠️ Regressed · 🆕 New · ➖ Removed · 🔄 Unchanged gap.
5. Separately compare protocol conformance: new/missing records, supersession, changed fingerprints, binding mismatches, gate changes, unsatisfied Evidence, and loop closure.
6. Compare layer scores prior → current; see score change patterns in the rubric.
7. Generate drift report per [`references/output.md`](references/output.md).
8. Offer to save updated baseline via `ask_user` (save template in rubric); if yes, overwrite `isee-report.md`.
9. `UPDATE todos SET status = 'done' WHERE id = 'drift-report';`

## Examples

- **Improved:** Prior: `copilot-instructions.md` absent → Current: file added with priorities → ✅ Improved, Intent 🔴→🟡.
- **Regression:** Prior: CI coverage threshold present → Current: threshold removed → ⚠️ Regressed, Structure 🟢→🟡.
- **New signal:** Agent definition added since prior assessment → 🆕 New signal in Execution.

## Troubleshooting

- **No prior report:** Prompt user via ask_user — do not invent a baseline.
- **Small changes:** Don't over-interpret one file added/removed — note but don't alarm.
- **Prior recommendation implemented:** Call it out positively by name.
- **Agents added since prior:** Trigger optional agent drift sub-scan (see rubric for agent drift dimensions).
