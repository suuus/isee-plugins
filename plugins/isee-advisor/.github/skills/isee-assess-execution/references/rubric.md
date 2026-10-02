# Execution rubric — full reference

This module is loaded on-demand by `SKILL.md` when assessing the Execution layer.

## Scan targets

Read these files if they exist:

1. `.github/isee/execution-manifest.json`, `.github/isee/preflight.json` — approved execution contract and preflight outcome
2. Workflow run metadata, deployment records, approvals, logs, or agent outputs — did execution consume the contract?
3. `.github/workflows/*.yml`, pipeline definitions, runbooks — selected entry points and required gates
4. `.github/pull_request_template.md` — does it carry Intent, manifest, work item, trade-off, and Evidence context?
5. `.github/agents/*.agent.md`, `.github/skills/*/SKILL.md` — do executors accept scoped responsibilities and immutable context?
6. `.github/copilot-instructions.md` — workflow sections, cross-tool chains, execution guidance
7. Recent commit messages and PR titles — do they retain upstream work and decision references?
8. `CODEOWNERS` or `.github/CODEOWNERS` — does execution route review to Structure-defined owners?

## Execution signals

### PRESENT
- Execution consumes an immutable `isee-execution-manifest/v1` contract
- Manifest, ADRP Intent, and ASRP Structure fingerprints are retained in run/deployment metadata
- Selected entry point is used and required blocking gates cannot be bypassed
- Approval and gate outcomes are persisted
- CODEOWNERS routes work to Structure-defined owners
- PR template that asks for context: "What problem does this solve?", "What trade-offs were made?"
- Commit messages that carry intent, not just changes ("Fix auth timeout to meet SLA" vs "Fix bug")
- Agent definitions execute within Structure-defined responsibilities
- Cross-tool workflows documented in copilot-instructions.md
- Service/module boundaries visible in repo structure
- ADRs (Architecture Decision Records) that distribute decision context

### ABSENT
- Execution bypasses the selected entry point or required gate
- Run artifacts cannot identify which Intent, Structure, or manifest governed the action
- Manifest bindings are copied incorrectly or mutate during execution
- No approval/gate result is retained for consequential work
- No CODEOWNERS or routing contradicts Structure-defined ownership
- PR template with only a checklist (no context fields)
- Commit messages that describe only mechanical changes
- No agent/skill definitions (no AI-native execution layer)
- No documented workflows or cross-tool chains
- Execution behavior contradicts the approved Structure
- Decisions or approvals are trapped in meeting notes or Slack
- No work item traceability — commits and PRs disconnected from upstream work tracking
- No cross-team context — execution appears isolated from organizational coordination

### UNKNOWN
When repo signals are weak, attempt to follow external coordination references (work item boards, team docs) using available tools. If unreachable, record as a finding — don't ask the user to go retrieve the content.

## Execution protocol conformance

Execution has no separate durable profile in the stack. Assess whether external executors honor the immutable ASRP-compiled manifest:

| Check | Exact conformance |
|-------|-------------------|
| Manifest consumption | Run/deployment metadata identifies the exact manifest ID and fingerprint |
| Binding retention | Exact ADRP and ASRP IDs/fingerprints survive into execution and Evidence |
| Entry point | The selected manifest entry point initiated the work |
| Gate enforcement | Required blocking gates ran before consequential action; advisory gates are visible |
| Approval | Required human or policy approval is durable and attributable |
| Outcome handoff | Execution emits or references AERP Evidence rather than success-shaped prose |

Classify execution conformance as **Exact**, **Reference**, **Absent**, **Invalid**, or **Unknown**. A repository may have healthy informal Execution without using manifests.

## Upstream context connections (Execution)

### Direct connections (discoverable in-repo)
- Work item references in commit messages (scan for `AB#\d+`, `JIRA-\d+`, `#\d+`, `fixes`, `closes`, `resolves`)
- PR template fields that require work item links or upstream references
- Cross-repo ownership references in CODEOWNERS comments
- Agent definitions distributed via packaging systems — remote agent packaging is a form of distributed execution context
- GitHub Projects or milestones referenced in issue templates

### Indirect connections (referenced but external)
- Team names or external stakeholders mentioned in docs
- References to cross-team dependencies ("coordinated with platform team")
- External workflow tools mentioned (Jira boards, ADO sprints, Linear)
- Meeting or ritual references that suggest external coordination patterns

## Profile-adjusted expectations

| Profile | Description | Threshold |
|---------|-------------|-----------|
| **Lightweight** | Small team | No CODEOWNERS needed. PR descriptions carrying context is the key signal. Agent usage is a bonus. Work item refs optional. |
| **Standard** | Established team | Context-rich PRs, documented entry points and gates, durable approvals, some agent integration, and work-item traceability. CODEOWNERS should agree with documented Structure. |
| **Regulated** | Compliance-heavy | Immutable execution contract or equivalent, exact decision/structure traceability, durable approvals and gate outcomes, policy-compliant workflows, and complete work-item traceability. |

## When signals are weak — ask_user template

```
Use ask_user:
  message: "Execution patterns are harder to assess from repo alone. A few questions:"
  requestedSchema:
    properties:
      team_structure:
        type: string
        title: "How is your team organized?"
        enum:
          - "Small team — everyone owns everything"
          - "Service-oriented — teams own specific services/modules"
          - "Platform + product teams — shared infrastructure layer"
          - "Other"
        default: "Small team — everyone owns everything"
      coordination:
        type: string
        title: "How does your team coordinate work?"
        enum:
          - "Mostly through artifacts (PRs, docs, tickets)"
          - "Mix of artifacts and meetings"
          - "Mostly through meetings and Slack"
        default: "Mix of artifacts and meetings"
      agents_in_use:
        type: boolean
        title: "Are you using AI agents (Copilot, etc.) in your workflow?"
        default: true
    required: [team_structure]
```

Ask only when in-repo signals are insufficient and no reachable external source exists. Never ask the user to fetch content for you.
