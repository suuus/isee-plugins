#!/usr/bin/env python3
"""Install the pinned ADRP, ASRP, AERP, and ISEE CLIs into a private venv."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import venv
from pathlib import Path


TOOLS = ("adrp", "asrp", "aerp", "isee")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prefix",
        type=Path,
        default=Path.home() / ".local" / "share" / "isee",
    )
    parser.add_argument(
        "--bin-dir",
        type=Path,
        default=Path.home() / ".local" / "bin",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    lock_path = root / "sources.lock.json"
    if not lock_path.is_file():
        raise SystemExit(f"missing source lock: {lock_path}")
    locks = json.loads(lock_path.read_text())["sources"]
    venv_dir = args.prefix / "venv"
    commands = [
        [
            str(venv_dir / ("Scripts" if os.name == "nt" else "bin") / "python"),
            "-m",
            "pip",
            "install",
            "--upgrade",
            *[
                f"git+{locks[name]['repository']}.git@{locks[name]['commit']}"
                for name in TOOLS
            ],
        ]
    ]

    if args.dry_run:
        print(json.dumps({"venv": str(venv_dir), "commands": commands}, indent=2))
        return

    args.prefix.mkdir(parents=True, exist_ok=True)
    venv.EnvBuilder(with_pip=True, upgrade_deps=True).create(venv_dir)
    for command in commands:
        subprocess.run(command, check=True)

    source_bin = venv_dir / ("Scripts" if os.name == "nt" else "bin")
    args.bin_dir.mkdir(parents=True, exist_ok=True)
    if os.name == "nt":
        print(f"Add {source_bin} to PATH to use: {', '.join(TOOLS)}")
        return

    for tool in TOOLS:
        link = args.bin_dir / tool
        target = source_bin / tool
        if link.exists() or link.is_symlink():
            if link.resolve() != target.resolve():
                raise SystemExit(f"refusing to replace existing command: {link}")
            continue
        link.symlink_to(target)
    print(f"installed {', '.join(TOOLS)}; ensure {args.bin_dir} is on PATH")


if __name__ == "__main__":
    main()
