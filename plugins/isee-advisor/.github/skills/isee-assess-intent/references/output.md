# Intent layer — output template

When the assessment is complete, produce this structure:

```
## Intent Layer Assessment

### Findings
[For each finding: Signal · State (Present/Absent/Unknown) · Confidence (High/Medium/Low) · Citation · Impact · Recommendation]

### Intent Levels
| Level | State | Source | Citation |
|-------|-------|--------|----------|
| Organizational | Present/Absent/Unknown | Direct/Indirect/— | [file or reference] |
| Business | ... | ... | ... |
| Product | ... | ... | ... |
| Architecture | ... | ... | ... |
| Platform | ... | ... | ... |

- **Breadth**: X of 5 levels addressed
- **Depth**: Traceable / Partially traceable / Fragmented
- **Coherence**: Aligned / Mixed / Contradictory

### Upstream Context Connections
- **Direct**: [list with citations, or "None found"]
- **Indirect**: [list with citations, or "None found"]
- **Context isolation risk**: Low / Medium / High

### Intent Protocol Conformance
- **ADRP**: Exact / Reference / Absent / Invalid / Unknown
- **Applicable records**: [decision IDs, versions, lifecycle states]
- **Authority and ratification**: [summary]
- **Autonomy boundaries**: [usable / partial / absent]
- **Integrity**: [verified fingerprints / references only / failed / unknown]

### Summary
- Signals found: X present, Y absent, Z unknown
- Confidence: [overall level]
- Key strength: [what's working well]
- Key gap: [most impactful missing signal]
- Top recommendation: [single most valuable next step]
```

## Critical scoring rule

**Unknown ≠ Absent.** Never score a team poorly because data is missing. Report insufficient evidence and suggest how to get it.

If most signals for the layer are Unknown, the layer-level grade should be 🟡 Developing with the note "Insufficient evidence to fully assess — score may improve with more data." Never grade 🔴 Weak based primarily on Unknown signals.
