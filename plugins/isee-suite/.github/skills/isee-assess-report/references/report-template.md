# ISEE Assessment Report — full template and process

This module is loaded on-demand by `SKILL.md` when generating the final assessment report.

## Scoring scale

| Score | Meaning |
|-------|---------|
| 🟢 **Strong** | Key signals present with high confidence. Minor gaps only. |
| 🟡 **Developing** | Some signals present, significant gaps exist. Clear path to improvement. |
| 🔴 **Weak** | Key signals absent or unknown. Foundational work needed. |

**Critical rule:** If most signals for a layer are **Unknown**, score as 🟡 Developing with a note: "Insufficient evidence to fully assess — score may improve with more data." Never score 🔴 Weak based primarily on Unknown signals.

## Report template

```markdown
# ISEE Assessment Report

**Repository:** {repo name}
**Date:** {date}
**Profile:** {Lightweight / Standard / Regulated}
**Assessed by:** ISEE Advisor (https://github.com/suuus/isee-advisor)

---

## Summary

| Layer | Score | Key Finding |
|-------|-------|-------------|
| Intent | 🟢/🟡/🔴 | {one-line summary} |
| Structure | 🟢/🟡/🔴 | {one-line summary} |
| Execution | 🟢/🟡/🔴 | {one-line summary} |
| Evidence | 🟢/🟡/🔴 | {one-line summary} |

**Overall maturity:** {narrative summary — 2-3 sentences}

### Protocol Conformance

Protocol conformance increases confidence but is not included as a penalty merely because a team uses equivalent non-profile artifacts.

| Capability | Status | Evidence |
|------------|--------|----------|
| ADRP records valid | Yes / No / Absent / Unknown | {citation or validation result} |
| ASRP records valid | Yes / No / Absent / Unknown | {citation or validation result} |
| Intent → Structure binding | Exact / Reference / Absent / Invalid / Unknown | {IDs and fingerprints} |
| Execution manifest | Valid / Missing / Invalid / Unknown | {manifest ID and fingerprint} |
| Manifest consumed by execution | Exact / Reference / Absent / Invalid / Unknown | {run or workflow citation} |
| AERP Evidence valid | Yes / No / Absent / Unknown | {citation or validation result} |
| Evidence → Intent binding | Exact / Reference / Absent / Invalid / Unknown | {IDs and fingerprints} |
| Evidence → Structure binding | Exact / Reference / Absent / Invalid / Unknown | {IDs and fingerprints} |
| Required Evidence satisfied | Complete / Partial / Failed / Unknown | {requirements and matching records} |
| ISEE loop | Closed / Partial / Open / Unknown | {visible upstream consumption} |

**Protocol summary:** {Exact chain / Partial chain / Reference-only / Invalid chain / No protocol artifacts / Unknown}

---

## Intent Layer {score emoji}

### Strengths
{bulleted list of Present findings with citations}

### Gaps
{bulleted list of Absent findings with recommendations}

### Insufficient evidence
{bulleted list of Unknown findings with how to get more data}

### Intent Levels
| Level | State | Source | Citation |
|-------|-------|--------|----------|
| Organizational | Present/Absent/Unknown | Direct/Indirect/— | [ref] |
| Business | ... | ... | ... |
| Product | ... | ... | ... |
| Architecture | ... | ... | ... |
| Platform | ... | ... | ... |

- **Breadth**: X of 5 levels addressed
- **Depth**: [Traceable / Partially traceable / Fragmented]
- **Coherence**: [Aligned / Mixed / Contradictory]

### Intent Protocol Conformance
- ADRP: [Exact / Reference / Absent / Invalid / Unknown]
- Applicable records, authority, autonomy, lifecycle, and integrity: [summary]

---

## Structure Layer {score emoji}

{same format as Intent — Strengths, Gaps, Insufficient evidence}

### Upstream Structural Inheritance
- [shared CI, inherited configs, agent packages from distribution systems, compliance policy refs]

### Structure Protocol Conformance
- ASRP: [Exact / Reference / Absent / Invalid / Unknown]
- Intent bindings, topology, execution contract, Evidence obligations, and integrity: [summary]

---

## Execution Layer {score emoji}

{same format}

### Work Item Traceability
- [Connected / Partial / None — with evidence]

### Execution Protocol Conformance
- Manifest consumption: [Exact / Reference / Absent / Invalid / Unknown]
- Retained bindings, entry point, gates, approvals, and Evidence handoff: [summary]

---

## Evidence Layer {score emoji}

{same format}

### Evidence Upstream Flow
- Evidence **produced**: [sources]
- Evidence **consumed upstream**: [what informs decisions]
- **Feedback loop**: [Closed / Partial / Open]

### Evidence Protocol Conformance
- AERP: [Exact / Reference / Absent / Invalid / Unknown]
- Intent/Structure bindings, requirement matching, provenance, validity, and integrity: [summary]

---

## Context Chain Traceability

### Evidence → Intent chain (bottom-up)
Can evidence be traced back through execution and structure to the intent it serves?
- **Grade**: [Traceable / Partially traceable / Fragmented / Unknown]
- **Evidence**: {what was found}

### Organizational → Platform chain (top-down)
Can intent be traced from organizational level down to platform-level decisions?
- **Grade**: [Traceable / Partially traceable / Fragmented / Unknown]
- **Evidence**: {what was found}

### Upstream context connections (across all layers)
| Layer | Direct | Indirect | Isolation Risk |
|-------|--------|----------|---------------|
| Intent | X connections | Y connections | Low/Medium/High |
| Structure | ... | ... | ... |
| Execution | ... | ... | ... |
| Evidence | ... | ... | ... |

---

## Agent & Agentic System Assessment
*(Only included when agent definitions were detected)*

### Per-Agent ISEE
| Agent | Intent | Structure | Execution | Evidence | Evidence Upstream |
|-------|--------|-----------|-----------|----------|-------------------|
| {name} | 🟢/🟡/🔴 | 🟢/🟡/🔴 | 🟢/🟡/🔴 | 🟢/🟡/🔴 | Flows/Partial/Trapped |

### System Assessment (if 2+ agents)
| Dimension | Score |
|-----------|-------|
| System Intent | Hierarchical / Flat-aligned / Disconnected |
| System Structure | Consistent / Partial / Inconsistent |
| System Execution | Well-partitioned / Some overlap / Fragmented |
| System Evidence | Flows upstream / Partially surfaces / Trapped |

### Agent Evidence Flow
- Agent output that **persists**: [list]
- Agent output that **informs decisions**: [list]
- Agent **feedback loop**: [does agent output improve agent config?]

---

## Top 3 Recommendations

Prioritized by impact and effort:

1. **{title}** — {description}. *Effort: {Low/Medium/High}. Impact: {description of what improves}.*
2. **{title}** — {description}. *Effort: {Low/Medium/High}. Impact: {description}.*
3. **{title}** — {description}. *Effort: {Low/Medium/High}. Impact: {description}.*

### Recommendation routing

Use the smallest project that addresses the demonstrated gap:

- **Ape Context** — repository context, MCP discovery, and Copilot instructions.
- **ADRP** — consequential Intent, authority, trade-offs, autonomy, and expected Evidence.
- **ASRP** — ownership, topology, interfaces, boundaries, gates, and execution contracts.
- **AERP** — durable observations, assessments, approvals, outcomes, drift, and integrity.
- **ISEE integration** — ordinary Copilot projection, preflight orchestration, and Evidence evaluation.

Do not recommend adopting a profile merely to improve the assessment score. Equivalent, well-governed artifacts remain valid ISEE implementations.

---

## Next Steps

- Re-run this assessment after implementing recommendations: `/isee-advisor drift`
- For deeper framework context: https://agentile.org
- Context and Copilot instructions: https://github.com/suuus/ape-context
- Intent records: https://github.com/suuus/adrp
- Structure records and execution manifests: https://github.com/suuus/asrp
- Evidence records: https://github.com/suuus/aerp
- Copilot and agentic-flow integration: https://github.com/suuus/isee
- Full article series: https://thesuzannedaniels.substack.com

---

*Generated by [ISEE Advisor](https://github.com/suuus/isee-advisor) · ISEE Framework by Suzanne Daniels*
```

## Post-report actions

### Offer to save

```
Use ask_user:
  message: "Here's your ISEE assessment. Would you like me to save it?"
  requestedSchema:
    properties:
      save:
        type: boolean
        title: "Save report to .github/isee-report.md?"
        description: "This creates a baseline for future drift detection."
        default: true
    required: [save]
```

If yes, write the report to `.github/isee-report.md`.
If no, the report remains in the conversation only.

### Offer the relevant setup path

Only offer a project when a finding maps directly to its responsibility. For repository context gaps:

```
Use ask_user:
  message: "Your assessment found gaps in your context layer. Would you like to set up Ape Context to configure MCP servers and generate copilot instructions?"
  requestedSchema:
    properties:
      setup_ape_context:
        type: boolean
        title: "Set up Ape Context?"
        description: "Copies the context-wizard agent from github.com/suuus/ape-context into your repo."
        default: false
    required: [setup_ape_context]
```

Only ask this if gaps are relevant. Never push it on a team with strong structure.

For ADRP, ASRP, AERP, or ISEE integration, explain the relevant project and ask whether the user wants a separate setup task. Assessment remains read-only and must not configure these tools directly.
