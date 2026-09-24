# Roblox Hidden Gems 💎

Privé-collectie van **unieke, minder bekende open-source Roblox-projecten** van publieke GitHub:
API's, VFX, game mechanics, networking, AI, tooling en meer.

**Bewust níet opgenomen:** standaard Roblox-functionaliteit, de bekende basics die iedereen al gebruikt,
exploits/cheats/executors, obfuscators, account-tools en spam-repos.

Totaal: **204 repos** in **16 categorieën**. ⭐ = GitHub-sterren op het moment van verzamelen (sept. 2026).

## Categorieën

- [VFX, graphics & rendering](categories/vfx.md) (22) — Effecten, shaders, licht, water, weer en canvas-rendering.
- [Networking & replicatie](categories/networking.md) (12) — Buffer-netcode, IDL-compilers, encryptie en eigen replicatie.
- [ECS & game-architectuur](categories/ecs.md) (10) — Entity Component Systems en frameworks voorbij Knit.
- [Combat, hitboxes & projectielen](categories/combat.md) (9) — Melee-hitboxes, projectielen, lag-compensatie en spatial queries.
- [Movement, physics & characters](categories/movement.md) (17) — Character controllers, IK, ragdolls, voertuigen, destructie en physics.
- [AI, NPC's & machine learning](categories/ai.md) (12) — Neurale netwerken, behavior trees, pathfinding en matchmaking.
- [Procedurele generatie & wereld](categories/procgen.md) (6) — Voxels, terrain, wave function collapse en ruimtelijke datastructuren.
- [UI & animatie](categories/ui.md) (21) — Reactieve UI, springs, custom tekst, inventories en mobiele controls.
- [Camera & cutscenes](categories/camera.md) (4) — Camera-shake, custom camera's en cinematics.
- [Data, opslag & state](categories/data.md) (11) — DataStores, serialisatie, state management en big numbers.
- [Next-level / experimenteel](categories/wild.md) (16) — Luau-in-Luau, emulators, DOOM, parsers en andere gekke projecten.
- [API's & externe integraties](categories/apis.md) (19) — Open Cloud, web-API's, Discord, databases, analytics en AI-agents.
- [Tooling & workflow](categories/tooling.md) (20) — Runtimes, package managers, asset-pipelines, deployment en docs.
- [Security & anticheat](categories/security.md) (5) — Hashing, logins, captcha's, permissies en anticheat.
- [Kant-en-klare game-systemen & plugins](categories/systems.md) (10) — Quests, placement, dialogen, sirenes en handige plugins.
- [Leren & collecties](categories/learn.md) (10) — Artikelen, code-collecties, open-source games en andere curated lijsten.

## Top picks per categorie

De drie met de meeste sterren per categorie. Klik op een categorie voor de volledige lijst.

### [VFX, graphics & rendering](categories/vfx.md)

- [boatbomber/WindShake](https://github.com/boatbomber/WindShake) — High-performance wind-animatie voor bladeren en foliage, duizenden objecten tegelijk
- [boatbomber/CullThrottle](https://github.com/boatbomber/CullThrottle) — Effecten voor tienduizenden objecten beheren met culling + throttling op afstand/zicht
- [EgoMoose/rbx-viewport-window](https://github.com/EgoMoose/rbx-viewport-window) — ViewportFrames als "portalen" naar andere dimensies/werelden

### [Networking & replicatie](categories/networking.md)

- [red-blox/zap](https://github.com/red-blox/zap) — IDL-compiler (Rust) die razendsnelle buffer-netcode genereert
- [1Axen/blink](https://github.com/1Axen/blink) — IDL-compiler in Luau voor buffer-networking met type-safety
- [ffrostfall/ByteNet](https://github.com/ffrostfall/ByteNet) — Moderne buffer-gebaseerde networking-library

### [ECS & game-architectuur](categories/ecs.md)

- [Ukendio/jecs](https://github.com/Ukendio/jecs) — Snelle, data-oriented ECS voor Luau (relaties, archetypes)
- [matter-ecs/matter](https://github.com/matter-ecs/matter) — Moderne ECS met hot-reloading en debugger
- [centau/ecr](https://github.com/centau/ecr) — Sparse-set gebaseerde ECS

### [Combat, hitboxes & projectielen](categories/combat.md)

- [Swordphin/raycastHitboxRbxl](https://github.com/Swordphin/raycastHitboxRbxl) — Klassieke RaycastHitbox voor melee-wapens
- [LDGerrits/QuickZone](https://github.com/LDGerrits/QuickZone) — Physics-vrije spatial queries (BVH), 60 FPS met 1M+ zones
- [1Axen/Secure-Cast](https://github.com/1Axen/Secure-Cast) — Server-authoritative projectielen met lag-compensatie

### [Movement, physics & characters](categories/movement.md)

- [easy-games/chickynoid](https://github.com/easy-games/chickynoid) — Server-authoritative character controller met client-prediction (anti-speedhack)
- [jaipack17/Nature2D](https://github.com/jaipack17/Nature2D) — Volledige 2D-physics-engine in GUI's
- [lisphm/A-Chassis](https://github.com/lisphm/A-Chassis) — Officieel A-Chassis: realistische auto's en motoren

### [AI, NPC's & machine learning](categories/ai.md)

- [ahmicy/simplepath](https://github.com/ahmicy/simplepath) — Pathfinding voor humanoids en non-humanoids in een paar regels
- [prooheckcp/RobloxStateMachine](https://github.com/prooheckcp/RobloxStateMachine) — State machines met states en transitions (NPC/game-flow)
- [Kironte/Roblox-Neural-Network-Library](https://github.com/Kironte/Roblox-Neural-Network-Library) — Object-georiënteerde neurale netwerken

### [Procedurele generatie & wereld](categories/procgen.md)

- [real2nix/mineblox](https://github.com/real2nix/mineblox) — Uitbreidbare voxel-engine (Minecraft-achtig)
- [Sleitnick/rbxts-octo-tree](https://github.com/Sleitnick/rbxts-octo-tree) — Octree voor snelle ruimtelijke lookups
- [EgoMoose/PolyBool-Lua](https://github.com/EgoMoose/PolyBool-Lua) — Boolean-operaties op polygonen (union, intersect, difference)

### [UI & animatie](categories/ui.md)

- [SirMallard/Iris](https://github.com/SirMallard/Iris) — Immediate-mode GUI (Dear ImGui) voor debug- en dev-tools
- [centau/vide](https://github.com/centau/vide) — Reactieve UI-library (Fusion-alternatief, heel snel)
- [fraktality/spr](https://github.com/fraktality/spr) — Klein en snel spring-animatie

### [Camera & cutscenes](categories/camera.md)

- [Sleitnick/RbxCameraShaker](https://github.com/Sleitnick/RbxCameraShaker) — Camera-shake presets en eigen shakes
- [rduoDevs/CameraService](https://github.com/rduoDevs/CameraService) — Alternatieve game-camera met veel controle
- [EgoMoose/patch-roblox-cameramodule](https://github.com/EgoMoose/patch-roblox-cameramodule) — Patch zodat de camera-API van PlayerModule runtime bereikbaar is

### [Data, opslag & state](categories/data.md)

- [MadStudioRoblox/ProfileStore](https://github.com/MadStudioRoblox/ProfileStore) — Session-locked DataStore saving (opvolger ProfileService)
- [littensy/charm](https://github.com/littensy/charm) — Atomic state management (Jotai-stijl)
- [paradoxum-games/lyra](https://github.com/paradoxum-games/lyra) — Geavanceerd player-data beheer met simpele API

### [Next-level / experimenteel](categories/wild.md)

- [kosuke14/vLuau](https://github.com/kosuke14/vLuau) — Luau VM + compiler die in Luau draait (loadstring-alternatief)
- [RadiatedExodus/LuauCeption](https://github.com/RadiatedExodus/LuauCeption) — Luau draaien in Luau (via Wasynth/WebAssembly)
- [jackhexed/luaup](https://github.com/jackhexed/luaup) — Lossless Luau-parser in Luau

### [API's & externe integraties](categories/apis.md)

- [matthewdean/roblox-web-apis](https://github.com/matthewdean/roblox-web-apis) — Lijst van (ongedocumenteerde) Roblox web-API's
- [noblox/noblox.js](https://github.com/noblox/noblox.js) — Node.js-wrapper voor Roblox web-API (groepen, ranks) — gearchiveerd
- [Chrrxs/robloxstudio-mcp](https://github.com/Chrrxs/robloxstudio-mcp) — MCP-server: AI-agents laten debuggen, playtesten en screenshots maken in Studio

### [Tooling & workflow](categories/tooling.md)

- [lune-org/lune](https://github.com/lune-org/lune) — Standalone Luau-runtime (scripts, place-files bewerken, CI)
- [MaximumADHD/Roblox-Client-Tracker](https://github.com/MaximumADHD/Roblox-Client-Tracker) — Automatisch bijgehouden info over elke Roblox-versie (API-dumps, FFlags)
- [luau-lang/lute](https://github.com/luau-lang/lute) — Officiële standalone Luau-runtime voor algemeen gebruik

### [Security & anticheat](categories/security.md)

- [PossiblePanda/QueryAuth](https://github.com/PossiblePanda/QueryAuth) — Type-safe permissie-checks met complexe logica
- [boatbomber/HashLib](https://github.com/boatbomber/HashLib) — Cryptografische hashes (SHA, MD5...) in pure Lua
- [EgoMoose/rbx-captcha](https://github.com/EgoMoose/rbx-captcha) — Captcha's in Roblox (anti-bot)

### [Kant-en-klare game-systemen & plugins](categories/systems.md)

- [Sleitnick/RbxObservers](https://github.com/Sleitnick/RbxObservers) — Observer-functies (tags, attributes, players)
- [AlexanderLindholt/SignalPlus](https://github.com/AlexanderLindholt/SignalPlus) — Zeer snelle signal-library
- [EgoMoose/Rbx-PSD-UI](https://github.com/EgoMoose/Rbx-PSD-UI) — Photoshop PSD-bestanden omzetten naar Roblox GUI

### [Leren & collecties](categories/learn.md)

- [Quenty/NevermoreEngine](https://github.com/Quenty/NevermoreEngine) — Enorme verzameling herbruikbare game-modules
- [Kampfkarren/Roblox](https://github.com/Kampfkarren/Roblox) — Scripts uit een echte game (o.a. DataStore2)
- [littensy/slither](https://github.com/littensy/slither) — Complete open-source game (roblox-ts + React)

## Uitbreiden

1. Voeg een regel toe aan [`data/repos.tsv`](data/repos.tsv) (`categorie<TAB>eigenaar/repo<TAB>sterren<TAB>omschrijving`).
2. Draai `python3 scripts/generate.py` — README en categoriepagina's worden opnieuw gegenereerd.

> Let op: controleer altijd de licentie van een repo voordat je code in je eigen game gebruikt.
