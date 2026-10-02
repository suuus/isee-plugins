---
name: isee-assess-execution
description: |
  Score the Execution layer of ISEE. Read-only scan for manifest consumption, gate outcomes, retained bindings, workflow behavior, and coordination patterns.

  USE FOR: assess execution, manifest consumption, gate enforcement, approvals, context distribution, coordination patterns, phase 3.

  DO NOT USE FOR: other ISEE layers, modifying files, reorganizing teams.
user-invocable: false
---

# Assess Execution Layer

Score how work is performed — whether execution follows approved entry points and gates, retains Intent and Structure bindings, and distributes context through durable artifacts instead of handoffs and meetings. Uses the ISEE rubric: Present/Absent/Unknown · High/Medium/Low confidence · Citation · Impact · Recommendation.

## Procedure

1. Scan files in [`references/rubric.md`](references/rubric.md) → *Scan targets*. Skip missing files.
2. Detect signals per *Execution signals* in the rubric: selected entry points, required gates, approvals, run metadata, retained fingerprints, PR/work-item context, and agent workflow behavior.
3. If an ISEE execution manifest exists, determine whether execution artifacts consume it and preserve its manifest, Intent, and Structure fingerprints. Do not run `isee preflight` or execute the system.
4. Scan for work item traceability: commit messages for `fixes`, `closes`, `AB#`, `JIRA-` patterns.
5. If signals are insufficient, use the `ask_user` template in the rubric.
6. Score against user profile (Lightweight / Standard / Regulated). **Unknown ≠ Absent.**
7. Emit output per [`references/output.md`](references/output.md), including Execution protocol conformance.
8. `UPDATE todos SET status = 'done' WHERE id = 'assess-execution';`

## Examples

- **Strong:** workflow consumes a fingerprinted execution manifest, records required gate outcomes, and retains exact Intent and Structure bindings → Present, High.
- **Context-rich:** PR template asks "What problem does this solve?" and links the work item and manifest → Present.
- **Weak:** Single `* @team` in CODEOWNERS + checklist-only PR template + generic commit messages → Absent.
- **Unknown:** No CODEOWNERS but user describes service-oriented teams → Unknown, use ask_user.

## Troubleshooting

- **No CODEOWNERS:** Not always a gap for Lightweight teams; check PR template richness instead.
- **Generic commit messages:** Only flag as Absent if the PR template also lacks context fields.
- **External coordination tools:** Attempt to follow Jira/ADO references; if unreachable, record as a finding.
- **Many Unknowns:** Score 🟡 Developing; never 🔴 based on Unknowns alone.
