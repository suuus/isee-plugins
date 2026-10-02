---
name: isee-assess-intent
description: |
  Score the Intent layer of ISEE. Read-only scan for outcome statements, priorities, decision criteria, ADRP records, the 5 intent levels, and the upstream context chain.

  USE FOR: assess intent, map intent levels, trace upstream context, detect broken context chains, phase 1.

  DO NOT USE FOR: other ISEE layers, modifying files, writing strategy docs.
user-invocable: false
---

# Assess Intent Layer

Score how clearly the team's intent is expressed for humans and agents. Uses the ISEE rubric: Present/Absent/Unknown · High/Medium/Low confidence · Citation · Impact · Recommendation.

## Procedure

1. Scan files in [`references/rubric.md`](references/rubric.md) → *Scan targets*. Skip missing files.
2. Detect signals per *Intent signals* in the rubric.
3. If ADRP records exist, inspect schema version, lifecycle/ratification, authority, autonomy, Evidence expectations, and fingerprints. Use read-only `adrp validate`, `adrp verify-set`, or `adrp fingerprint` when installed.
4. Map the 5 intent levels; compute Breadth, Depth, Coherence.
5. Follow the context chain. Fetch external refs with available tools. Unreachable → finding: *context chain broken at [citation]*. Never delegate fetching to the user.
6. If signals are insufficient, use the `ask_user` template in the rubric.
7. Score against the user's profile (Lightweight / Standard / Regulated). **Unknown ≠ Absent.**
8. Emit output per [`references/output.md`](references/output.md), including Intent protocol conformance.
9. `UPDATE todos SET status = 'done' WHERE id = 'assess-intent';`

## Examples

- **Strong:** copilot-instructions.md *"Priorities: Reliability > Velocity > Cost. Escalate conflicts to platform."* → Present, High.
- **Broken chain:** README references *"architecture on Confluence"* with no URL → finding: *context chain broken at README*.
- **Unknown vs Absent:** no docs and no refs → Absent. No docs but unreachable Confluence link → Unknown.
- **Canonical Intent:** effective ADRP record with authority, autonomy, expected Evidence, and a verified fingerprint → Present, High; report exact protocol conformance separately.

## Troubleshooting

- **Many Unknowns:** score 🟡 Developing, never 🔴 based on Unknowns alone.
- **External URL 404/403:** that *is* a finding. Record it and continue.
- **Profile mismatch:** confirm the orchestrator-selected profile; Lightweight intent in README is legitimately strong.
- **Conflicting levels:** *"reliability first"* + infra with no limits → Coherence: Contradictory. Surface in Top Recommendation.

