# Evidence layer — output template

When the assessment is complete, produce this structure:

```
## Evidence Layer Assessment

### Findings
[For each finding: Signal · State (Present/Absent/Unknown) · Confidence (High/Medium/Low) · Citation · Impact · Recommendation]

### Upstream Context Connections (Evidence)
- **Direct**: [CI reporting flows, agent artifacts, MCP monitoring — with citations]
- **Indirect**: [dashboard refs, retro process mentions, incident system refs — with citations]
- **Feedback loop traceability**: [Closed loop / Partial loop / Open loop — does evidence flow back to decisions?]

### Evidence Upstream Flow
- Evidence **produced**: [list sources — CI, monitoring, agents, changelogs]
- Evidence **consumed upstream**: [what evidence visibly informs decisions?]
- Evidence **closing the loop**: [incidents → backlog? metrics → priorities? agent findings → config changes?]

### Evidence Protocol Conformance
- **AERP**: Exact / Reference / Absent / Invalid / Unknown
- **Intent bindings**: [exact / partial / mismatched / unknown]
- **Structure bindings**: [exact / partial / mismatched / unknown]
- **Manifest requirements**: [satisfied / partial / failed / unknown]
- **Provenance and validity**: [attributable and current / partial / invalid / unknown]
- **Record and artifact integrity**: [verified / failed / unknown]

### Summary
- Signals found: X present, Y absent, Z unknown
- Confidence: [overall confidence level]
- Key strength: [what's working well]
- Key gap: [most impactful missing signal]
- Top recommendation: [single most valuable next step]
```

## Critical scoring rule

**Unknown ≠ Absent.** Never score a team poorly because data is missing. Report insufficient evidence and suggest how to get it.

If most signals for the layer are Unknown, the layer-level grade should be 🟡 Developing with the note "Insufficient evidence to fully assess — score may improve with more data." Never grade 🔴 Weak based primarily on Unknown signals.
