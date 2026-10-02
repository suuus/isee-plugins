---
name: isee-assess-evidence
description: |
  Score the Evidence layer of ISEE. Read-only scan for AERP records, exact bindings, artifact integrity, feedback loops, monitoring, CI reporting, and upstream signal flow.

  USE FOR: assess evidence, check feedback loops, monitor signal flow, ci reporting, phase 4.

  DO NOT USE FOR: other ISEE layers, modifying files, configuring monitoring tools.
user-invocable: false
---

# Assess Evidence Layer

Score whether the team produces observable signals that flow back upstream — evidence that actually changes the next decision. Uses the ISEE rubric: Present/Absent/Unknown · High/Medium/Low confidence · Citation · Impact · Recommendation.

## Procedure

1. Scan files in [`references/rubric.md`](references/rubric.md) → *Scan targets*. Skip missing files.
2. Detect signals per *Evidence signals* in the rubric (AERP records, CI reporting, monitoring, alerting, changelogs).
3. If AERP records or bundles exist, inspect exact ADRP/ASRP bindings, subjects, results, criteria, producer identity, artifact integrity, validity, and supersession. Use read-only `aerp validate`, `aerp verify`, or `isee evaluate` when installed.
4. Assess upstream flow: incident → backlog, metrics → priorities, agent output → decisions.
5. If signals are insufficient, use the `ask_user` template in the rubric.
6. Score against user profile (Lightweight / Standard / Regulated). **Unknown ≠ Absent.**
7. Emit output per [`references/output.md`](references/output.md), including Evidence protocol conformance and loop closure.
8. `UPDATE todos SET status = 'done' WHERE id = 'assess-evidence';`

## Examples

- **Strong:** CI uploads coverage + Datadog alerts wired + CHANGELOG.md present → Present, High.
- **Canonical Evidence:** valid AERP record with exact ADRP and ASRP bindings satisfies a manifest requirement and passes artifact verification → Present, High.
- **Open loop:** Monitoring dashboards exist but no backlog items ever cite them → finding: *feedback loop open*.
- **Unknown vs Absent:** No monitoring refs in repo but user describes Grafana → Unknown, not Absent.

## Troubleshooting

- **External monitoring tools:** Attempt to follow dashboard URLs; if unreachable, record as a finding — don't ask the user to retrieve content.
- **Many Unknowns:** Score 🟡 Developing; never 🔴 based on Unknowns alone.
- **Agent evidence:** Check whether agent output persists (saved reports) or stays in conversation only.
- **Profile mismatch:** Confirm profile; Lightweight evidence can be a CI status badge + error tracking.
