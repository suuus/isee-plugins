# Agent assessment — output template

When the assessment is complete, produce this structure:

```
## Agent & Agentic System Assessment

### Agents Detected
[List each agent with file path]

### Per-Agent ISEE Assessment

#### {Agent Name} (`{file path}`)
| Layer | Score | Key Finding |
|-------|-------|-------------|
| Intent | 🟢/🟡/🔴 | {one-line} |
| Structure | 🟢/🟡/🔴 | {one-line} |
| Execution | 🟢/🟡/🔴 | {one-line} |
| Evidence | 🟢/🟡/🔴 | {one-line} |

**Evidence upstream flow**: [Flows to decisions / Partially surfaces / Trapped in conversation]

[Repeat for each agent]

### Multi-Agent System Assessment
*(Only if 2+ agents detected)*

| Dimension | Score | Finding |
|-----------|-------|---------|
| System Intent | Hierarchical/Flat-aligned/Disconnected | {one-line} |
| System Structure | Consistent/Partial/Inconsistent | {one-line} |
| System Execution | Well-partitioned/Some overlap/Fragmented | {one-line} |
| System Evidence | Flows upstream/Partially surfaces/Trapped | {one-line} |

### Evidence Upstream Flow Analysis
- Evidence **produced** by agents: [list what agents output]
- Evidence **persisted**: [list what gets saved vs conversation-only]
- Evidence **reaching humans**: [how findings surface to decision-makers]
- Evidence **closing the loop**: [does output inform next configuration/decision?]

### Summary
- Agents assessed: X
- Agents with strong evidence flow: Y
- System coordination: [description]
- Key strength: [what's working]
- Key gap: [most impactful missing signal]
- Top recommendation: [single most valuable next step]
```

## Critical scoring rule

**Unknown ≠ Absent.** Never score an agent poorly because data is missing. Report insufficient evidence and suggest how to get it.

If most signals for a layer are Unknown, grade as 🟡 Developing with the note "Insufficient evidence to fully assess." Never grade 🔴 Weak based primarily on Unknown signals.
