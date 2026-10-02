# Intent rubric — full reference

This module is loaded on-demand by `SKILL.md` when assessing the Intent layer.

## Scan targets

Read these files if they exist:

1. `.github/copilot-instructions.md` — intent statements, priorities, values, outcome definitions
2. `README.md` — project goals, purpose, outcome-oriented descriptions
3. `CONTRIBUTING.md` — decision criteria, what counts as "done"
4. `.github/agents/*.agent.md` — embedded intent, constraints, operating rules
5. `docs/` — strategy docs, ADRs, team charters
6. `.github/isee/` or `docs/isee/` — dedicated ISEE documentation
7. `.github/pull_request_template.md` — does it ask for intent/outcome?
8. `.github/ISSUE_TEMPLATE/` — do they require outcome/goal statements?
9. `.github/decisions/**/*.json`, `decisions/**/*.json`, `docs/decisions/**/*.json` — ADRP records
10. `.github/isee/active-intent.json`, `.github/isee/context.md`, `.github/isee/preflight.json` — resolved Intent projection

## Intent signals

### PRESENT
- Explicit outcome statements ("aims to reduce deployment time by 50%")
- Priority declarations ("reliability > feature velocity")
- Decision criteria ("PRs must demonstrate user impact")
- Values or principles that guide trade-offs
- Agent-readable intent (clear enough for an AI to act on without guessing)
- Valid ADRP records with `schema_version: ape-decision-record/v1`
- Effective, ratified ADRP Intent with explicit authority, autonomy, lifecycle, and expected Evidence

### ABSENT
- Project purpose described only in terms of what it IS, not what it ACHIEVES
- No explicit priorities or trade-off guidance
- Ambiguous language that could be interpreted multiple ways
- Intent trapped in tribal knowledge (nothing written down)
- No distinction between "must have" and "nice to have"
- Intent exists at only one level (e.g., product-only)
- No traceable chain between intent levels
- No upstream context connections — intent appears in isolation
- ADRP records are draft, expired, revoked, unratified, or lack authority but are treated as active
- Multiple active ADRP records conflict without an explicit resolution

## ADRP protocol conformance

Protocol conformance is an additional confidence dimension, not a prerequisite for strong Intent.

When ADRP artifacts are present, assess:

| Check | Exact conformance |
|-------|-------------------|
| Schema | `schema_version` is `ape-decision-record/v1`; `adrp validate` succeeds when available |
| Lifecycle | Record is effective for the assessed time and not revoked, expired, or superseded |
| Authority | Decision owner, deciders/approvers, and ratification are explicit |
| Autonomy | `proceed`, `always_ask`, and `never` boundaries are usable by agents |
| Evidence expectation | Implementation or Evidence references state what would prove the decision worked |
| Integrity | Canonical fingerprint is present or reproducible |
| Resolution | Scope resolution identifies the applicable record set without unresolved conflicts |

Classify ADRP conformance as:

- **Exact** — deterministic checks pass and the applicable record is authoritative.
- **Reference** — ADRP-shaped or linked records exist, but exact validation, authority, or fingerprints are incomplete.
- **Absent** — no ADRP artifacts. This is not automatically an Intent maturity gap.
- **Invalid** — artifacts claim ADRP conformance but fail schema, lifecycle, conflict, or integrity checks.
- **Unknown** — deterministic validation could not be performed.

## Intent levels

Score which of the 5 levels have explicit intent and whether they form a traceable chain.

| Level | Captures | Direct sources | Indirect indicators |
|-------|----------|----------------|---------------------|
| **Organizational** | Mission, vision, why the team exists | README (mission), `docs/strategy/`, `.github/isee/` | Refs to company OKRs, external strategy docs |
| **Business** | Priorities, outcomes, trade-offs | `.github/copilot-instructions.md` (priorities), ADRs | Linked Jira epics, GitHub Project descriptions |
| **Product** | What to build, for whom, success criteria | Issue templates, `docs/product/`, PR templates | Linked specs, user stories, acceptance criteria |
| **Architecture** | System constraints, quality attributes, boundaries | `ARCHITECTURE.md`, ADRs, `docs/architecture/` | C4 model links, API contract refs |
| **Platform** | Runtime constraints, deployment model, toolchain | Infra config, CI/CD config, `.mcp.json`, linter configs | Platform docs, shared infra repos |

For each level: **State** (Present/Absent/Unknown) and **Source** (Direct = in-repo, Indirect = referenced).

Score on three dimensions:
- **Breadth** — how many of 5 levels have explicit intent
- **Depth** — can intent be traced organizational → platform?
- **Coherence** — do lower-level statements align with higher-level ones?

## Upstream context connections

### Direct (discoverable in-repo)
- GitHub Issues/Projects linked in docs or config
- Cross-repo references (`see also: org/other-repo`, `inherits from:`)
- `.github/isee/context.md` or equivalent
- Work item refs in PR/issue templates (`fixes #`, `AB#`, Jira keys)

### Indirect (referenced — try to follow)
- URLs to external docs (Confluence, Notion, wiki) — fetch if reachable. If unreachable → finding.
- References to org policies ("per security policy X") — can the policy be found?
- Team/stakeholder/external-owner mentions
- Tool names suggesting external intent sources (Jira, ADO, ServiceNow, Aha!)

### Broken connections (key finding)
When the repo says "our architecture docs are on X" but the link is dead or no URL is provided:
> "Upstream intent referenced but not reachable — context chain broken at [citation]."

Do not ask the user to retrieve external content. Either the context flows into the repo (or is reachable from it), or it doesn't.

## Profile-adjusted expectations

| Profile | Description | Threshold |
|---------|-------------|-----------|
| **Lightweight** | Startup, small team | Intent in README suffices. 2-3 explicit statements = strong. 2+ levels. Upstream optional. |
| **Standard** | Established team | Dedicated docs or copilot-instructions section. 5+ explicit statements. 3+ levels. Some upstream connections. |
| **Regulated** | Compliance-heavy | Approved strategy docs or authoritative ADRP records, compliance-linked outcomes. 4+ levels with traceable chain. Upstream → organizational/compliance required. |

## When signals are weak — ask_user template

```
Use ask_user:
  message: "I found limited explicit intent in your repo. A few quick questions:"
  requestedSchema:
    properties:
      priorities:
        type: string
        title: "What are your team's top 2-3 priorities right now?"
        description: "e.g., reliability, shipping speed, cost reduction, security posture"
      outcomes:
        type: string
        title: "How does your team define 'done' for a feature or project?"
      where_intent_lives:
        type: string
        title: "Where does your team document goals and priorities?"
        description: "e.g., README, Confluence, Notion, Jira epics, team meetings, nowhere"
    required: [priorities]
```

Ask only when in-repo signals are insufficient and no reachable external source exists. Never ask the user to fetch content for you.
