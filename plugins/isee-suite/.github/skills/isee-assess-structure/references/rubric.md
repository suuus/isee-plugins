# Structure rubric — full reference

This module is loaded on-demand by `SKILL.md` when assessing the Structure layer.

## Scan targets

Read these files if they exist:

1. `.mcp.json` — tool scoping (read-only vs read+write), server boundaries. **Read and assess only — do not offer to configure or add MCP servers.**
2. `.github/workflows/*.yml`, `azure-pipelines.yml`, `Jenkinsfile` — automated gates, required checks, deployment approvals
3. Branch protection rules — required reviews, status checks, branch rules (ask user if not visible from repo)
4. `SECURITY.md`, `.github/dependabot.yml`, CodeQL config, secret scanning
5. `.github/copilot-instructions.md` — constraint sections, "do not" rules, guardrails
6. `Dockerfile`, Terraform/Bicep files, Kubernetes manifests — cost limits, resource boundaries, scaling constraints
7. `.eslintrc`, `.prettierrc`, `tsconfig.json` (strict mode), `Cargo.toml` (deny warnings) — codified quality standards
8. Azure/AWS budget alerts, resource quotas, rate limiting config
9. `.npmrc`, `package.json` (engines, overrides), lockfile presence
10. `.github/structures/**/*.json`, `structures/**/*.json`, `docs/structures/**/*.json` — ASRP records
11. `.github/isee/execution-manifest.json` — compiled Structure contract for execution
12. Architecture/API/policy/workflow artifacts referenced by ASRP records

## Structure signals

### PRESENT
- Tool scoping in `.mcp.json` (not just `"tools": ["*"]` everywhere)
- CI checks that enforce quality gates (tests, coverage thresholds, linting)
- Required PR reviews or approval gates
- Security scanning in CI pipeline
- Explicit cost/resource boundaries in infrastructure config
- Dependency update policies (Dependabot, Renovate)
- Strict compiler/linter settings (treating warnings as errors)
- Agent guardrails in copilot-instructions.md ("do not merge", "do not deploy")
- Explicit actors, ownership, components, responsibilities, interfaces, dependencies, and trust boundaries
- Effective ASRP records with exact ADRP Intent bindings
- Compiled execution manifest with selected entry point, dependency-expanded elements, required gates, and Evidence obligations

### ABSENT
- `.mcp.json` with all servers at `"tools": ["*"]` (no scoping)
- No CI checks or only trivial checks (build-only, no quality gates)
- No branch protection
- No security scanning configured
- Infrastructure with no resource limits
- No linting or formatting enforcement
- Copilot instructions with no constraint section
- No dependency management policy
- No connection to upstream structural constraints — structure appears entirely local with no organizational inheritance
- Ownership and component boundaries are inferred only from execution activity
- ASRP or manifest fingerprints do not match their referenced records
- Required gates or Evidence obligations disappear during manifest compilation

## ASRP protocol conformance

Protocol conformance supplements the Structure maturity score.

When ASRP or execution-manifest artifacts are present, assess:

| Check | Exact conformance |
|-------|-------------------|
| Schema | `ape-structure-record/v1` and `isee-execution-manifest/v1`; read-only validation succeeds when available |
| Lifecycle | Applicable Structure is effective and not revoked, expired, or superseded |
| Intent binding | Each applicable ADRP record is referenced by exact decision ID and fingerprint |
| Topology | Actors, elements, ownership, responsibilities, dependencies, interfaces, and boundaries are explicit |
| Execution contract | Entry point, dependency closure, and required blocking/advisory gates are compiled |
| Evidence contract | Evidence requirements identify type, subject, accepted result, artifact roles, and criteria where applicable |
| Artifact integrity | Referenced architecture, policy, IaC, workflow, or API artifacts remain under the declared root and match digests |
| Manifest integrity | Manifest fingerprint is present or reproducible |

Classify ASRP conformance as **Exact**, **Reference**, **Absent**, **Invalid**, or **Unknown**. Absence does not automatically make informal Structure weak.

### UNKNOWN
When signals are ambiguous or external, attempt to follow external constraint references (compliance policies, org rulesets) using available tools. If unreachable, record as a finding — don't ask the user to go retrieve the content.

## Upstream context connections (Structure)

### Direct connections (discoverable in-repo)
- Shared CI templates referenced from external repos (e.g., `uses: org/.github/workflows/shared.yml`)
- Org-level rulesets inherited (GitHub org settings, references in docs)
- Shared linting/formatting configs extended from packages (`extends: @org/eslint-config`)
- Infrastructure modules sourced from shared repos (Terraform modules, Bicep registries)
- Agent context distributed via packaging/distribution systems — these count as **remote distribution** of structure/guardrails. Look for package manifests, policy files, or installed module directories that indicate constraints are centrally managed.

### Indirect connections (referenced but external)
- References to compliance policies ("per SOC2 requirements", "as defined in security policy")
- Platform team constraints mentioned but not codified locally
- External approval workflows (ServiceNow, change management systems)
- Shared infrastructure constraints referenced in docs

**Note:** Structure from a remote distribution system (agent packaging/registry) is a **positive signal** — it means guardrails are centrally managed and consistently applied.

## Profile-adjusted expectations

| Profile | Description | Threshold |
|---------|-------------|-----------|
| **Lightweight** | Startup, small team | Basic CI checks + linting sufficient. Informal constraints documented somewhere. Upstream connections optional. |
| **Standard** | Established team | CI with quality gates, branch protection, tool scoping, security scanning, documented constraints. Some upstream structural inheritance expected (shared CI, org policies). |
| **Regulated** | Compliance-heavy | Policy-as-code, mandatory approval gates, authoritative ASRP or equivalent records, audit-grade security scanning, cost controls, and traceable organizational/compliance constraints. |

## When signals are weak — ask_user template

```
Use ask_user:
  message: "Some structure signals may live outside the repo. A few questions:"
  requestedSchema:
    properties:
      branch_protection:
        type: string
        title: "Do you have branch protection rules enabled?"
        enum: ["Yes — required reviews + status checks", "Yes — basic (reviews only)", "No", "Not sure"]
        default: "Not sure"
      security_scanning:
        type: string
        title: "Do you use security scanning tools?"
        enum: ["Yes — in CI pipeline", "Yes — external tool (Snyk, SonarCloud, etc.)", "No", "Not sure"]
        default: "Not sure"
      cost_guardrails:
        type: string
        title: "Do you have cost or resource limits in place?"
        enum: ["Yes — budget alerts / resource quotas", "Informal limits", "No", "Not applicable"]
        default: "Not sure"
    required: [branch_protection]
```

Ask only when in-repo signals are insufficient and no reachable external source exists. Never ask the user to fetch content for you.
