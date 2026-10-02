---
name: isee-assess-agents
description: |
  Score agents and agentic systems through the ISEE lens. Read-only. Only runs when agent definitions are detected.

  USE FOR: assess agents, agent guardrails, multi-agent systems, skill playbooks, agent evidence flow, phase 5.

  DO NOT USE FOR: other ISEE layers, modifying agent files, configuring tools.
user-invocable: false
---

# Assess Agents & Agentic Systems

Score whether agents in this repository follow the ISEE framework — and whether multi-agent systems maintain alignment across Intent, Structure, Execution, and Evidence. **Optional phase — only triggered when agent definitions are detected.**

## Procedure

1. Check for agent definitions: `.github/agents/*.agent.md`, `.github/skills/*/SKILL.md`, `.mcp.json`, `.github/copilot-instructions.md` agent sections. If none found, mark `[SKIPPED]` and stop.
2. For each agent, assess all four ISEE layers using signals in [`references/rubric.md`](references/rubric.md).
3. Check for remote distribution signals (agent packaging/policy files) — see rubric for details.
4. If 2+ agents detected, run system-level assessment per [`references/agent-system-assessment.md`](references/agent-system-assessment.md).
5. Score per-agent (🟢/🟡/🔴) and system dimensions per rubric scoring guide.
6. Emit output per [`references/output.md`](references/output.md).
7. `UPDATE todos SET status = 'done' WHERE id = 'assess-agents';`

## Examples

- **Strong agent:** Clear role statement + read-only tool scoping + structured findings with citations → 🟢 Strong.
- **Black box:** Agent acts but produces unstructured prose with no citations and no saved output → 🔴 Weak Evidence.
- **Remote distribution:** Skills installed from a registry with policy enforcement → positive signal; note version traceability.

## Troubleshooting

- **No agent definitions found:** Skip entirely — mark `[SKIPPED — No agent definitions detected]`.
- **Overlapping agent responsibilities:** Surface as Execution gap; don't attempt to resolve it.
- **Agent output stays in conversation:** That is an Evidence gap — flag it clearly.
- **Many Unknowns:** Grade 🟡 Developing; never 🔴 based on Unknowns alone.
