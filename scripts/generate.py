#!/usr/bin/env python3
"""Genereert README.md en categories/*.md uit data/repos.tsv.

Gebruik:  python3 scripts/generate.py
Nieuwe repo toevoegen: voeg een regel toe aan data/repos.tsv en draai dit script opnieuw.
"""
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "repos.tsv"
EXTRA = ROOT / "data" / "extra.tsv"
SIGNALS = ROOT / "data" / "signals.tsv"
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


def load(path=DATA):
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
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


def load_signals():
    if not SIGNALS.exists():
        return {}
    with SIGNALS.open(encoding="utf-8") as f:
        return {r["repo"].lower(): r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)}


def score(r, sig, curated):
    """Hoe belangrijk een repo is: sterren wegen het zwaarst, dan forks, recente activiteit en handcuratie."""
    s = sig.get(r["repo"].lower(), {})
    forks = int(s.get("forks") or 0)
    pushed = s.get("pushed") or ""
    v = 3 * math.log10(r["stars"] + 1) + 1.2 * math.log10(forks + 1)
    v += 1.0 if pushed >= "2025-09" else 0.5 if pushed >= "2024-09" else 0
    v += 2.0 if r["repo"].lower() in curated else 0
    v += 0.3 if s.get("license") and s.get("license") != "NOASSERTION" else 0
    return v


def top_table(rows, sig, curated, n):
    lines = ["| # | Repo | ⭐ | 🍴 | Laatst actief | Wat het doet |", "|---:|---|---:|---:|---|---|"]
    ranked = sorted(rows, key=lambda r: -score(r, sig, curated))[:n]
    for i, r in enumerate(ranked, 1):
        s = sig.get(r["repo"].lower(), {})
        mark = " ✋" if r["repo"].lower() in curated else ""
        lines.append(f"| {i} | [{r['repo']}](https://github.com/{r['repo']}){mark} | {r['stars']} | "
                     f"{s.get('forks', '?')} | {(s.get('pushed') or '?')[:7]} | {r['note']} |")
    return "\n".join(lines)


def write_highlights(rows, extra, index):
    """BELANGRIJKSTE.md: de belangrijkste repos uit de hele collectie (gecureerd + index)."""
    sig = load_signals()
    curated = {r["repo"].lower() for r in rows}
    everything = rows + extra
    fresh = [r for r in everything
             if (sig.get(r["repo"].lower(), {}).get("created") or "") >= "2025-09"
             and (sig.get(r["repo"].lower(), {}).get("pushed") or "") >= "2026-03"]
    page = [
        "# Belangrijkste Roblox-repos ⭐",
        "",
        f"De belangrijkste projecten uit alle **{len(everything)}** repos van deze collectie, gerangschikt op belang:",
        "sterren wegen het zwaarst, daarna forks (🍴), recente activiteit, een open-source licentie en of de repo",
        "handgecureerd is (✋ = handgecureerd, met Nederlandse uitleg).",
        "",
        "- [Top 150 overall](#top-150-overall)",
        "- [Nieuw en actief (sinds sept. 2025)](#nieuw-en-actief-sinds-sept-2025)",
    ]
    page += [f"- [{title}](#{anchor(title)})" for key, title, *_ in index]
    page += ["", "## Top 150 overall", "", top_table(everything, sig, curated, 150), ""]
    page += ["## Nieuw en actief (sinds sept. 2025)", "",
             "Projecten die in het afgelopen jaar zijn gestart en het afgelopen halfjaar nog zijn bijgewerkt.", "",
             top_table(fresh, sig, curated, 100), ""]
    for key, title, blurb, cat_rows, cat_extra in index:
        page += [f"## {title}", "", f"{blurb} Top 30 van {len(cat_rows) + len(cat_extra)} "
                 f"([alles in deze categorie](categories/{key}.md)).", "",
                 top_table(cat_rows + cat_extra, sig, curated, 30), ""]
    page += ["[← Terug naar overzicht](README.md)", ""]
    (ROOT / "BELANGRIJKSTE.md").write_text("\n".join(page), encoding="utf-8")


def anchor(title):
    """GitHub-stijl anchor voor een kopje."""
    a = title.lower()
    a = "".join(ch for ch in a if ch.isalnum() or ch in " -")
    return a.replace(" ", "-")


def main():
    rows = load()
    curated = {r["repo"].lower() for r in rows}
    extra = [r for r in load(EXTRA) if r["repo"].lower() not in curated]
    OUT_DIR.mkdir(exist_ok=True)
    index = []
    for key, (title, blurb) in CATEGORIES.items():
        cat_rows = [r for r in rows if r["category"] == key]
        cat_extra = [r for r in extra if r["category"] == key]
        if not cat_rows and not cat_extra:
            continue
        page = f"# {title}\n\n{blurb}\n\n## Handgecureerd ({len(cat_rows)})\n\n{table(cat_rows)}\n"
        if cat_extra:
            page += (
                f"\n## Uitgebreide index ({len(cat_extra)})\n\n"
                "Automatisch verzameld en gefilterd (geen exploits/cheats/spam, geen klonen of spamfarms), "
                "categorie op trefwoorden. Omschrijving = originele GitHub-omschrijving; "
                "\"(uit README)\" = eerste alinea van de README (repo had geen omschrijving); "
                "\"(geen omschrijving op GitHub)\" = opgenomen op basis van een duidelijke reponaam.\n\n"
                f"{table(cat_extra)}\n"
            )
        page += "\n[← Terug naar overzicht](../README.md)\n"
        (OUT_DIR / f"{key}.md").write_text(page, encoding="utf-8")
        index.append((key, title, blurb, cat_rows, cat_extra))

    readme = [
        "# Roblox Hidden Gems 💎",
        "",
        "Privé-collectie van **unieke, minder bekende open-source Roblox-projecten** van publieke GitHub:",
        "API's, VFX, game mechanics, networking, AI, tooling en meer.",
        "",
        "**Bewust níet opgenomen:** standaard Roblox-functionaliteit, de bekende basics die iedereen al gebruikt,",
        "exploits/cheats/executors/spoofers, obfuscators, account-tools en SEO-spamrepos.",
        "",
        "👉 **[De belangrijkste repos](BELANGRIJKSTE.md)**: top 150, nieuwe actieve projecten en de top 30 per categorie.",
        "",
        "Tip: ⭐ zegt weinig bij nieuwe projecten, veel pareltjes hebben (nog) bijna geen sterren.",
        "",
        f"Totaal: **{len(rows) + len(extra)} repos** in **{len(index)} categorieën**: "
        f"**{len(rows)}** handgecureerd (met Nederlandse uitleg, hieronder) + **{len(extra)}** in de uitgebreide index "
        "(automatisch verzameld en gefilterd, op de categoriepagina's). ⭐ = GitHub-sterren op het moment van verzamelen (sept. 2026).",
        "",
        "## Categorieën",
        "",
    ]
    for key, title, blurb, cat_rows, cat_extra in index:
        readme.append(
            f"- [{title}](#{anchor(title)}) — **{len(cat_rows)}** gecureerd + **{len(cat_extra)}** in index "
            f"([volledige pagina](categories/{key}.md))"
        )
    readme.append("")
    for key, title, blurb, cat_rows, cat_extra in index:
        more = f" — nog **{len(cat_extra)}** meer in de [uitgebreide index](categories/{key}.md#uitgebreide-index-{len(cat_extra)})" if cat_extra else ""
        readme += [f"## {title}", "", f"{blurb} ({len(cat_rows)} gecureerd{more})", "", table(cat_rows), ""]
    readme += [
        "## Uitbreiden",
        "",
        "1. Voeg een regel toe aan [`data/repos.tsv`](data/repos.tsv) (`categorie<TAB>eigenaar/repo<TAB>sterren<TAB>omschrijving`).",
        "2. Draai `python3 scripts/generate.py` — README en categoriepagina's worden opnieuw gegenereerd.",
        "3. De uitgebreide index (`data/extra.tsv`) wordt gebouwd met `python3 scripts/build_extra.py <pool.json>` uit opgeslagen zoekresultaten.",
        "4. Omschrijvingen uit README's (voor repos zonder GitHub-omschrijving) komen uit `python3 scripts/summarize_readmes.py <pool.json> <readme-map>`; repos waarvan de README een exploit/cheat blijkt, staan in `data/readme_blocked.txt` en worden overgeslagen.",
        "",
        "> Let op: controleer altijd de licentie van een repo voordat je code in je eigen game gebruikt.",
        "",
    ]
    (ROOT / "README.md").write_text("\n".join(readme), encoding="utf-8")
    write_highlights(rows, extra, index)
    print(f"{len(rows)} gecureerd + {len(extra)} index = {len(rows) + len(extra)} repos, {len(index)} categorieën gegenereerd")


if __name__ == "__main__":
    main()
