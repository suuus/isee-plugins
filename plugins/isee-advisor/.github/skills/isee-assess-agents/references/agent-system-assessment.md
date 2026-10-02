# Multi-agent system assessment — full reference

This module is loaded on-demand by `SKILL.md` when 2 or more agents are detected.

## System-level assessment

When **2 or more agents** are detected, assess the system as a whole across all four ISEE layers.

### System Intent
- Is there an **intent hierarchy**? (orchestrator agent → specialist agents, or shared mission)
- Do agents share a **common purpose**, or are they disconnected?
- Is there a **parent intent** that child agents serve? (e.g., "improve engineering quality" → assess agent + context agent + review agent)
- Does the system's collective purpose align with the repo's **organizational/business intent**?

### System Structure
- Are **guardrails consistent** across agents? (e.g., all agents respect read-only constraints)
- Are **tool permissions scoped per agent**, not shared broadly?
- Are **ownership, responsibilities, interfaces, dependencies, and boundaries between agents clear**?
- Does an ASRP record or equivalent make the coordination topology explicit?

### System Execution
- Do agents execute through approved entry points and preserve governing bindings?
- Are required gates and approvals enforced before consequential actions?
- Do handoffs use Structure-defined interfaces and durable artifacts?
- Is actual behavior consistent with the declared topology and autonomy boundaries?

### System Evidence (upstream flow across agents)
- Does evidence from **one agent flow to another's context**? (e.g., assessment findings available to advise mode)
- Is there **system-level observability**? (can you see what all agents did collectively?)
- Does evidence **roll up** from agent-level to system-level? (individual findings → aggregate report)
- Does system evidence **surface to human decision-makers**? (not trapped inside agent conversations)
- Can a human **trace through the system**: *what was decided → by which agent → based on what evidence → why*?
- Is there a **system feedback loop**? Agent output → human review → configuration update → improved agent behavior?

## System scoring

Score the system on the four system-level signals:
- **System Intent**: Hierarchical / Flat-aligned / Disconnected
- **System Structure**: Consistent / Partial / Inconsistent
- **System Execution**: Well-partitioned / Some overlap / Fragmented
- **System Evidence**: Flows upstream / Partially surfaces / Trapped
