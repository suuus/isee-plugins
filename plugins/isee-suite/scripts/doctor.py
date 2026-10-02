#!/usr/bin/env python3
"""Check availability and versions of the complete ISEE toolchain."""

from __future__ import annotations

import json
import shutil
import subprocess


TOOLS = ("adrp", "asrp", "aerp", "isee")


def main() -> None:
    results = []
    healthy = True
    for tool in TOOLS:
        path = shutil.which(tool)
        if not path:
            healthy = False
            results.append({"tool": tool, "available": False})
            continue
        process = subprocess.run(
            [path, "--version"], capture_output=True, text=True, check=False
        )
        healthy &= process.returncode == 0
        results.append(
            {
                "tool": tool,
                "available": True,
                "path": path,
                "version": (process.stdout or process.stderr).strip(),
                "healthy": process.returncode == 0,
            }
        )
    print(json.dumps({"healthy": healthy, "tools": results}, indent=2))
    raise SystemExit(0 if healthy else 1)


if __name__ == "__main__":
    main()
