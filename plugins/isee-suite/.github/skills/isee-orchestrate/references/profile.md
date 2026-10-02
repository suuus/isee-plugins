# Profile selection

Before starting the pipeline, ask the user which profile fits their team. This calibrates expectations across every phase.

## ask_user schema

```
Use ask_user with:
  message: "What best describes your team's environment? This calibrates the ISEE assessment."
  requestedSchema:
    properties:
      profile:
        type: string
        title: Team profile
        enum:
          - Lightweight (startup, small team, moving fast)
          - Standard (established team, moderate process)
          - Regulated (compliance-heavy, audit requirements)
        default: Standard (established team, moderate process)
    required: [profile]
```

## What each profile expects

| Profile | Intent | Structure | Execution | Evidence |
|---------|--------|-----------|-----------|----------|
| **Lightweight** | README is fine | Basic CI + linting | Small team, no formal CODEOWNERS | CI passing |
| **Standard** | Dedicated docs + copilot-instructions | CI w/ quality gates, branch protection, tool scoping | CODEOWNERS, context-rich PRs, ADRs | Monitoring + reporting + smoke tests after deploy |
| **Regulated** | Approved strategy docs, ADRs, compliance-linked outcomes | Policy-as-code, mandatory approval gates, audit-grade scanning | Formal ownership, decision audit trail, policy-compliant workflows | Audit-grade trails, mandatory post-incident reviews, SLA monitoring |

## Pass the profile downstream

When invoking each phase skill, include the selected profile in the prompt. Phase skills use the profile to adjust their scoring thresholds (see each skill's `references/rubric.md` → "Profile-adjusted expectations").
