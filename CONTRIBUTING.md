# Contributing to ISEE Plugins

ISEE Plugins is a distribution repository. Normative standards, CLI behavior,
agents, and specialist skills belong in their source repositories:

- [ADRP](https://github.com/suuus/adrp)
- [ASRP](https://github.com/suuus/asrp)
- [AERP](https://github.com/suuus/aerp)
- [ISEE](https://github.com/suuus/isee)
- [ISEE Advisor](https://github.com/suuus/isee-advisor)

Make substantive changes there first. Then update this bundle:

```bash
python scripts/sync_sources.py
python scripts/validate.py
python scripts/verify_sources.py
```

Distribution-specific changes—installation, marketplace metadata, source
locking, setup tooling, and packaging—belong directly in this repository.

Before opening a pull request:

1. Keep source commits pinned in `sources.lock.json`.
2. Do not hand-edit generated agents or skills under `plugins/`.
3. Update `CHANGELOG.md`.
4. Test marketplace and suite installation with an isolated `COPILOT_HOME`.
5. Confirm the CLI installer with `--dry-run`.
