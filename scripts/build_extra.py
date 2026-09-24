#!/usr/bin/env python3
"""Bouwt data/extra.tsv (uitgebreide index) uit een pool met GitHub-zoekresultaten.

Gebruik:  python3 scripts/build_extra.py pad/naar/pool.json

De pool is een JSON-object {repo_lowercase: {repo, stars, desc, topics, lang, fork, archived, created}}.
Elke repo wordt gefilterd (geen exploits/cheats/spam, wel Roblox-relevant) en automatisch
in een categorie geplaatst op basis van naam, omschrijving en topics.
Repos die al in data/repos.tsv (de handmatig gecureerde lijst) staan, worden overgeslagen.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURATED = ROOT / "data" / "repos.tsv"
OUT = ROOT / "data" / "extra.tsv"

# Moet over Roblox/Luau gaan
RELEVANT = re.compile(
    r"roblox|rblx|\brbx|rbxts|\bluau\b|\broact\b|roblox-ts|\bwally\b|\blune\b|robloxstudio|"
    r"\bknit\b|\bfusion\b|\bvide\b|\bjecs\b|datastore|\bobby\b",
    re.I,
)

# Uitsluiten: exploits, cheats, account-/botting-tools, spam enz.
BLOCK = re.compile(
    r"exploit|execut(or|er)\b|\binject|aimbot|aim ?lock|silent ?aim|\besp\b|wall ?hack|triggerbot|cheat|"
    r"\bhack(s|ed|ing|er)?\b|script ?hub|\bhub\b|keyless|key ?system|no ?key|spoof|bypass|unlocker|"
    r"fps ?unlock|bootstrap|launcher|fflag|fast ?flag|cookie|stealer|grabber|token ?log|ip ?log|phish|"
    r"\brat\b|sniper|snipe|botter|botting|follow ?bot|visit ?bot|group ?join|account ?(gen|creat|manag|check|switch)|"
    r"multi ?(instance|account|roblox)|checker|mass ?(report|upload|unfollow|friend|message)|auto ?-?farm|"
    r"\bmacro|anti ?-?afk|\bafk\b|auto ?-?click|clicker|obfusc|deobf|decompil|dumper|\bdump\b|saveinstance|"
    r"save ?instance|uncopylock|remote ?spy|remotespy|\bdex\b|revival|\brcc\b|robux|rolimons|limiteds?\b|"
    r"trade ?bot|\bugc ?(sniper|bot)|free ?robux|undetect|synapse|\bkrnl\b|fluxus|arceus|solara|hydrogen|"
    r"loadstring|httpget|offsets?\b|\bdll\b|\bcheat ?engine|kernel|vulnerab|crash(er)?\b|\bnuke|lag ?switch|"
    r"fe ?bypass|\bfe ?script|filtering ?enabled ?bypass|\bskid|\bgui script|\bmod ?menu|godmode|infinite ?(yield|jump|money)|"
    r"fix for windows|direct download|install steps|download link|\bcrack|keygen|\bpatcher\b|\bwin(dows)? 1[01]\b|"
    r"pastebin|self ?-?bot|\bfly ?(script|hack|gui)|noclip|teleport ?script|\bkill ?(all|aura)|dynamic-link|game client|\bloggers? (in|for) |fake ?(vr|lag|ping|player|admin)|creates? (roblox )?accounts|ally ?(bot|request)|\bmass\b|\bscrap(e|er|ing)\b|password|discord\.gg|pirat|afk(er)?\b|all games|universal ?scripts?|the script for|scripts? for (the )?(experience|game)|roblox-?like client|play (old|classic) (games|roblox)|old roblox|\bbackup of|\bscripts? ?(20\d\d|edition|pack)|\(20\d\d edition\)|roblox ?scripts?\b|unlock ?all|spammer|\bspam\b|unblocker|server ?(joiner|hop|finder)|re-?join|brainrot|\bfling|\bdelta\b|multi ?-?acc|multiple ?(sessions|instances|clients|accounts)|несколько|zapret|обход|\bgamepass(es)? ?free|\bfree ?(gamepass|items|ugc)|\bautomation ?tool|\bauto ?(buy|sell|rejoin|join|play)|\bbot for\b|voice ?chat ?guide|clothing ?(guide|store|farm)|\bpremium\b ?free|giveaway|\bscam|\bbeam(ing|er)\b",
    re.I,
)
# Game-specifieke cheatscripts ("Blox Fruits script", "Da Hood auto farm", ...)
GAME_SCRIPT = re.compile(
    r"(blox ?fruits?|da ?hood|arsenal|bed ?wars|murder ?mystery|\bmm2\b|pet ?sim|grow ?a ?garden|99 ?nights|"
    r"steal ?a ?brainrot|jail ?break|adopt ?me|\bdoors\b|\brivals\b|blade ?ball|\bfisch\b|dead ?rails|bee ?swarm|"
    r"brookhaven|tower ?defense ?simulator|phantom ?forces|bloxburg|king ?legacy|anime ?(defenders|vanguards|adventures)|"
    r"toilet ?tower|jujutsu|the ?strongest|hunty|forsaken|evade|natural ?disaster|bladeball|sols ?rng|pls ?donate|"
    r"counter ?blox|bad ?business|combat ?warriors|shindo|project ?slayers|gpo|grand ?piece|a ?one ?piece)"
    r".{0,40}(script|auto|farm|gui|macro|hub|mod|tool)|(script|auto ?farm|macro|hub)s?.{0,30}"
    r"(blox ?fruits?|da ?hood|arsenal|bed ?wars|murder ?mystery|mm2|pet ?sim|grow ?a ?garden|99 ?nights|doors|blade ?ball|fisch)",
    re.I,
)
NOT_ROBLOX = re.compile(r"noctalia|polytoria|love2d|\blöve\b|pico-?8|neovim|nvim|wezterm|hammerspoon|\bmpv\b|\bdefold\b", re.I)

CATEGORY_RULES = [
    ("aitools", r"\bmcp\b|model context protocol|\bai\b|\bllm|\bgpt|claude|chatgpt|openai|gemini|copilot|\bagents?\b|chatbot|ollama|cursor rules|agent skills?"),
    ("vr", r"\bvr\b|virtual reality|oculus|steamvr|openxr|quest ?[23]|motion ?track|full ?body ?track|webcam track"),
    ("tooling", r"toolchain|package ?manager|language ?server|\blsp\b|\bcli\b|command ?line|compiler|transpil|formatter|\blint(er)?\b|\bwally\b|\bpesde\b|\baftman\b|\bforeman\b|\brokit\b|\bselene\b|stylua|vs ?code ?extension"),
    ("security", r"anti ?-?cheat|anticheat|security|encrypt|decrypt|\bhash|sha-?256|\bsha1|\bmd5|\baes\b|\brsa\b|crypto|sanitiz|rate ?limit|\bauth|permission|\bban ?(system|service)|moderation|admin ?(system|panel|commands?)|\badonis\b|kohl"),
    ("vehicles", r"vehicle|\bcars?\b|chassis|\bboats?\b|\btrains?\b|railway|\bplanes?\b|aircraft|airplane|flight|helicopter|\btanks?\b|suspension|racing|drift|motorcycle|\bbikes?\b|\bship"),
    ("camera", r"camera|cutscene|cinematic|freecam|\bshake"),
    ("audio", r"\baudio|\bsounds?\b|music|\bsfx\b|\bradio\b|spotify|\bmidi\b|\bpiano|\bsong|playlist|voice"),
    ("landscape", r"terrain|landscape|\bwater\b|ocean|\bwaves?\b|weather|\brain\b|\bsnow|grass|foliage|\btrees?\b|biome|day ?/?night|\bsky|cloud|heightmap|\bplanet|\bcaves?\b|river|\bmaps? ?gen|world ?gen|real ?world ?map|osm|openstreetmap"),
    ("vfx", r"\bvfx|particle|shader|lighting|post ?-?process|\beffects?\b|render|ray ?trac|\bglow|\bbeam\b|\btrails?\b|bloom|\bfx\b|editableimage|editablemesh|\bpixel|graphics|\bcanvas|\bportal|\bdecal|\bmesh ?deform|explosion|\bfire\b|lightning"),
    ("animation", r"animat|\bik\b|inverse kinematic|\brig(s|ging)?\b|keyframe|\btween|\bsprings?\b|\bemotes?\b|\bmocap|motion ?capture|procedural anim|\bmoon animator|\bblender"),
    ("combat", r"combat|hitbox|weapon|\bguns?\b|\bswords?\b|\bfps\b|shooter|projectile|bullet|\bmelee|damage|fastcast|\bballistic|\bfighting|\bpvp\b|\bmagic|abilit(y|ies)|\bskills?\b"),
    ("movement", r"movement|character ?controller|parkour|ragdoll|physics|wall ?-?run|\bclimb|sprint|\bdash\b|gravity|\bswim|ledge|\bslide|\bgrapple|grappling|\bjump|walk|locomotion|\bcharacter\b"),
    ("ai", r"pathfind|\bnpcs?\b|behaviou?r ?tree|neural|machine ?learning|\bml\b|navmesh|boids|\bgoap\b|\bfsm\b|state ?machine|\ba\*|\bastar\b|flocking|\bbots? ai|reinforcement"),
    ("procgen", r"procedural|\bnoise|perlin|simplex|voxel|\bmaze|dungeon|(map|world|level|terrain|dungeon|maze|name|noise|city|room|planet|island) ?gen(erator|eration)?\b|wave ?function|\bwfc\b|\bmath|bezier|geometry|algorithm|\bbvh|octree|quadtree|delaunay|triangulat|spline|matrix|vector|quaternion|\bcsg\b|fractal"),
    ("networking", r"network|\bremotes?\b|replicat|netcode|packet|\brpc\b|bytenet|\bnet\b|client ?-?server|lag ?compens|interpolat|rollback|messaging ?service|cross ?-?server"),
    ("data", r"datastore|data ?store|\bsav(e|ing) ?(system|data)|serializ|\bprofile|compress|\bbuffers?\b|state ?management|\bstate\b|storage|big ?num|\bbignum|infinite ?number|\bjson\b|\bcache|leaderboard|\bstats?\b"),
    ("ecs", r"\becs\b|entity ?component|framework|\bknit\b|architecture|dependency ?injection|\blifecycle|service ?locator|\bmodule ?loader|flamework"),
    ("plugins", r"\bplugins?\b"),
    ("ui", r"\bui\b|\bgui\b|interface|\breact\b|\broact\b|\bfusion\b|\bvide\b|components?\b|\bhud\b|\bmenus?\b|inventory|backpack|\btext\b|\bfonts?\b|notification|topbar|\bicons?\b|\bbuttons?\b|dialog|\bchat\b|layout|\btheme"),
    ("apis", r"open ?cloud|opencloud|discord|\bbots?\b|webhook|\bhttps?\b|rest ?api|web ?api|\bapi (wrapper|client)|api ?wrapper|wrapper for|trello|\bproxy\b|\bgroup ?(rank|management)|ranking|\bweb\b|website|browser ?extension|chrome ?extension|\bextension\b|\bsdk\b|\bnpm\b|\bpypi\b|analytics|telegram|twitter|\bexpress\b|\bnode(js)?\b|noblox|endpoints?|\.com\b|roblox ?api"),
    ("tooling", r"\brojo\b|\bsync|\bcli\b|\btools?\b|tooling|\blint|formatter|compiler|transpil|\bpackage|\bwally\b|\bpesde\b|\blsp\b|language ?server|vs ?code|vscode|typescript|roblox-ts|rbxts|\btests?\b|testing|\bci\b|\bbuild|parser|\btypes?\b|\brbxlx?\b|\brbxmx?\b|\bmeshes?\b|\bassets?\b|upload|\bdocs?\b|documentation|\bsyntax|highlight|\bdevtools?|debugg|profil|benchmark|\bgit\b|version ?control|\bfile ?format"),
    ("wild", r"emulat|interpreter|\bvm\b|virtual ?machine|\bdoom\b|\bport(ed)? of|chip-?8|game ?boy|\bnes\b|\bcpu\b|minecraft|\blinux\b|operating ?system|\bos\b|\bcomputer\b|\bbrainf|lua ?in ?lua|luau ?in ?luau|\bjvm\b|\bwasm|webassembly|\bx86|\bassembly|\bsql\b"),
    ("learn", r"\bgames?\b|tutorial|example|template|learn|course|portfolio|showcase|\bobby\b|tycoon|simulator|awesome|\blist\b|collection|\bguide|\bdemo\b|starter|boilerplate|uncopylocked|open ?-?source ?game|\bclone\b|recreation|remake|\bprojects?\b|\bclass\b|school|university|homework|assignment|\bjam\b"),
]
CATEGORY_RULES = [(c, re.compile(p, re.I)) for c, p in CATEGORY_RULES]


def categorize(text):
    for cat, rx in CATEGORY_RULES:
        if rx.search(text):
            return cat
    return "systems"


def clean(s):
    s = re.sub(r"\s+", " ", s.replace("|", "/")).strip()
    s = s.replace("\t", " ")
    return s[:157] + "..." if len(s) > 160 else s


def main(pool_path):
    pool = json.load(open(pool_path, encoding="utf-8"))
    with CURATED.open(encoding="utf-8") as f:
        curated = {r["repo"].lower() for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)}
    rows, reasons = [], {}
    for key, it in pool.items():
        def skip(why):
            reasons[why] = reasons.get(why, 0) + 1
        if key in curated:
            skip("al gecureerd"); continue
        if it["repo"].split("/")[0].lower() in ("roblox", "luau-lang"):
            skip("officieel"); continue
        if it.get("fork"):
            skip("fork"); continue
        desc = it.get("desc") or ""
        topics = " ".join(it.get("topics") or [])
        name = it["repo"].split("/")[1]
        text = f"{name.replace('-', ' ').replace('_', ' ')} {desc} {topics}"
        if len(desc) < 12 or (len(desc.split()) < 4 and int(it.get("stars") or 0) < 5):
            skip("geen/te korte omschrijving"); continue
        rojo_ok = re.search(r"\brojo\b", topics, re.I) or (
            re.search(r"\brojo\b", f"{name} {desc}", re.I)
            and (it.get("lang") in ("Luau", "Lua", "Rust", "TypeScript") or re.search(r"roblox|studio", text, re.I)))
        if not (RELEVANT.search(text) or rojo_ok or it.get("lang") == "Luau"):
            skip("niet roblox"); continue
        if NOT_ROBLOX.search(text) and not re.search(r"roblox", text, re.I):
            skip("niet roblox"); continue
        if BLOCK.search(text) or GAME_SCRIPT.search(text):
            skip("exploit/cheat/spam"); continue
        if it.get("lang") == "HTML" and re.search(r"20(25|26)", text) and it.get("created", "") >= "2026-06":
            skip("seo-spam"); continue
        if re.search(r"\b(best|top|ultimate)\b.{0,40}\b2026\b|\b2026\b.{0,20}\b(best|guide|free)\b", text, re.I):
            skip("seo-spam"); continue
        rows.append((categorize(text), it["repo"], int(it.get("stars") or 0), clean(desc)))
    rows.sort(key=lambda r: (r[0], -r[2], r[1].lower()))
    with OUT.open("w", encoding="utf-8") as f:
        f.write("category\trepo\tstars\tnote\n")
        for r in rows:
            f.write("\t".join(map(str, r)) + "\n")
    print(f"{len(rows)} repos naar {OUT.relative_to(ROOT)}")
    for k, v in sorted(reasons.items(), key=lambda x: -x[1]):
        print(f"  overgeslagen ({k}): {v}")
    counts = {}
    for r in rows:
        counts[r[0]] = counts.get(r[0], 0) + 1
    print("  " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main(sys.argv[1])
