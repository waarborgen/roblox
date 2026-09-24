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
    "vfx": ("VFX, graphics & rendering", "Particles, shaders, lighting, portalen, raytracing en canvas-rendering."),
    "landscape": ("Landschap, terrain, water & weer", "Terrain-generators, echte kaarten, grotten, oceanen, foliage, dag/nacht en weer."),
    "animation": ("Animatie, IK & rigging", "Animatie-solvers, IK, Blender/Mixamo-pipelines, procedurele animatie en springs."),
    "movement": ("Movement, physics & characters", "Character controllers, ragdolls, destructie, parkour en eigen physics-engines."),
    "vehicles": ("Voertuigen, boten & treinen", "Chassis, suspensie, hover, raketten, drijfvermogen en treinen."),
    "combat": ("Combat, hitboxes & wapens", "Melee-hitboxes, projectielen, guns, lag-compensatie en zones."),
    "ai": ("AI, NPC's & machine learning", "Neurale netwerken, behavior trees, pathfinding, boids en LLM-NPC's."),
    "procgen": ("Procedurele generatie & wiskunde", "Voxels, dungeons, doolhoven, wave function collapse, noise en curves."),
    "networking": ("Networking & replicatie", "Buffer-netcode, IDL-compilers, encryptie en eigen replicatie."),
    "ecs": ("ECS & game-architectuur", "Entity Component Systems en frameworks voorbij Knit."),
    "ui": ("UI & interface", "Reactieve UI, custom tekst, inventories, 2D-engines en mobiele controls."),
    "camera": ("Camera & cutscenes", "Camera-shake, custom camera's, cutscene-tools en timelines."),
    "audio": ("Audio", "3D-audio, occlusie/reverb, adaptieve muziek en radio."),
    "vr": ("VR & motion tracking", "Full-body VR, SteamVR-trackers en webcam-tracking."),
    "data": ("Data, opslag & serialisatie", "DataStores, serialisatie, compressie, state en big numbers."),
    "systems": ("Game-systemen & utilities", "Quests, dialogen, input, trading, admin, signals en meer."),
    "security": ("Security & anticheat", "Hashing, encryptie, logins, permissies, rate limiting en anticheat."),
    "wild": ("Next-level / experimenteel", "Luau-in-Luau, emulators, DOOM, N64, video, Python-in-Luau en game-ports."),
    "apis": ("API's & externe integraties", "Open Cloud, web-API's, Discord, databases en analytics."),
    "aitools": ("AI-tools voor Roblox-development", "MCP-servers, AI-agents en skills die in Studio kunnen bouwen."),
    "tooling": ("Tooling & workflow", "Runtimes, sync-tools, package managers, asset-pipelines, CI en docs."),
    "plugins": ("Studio-plugins", "Handige plugins voor bouwen, terrain, UI en workflow."),
    "learn": ("Leren, open-source games & collecties", "Artikelen, complete open-source games, templates en curated lijsten."),
}


def load():
    with DATA.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
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


def anchor(title):
    """GitHub-stijl anchor voor een kopje."""
    a = title.lower()
    a = "".join(ch for ch in a if ch.isalnum() or ch in " -")
    return a.replace(" ", "-")


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
        "exploits/cheats/executors/spoofers, obfuscators, account-tools en SEO-spamrepos.",
        "",
        "Tip: ⭐ zegt weinig bij nieuwe projecten, veel pareltjes hebben (nog) bijna geen sterren.",
        "",
        f"Totaal: **{len(rows)} repos** in **{len(index)} categorieën**. ⭐ = GitHub-sterren op het moment van verzamelen (sept. 2026).",
        "",
        "## Categorieën",
        "",
    ]
    for key, title, blurb, cat_rows in index:
        readme.append(f"- [{title}](#{anchor(title)}) — **{len(cat_rows)}** repos ([losse pagina](categories/{key}.md))")
    readme.append("")
    for key, title, blurb, cat_rows in index:
        readme += [f"## {title}", "", f"{blurb} ({len(cat_rows)} repos)", "", table(cat_rows), ""]
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
