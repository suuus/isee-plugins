# Structure layer — output template

When the assessment is complete, produce this structure:

```
## Structure Layer Assessment

### Findings
[For each finding: Signal · State (Present/Absent/Unknown) · Confidence (High/Medium/Low) · Citation · Impact · Recommendation]

### Upstream Context Connections (Structure)
- **Direct**: [shared CI templates, inherited configs, agent packages — with citations]
- **Indirect**: [compliance policy references, platform constraints — with citations]
- **Structural inheritance**: [Does structure come from upstream? Centrally managed or local-only?]

### Structure Protocol Conformance
- **ASRP**: Exact / Reference / Absent / Invalid / Unknown
- **Intent bindings**: [exact / references only / missing / mismatched]
- **Topology and boundaries**: [actors, ownership, elements, interfaces, dependencies]
- **Execution contract**: [entry point, gates, dependency closure]
- **Evidence obligations**: [complete / partial / absent]
- **Artifact and manifest integrity**: [verified / failed / unknown]

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
