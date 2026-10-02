#!/usr/bin/env python3
"""Verify bundled plugin components byte-for-byte against pinned repositories."""

from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def inventory(root: Path) -> dict[str, str]:
    paths = [root / "plugin.json"]
    paths.extend((root / ".github" / "agents").rglob("*"))
    paths.extend((root / ".github" / "skills").rglob("*"))
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
        if path.is_file()
    }


def main() -> None:
    locks = json.loads((ROOT / "sources.lock.json").read_text())["sources"]
    with tempfile.TemporaryDirectory(prefix="isee-plugin-sources-") as temporary:
        temp = Path(temporary)
        for project, lock in locks.items():
            checkout = temp / project
            subprocess.run(
                [
                    "git",
                    "clone",
                    "--quiet",
                    "--filter=blob:none",
                    lock["repository"],
                    str(checkout),
                ],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(checkout), "checkout", "--quiet", lock["commit"]],
                check=True,
            )
            expected = inventory(checkout)
            actual = inventory(ROOT / "plugins" / project)
            if actual != expected:
                missing = sorted(expected.keys() - actual.keys())
                extra = sorted(actual.keys() - expected.keys())
                changed = sorted(
                    path
                    for path in expected.keys() & actual.keys()
                    if expected[path] != actual[path]
                )
                raise SystemExit(
                    f"{project} differs from {lock['commit']} "
                    f"(missing={missing}, extra={extra}, changed={changed})"
                )
            print(f"{project}: verified {lock['commit']}")


if __name__ == "__main__":
    main()
