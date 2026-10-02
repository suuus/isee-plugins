#!/usr/bin/env python3
"""Synchronize pinned ISEE plugin components from local source repositories."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


PROJECTS = ("adrp", "asrp", "aerp", "isee", "isee-advisor")


def run(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], text=True
    ).strip()


def copy_tree(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sources-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Directory containing adrp, asrp, aerp, isee, and isee-advisor",
    )
    parser.add_argument(
        "--repository-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    args = parser.parse_args()

    root = args.repository_root.resolve()
    plugins = root / "plugins"
    suite = plugins / "isee-suite"
    locks: dict[str, dict[str, str]] = {}

    for project in PROJECTS:
        source = (args.sources_root / project).resolve()
        if not (source / ".git").exists():
            raise SystemExit(f"missing source repository: {source}")
        if run(source, "status", "--porcelain"):
            if project != "adrp":
                raise SystemExit(f"source repository is dirty: {source}")
            unexpected = [
                line
                for line in run(source, "status", "--porcelain").splitlines()
                if line != "?? docs/examples/ADR-TOOLING-TEST.v1.json"
            ]
            if unexpected:
                raise SystemExit(f"source repository is dirty: {source}")

        target = plugins / project
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / "plugin.json", target / "plugin.json")
        copy_tree(source / ".github" / "agents", target / ".github" / "agents")
        copy_tree(source / ".github" / "skills", target / ".github" / "skills")

        locks[project] = {
            "repository": f"https://github.com/suuus/{project}",
            "commit": run(source, "rev-parse", "HEAD"),
            "version": json.loads((source / "plugin.json").read_text())["version"],
        }

    suite_agents = suite / ".github" / "agents"
    suite_skills = suite / ".github" / "skills"
    for path in (suite_agents, suite_skills):
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True)

    for project in PROJECTS:
        source = plugins / project / ".github"
        for agent in (source / "agents").glob("*.agent.md"):
            shutil.copy2(agent, suite_agents / agent.name)
        for skill in (source / "skills").iterdir():
            if skill.is_dir():
                copy_tree(skill, suite_skills / skill.name)

    setup_source = root / "components" / "isee-setup"
    copy_tree(setup_source, suite_skills / "isee-setup")
    lock_text = (
        json.dumps(
            {"schema_version": "isee-plugin-sources/v1", "sources": locks}, indent=2
        )
        + "\n"
    )
    (root / "sources.lock.json").write_text(lock_text)
    (suite / "sources.lock.json").write_text(lock_text)
    suite_scripts = suite / "scripts"
    suite_scripts.mkdir(exist_ok=True)
    for script in ("doctor.py", "install_clis.py"):
        shutil.copy2(root / "scripts" / script, suite_scripts / script)

    setup_skill = suite_skills / "isee-setup"
    (setup_skill / "scripts").mkdir(exist_ok=True)
    (setup_skill / "sources.lock.json").write_text(lock_text)
    for script in ("doctor.py", "install_clis.py"):
        shutil.copy2(root / "scripts" / script, setup_skill / "scripts" / script)

    marketplace_path = root / ".github" / "plugin" / "marketplace.json"
    marketplace = json.loads(marketplace_path.read_text())
    for entry in marketplace["plugins"]:
        if entry["name"] in locks:
            entry["version"] = locks[entry["name"]]["version"]
    marketplace_path.write_text(json.dumps(marketplace, indent=2) + "\n")


if __name__ == "__main__":
    main()
