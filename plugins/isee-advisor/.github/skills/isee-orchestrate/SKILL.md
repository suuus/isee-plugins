---
name: isee-orchestrate
description: |
  Run a full ISEE assessment: invoke the 4 layer skills, optionally the agents skill, then the report.

  USE FOR: full ISEE assessment, complete maturity scan, multi-phase orchestrate, /isee-advisor assess.

  DO NOT USE FOR: ad-hoc questions (use isee-advise), drift detection (use isee-drift), single layer scans.
user-invocable: true
---

# ISEE Orchestrate

Run the full ISEE assessment pipeline. Invokes the four layer skills in order, the optional agents skill if relevant, then the report skill. Each layer assesses framework maturity and protocol conformance separately. Tracks progress with SQL todos so failures in one phase don't block downstream.

## Procedure

1. Ask the user for their profile via `ask_user` — see [`references/profile.md`](references/profile.md).
2. Seed phase todos + deps — SQL in [`references/pipeline.md`](references/pipeline.md).
3. Inventory canonical artifacts: ADRP decisions, ASRP structures, ISEE projections/manifests, and AERP Evidence. Record which read-only CLIs are available; CLI absence makes deterministic validation Unknown, not failed.
4. Execute each phase: `in_progress` → invoke skill → `done`. Continue on `[INCOMPLETE]` / `[SKIPPED]`.
5. Invoke `isee-assess-intent`.
6. Invoke `isee-assess-structure`.
7. Invoke `isee-assess-execution`.
8. Invoke `isee-assess-evidence`.
9. If `.github/agents/*.agent.md` or `.github/skills/*/SKILL.md` exist, invoke `isee-assess-agents`. Otherwise `[SKIPPED]`.
10. Invoke `isee-assess-report`.

## Examples

- **Standard team with agents:** all 6 phases run; report has per-agent ISEE plus 4 layers.
- **Lightweight startup, no agents:** Phases 1-4 + 6 run; Phase 5 `[SKIPPED]`; report omits agent section.
- **Partial data:** Phase 2 hits unreachable Confluence link → `[INCOMPLETE]` with broken-chain finding; downstream phases run; report notes reduced confidence.
- **Protocol-aware:** ADRP, ASRP, manifest, and AERP artifacts exist → assess exact bindings and integrity without performing execution.

## Troubleshooting

- **Skipped phases inflate the score.** Don't let `[SKIPPED]` phases contribute to the maturity grade.
- **Agent delegates fetching to user.** Wrong — fetch with available tools or record the broken chain.
- **Empty findings.** Mark `[INCOMPLETE]` with one-line reason; don't silently continue.
- **Profile drift.** Confirm the user-selected profile reaches every phase consistently.
- **Protocol tooling absent.** Inspect artifacts, mark deterministic checks Unknown, and continue; never claim a fingerprint or schema is valid without verification.
