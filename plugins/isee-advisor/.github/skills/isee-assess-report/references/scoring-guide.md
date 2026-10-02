# Assessment report — scoring guide

This module is loaded on-demand by `SKILL.md` when scoring individual layers for the report.

## Scoring scale

| Score | Meaning |
|-------|---------|
| 🟢 **Strong** | Key signals present with high confidence. Minor gaps only. |
| 🟡 **Developing** | Some signals present, significant gaps exist. Clear path to improvement. |
| 🔴 **Weak** | Key signals absent or unknown. Foundational work needed. |

**Critical rule:** If most signals for a layer are **Unknown**, score as 🟡 Developing with the note: "Insufficient evidence to fully assess — score may improve with more data." **Never score 🔴 Weak based primarily on Unknown signals.**

## How to score each layer

Use the findings from each assess skill phase:

| Layer | Source phase | Key signals to weigh |
|-------|-------------|----------------------|
| Intent | Phase 1 | Intent levels breadth/depth/coherence, authority, autonomy, upstream context |
| Structure | Phase 2 | Ownership, boundaries, interfaces, constraints, gates, structural inheritance |
| Execution | Phase 3 | Entry points, gate/approval behavior, durable context, manifest/work-item traceability |
| Evidence | Phase 4 | Claim quality, provenance, integrity, feedback-loop traceability, monitoring, upstream flow |

## Protocol conformance is not the maturity score

ADRP, ASRP, ISEE manifests, and AERP provide stronger machine-verifiable
traceability. Score protocol conformance separately as Exact, Reference, Absent,
Invalid, or Unknown.

- **Absent** profile artifacts do not reduce framework maturity when equivalent
  practices are demonstrated through other governed artifacts.
- **Exact** conformance raises confidence in findings but does not compensate
  for weak outcomes or an open learning loop.
- **Invalid** claimed conformance is a real gap because consumers may trust a
  broken fingerprint, lifecycle state, binding, gate, or Evidence result.
- Never average protocol status into the four layer emojis.

## Aggregate maturity narrative

After scoring all four layers:

- **🟢🟢🟢🟢 (all strong):** "This team has strong ISEE hygiene. Focus on maintaining and evolving."
- **Mixed 🟢/🟡:** "Solid foundation with clear improvement opportunities in [weakest layer]."
- **Mostly 🟡:** "Developing maturity — prioritize the layer with the most downstream dependencies (Intent first, then Structure)."
- **Any 🔴:** "Foundational work needed in [layer]. Start here before addressing other layers."

## Context chain traceability scoring

After scoring individual layers, assess the cross-cutting chain:

| Chain | Grade | Meaning |
|-------|-------|---------|
| Traceable | 🟢 | Evidence can be followed from bottom (Evidence) to top (Organizational Intent) |
| Partially traceable | 🟡 | Some links exist; gaps in one or more chain segments |
| Fragmented | 🔴 | Chain broken — no clear path between evidence and intent |
| Unknown | 🟡 | Insufficient data to assess; note what evidence would clarify |
