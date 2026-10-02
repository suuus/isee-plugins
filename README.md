# ISEE Plugins

Install the complete **Intent → Structure → Execution → Evidence** operating
system for GitHub Copilot CLI from one repository.

## Installation

Register the marketplace and install the complete suite:

```bash
copilot plugin marketplace add suuus/isee-plugins
copilot plugin install isee-suite@isee
```

Then select `/agent isee`.

The suite includes:

- `isee` — umbrella workflow for regular Copilot sessions and agentic flows;
- `adrp` — durable, human-ratified Intent;
- `asrp` — Structure records and execution manifests;
- `aerp` — durable, verifiable Evidence;
- `isee-advisor` — maturity, conformance, and drift assessment;
- `isee-setup` — explicit CLI installation and diagnostics.

Browse all available plugins:

```bash
copilot plugin marketplace add suuus/isee-plugins
copilot plugin marketplace browse isee
```

Or install only what you need:

```bash
copilot plugin install adrp@isee
copilot plugin install asrp@isee
copilot plugin install aerp@isee
copilot plugin install isee@isee
copilot plugin install isee-advisor@isee
```

Do not install `isee-suite` together with its individual component plugins;
that would load duplicate agent and skill names.

Direct installation with `copilot plugin install suuus/isee-plugins` is
currently supported by Copilot CLI, but direct repository installs are
deprecated. The marketplace route above is the durable installation path.

## Deterministic CLIs

The plugin provides Copilot agents and skills immediately. The deterministic
Python CLIs remain explicit executables because installing a plugin must not
silently modify the user's machine.

Ask Copilot to use `isee-setup`, or run:

```bash
python scripts/doctor.py
python scripts/install_clis.py --dry-run
python scripts/install_clis.py
```

The installer:

- uses the exact published commits in `sources.lock.json`;
- creates `~/.local/share/isee/venv`;
- links `adrp`, `asrp`, `aerp`, and `isee` into `~/.local/bin`;
- refuses to replace unrelated existing commands.

## First repository

After the CLIs are available:

```bash
isee init
isee doctor
```

For regular Copilot:

```text
@.github/isee/context.md
@.github/isee/execution-manifest.json

Implement the requested change.
```

For the full workflow, use `/agent isee`.

## Product boundaries

- ADRP owns Intent.
- ASRP owns Structure.
- Execution stays external.
- AERP owns Evidence.
- ISEE integrates preflight, Copilot projection, and Evidence evaluation.
- ISEE Advisor assesses maturity and conformance; it does not execute changes.

## Reproducibility

`sources.lock.json` records the exact commit and plugin version for each source
project. Maintainers update the bundle with:

```bash
python scripts/sync_sources.py
python scripts/validate.py
```

The suite is a distribution layer. The profile schemas, CLIs, and normative
documentation remain owned by their source repositories.
