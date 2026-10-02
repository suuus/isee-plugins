---
name: isee-assess-report
description: |
  Compile ISEE layer findings into a scored maturity report. Read-only until user approves saving.

  USE FOR: generate isee report, compile findings, maturity score, phase 5, final report.

  DO NOT USE FOR: individual layer assessments, modifying files without user approval.
user-invocable: false
---

# Generate ISEE Assessment Report

Compile findings from all four ISEE layers (and optionally agents) into a structured report that keeps framework maturity separate from protocol conformance. Scores each layer 🟢/🟡/🔴 and generates prioritized recommendations.

## Procedure

1. Collect findings from Phases 1–4 (and Phase 5 if agents were assessed).
2. Include `[INCOMPLETE]` phases at reduced confidence; exclude `[SKIPPED]` phases with a note.
3. Score each layer using the 3-level scale in [`references/report-template.md`](references/report-template.md). **Unknown ≠ Absent → 🟡 Developing, never 🔴.**
4. Compile the protocol table independently: ADRP, ASRP, manifest consumption, AERP, exact bindings, integrity, Evidence satisfaction, and loop closure.
5. Generate the full report from the template in [`references/report-template.md`](references/report-template.md).
6. Route recommendations to the correct product: Ape Context, ADRP, ASRP, AERP, or ISEE integration. Never recommend profile adoption solely to improve a score.
7. Show report to user, then offer to save via `ask_user` (template in report-template.md).
8. `UPDATE todos SET status = 'done' WHERE id = 'assess-report';`

## Examples

- **All layers complete:** Produces full 5-section report with context chain traceability table.
- **Phase skipped by user:** Report notes "[SKIPPED — not assessed]" for that layer.
- **Mostly Unknowns:** Scores 🟡 Developing with note "Insufficient evidence — score may improve."

## Troubleshooting

- **Missing layer findings:** Include incomplete phases at reduced confidence rather than omitting.
- **Unknown signals dominate:** Never grade 🔴 Weak on Unknowns — use 🟡 Developing.
- **User declines save:** Report stays conversation-only; note drift detection needs a saved baseline.
- **Agents phase was skipped:** Omit agent section from report; note it was not assessed.
