# ISEE Advise — rubric and response guide

This module is loaded on-demand by `SKILL.md` when providing ISEE framework guidance.

## When to ask for more context

If the user's question is vague, gather context first:

```
Use ask_user:
  message: "To give you the best ISEE guidance, a bit more context would help:"
  requestedSchema:
    properties:
      scenario:
        type: string
        title: "What's the situation or challenge?"
        description: "Describe what you're trying to solve or decide."
      current_state:
        type: string
        title: "What exists today?"
        description: "e.g., team size, tools in use, current process"
      desired_outcome:
        type: string
        title: "What would 'good' look like?"
    required: [scenario]
```

## Response structure

### 1. Frame in ISEE
Identify which layers are at play. Most questions touch multiple layers — name them.

### 2. Diagnose
What's the root issue through the ISEE lens? Common patterns:
- **Intent drift**: The team is doing things without clear outcomes ("We ship features but don't know if they matter")
- **Structure gap**: Speed is outrunning guardrails ("Things break and we catch them in production")
- **Execution fragmentation**: Context doesn't travel ("Left hand doesn't know what right hand is doing")
- **Evidence void**: No feedback loop ("We shipped it but have no idea if it worked")

### 3. Recommend
Provide 2–3 specific, actionable steps. Each should state:
- What to do
- Why it helps (which ISEE layer it strengthens)
- How to start (concrete first step)

Route tooling recommendations by the actual gap:

| Gap | Appropriate project |
|-----|---------------------|
| Repository context, MCP discovery, Copilot instructions | [Ape Context](https://github.com/suuus/ape-context) |
| Consequential Intent, decisions, authority, autonomy | [ADRP](https://github.com/suuus/adrp) |
| Ownership, topology, boundaries, gates, execution contract | [ASRP](https://github.com/suuus/asrp) |
| Durable observations, assessments, approvals, outcomes, drift | [AERP](https://github.com/suuus/aerp) |
| Ordinary Copilot projection, preflight, and Evidence evaluation | [ISEE integration](https://github.com/suuus/isee) |

Recommend the smallest appropriate intervention. Do not prescribe the profile tooling when the team's existing artifacts already provide equivalent maturity and traceability.

### 4. Anti-patterns to avoid
Name the relevant anti-patterns from the ISEE operating contract:
- Inferring intent from incomplete context without confirming
- Bypassing constraints to move faster
- Shipping without evidence
- Treating trade-offs as someone else's problem
- Holding context instead of sharing it

## Tone

- Practical over theoretical
- Opinionated but justified
- Direct — don't hedge when the framework has a clear position
- Empathetic — acknowledge the difficulty of organizational change
- Never preachy — ISEE is a tool, not a religion

## Important boundaries

- If the question is about tool setup, identify whether it is context, Intent, Structure, Evidence, or integration before naming a project
- If the question is about a specific layer, focus on that layer but note upstream/downstream dependencies
- If you don't know enough to advise well, say so and ask for more context
- Reference https://agentile.com/agents as the canonical ISEE source
