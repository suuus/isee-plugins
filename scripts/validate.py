#!/usr/bin/env python3
"""Validate the ISEE plugin marketplace and bundled components."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"^[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?$")


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def validate_plugin(path: Path) -> tuple[set[str], set[str]]:
    manifest = load(path / "plugin.json")
    name = manifest["name"]
    if not NAME.fullmatch(name) or "--" in name or ".." in name:
        raise ValueError(f"invalid plugin name: {name}")

    agents_dir = path / manifest["agents"]
    skills_dir = path / manifest["skills"]
    agents = {item.stem.removesuffix(".agent") for item in agents_dir.glob("*.agent.md")}
    skills = {item.parent.name for item in skills_dir.glob("*/SKILL.md")}
    if not agents:
        raise ValueError(f"{name}: no agents")
    if not skills:
        raise ValueError(f"{name}: no skills")

    for skill_file in skills_dir.glob("*/SKILL.md"):
        text = skill_file.read_text()
        if not text.startswith("---\n"):
            raise ValueError(f"{skill_file}: missing frontmatter")
        frontmatter = text.split("---", 2)[1]
        for field in ("name:", "description:"):
            if field not in frontmatter:
                raise ValueError(f"{skill_file}: missing {field[:-1]}")
    return agents, skills


def main() -> None:
    marketplace = load(ROOT / ".github" / "plugin" / "marketplace.json")
    entries = marketplace["plugins"]
    names = [entry["name"] for entry in entries]
    if len(names) != len(set(names)):
        raise ValueError("duplicate marketplace plugin names")

    components: dict[str, tuple[set[str], set[str]]] = {}
    for entry in entries:
        path = ROOT / entry["source"]
        manifest = load(path / "plugin.json")
        if manifest["name"] != entry["name"]:
            raise ValueError(f"marketplace name mismatch: {entry['name']}")
        if manifest["version"] != entry["version"]:
            raise ValueError(f"marketplace version mismatch: {entry['name']}")
        components[entry["name"]] = validate_plugin(path)

    suite_agents, suite_skills = components["isee-suite"]
    expected_agents: set[str] = set()
    expected_skills = {"isee-setup"}
    for name, (agents, skills) in components.items():
        if name == "isee-suite":
            continue
        expected_agents |= agents
        expected_skills |= skills
    if suite_agents != expected_agents:
        raise ValueError("suite agents differ from individual plugins")
    if suite_skills != expected_skills:
        raise ValueError("suite skills differ from individual plugins plus isee-setup")
    setup = ROOT / "plugins" / "isee-suite" / ".github" / "skills" / "isee-setup"
    for relative in (
        "sources.lock.json",
        "scripts/doctor.py",
        "scripts/install_clis.py",
    ):
        if not (setup / relative).is_file():
            raise ValueError(f"isee-setup missing resource: {relative}")

    locks = load(ROOT / "sources.lock.json")["sources"]
    for project, lock in locks.items():
        if not re.fullmatch(r"[0-9a-f]{40}", lock["commit"]):
            raise ValueError(f"{project}: invalid commit lock")
        remote_refs = subprocess.check_output(
            ["git", "ls-remote", lock["repository"]], text=True
        ).splitlines()
        if lock["commit"] not in {line.split()[0] for line in remote_refs}:
            raise ValueError(f"{project}: locked commit is not published")

    root_manifest = load(ROOT / "plugin.json")
    suite_manifest = load(ROOT / "plugins" / "isee-suite" / "plugin.json")
    for field in (
        "name",
        "description",
        "version",
        "author",
        "homepage",
        "repository",
        "license",
        "keywords",
    ):
        if root_manifest[field] != suite_manifest[field]:
            raise ValueError(f"root direct-install manifest differs on {field}")
    print(
        f"valid marketplace: {len(entries)} plugins, "
        f"{len(suite_agents)} agents, {len(suite_skills)} skills"
    )


if __name__ == "__main__":
    main()
