#!/usr/bin/env python3
"""Genereert README.md en categories/*.md uit data/repos.tsv.

Gebruik:  python3 scripts/generate.py
Nieuwe repo toevoegen: voeg een regel toe aan data/repos.tsv en draai dit script opnieuw.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "repos.tsv"
OUT_DIR = ROOT / "categories"

# Volgorde en titels van de categorieën
CATEGORIES = {
    "vfx": ("VFX, graphics & rendering", "Effecten, shaders, licht, water, weer en canvas-rendering."),
    "networking": ("Networking & replicatie", "Buffer-netcode, IDL-compilers, encryptie en eigen replicatie."),
    "ecs": ("ECS & game-architectuur", "Entity Component Systems en frameworks voorbij Knit."),
    "combat": ("Combat, hitboxes & projectielen", "Melee-hitboxes, projectielen, lag-compensatie en spatial queries."),
    "movement": ("Movement, physics & characters", "Character controllers, IK, ragdolls, voertuigen, destructie en physics."),
    "ai": ("AI, NPC's & machine learning", "Neurale netwerken, behavior trees, pathfinding en matchmaking."),
    "procgen": ("Procedurele generatie & wereld", "Voxels, terrain, wave function collapse en ruimtelijke datastructuren."),
    "ui": ("UI & animatie", "Reactieve UI, springs, custom tekst, inventories en mobiele controls."),
    "camera": ("Camera & cutscenes", "Camera-shake, custom camera's en cinematics."),
    "data": ("Data, opslag & state", "DataStores, serialisatie, state management en big numbers."),
    "wild": ("Next-level / experimenteel", "Luau-in-Luau, emulators, DOOM, parsers en andere gekke projecten."),
    "apis": ("API's & externe integraties", "Open Cloud, web-API's, Discord, databases, analytics en AI-agents."),
    "tooling": ("Tooling & workflow", "Runtimes, package managers, asset-pipelines, deployment en docs."),
    "security": ("Security & anticheat", "Hashing, logins, captcha's, permissies en anticheat."),
    "systems": ("Kant-en-klare game-systemen & plugins", "Quests, placement, dialogen, sirenes en handige plugins."),
    "learn": ("Leren & collecties", "Artikelen, code-collecties, open-source games en andere curated lijsten."),
}


def load():
    with DATA.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for r in rows:
        r["stars"] = int(r["stars"])
        if r["category"] not in CATEGORIES:
            raise SystemExit(f"Onbekende categorie '{r['category']}' voor {r['repo']}")
    return rows


def table(rows):
    lines = ["| Repo | ⭐ | Wat het doet |", "|---|---:|---|"]
    for r in sorted(rows, key=lambda r: -r["stars"]):
        lines.append(f"| [{r['repo']}](https://github.com/{r['repo']}) | {r['stars']} | {r['note']} |")
    return "\n".join(lines)


def main():
    rows = load()
    OUT_DIR.mkdir(exist_ok=True)
    index = []
    for key, (title, blurb) in CATEGORIES.items():
        cat_rows = [r for r in rows if r["category"] == key]
        if not cat_rows:
            continue
        (OUT_DIR / f"{key}.md").write_text(
            f"# {title}\n\n{blurb}\n\n{table(cat_rows)}\n\n[← Terug naar overzicht](../README.md)\n",
            encoding="utf-8",
        )
        index.append((key, title, blurb, cat_rows))

    readme = [
        "# Roblox Hidden Gems 💎",
        "",
        "Privé-collectie van **unieke, minder bekende open-source Roblox-projecten** van publieke GitHub:",
        "API's, VFX, game mechanics, networking, AI, tooling en meer.",
        "",
        "**Bewust níet opgenomen:** standaard Roblox-functionaliteit, de bekende basics die iedereen al gebruikt,",
        "exploits/cheats/executors, obfuscators, account-tools en spam-repos.",
        "",
        f"Totaal: **{len(rows)} repos** in **{len(index)} categorieën**. ⭐ = GitHub-sterren op het moment van verzamelen (sept. 2026).",
        "",
        "## Categorieën",
        "",
    ]
    for key, title, blurb, cat_rows in index:
        readme.append(f"- [{title}](categories/{key}.md) ({len(cat_rows)}) — {blurb}")
    readme += [
        "",
        "## Top picks per categorie",
        "",
        "De drie met de meeste sterren per categorie. Klik op een categorie voor de volledige lijst.",
        "",
    ]
    for key, title, blurb, cat_rows in index:
        top = sorted(cat_rows, key=lambda r: -r["stars"])[:3]
        readme.append(f"### [{title}](categories/{key}.md)")
        readme.append("")
        for r in top:
            readme.append(f"- [{r['repo']}](https://github.com/{r['repo']}) — {r['note']}")
        readme.append("")
    readme += [
        "## Uitbreiden",
        "",
        "1. Voeg een regel toe aan [`data/repos.tsv`](data/repos.tsv) (`categorie<TAB>eigenaar/repo<TAB>sterren<TAB>omschrijving`).",
        "2. Draai `python3 scripts/generate.py` — README en categoriepagina's worden opnieuw gegenereerd.",
        "",
        "> Let op: controleer altijd de licentie van een repo voordat je code in je eigen game gebruikt.",
        "",
    ]
    (ROOT / "README.md").write_text("\n".join(readme), encoding="utf-8")
    print(f"{len(rows)} repos, {len(index)} categorieën gegenereerd")


if __name__ == "__main__":
    main()
