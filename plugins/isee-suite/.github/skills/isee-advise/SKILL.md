---
name: isee-advise
description: |
  Answer ISEE framework questions with opinionated, layer-specific guidance for any scenario. Read-only.

  USE FOR: isee advice, framework guidance, diagnose isee gaps, which layer to improve, team structure questions.

  DO NOT USE FOR: running full assessments, modifying files, writing strategy docs.
user-invocable: false
---

# ISEE Advise

On-demand Q&A skill that answers ISEE framework questions with practical, layer-specific guidance. Frames any scenario through Intent, Structure, Execution, and Evidence.

## Procedure

1. Identify which ISEE layer(s) the question touches (often multiple).
2. If question is vague, use the `ask_user` template in [`references/rubric.md`](references/rubric.md).
3. Diagnose root issue through the ISEE lens — see *Common patterns* in the rubric.
4. Provide 2–3 specific, actionable steps (what, why it helps, how to start).
5. Name relevant anti-patterns from the ISEE operating contract (rubric).
6. If specific articles are relevant, link from [`references/further-reading.md`](references/further-reading.md).

## Examples

- **Intent drift:** Team ships features without knowing if they matter → recommend outcome statements + priority declarations.
- **Structure gap:** Breaks happen in production → recommend CI quality gates + agent guardrails.
- **Evidence void:** Shipped but no feedback → recommend monitoring, changelog, and verify-after-action patterns.

## Troubleshooting

- **Question is too vague:** Use ask_user to gather scenario, current state, desired outcome before advising.
- **Question spans all 4 layers:** Address the weakest layer first; note upstream/downstream dependencies.
- **User asks about tool setup:** Suggest running a full assess first or point to Ape Context.
- **Framework position unclear:** Reference https://agentile.com/agents as canonical ISEE source.
