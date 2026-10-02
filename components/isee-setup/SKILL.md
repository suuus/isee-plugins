---
name: isee-setup
description: |
  Set up or diagnose the complete ISEE toolchain after installing the isee-suite plugin.

  USE FOR: install ISEE CLIs, check ISEE installation, initialize ISEE in a repository, explain plugin setup.

  DO NOT USE FOR: silently installing software, running deployments, approving decisions, or fabricating Evidence.
user-invocable: true
---

# Set Up ISEE

Use the installed suite for Copilot guidance immediately. The deterministic
`adrp`, `asrp`, `aerp`, and `isee` CLIs are separate executables.

## Procedure

1. Resolve paths relative to this `SKILL.md` and run
   `python scripts/doctor.py`, or check each command with `adrp --version`,
   `asrp --version`, `aerp --version`, and `isee --version`.
2. If tools are missing, explain that installation changes the user's machine
   and request explicit approval.
3. After approval, run the skill-local `python scripts/install_clis.py`. It
   creates a private virtual environment under `~/.local/share/isee` and links
   commands into `~/.local/bin` without replacing unrelated existing commands.
4. Run the doctor again.
5. For a repository, use `isee init`, then explain the generated files before
   running any preflight.

## Boundaries

- Plugin installation loads agents and skills; it does not silently install
  Python packages.
- CLI installation is pinned to `sources.lock.json`.
- `isee preflight` and `isee evaluate` are explicit user workflows.
- Execution and deployment remain external to the ISEE plugin.
