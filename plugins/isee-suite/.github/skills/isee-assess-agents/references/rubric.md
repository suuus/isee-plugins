# Agent assessment rubric — full reference

This module is loaded on-demand by `SKILL.md` when assessing individual agents.

## Scan targets

1. `.github/agents/*.agent.md` — each agent's purpose, rules, constraints, output patterns
2. `.github/skills/*/SKILL.md` — scoped responsibilities, input/output contracts, execution patterns
3. `.github/copilot-instructions.md` — shared agent context, cross-agent rules
4. `.mcp.json` — tool access per agent/context, read-only vs read-write scoping
5. `.github/workflows/*.yml` — agent-triggered automation, CI integration with agents
6. Agent output artifacts — patterns where agents write findings, reports, or logs
7. Agent packaging/distribution manifests — package manifests, lockfiles, dependency declarations, installed module directories, or policy files that govern agent packages
8. `.github/isee/execution-manifest.json` and AERP records — governed agent entry points, bindings, gate outcomes, and durable Evidence

## Remote distribution as a signal

When agent context comes from a packaging or distribution system (rather than being defined only in the local repo), this is a strong positive signal — it means intent, structure, and execution boundaries can be centrally managed, versioned, and consistently applied across repos.

**What to look for:**
- Package manifests or lockfiles that declare agent dependencies (skills, instructions, agent definitions sourced from external repos or registries)
- Policy files that enforce organizational constraints on what agent packages are allowed
- Installed module directories containing downloaded agent primitives
- Versioning and reproducibility signals (pinned versions, content hashes, lockfiles)

**What these systems typically carry for ISEE:**
- **Intent**: Skill/agent descriptions that define purpose and when to use
- **Structure**: Always-loaded instructions, ownership, responsibilities, interfaces, boundaries, guardrails, organizational policy enforcement, and tool scoping
- **Execution**: Actual invocation through approved entry points, manifest consumption, gate enforcement, approvals, and handoffs
- **Evidence**: ⚠️ Typically a gap — most agent packaging systems do not natively define what evidence an agent should produce. This is where ISEE adds unique value.

**Key question:** When agent context comes from a remote source, can you trace it back to its origin? Is it versioned? Is there governance over what gets installed? Does the upstream source carry intent, or just code?

## Per-agent signals

### Agent Intent (does the agent have clear, scoped purpose?)

**PRESENT:**
- Explicit role statement ("You are the X advisor" or "You handle Y")
- Scoped boundaries ("I do X, not Y", "This agent focuses on...")
- Outcome orientation (purpose defined in terms of what it achieves, not just what it does)
- Clear distinction from other agents (no ambiguous overlap)
- Intent readable by both humans and other agents

**ABSENT:**
- Generic purpose ("You are a helpful assistant")
- No boundaries — agent tries to do everything
- Purpose described only in terms of actions, not outcomes
- Indistinguishable from other agents in the system

### Agent Structure (does the agent have guardrails?)

**PRESENT:**
- Tool scoping in `.mcp.json` (not `"tools": ["*"]` — specific tools listed)
- Explicit constraints ("do not merge", "do not deploy", "read-only")
- Read-only vs read-write boundaries clearly defined
- Error handling rules (what to do when uncertain, when to escalate)
- Operating rules section in agent definition
- Skill-level constraints (each skill has scoped responsibilities)
- Explicit responsibility, interface, dependency, and trust-boundary declarations
- Exact ASRP Structure binding when the protocol is used

**ABSENT:**
- All tools available to all agents (no scoping)
- No explicit "do not" rules
- No escalation path defined
- No distinction between read and write operations
- Agent can modify anything without approval

### Agent Execution (does the agent operate within the approved Structure?)

**PRESENT:**
- Invoked through an approved entry point or documented workflow
- Consumes and retains the governing Intent/Structure/manifest references
- Required gates and approvals run before consequential actions
- Handoffs occur through defined interfaces and durable artifacts
- Execution stays within Structure-defined responsibility and access boundaries
- Escalation paths to humans are used when autonomy boundaries require them

**ABSENT:**
- Bypasses an approved entry point, required gate, or approval
- Loses or mutates governing bindings during execution
- Performs responsibilities assigned to another agent or owner
- Handoffs rely on transient conversation rather than the defined interface
- Acts outside autonomy boundaries without human escalation

### Agent Evidence (does the agent produce reviewable output that flows upstream?)

**This is the critical layer for agents.** An agent that acts but produces no reviewable evidence is a black box.

**PRESENT:**
- **Citations in output**: Agent cites sources for its decisions (file paths, line numbers, URLs)
- **Structured findings**: Output follows a reviewable format (not just prose dumps)
- **Decision logging**: Agent explains *why* it made a choice, not just *what* it did
- **Audit trail**: Agent actions can be traced after the fact (SQL todos, status updates, saved reports)
- **Evidence → human review flow**: Agent output is designed to be reviewed by humans (clear summaries, actionable items)
- **Evidence → upstream decisions**: Agent-produced evidence informs team decisions (assessment findings → priority changes, drift reports → backlog items)
- **Feedback loop**: Evidence from agent output flows back to agent configuration (reports inform instruction updates, findings lead to guardrail changes)
- **Verify-after-action patterns**: Agent instructions include "check your work", "verify the output", "confirm before proceeding"
- **AERP Evidence**: Agent output is captured as attributable Evidence bound to exact Intent and Structure when the protocol is used

**ABSENT:**
- Agent produces output but doesn't cite sources
- Output is unstructured prose with no clear findings
- No explanation of decisions — just results
- Actions are not logged or traceable
- Output stays in conversation — never persisted or surfaced
- No connection between agent output and team decisions
- No feedback loop — agent config never updated based on its own findings
- Agent acts autonomously with no human review checkpoint

**Evidence upstream flow — key questions:**
1. Can a human **trace** what the agent decided and why?
2. Does agent output **reach** decision-makers (saved reports, notifications, PR comments)?
3. Does agent evidence **change** the next decision (findings → backlog, scores → priorities)?
4. Is there a **closed loop** where agent output improves agent configuration over time?

## Scoring — per-agent

For each agent, score all four ISEE layers using the standard rubric:
Signal, State (Present/Absent/Unknown), Confidence, Citation, Impact, Recommendation

Then assign a per-agent ISEE grade:
- 🟢 **Strong**: Clear intent, scoped structure, clean execution boundaries, evidence flows upstream
- 🟡 **Developing**: Some layers strong, others have gaps. Evidence may exist but doesn't consistently flow upstream
- 🔴 **Weak**: Unclear purpose, no guardrails, overlapping responsibilities, or black-box output

## Profile-adjusted expectations

| Profile | Description | Threshold |
|---------|-------------|-----------|
| **Lightweight** | Startup, small team | 1-2 agents with clear purpose and basic guardrails is strong. Evidence = structured output in conversation. |
| **Standard** | Established team | Agents with scoped tools, defined boundaries, and evidence that persists (saved reports, PR comments). System-level coordination visible. |
| **Regulated** | Compliance-heavy | Agents with audit-grade evidence trails, explicit escalation paths, tool access logs, and evidence that demonstrably informs decisions. System traceability required. |
