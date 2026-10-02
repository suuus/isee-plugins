# Execution layer — output template

When the assessment is complete, produce this structure:

```
## Execution Layer Assessment

### Findings
[For each finding: Signal · State (Present/Absent/Unknown) · Confidence (High/Medium/Low) · Citation · Impact · Recommendation]

### Upstream Context Connections (Execution)
- **Direct**: [work item refs in commits/PRs, cross-repo ownership — with citations]
- **Indirect**: [team/stakeholder references, external workflow tools — with citations]
- **Work item traceability**: [Connected / Partial / None — can execution be traced to upstream work items?]

### Execution Protocol Conformance
- **Manifest consumption**: Exact / Reference / Absent / Invalid / Unknown
- **Manifest fingerprint retained**: [yes / no / unknown]
- **Intent and Structure bindings retained**: [exact / partial / mismatched / unknown]
- **Entry point followed**: [yes / no / unknown]
- **Required gates and approvals**: [enforced / partial / bypassed / unknown]
- **Evidence handoff**: [AERP / durable equivalent / prose only / unknown]

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
