# Evidence rubric — full reference

This module is loaded on-demand by `SKILL.md` when assessing the Evidence layer.

## Scan targets

Read these files if they exist:

1. `.github/workflows/*.yml` — test reporting, coverage uploads, status checks, deployment notifications
2. Monitoring config references in code, config, or docs (Datadog, Grafana, App Insights, CloudWatch)
3. Alert definitions in infrastructure files, PagerDuty/OpsGenie config references
4. Test configuration files, coverage thresholds, test reporting formats
5. `.github/copilot-instructions.md` — evidence/reporting sections, "after deploying, verify" patterns
6. `.mcp.json` — monitoring/observability servers configured (datadog-mcp-server, etc.)
7. `README.md` — CI status badges, coverage badges, health indicators
8. `CHANGELOG.md`, release workflows — does the team produce evidence of what shipped?
9. References to Sentry, Bugsnag, Application Insights in config or dependencies
10. `evidence/**/*.json`, `.github/evidence/**/*.json`, deployment evidence directories — AERP records and bundles
11. `.github/isee/execution-manifest.json` — Evidence requirements to evaluate
12. `.github/isee/` evaluation outputs or reports from `isee evaluate`

## Evidence signals

### PRESENT
- CI pipeline that reports test results (not just pass/fail)
- Coverage thresholds enforced in CI
- Monitoring/alerting configured and referenced in docs
- Status badges in README (public evidence of system health)
- Deployment verification steps in CI/CD (smoke tests, health checks after deploy)
- Changelog or release notes that document what shipped and why
- MCP servers for monitoring tools (agents can query observability data)
- Error tracking integrated (errors flow upstream automatically)
- Agent instructions that include "verify after action" patterns
- Valid AERP records with exact ADRP Intent and ASRP Structure bindings
- Evidence subjects, results, criteria, and artifact roles satisfy manifest requirements
- Artifact bytes and record fingerprints verify
- Producer identity, method, timing, environment, and validity are explicit

### ABSENT
- CI runs tests but doesn't report results or coverage
- No monitoring references anywhere in the repo
- No alerting configuration
- Deployments with no verification step
- No changelog or release documentation
- No status badges or health indicators
- Agents with no "check your work" guidance
- Feedback that stays in dashboards but doesn't flow to decisions
- No incident → backlog traceability
- Agent output stays in conversation — never persisted or surfaced to decision-makers
- AERP Evidence is bound to the right Intent but the wrong Structure, or vice versa
- Evidence claims success but does not satisfy the manifest's subject, result, criteria, or artifact requirements
- Evidence artifacts are missing, modified, expired, revoked, or unverifiable

## AERP protocol conformance

Protocol conformance supplements the broader Evidence and feedback-loop assessment.

When AERP records, bundles, or ISEE evaluation outputs exist, assess:

| Check | Exact conformance |
|-------|-------------------|
| Schema | `aerp-evidence-record/v1`; read-only validation succeeds when available |
| Intent binding | Expected ADRP IDs and fingerprints are present |
| Structure binding | Expected ASRP IDs and fingerprints are present |
| Claim matching | Evidence type, subject, accepted result, criteria, and artifact roles satisfy the manifest requirement |
| Provenance | Producer identity, method, invocation, timing, and environment are attributable |
| Integrity | Record and artifact fingerprints verify; paths do not escape the declared artifact root |
| Validity | Evidence is current, not revoked, and supersession is explicit |
| Loop closure | Evidence is evaluated and visibly informs review, backlog, configuration, or a new Intent decision |

Classify AERP conformance as **Exact**, **Reference**, **Absent**, **Invalid**, or **Unknown**. Exact Evidence bindings do not by themselves prove the learning loop is closed.

### UNKNOWN
Much of evidence lives outside the repo. If the repo references external evidence systems (monitoring dashboards, incident tools, etc.), attempt to follow those references. If unreachable, record that as a finding — don't ask the user to go retrieve the content.

## Upstream context connections (Evidence)

### Direct connections (discoverable in-repo)
- CI/CD reporting that flows to external systems (Slack notifications, dashboard URLs in config)
- Post-incident review templates or references to retro processes
- Backlog item patterns: evidence of metric/incident → work item flow (issue templates with "root cause" or "triggered by" fields)
- Agent-produced artifacts that persist and inform decisions (saved reports, generated docs)
- MCP servers connecting to monitoring/observability tools
- Coverage/test trend tracking (not just current run — historical evidence)

### Indirect connections (referenced but external)
- References to dashboards, SLA reports, or KPI tracking
- Mentions of retro/post-mortem processes in docs
- References to incident management systems (PagerDuty, OpsGenie, Statuspage)
- Feedback loop descriptions ("we review metrics monthly", "post-mortems feed the backlog")

### Evidence upstream flow — critical questions
1. **Incident → Backlog**: Do post-incidents create issues/work items?
2. **Metrics → Priorities**: Are there references to data-driven priority changes?
3. **Agent output → Team decisions**: Do agent-produced reports get referenced in subsequent changes?
4. **Production → Configuration**: Do monitoring signals lead to infrastructure/config updates?

## Profile-adjusted expectations

| Profile | Description | Threshold |
|---------|-------------|-----------|
| **Lightweight** | Startup, small team | CI reporting pass/fail + basic error tracking. Feedback loop can be informal. Upstream flow via conversation acceptable. |
| **Standard** | Established team | Coverage thresholds, monitoring, alerting, deployment verification, changelog. Feedback flows to backlog. Evidence from agents persists. Some upstream traceability. |
| **Regulated** | Compliance-heavy | Audit-grade AERP or equivalent evidence trails, exact Intent/Structure traceability, mandatory post-incident reviews, compliance reporting, SLA monitoring, and demonstrable feedback into decisions. |

## When signals are weak — ask_user template

```
Use ask_user:
  message: "Evidence signals often live in external tools. A few questions:"
  requestedSchema:
    properties:
      monitoring:
        type: string
        title: "What monitoring/observability tools does your team use?"
        enum:
          - "Datadog / Grafana / Prometheus"
          - "Azure Monitor / App Insights"
          - "AWS CloudWatch"
          - "Basic (just CI status)"
          - "None"
          - "Other"
        default: "Basic (just CI status)"
      alerting:
        type: string
        title: "How are you alerted when something goes wrong?"
        enum:
          - "Automated alerts (PagerDuty, OpsGenie, etc.)"
          - "CI failure notifications"
          - "Manual checking"
          - "We find out from users"
        default: "CI failure notifications"
      feedback_to_decisions:
        type: string
        title: "Does production feedback change your next decisions?"
        description: "e.g., post-incident reviews lead to backlog items, metrics drive priorities"
        enum:
          - "Yes — structured process (retros, post-mortems → action items)"
          - "Sometimes — ad hoc"
          - "Rarely — we react but don't systematically learn"
        default: "Sometimes — ad hoc"
    required: [monitoring]
```

Ask only when in-repo signals are insufficient and no reachable external source exists. Never ask the user to fetch content for you.
