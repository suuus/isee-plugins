# Security Policy

Do not report vulnerabilities through a public issue. Use
[GitHub private vulnerability reporting](https://github.com/suuus/isee-plugins/security/advisories/new).

Include the affected plugin, source commit, installation path, reproduction
steps, and potential impact.

## Trust boundaries

- Plugin installation loads agent and skill instructions.
- CLI installation is separate, explicit, and pinned to published commits.
- The installer creates a private virtual environment and refuses to replace
  unrelated commands.
- Fingerprints provide local integrity, not producer authentication or
  cryptographic signatures.
- Execution and deployment remain external to this repository.

Only the latest published version is supported.
