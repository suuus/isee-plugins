# Drift detection — rubric and templates

This module is loaded on-demand by `SKILL.md` when running drift detection.

## When no prior report exists — ask_user template

```
Use ask_user:
  message: "No prior ISEE assessment found (.github/isee-report.md). Would you like to run a full assessment first, or proceed with a baseline-free scan?"
  requestedSchema:
    properties:
      approach:
        type: string
        title: "How to proceed?"
        enum:
          - "Run full assessment first (recommended)"
          - "Scan current state without comparison"
        default: "Run full assessment first (recommended)"
    required: [approach]
```

If "Run full assessment" → hand off to the assess workflow.
If "Scan without comparison" → proceed with current-state-only analysis.

## SQL todo template

```sql
INSERT INTO todos (id, title, description, status) VALUES
  ('drift-intent',    'Drift: Intent layer',    'Re-scan intent signals including intent levels and upstream context', 'pending'),
  ('drift-structure', 'Drift: Structure layer',  'Re-scan structure signals including upstream structural inheritance', 'pending'),
  ('drift-execution', 'Drift: Execution layer',  'Re-scan execution signals including work item traceability', 'pending'),
  ('drift-evidence',  'Drift: Evidence layer',   'Re-scan evidence signals including feedback loop traceability', 'pending'),
  ('drift-agents',    'Drift: Agents (optional)','Re-scan agent ISEE signals if agent definitions detected', 'pending'),
  ('drift-report',    'Drift: Generate report',  'Compare and report including intent levels, context chain, agent changes', 'pending');

INSERT INTO todo_deps (todo_id, depends_on) VALUES
  ('drift-structure', 'drift-intent'),
  ('drift-execution', 'drift-structure'),
  ('drift-evidence',  'drift-execution'),
  ('drift-agents',    'drift-evidence'),
  ('drift-report',    'drift-agents');
```

## Comparison status codes

| Status | Meaning |
|--------|---------|
| ✅ **Improved** | Was Absent/Unknown, now Present |
| ✅ **Maintained** | Was Present, still Present |
| ⚠️ **Regressed** | Was Present, now Absent |
| 🆕 **New signal** | Not in prior report (new file, new config, new pattern) |
| ➖ **Removed** | Prior signal source deleted (file removed, config deleted) |
| 🔄 **Unchanged gap** | Was Absent, still Absent |

## Score change patterns

| Change | Label |
|--------|-------|
| 🟢→🟢 | Maintained strong |
| 🟡→🟢 | Improved to strong |
| 🔴→🟡 | Improving |
| 🟢→🟡 | Regressed |
| 🟡→🔴 | Regressed significantly |
| Same score, different findings | Note what shifted |

## Additional drift dimensions

### Intent levels drift
- Did new intent levels appear? (e.g., architecture intent added)
- Did breadth/depth/coherence change?
- Were upstream context connections added or lost?

### Context chain drift
- Did traceability improve or degrade?
- Were new upstream connections established?
- Did any direct connections become indirect (or vice versa)?

### Protocol conformance drift
- Did an ADRP or ASRP record become effective, expire, get revoked, or become superseded?
- Did any canonical fingerprint change without a corresponding version or supersession relationship?
- Did Intent → Structure or Evidence → Intent/Structure bindings become exact, partial, mismatched, or disappear?
- Did the compiled manifest change entry point, gates, Evidence requirements, or artifact digests?
- Did required Evidence become satisfied, stale, revoked, or invalid?
- Did the learning loop move from Open → Partial → Closed, or regress?

### Agent ISEE drift (if agents present in both assessments)
- Did per-agent ISEE scores change?
- Were new agents added or existing ones removed?
- Did evidence upstream flow improve?
- Did system-level coordination patterns change?
- Were agent packages from distribution systems added or updated?

## Save ask_user template

```
Use ask_user:
  message: "Drift analysis complete. Save results?"
  requestedSchema:
    properties:
      save:
        type: boolean
        title: "Update .github/isee-report.md with current assessment?"
        description: "This becomes the new baseline for future drift detection."
        default: true
    required: [save]
```

If yes, overwrite `.github/isee-report.md` with the full current assessment (not the drift report — the drift report is conversation-only, the baseline is a clean assessment).
