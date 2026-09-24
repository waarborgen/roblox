# Roblox Hidden Gems 💎

Privé-collectie van **unieke, minder bekende open-source Roblox-projecten** van publieke GitHub:
API's, VFX, game mechanics, networking, AI, tooling en meer.

**Bewust níet opgenomen:** standaard Roblox-functionaliteit, de bekende basics die iedereen al gebruikt,
exploits/cheats/executors/spoofers, obfuscators, account-tools en SEO-spamrepos.

Tip: ⭐ zegt weinig bij nieuwe projecten, veel pareltjes hebben (nog) bijna geen sterren.

Totaal: **1231 repos** in **23 categorieën**. ⭐ = GitHub-sterren op het moment van verzamelen (sept. 2026).

## Categorieën

- [VFX, graphics & rendering](#vfx-graphics--rendering) — **58** repos ([losse pagina](categories/vfx.md))
- [Landschap, terrain, water & weer](#landschap-terrain-water--weer) — **48** repos ([losse pagina](categories/landscape.md))
- [Animatie, IK & rigging](#animatie-ik--rigging) — **51** repos ([losse pagina](categories/animation.md))
- [Movement, physics & characters](#movement-physics--characters) — **51** repos ([losse pagina](categories/movement.md))
- [Voertuigen, boten & treinen](#voertuigen-boten--treinen) — **17** repos ([losse pagina](categories/vehicles.md))
- [Combat, hitboxes & wapens](#combat-hitboxes--wapens) — **40** repos ([losse pagina](categories/combat.md))
- [AI, NPC's & machine learning](#ai-npcs--machine-learning) — **25** repos ([losse pagina](categories/ai.md))
- [Procedurele generatie & wiskunde](#procedurele-generatie--wiskunde) — **22** repos ([losse pagina](categories/procgen.md))
- [Networking & replicatie](#networking--replicatie) — **37** repos ([losse pagina](categories/networking.md))
- [ECS & game-architectuur](#ecs--game-architectuur) — **21** repos ([losse pagina](categories/ecs.md))
- [UI & interface](#ui--interface) — **88** repos ([losse pagina](categories/ui.md))
- [Camera & cutscenes](#camera--cutscenes) — **13** repos ([losse pagina](categories/camera.md))
- [Audio](#audio) — **12** repos ([losse pagina](categories/audio.md))
- [VR & motion tracking](#vr--motion-tracking) — **14** repos ([losse pagina](categories/vr.md))
- [Data, opslag & serialisatie](#data-opslag--serialisatie) — **48** repos ([losse pagina](categories/data.md))
- [Game-systemen & utilities](#game-systemen--utilities) — **124** repos ([losse pagina](categories/systems.md))
- [Security & anticheat](#security--anticheat) — **18** repos ([losse pagina](categories/security.md))
- [Next-level / experimenteel](#next-level--experimenteel) — **101** repos ([losse pagina](categories/wild.md))
- [API's & externe integraties](#apis--externe-integraties) — **64** repos ([losse pagina](categories/apis.md))
- [AI-tools voor Roblox-development](#ai-tools-voor-roblox-development) — **34** repos ([losse pagina](categories/aitools.md))
- [Tooling & workflow](#tooling--workflow) — **203** repos ([losse pagina](categories/tooling.md))
- [Studio-plugins](#studio-plugins) — **25** repos ([losse pagina](categories/plugins.md))
- [Leren, open-source games & collecties](#leren-open-source-games--collecties) — **117** repos ([losse pagina](categories/learn.md))

## VFX, graphics & rendering

Particles, shaders, lighting, portalen, raytracing en canvas-rendering. (58 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [Extravi/Bloxshade](https://github.com/Extravi/Bloxshade) | 112 | Installer voor ReShade/NVIDIA-shaders op de Roblox-client |
| [boatbomber/CullThrottle](https://github.com/boatbomber/CullThrottle) | 79 | Effecten voor tienduizenden objecten beheren met culling + throttling op afstand/zicht |
| [EgoMoose/rbx-viewport-window](https://github.com/EgoMoose/rbx-viewport-window) | 77 | ViewportFrames als "portalen" naar andere dimensies/werelden |
| [MaximumADHD/Roblox-Materials](https://github.com/MaximumADHD/Roblox-Materials) | 61 | Alle PBR-materiaaltextures van Roblox (voor/na 2022) |
| [boatbomber/GradientCanvas](https://github.com/boatbomber/GradientCanvas) | 58 | Canvas-renderer die met greedy gradients pixels tekent in GUI |
| [boatbomber/ViewportCanvas](https://github.com/boatbomber/ViewportCanvas) | 53 | Greedy-meshed canvas voor willekeurige tekeningen in 3D/viewport |
| [evaera/EvLightning](https://github.com/evaera/EvLightning) | 52 | Realistische bliksemschichten genereren |
| [OMouta/RobloxShadeHost](https://github.com/OMouta/RobloxShadeHost) | 37 | ReShade-presets gebruiken met Roblox |
| [ryanlua/Shime](https://github.com/ryanlua/Shime) | 34 | Shimmer/loading-glans op elk GuiObject |
| [Mqxsyy/Lumina](https://github.com/Mqxsyy/Lumina) | 30 | Eigen particle-systeem API met node/graph-editor (à la Unity VFX Graph) |
| [boatbomber/EditableImageBlur](https://github.com/boatbomber/EditableImageBlur) | 28 | Snelle blur-algoritmes voor EditableImage |
| [Razorboot/radiosity_engine_luau](https://github.com/Razorboot/radiosity_engine_luau) | 20 | Radiosity baked lighting (global illumination) volledig in Luau |
| [joeldesante/rParticle](https://github.com/joeldesante/rParticle) | 20 | Lichtgewicht 2D particle-systeem voor GUI |
| [rotntake/BloodEngine](https://github.com/rotntake/BloodEngine) | 18 | Druppel-emitter: bloed/vloeistof die spettert en op oppervlakken blijft liggen |
| [zilibobi/forge-vfx](https://github.com/zilibobi/forge-vfx) | 17 | Emit-module van de VFX Forge plugin: complete VFX-rigs (particles, beams, meshes) afvuren vanuit code |
| [AnotherSubatomo/RbxShader](https://github.com/AnotherSubatomo/RbxShader) | 17 | Een shader-engine in Luau (fragment-shaders via EditableImage) |
| [Razorboot/luau-2016-shadow-engine](https://github.com/Razorboot/luau-2016-shadow-engine) | 12 | Schaduw-engine in Luau |
| [boatbomber/ImageMask](https://github.com/boatbomber/ImageMask) | 8 | Images clippen/masken met een ViewportFrame-truc |
| [KalaYoScripting/Ember](https://github.com/KalaYoScripting/Ember) | 7 | Particle-emitter gemaakt van UI-elementen (particles op elke GUI) |
| [diigit/EmitYourParticles](https://github.com/diigit/EmitYourParticles) | 4 | Geoptimaliseerde 2D GUI particle-emitter |
| [thom463s/2D-Particle-Emitter](https://github.com/thom463s/2D-Particle-Emitter) | 4 | 2D particle-emitter oplossing |
| [cg955gtr/PartCache](https://github.com/cg955gtr/PartCache) | 4 | Linked-list part cache (snel parts hergebruiken voor projectielen/VFX) |
| [QwinkleTee/Qwinkles-Particles-2](https://github.com/QwinkleTee/Qwinkles-Particles-2) | 3 | Qwinkle's Part-icles 2 plugin (part-gebaseerde particles) |
| [arindam-codes/roblox-cinematic-experience](https://github.com/arindam-codes/roblox-cinematic-experience) | 3 | Cinematische camera, lighting en player-control voor storytelling |
| [StephenSHorton/immersive-portals](https://github.com/StephenSHorton/immersive-portals) | 3 | Immersive portal-rendering (door portalen kijken én lopen) voor roblox-ts |
| [MiaGobble/VolumetricLighting](https://github.com/MiaGobble/VolumetricLighting) | 2 | Eenvoudige volumetric lighting (god rays) |
| [hexa0/lighting-profile](https://github.com/hexa0/lighting-profile) | 2 | Lighting-profielen opslaan/wisselen (plugin) |
| [nightcycle/editable-image-util](https://github.com/nightcycle/editable-image-util) | 2 | Snel EditableImages bewerken |
| [rookie-codes/WindLines](https://github.com/rookie-codes/WindLines) | 2 | Geanimeerde windlijnen met Attachments en Trails |
| [Y-Workplace/DissolveEffect](https://github.com/Y-Workplace/DissolveEffect) | 1 | Pixel-dissolve/materialize effect met gloeiende randen via EditableImage |
| [PAKILA0/RBX-SpaceDust](https://github.com/PAKILA0/RBX-SpaceDust) | 1 | Screenspace VFX: ruimtestof rond de camera |
| [Tsukeruu/rock-spawn-roblox](https://github.com/Tsukeruu/rock-spawn-roblox) | 1 | Krater/rotsen-ring effect (populaire anime-VFX trend) |
| [MiaGobble/Effect-Design-Suite](https://github.com/MiaGobble/Effect-Design-Suite) | 1 | Studio-plugin om VFX te ontwerpen en te timen |
| [Matthhhh/MuParticles](https://github.com/Matthhhh/MuParticles) | 1 | Particles in de UI emitten |
| [cruzfelipee/GuiParticleService](https://github.com/cruzfelipee/GuiParticleService) | 1 | UI-particles met dezelfde API als de 3D ParticleEmitter |
| [xyxneweraxyx/tornado-old](https://github.com/xyxneweraxyx/tornado-old) | 1 | Particle-tornado met realistische sinus-bewegingen |
| [ShakAsante/vfx-lib](https://github.com/ShakAsante/vfx-lib) | 1 | Meshes, beams, sounds en custom particles emitten via één API |
| [EL4CTEO/RLSS](https://github.com/EL4CTEO/RLSS) | 1 | "DLSS-achtig": leest wat de camera ziet en past lighting/post-FX live aan |
| [SentientShades/LUAU-Pixel-Shader](https://github.com/SentientShades/LUAU-Pixel-Shader) | 1 | Pixel-shader effect in Luau |
| [fau-1o/Artnet2Roblox](https://github.com/fau-1o/Artnet2Roblox) | 1 | Echte DMX-lichtshows (MA3, QLC+) live naar Roblox via Art-Net |
| [ThomasBignolas/ShowForge](https://github.com/ThomasBignolas/ShowForge) | 1 | Procedurele concert/stadion-lichtontwerp in Blender met Roblox-bridge |
| [jaipack17/lumen](https://github.com/jaipack17/lumen) | 1 | Non-realtime ray-tracing engine in Roblox |
| [jun-ro/Mango](https://github.com/jun-ro/Mango) | 1 | Framework voor in-game VFX en cutscenes |
| [HenriMalahieude/Roblox-Raycast-Renderer](https://github.com/HenriMalahieude/Roblox-Raycast-Renderer) | 1 | Eigen raycast-renderer in Roblox |
| [NumericAbyss408/Non-EuclideanPortalSystem](https://github.com/NumericAbyss408/Non-EuclideanPortalSystem) | 1 | Non-Euclidische portalen (ruimtes groter van binnen) |
| [usercontent0/DroneSystem](https://github.com/usercontent0/DroneSystem) | 1 | Drone-shows maken voor events (lichtshows in de lucht) |
| [scrpt2r/axonEngine](https://github.com/scrpt2r/axonEngine) | 1 | CPU 3D-software-renderer in Luau |
| [Danonienko/Seeing-Things](https://github.com/Danonienko/Seeing-Things) | 1 | Objecten geleidelijk laten verschijnen/verdwijnen op afstand |
| [afrxo/react-particle](https://github.com/afrxo/react-particle) | 0 | Particle-systeem met React en roblox-ts |
| [WildCake/Voxel-Particles-Plugin](https://github.com/WildCake/Voxel-Particles-Plugin) | 0 | Voxel-particle effecten maken en previewen |
| [Shuzaiku/Particle-Scaler](https://github.com/Shuzaiku/Particle-Scaler) | 0 | ParticleEmitters dynamisch schalen over hun levensduur |
| [DeroXP/Roblox-SSGI-SSRT](https://github.com/DeroXP/Roblox-SSGI-SSRT) | 0 | Screen-space global illumination / raytracing experiment |
| [Y-Workplace/Liquid-Simulation](https://github.com/Y-Workplace/Liquid-Simulation) | 0 | WebGL Water (vloeistof-simulatie) geport naar EditableMesh |
| [gaymeowing/PBR-Surface-Applier](https://github.com/gaymeowing/PBR-Surface-Applier) | 0 | PBR-materialen op part-oppervlakken toepassen (library + plugin) |
| [ElixNoir/Roblox-Canvas](https://github.com/ElixNoir/Roblox-Canvas) | 0 | Teken-algoritmes voor buffers/EditableImage |
| [AnotherSubatomo/Cezanne](https://github.com/AnotherSubatomo/Cezanne) | 0 | Paralleliseerbare image-filters in pure Luau |
| [NotRllyRn/PixelRender](https://github.com/NotRllyRn/PixelRender) | 0 | Pixel raycasting-renderer |
| [InfernoAmaruq/EasyPool](https://github.com/InfernoAmaruq/EasyPool) | 0 | Object pooling framework |

## Landschap, terrain, water & weer

Terrain-generators, echte kaarten, grotten, oceanen, foliage, dag/nacht en weer. (48 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [boatbomber/WindShake](https://github.com/boatbomber/WindShake) | 87 | High-performance wind-animatie voor bladeren en foliage, duizenden objecten tegelijk |
| [buildthomas/Rain](https://github.com/buildthomas/Rain) | 44 | Volledige regen-simulatie (druppels, splashes, geluid, occlusie) |
| [boatbomber/Distortion-Screen-Rain](https://github.com/boatbomber/Distortion-Screen-Rain) | 28 | Waterdruppels op het scherm voor immersie (regen/onderwater) |
| [Sir-Tiffy/MinecraftToRoblox](https://github.com/Sir-Tiffy/MinecraftToRoblox) | 16 | Minecraft-werelden omzetten naar een Roblox-map |
| [tiffany352/Roblox-Terrain-Generator](https://github.com/tiffany352/Roblox-Terrain-Generator) | 11 | Framework voor terrain-generators |
| [Francessco121/roblox-classic-terrain-tools](https://github.com/Francessco121/roblox-classic-terrain-tools) | 11 | Klassiek (blok)terrain importeren in moderne places |
| [TheArturZh/RTerrainGenerator](https://github.com/TheArturZh/RTerrainGenerator) | 8 | Procedurele terrain-generator (MIT) |
| [Tunahan-Uysal/RoGen](https://github.com/Tunahan-Uysal/RoGen) | 8 | Afbeelding → 3D-map generator (Python + Lune) |
| [Klingaac/WorldLoader-Roblox-Plugin](https://github.com/Klingaac/WorldLoader-Roblox-Plugin) | 7 | Echte plekken nabouwen: OpenStreetMap + hoogtedata → terrain, gebouwen, wegen en spoorlijnen |
| [Quenty/PartToTerrainPlugin](https://github.com/Quenty/PartToTerrainPlugin) | 7 | Parts naar terrain met behoud van onderliggend terrain |
| [GeoCodeCrafter/Cave](https://github.com/GeoCodeCrafter/Cave) | 6 | Procedurele mijnen/grotten: elke server een nieuwe mijn, alle grotten verbonden |
| [ribzix/ribzix.github.io](https://github.com/ribzix/ribzix.github.io) | 5 | Heightmap-generator van echte aardrijkskunde, aangepast voor Roblox |
| [howhow2315/jonswap-ocean](https://github.com/howhow2315/jonswap-ocean) | 4 | JONSWAP oceaan-spectrum (echte golf-fysica) in Luau |
| [ItipatS/DayNightCycleAndEvent](https://github.com/ItipatS/DayNightCycleAndEvent) | 4 | Dag/nacht-cyclus met dynamische events |
| [ffrostfall/optimized-gerstner-waves](https://github.com/ffrostfall/optimized-gerstner-waves) | 4 | Geoptimaliseerde Gerstner-golven (oceaan) |
| [maddoxbouldin/roblox-runtime-terrain](https://github.com/maddoxbouldin/roblox-runtime-terrain) | 3 | Runtime terrain: chunk-streaming, Parallel Luau, grotten, vegetatie |
| [MaximumADHD/Minecrafted-Smooth-Terrain](https://github.com/MaximumADHD/Minecrafted-Smooth-Terrain) | 3 | Smooth terrain reskinnen met Minecraft-voxels/textures |
| [rynstwrt/Pixel-Terrain](https://github.com/rynstwrt/Pixel-Terrain) | 3 | Pixel-achtig custom terrain |
| [stravant/roblox-polymap](https://github.com/stravant/roblox-polymap) | 2 | Mesh-editor voor part-gebaseerd terrain (van de maker van GapFill/ResizeAlign) |
| [Anaminus/nudgecell](https://github.com/Anaminus/nudgecell) | 2 | Occupancy van individuele terrain-cellen bijstellen |
| [Axxerus/Roblox-Procedural-Ocean](https://github.com/Axxerus/Roblox-Procedural-Ocean) | 2 | Procedurele oceaan |
| [Redon-Tech/Weather-Systems](https://github.com/Redon-Tech/Weather-Systems) | 2 | Weer-systeem plugin (gerepareerde TwentyTwoPilots-versie) |
| [MrChickenRocket/sdf-procedural-toolkit](https://github.com/MrChickenRocket/sdf-procedural-toolkit) | 2 | SDF-meshes genereren (Surface Nets + QEM) → MeshPart, van de Chickynoid-maker |
| [BrakingF1/Ro-Racing-Tracks](https://github.com/BrakingF1/Ro-Racing-Tracks) | 2 | Racecircuits als open-source assets |
| [onlymateo/roblox-ocean-wave-generation](https://github.com/onlymateo/roblox-ocean-wave-generation) | 1 | Dynamische oceaan: golven, drijven, onderwater-effecten |
| [TaylorDevGD/Roblox-Terrain-Storage-Repo](https://github.com/TaylorDevGD/Roblox-Terrain-Storage-Repo) | 1 | Terrain opslaan/verplaatsen zoals parts (naar ReplicatedStorage) |
| [goldenstein64/InfiniteTerrain](https://github.com/goldenstein64/InfiniteTerrain) | 1 | Configureerbaar oneindig terrain (door 5uphi) |
| [maybe-tammyy/Terrain-Generation](https://github.com/maybe-tammyy/Terrain-Generation) | 1 | Chunk-terrain met multi-octave Perlin en server-seeds |
| [nikolapesevic/genesis](https://github.com/nikolapesevic/genesis) | 1 | 3D Perlin-noise maps genereren |
| [DaniiTheFox/Roblox-procedural-generation](https://github.com/DaniiTheFox/Roblox-procedural-generation) | 1 | Chunk-engine uit BrickVox geport naar Roblox |
| [mateusdcc/plant-generator](https://github.com/mateusdcc/plant-generator) | 1 | Deterministische procedurele planten/bomen met L-systems (roblox-ts) |
| [Distracted-Games/ProDayNightCycle](https://github.com/Distracted-Games/ProDayNightCycle) | 1 | Configureerbare, event-driven dag/nacht-cyclus |
| [stravant/roblox-roadhelper](https://github.com/stravant/roblox-roadhelper) | 1 | Helper voor procedurele wegsegmenten |
| [CaidenSteele05/Procedural-3D-Terrain-Generator](https://github.com/CaidenSteele05/Procedural-3D-Terrain-Generator) | 1 | Noise-heightmaps, biome-kleuren en chunk-loading rond de speler |
| [adrian-alberto/minimap_renderer](https://github.com/adrian-alberto/minimap_renderer) | 1 | Rendert minimaps uit heightmap-data (Pirates Life) |
| [PCN29/sea-game](https://github.com/PCN29/sea-game) | 0 | Realtime FFT-oceaan met displacement voor naval/open-world games |
| [stravant/roblox-pullup](https://github.com/stravant/roblox-pullup) | 0 | Terrain-editor plugin van stravant |
| [GravyPouch/RobloxTerrainCreator](https://github.com/GravyPouch/RobloxTerrainCreator) | 0 | Web-tool: biomes schilderen in 2D, 3D preview, direct importeren in Studio |
| [Avenze/proceduralterrain-repository](https://github.com/Avenze/proceduralterrain-repository) | 0 | Eindeloos smooth procedural terrain |
| [gcmodev/robloxcitygenerator](https://github.com/gcmodev/robloxcitygenerator) | 0 | Procedurele stad-generator plugin |
| [KashTheKing/ocean](https://github.com/KashTheKing/ocean) | 0 | Oneindige Gerstner-golf oceaan op EditableMesh |
| [raxdiusid/ForestGen](https://github.com/raxdiusid/ForestGen) | 0 | Bomen/bossen genereren |
| [R3velation/SnowFX](https://github.com/R3velation/SnowFX) | 0 | Sneeuw-effectsysteem |
| [SuperInstance/luau-biome](https://github.com/SuperInstance/luau-biome) | 0 | Deterministische biome-generatie met 10 zones en seeds |
| [Angryblobfish/Roblox-Infinite-Terrain](https://github.com/Angryblobfish/Roblox-Infinite-Terrain) | 0 | Oneindig terrain met biomes en foliage, performance-gericht |
| [Gzeu/roblox-procedural-worlds](https://github.com/Gzeu/roblox-procedural-worlds) | 0 | Collectie: biomes, terrain, grotten en chunk-generatie |
| [ryan-c-scott/roblox-leveler](https://github.com/ryan-c-scott/roblox-leveler) | 0 | Tiled-kaarten omzetten naar heightmap-terrain, water en objecten |
| [mateirenn/solum](https://github.com/mateirenn/solum) | 0 | Local-first terrain-authoring studio (Tauri) voor Roblox |

## Animatie, IK & rigging

Animatie-solvers, IK, Blender/Mixamo-pipelines, procedurele animatie en springs. (51 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [Reselim/Flipper](https://github.com/Reselim/Flipper) | 144 | Motion/spring-library |
| [fraktality/spr](https://github.com/fraktality/spr) | 143 | Klein en snel spring-animatie |
| [littensy/ripple](https://github.com/littensy/ripple) | 130 | Elegante spring/motion-library |
| [Cautioned/Blender-Animations-Plugin](https://github.com/Cautioned/Blender-Animations-Plugin) | 101 | Blender-addon om Roblox-animaties te importeren én exporteren |
| [ffrostfall/crunchyroll](https://github.com/ffrostfall/crunchyroll) | 98 | Eigen animatie-solver (vervangt Animator) voor volledige controle |
| [MaximumADHD/Moonlite](https://github.com/MaximumADHD/Moonlite) | 76 | Lichtgewicht in-game player voor Moon Animator-animaties (cutscenes!) |
| [chriscerie/roact-spring](https://github.com/chriscerie/roact-spring) | 73 | react-spring voor react-lua |
| [evaera/roblox-animation-transfer](https://github.com/evaera/roblox-animation-transfer) | 53 | Animaties overzetten naar een andere eigenaar/groep |
| [TylerAtStarboard/AnimationPublisher](https://github.com/TylerAtStarboard/AnimationPublisher) | 37 | Widget om custom animaties te updaten/uploaden |
| [TylerAtStarboard/AssetReuploader](https://github.com/TylerAtStarboard/AssetReuploader) | 32 | Images, meshes en animaties van je eigen games opnieuw uploaden en vervangen |
| [astrealRBLX/RoUI3](https://github.com/astrealRBLX/RoUI3) | 30 | GUI-animatie plugin met timeline |
| [TK-DZ/Roblox-IK-R15](https://github.com/TK-DZ/Roblox-IK-R15) | 24 | R15-rig met IK voor animeren in Blender |
| [EgoMoose/character-animate](https://github.com/EgoMoose/character-animate) | 23 | Package om standaard avatars te animeren zonder het Animate-script |
| [wrello/Animations](https://github.com/wrello/Animations) | 20 | Animaties afspelen en preloaden |
| [AlexanderLindholt/TweenPlus](https://github.com/AlexanderLindholt/TweenPlus) | 19 | Tweening met geavanceerde datatypes en interpolatie |
| [MiaGobble/Seam](https://github.com/MiaGobble/Seam) | 19 | Reactieve states + animatie |
| [datlass/Rbx-CCDIK](https://github.com/datlass/Rbx-CCDIK) | 18 | CCD inverse kinematics voor Motor6D-rigs (procedurele benen/armen) |
| [michaeldougal/AnimNation](https://github.com/michaeldougal/AnimNation) | 15 | Springs, tweens en splines op properties in één utility |
| [leo-prad/Twinkle](https://github.com/leo-prad/Twinkle) | 13 | UI-animator zonder tween-boilerplate |
| [Khaomi/Animator](https://github.com/Khaomi/Animator) | 10 | Alternatieve animation player (KeyframeSequences zelf afspelen) |
| [Chrrxs/kimodo-r15-retarget](https://github.com/Chrrxs/kimodo-r15-retarget) | 9 | NVIDIA text-to-motion (BVH) retargeten naar R15 KeyframeSequences |
| [unityjaeger/reel](https://github.com/unityjaeger/reel) | 8 | Eigen animatie-solver |
| [datlass/fabrik-ik-motor6d](https://github.com/datlass/fabrik-ik-motor6d) | 8 | FABRIK IK-solver voor Motor6D-rigs |
| [sivert-io/fbx-action-exporter](https://github.com/sivert-io/fbx-action-exporter) | 6 | Alle Blender-actions als losse FBX exporteren |
| [jackTabsCode/bau](https://github.com/jackTabsCode/bau) | 5 | Bulk animatie-uploader |
| [sentinel69402/Anima](https://github.com/sentinel69402/Anima) | 5 | Lichtgewicht animatie-library zonder boilerplate |
| [NotBlackrus/PlayerAnimator](https://github.com/NotBlackrus/PlayerAnimator) | 4 | Eigen animator-replicatie |
| [wes-BAN/crux-animation](https://github.com/wes-BAN/crux-animation) | 4 | Animatie-engine geïnspireerd op Unity's animatie-API |
| [jiwonz/anim2rbx](https://github.com/jiwonz/anim2rbx) | 4 | Animatiebestanden (FBX e.d.) omzetten naar KeyframeSequence |
| [include-marcy/Hera](https://github.com/include-marcy/Hera) | 4 | Interface-animatie ontwerptool + API |
| [TheNexusAvenger/Nexus-Motor6D-Creator](https://github.com/TheNexusAvenger/Nexus-Motor6D-Creator) | 4 | Plugin om Motor6Ds te maken (rigging) |
| [nitingit7/Mixamo_To_Roblox_Studio](https://github.com/nitingit7/Mixamo_To_Roblox_Studio) | 3 | Mixamo-animaties importeren in Studio |
| [seaofvoices/easing-styles](https://github.com/seaofvoices/easing-styles) | 3 | Alle bekende easing-functies |
| [TaseenA09/Dynamic-Walk-Animations-and-Footing-for-Roblox](https://github.com/TaseenA09/Dynamic-Walk-Animations-and-Footing-for-Roblox) | 3 | Dynamische loopanimaties met voetplaatsing |
| [RAMPAGELLC/ProceduralAnimator](https://github.com/RAMPAGELLC/ProceduralAnimator) | 2 | Modellen procedureel laten opbouwen/exploderen |
| [Jessdevzz/ROBLOX-Dynamic-Npc-Animations](https://github.com/Jessdevzz/ROBLOX-Dynamic-Npc-Animations) | 2 | Dynamische NPC-animaties |
| [Moonpigguy/hl2strider](https://github.com/Moonpigguy/hl2strider) | 1 | Half-Life 2 Strider met IK-procedurele animatie |
| [Ehonix/Dynamo](https://github.com/Ehonix/Dynamo) | 1 | Procedurele animator |
| [skatingii/PerfectSequencer](https://github.com/skatingii/PerfectSequencer) | 1 | Frame-accurate events, ook gelockt aan de timeline van een AnimationTrack |
| [thezoMx/keyframe_uploader](https://github.com/thezoMx/keyframe_uploader) | 1 | Plugin die keyframe-sequences automatisch uploadt |
| [RAMPAGELLC/RBLXKeyframePlayer](https://github.com/RAMPAGELLC/RBLXKeyframePlayer) | 1 | Speelt KeyframeSequences af zonder massa-upload van animatie-ID's |
| [worhasdev/Emote-Class-ROBLOX](https://github.com/worhasdev/Emote-Class-ROBLOX) | 1 | Emote-class met animatie + muziek |
| [Alphanumeriic/roblox-procedural-ik-spider](https://github.com/Alphanumeriic/roblox-procedural-ik-spider) | 0 | Procedurele IK-spin (poten die zich aan de grond aanpassen) |
| [Zekiah-A/dream-roblox-blender-rig](https://github.com/Zekiah-A/dream-roblox-blender-rig) | 0 | Blender-rig met IK, custom bones en wisselbare gezichten |
| [emdomanus/anatomy](https://github.com/emdomanus/anatomy) | 0 | Rig/addon-anatomie: named sockets, surfaces, mounts (accessoires aan rigs koppelen) |
| [CodedBunny/Roblox-Rootmotion](https://github.com/CodedBunny/Roblox-Rootmotion) | 0 | Root motion voor animaties (strict typed) |
| [Storm99999/Motionflow](https://github.com/Storm99999/Motionflow) | 0 | Compacte animatie-engine |
| [gyutedy/FLOTTE-FERRUS](https://github.com/gyutedy/FLOTTE-FERRUS) | 0 | Pipeline: FBX-mocap naar Roblox R15 |
| [Naresh-x86/Mocap-Demo](https://github.com/Naresh-x86/Mocap-Demo) | 0 | Tech-demo van Studio's video-naar-mocap |
| [Aymdma/Roblox-Mocap](https://github.com/Aymdma/Roblox-Mocap) | 0 | Motion capture (Python) naar Roblox |
| [realllityyt/myanimator](https://github.com/realllityyt/myanimator) | 0 | Animaties per ledemaat mixen: crossfade, additive layers, events |

## Movement, physics & characters

Character controllers, ragdolls, destructie, parkour en eigen physics-engines. (51 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [easy-games/chickynoid](https://github.com/easy-games/chickynoid) | 264 | Server-authoritative character controller met client-prediction (anti-speedhack) |
| [jaipack17/Nature2D](https://github.com/jaipack17/Nature2D) | 181 | Volledige 2D-physics-engine in GUI's |
| [MaximumADHD/Character-Realism](https://github.com/MaximumADHD/Character-Realism) | 132 | Realistische characters: hoofd/torso volgen camera, first-person body |
| [MaximumADHD/sm64-roblox](https://github.com/MaximumADHD/sm64-roblox) | 117 | Super Mario 64 bewegingscode geport naar Luau |
| [EgoMoose/Rbx-Gravity-Controller](https://github.com/EgoMoose/Rbx-Gravity-Controller) | 51 | Karakters die zwaartekracht trotseren (lopen op bollen/planeten) |
| [EgoMoose/rbx-wallstick](https://github.com/EgoMoose/rbx-wallstick) | 49 | Karakters plakken aan muren en bewegende objecten |
| [daftcube/orbitlib](https://github.com/daftcube/orbitlib) | 35 | Two-body orbital mechanics (ruimtevaart/planeten-banen) |
| [prisma-dev/delta](https://github.com/prisma-dev/delta) | 30 | Deterministische physics-library (voor rollback/replays) |
| [EgoMooseOldProjects/Custom-Character-Controller](https://github.com/EgoMooseOldProjects/Custom-Character-Controller) | 23 | Custom character controller: op muren lopen |
| [jovannic/ragdoll](https://github.com/jovannic/ragdoll) | 21 | Ragdoll-systeem (van een Roblox-engineer) |
| [boatbomber/AlarmClock](https://github.com/boatbomber/AlarmClock) | 15 | Houdt BaseParts "wakker" in de physics-engine |
| [LeoStormer/ragdoll-system](https://github.com/LeoStormer/ragdoll-system) | 13 | Ragdoll-physics systeem voor games |
| [Bartokens/VoxBreaker](https://github.com/Bartokens/VoxBreaker) | 11 | Voxel-destructie: muren/objecten kapotslaan in blokjes |
| [datlass/PhysicsCharacterController](https://github.com/datlass/PhysicsCharacterController) | 10 | Character controller met mover-constraints |
| [magicoal-nerb/impulse](https://github.com/magicoal-nerb/impulse) | 9 | Luau physics-engine met sequential impulses, herimplementeert Humanoid-physics |
| [ffrostfall/character-interpolation-example](https://github.com/ffrostfall/character-interpolation-example) | 9 | Voorbeeld: character-interpolatie (smooth netwerk-movement) |
| [jaipack17/GuiCollisionService](https://github.com/jaipack17/GuiCollisionService) | 9 | Collision-detectie tussen GUI-elementen (2D-games) |
| [Brawldude2/RagdollService](https://github.com/Brawldude2/RagdollService) | 7 | Ragdoll-module voor alle rig-types |
| [Fizzyhex/BufferModule](https://github.com/Fizzyhex/BufferModule) | 7 | Input-latency oplossen bij physics-items (gooien/vasthouden) |
| [fewkz/character-realism](https://github.com/fewkz/character-realism) | 7 | Verbeterde fork van Character-Realism |
| [ScriptBreakpoint-QK/Realistic-Water-Simulation](https://github.com/ScriptBreakpoint-QK/Realistic-Water-Simulation) | 5 | Realistische water-physics |
| [jaipack17/RayCast2](https://github.com/jaipack17/RayCast2) | 4 | Raycasting voor GUI's (2D) |
| [TheSecondTry/RobloxTAS](https://github.com/TheSecondTry/RobloxTAS) | 4 | Tool-assisted speedrun (TAS) opnemen en afspelen |
| [AngrySalt/Roblox-Grabbing-System](https://github.com/AngrySalt/Roblox-Grabbing-System) | 3 | Physics-based oppakken en slepen (Cook Burgers-stijl) |
| [Ecliptorhizes/Hooksystem](https://github.com/Ecliptorhizes/Hooksystem) | 2 | Dubbele grappling hooks: swingen, in/uit rollen, boost |
| [evilbocchi/jconveyor](https://github.com/evilbocchi/jconveyor) | 2 | Gesimuleerde lopende-band physics voor tycoons |
| [lun-lun-lun-lun/demolish](https://github.com/lun-lun-lun-lun/demolish) | 2 | Voxel-destructie physics (roblox-ts) |
| [jaipack17/rope-swinging](https://github.com/jaipack17/rope-swinging) | 2 | 2D touw-swing physics met GUI's |
| [HappGamr/New-Wall-Collision-Maker](https://github.com/HappGamr/New-Wall-Collision-Maker) | 2 | Maakt extra collision voor te dunne muren (tegen doorglippen) |
| [JonasBuffington/Voxel-Carver](https://github.com/JonasBuffington/Voxel-Carver) | 1 | Geparallelliseerde voxel-destructie, deformatie en slicing |
| [welcomestohell/obby-physics](https://github.com/welcomestohell/obby-physics) | 1 | EnhancedCharacterPhysics als module (betere obby-beweging) |
| [Project-Ptolemy/Project-Gravity-02](https://github.com/Project-Ptolemy/Project-Gravity-02) | 1 | Losse parts in vormen rond je laten zweven met constraints |
| [magicoal-nerb/quakem](https://github.com/magicoal-nerb/quakem) | 1 | Quake-beweging (strafe-jumping, bhop) |
| [Kyr4vex/roblox-ball-movement](https://github.com/Kyr4vex/roblox-ball-movement) | 1 | Ballen-movement: speler zit in een rollende bal |
| [kalidrios/B.E.P](https://github.com/kalidrios/B.E.P) | 1 | Destructie-simulator engine met client micro-batch debris |
| [thezoMx/grappling-hook-roblox](https://github.com/thezoMx/grappling-hook-roblox) | 0 | Momentum-movement: grappling hook, wallrun, dash, slide op eigen physics |
| [ashreigns/advanced-luau-parkour-engine](https://github.com/ashreigns/advanced-luau-parkour-engine) | 0 | Modulair OOP movement/parkour-framework |
| [mimatic/ClimbingSystems](https://github.com/mimatic/ClimbingSystems) | 0 | Klimsysteem dat ook met Roblox-terrain werkt |
| [Nooble12/Roblox-Movement-System](https://github.com/Nooble12/Roblox-Movement-System) | 0 | Wall mantle / klimmen |
| [kipuki/zelda-recall-mechanic](https://github.com/kipuki/zelda-recall-mechanic) | 0 | "Recall" uit Zelda: Tears of the Kingdom nagebouwd (objecten terugspoelen in de tijd) |
| [kipuki/skydiving-game-mechanics](https://github.com/kipuki/skydiving-game-mechanics) | 0 | Skydiving-mechanics |
| [Zyn-ic/LedgeGrabLogic](https://github.com/Zyn-ic/LedgeGrabLogic) | 0 | Ledge-grab detectie en snapping |
| [SilverLaw999/roblox-physics-simulation](https://github.com/SilverLaw999/roblox-physics-simulation) | 0 | Verlet-physics: vloeistof die klotst, doek in de wind, constraint solving |
| [spavdigital/roblox-sprint-stamina](https://github.com/spavdigital/roblox-sprint-stamina) | 0 | Server-authoritative sprinten + stamina |
| [Caram3lInu/GrabSystem](https://github.com/Caram3lInu/GrabSystem) | 0 | Grab-systeem (objecten oppakken) |
| [unixtensor/OpenXen](https://github.com/unixtensor/OpenXen) | 0 | Physics- en collision-engine vanaf nul in Luau |
| [mkl48/Chunkr](https://github.com/mkl48/Chunkr) | 0 | Teardown-achtige voxel-destructie: rigid bodies, fracture-patronen, structurele stress |
| [debugasync/Rubble](https://github.com/debugasync/Rubble) | 0 | Lokale destructie op impactpunt via GeometryService fragment-API |
| [darel919/kemudi](https://github.com/darel919/kemudi) | 0 | Soft-body physics (WIP) |
| [ramsa-rgb/Rope-Type-Elevator](https://github.com/ramsa-rgb/Rope-Type-Elevator) | 0 | Lift aan kabels via de physics-engine |
| [Pepsied-5229/RBX-Constraints](https://github.com/Pepsied-5229/RBX-Constraints) | 0 | Voorbeelden van alle soorten physics-constraints |

## Voertuigen, boten & treinen

Chassis, suspensie, hover, raketten, drijfvermogen en treinen. (17 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [lisphm/A-Chassis](https://github.com/lisphm/A-Chassis) | 102 | Officieel A-Chassis: realistische auto's en motoren |
| [anywaymachines/overengineered](https://github.com/anywaymachines/overengineered) | 31 | Complete sandbox-game: voertuigen bouwen en slopen (roblox-ts, open-source) |
| [LeehamsonThe3rd/raycastsuspensionwheel](https://github.com/LeehamsonThe3rd/raycastsuspensionwheel) | 16 | Wielen met raycast-suspensie i.p.v. physics-wielen (stabieler, arcade) |
| [chedsapp/rowheel](https://github.com/chedsapp/rowheel) | 8 | Rust-app: echt racestuur + force feedback in Roblox |
| [anthony0br/RocketSys](https://github.com/anthony0br/RocketSys) | 7 | Realistische raket- en projectiel-physics |
| [OpenChassis/OpenChassis](https://github.com/OpenChassis/OpenChassis) | 5 | Open-source gemotoriseerd voertuig-chassis |
| [ribzix/nomernoy-trainkit](https://github.com/ribzix/nomernoy-trainkit) | 4 | Trein-kit gebaseerd op Roblox-physics |
| [totallyahuman445/Roblox-Entity-RA](https://github.com/totallyahuman445/Roblox-Entity-RA) | 2 | Entity's RA land-voertuig chassis (auto's, motoren) |
| [EricApostal/car-physics-playground](https://github.com/EricApostal/car-physics-playground) | 2 | Experimentele softbody-physics voor auto's |
| [Astrophsica/Racing-Kit-Roblox](https://github.com/Astrophsica/Racing-Kit-Roblox) | 2 | Open-source go-kart racing kit |
| [ProfessorOfK3ology/RobloxFlightSim](https://github.com/ProfessorOfK3ology/RobloxFlightSim) | 2 | Open-source flight simulator |
| [Rung2ne/A-Chassis-Realistic-Manual](https://github.com/Rung2ne/A-Chassis-Realistic-Manual) | 2 | Realistischere handgeschakelde versnellingsbak voor A-Chassis |
| [muzscripter/buoyancy](https://github.com/muzscripter/buoyancy) | 1 | Drijfvermogen (buoyancy) nabootsen |
| [1nOnlyMinhaz/TrainStackX](https://github.com/1nOnlyMinhaz/TrainStackX) | 1 | Framework voor treinen bouwen en beheren |
| [Kaminoan-Engineers/repulsyn](https://github.com/Kaminoan-Engineers/repulsyn) | 0 | Modulair repulsorlift/hover-systeem voor land-, zee- en luchtvoertuigen |
| [cassicoder/boat-game](https://github.com/cassicoder/boat-game) | 0 | Boot-game: Matter ECS + Gerstner-oceaan + drijfvermogen + vissen |
| [HassanJN66/roblox-vehicle-framework](https://github.com/HassanJN66/roblox-vehicle-framework) | 0 | Raycast-wielen + soft physics body, FWD/RWD/AWD |

## Combat, hitboxes & wapens

Melee-hitboxes, projectielen, guns, lag-compensatie en zones. (40 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [1ForeverHD/ZonePlus](https://github.com/1ForeverHD/ZonePlus) | 101 | Zones: spelers/parts binnen gebieden detecteren |
| [Swordphin/raycastHitboxRbxl](https://github.com/Swordphin/raycastHitboxRbxl) | 70 | Klassieke RaycastHitbox voor melee-wapens |
| [LDGerrits/QuickZone](https://github.com/LDGerrits/QuickZone) | 55 | Physics-vrije spatial queries (BVH), 60 FPS met 1M+ zones |
| [Nyemse/SPEARHEAD](https://github.com/Nyemse/SPEARHEAD) | 50 | Gratis wapensysteem (FPS) |
| [1Axen/Secure-Cast](https://github.com/1Axen/Secure-Cast) | 30 | Server-authoritative projectielen met lag-compensatie |
| [RedTrioVirus/HitboxClass](https://github.com/RedTrioVirus/HitboxClass) | 28 | Eenvoudige maar krachtige hitbox-class |
| [weenachuangkud/FastCast2](https://github.com/weenachuangkud/FastCast2) | 27 | FastCast met Parallel Luau, object pooling en strikte types |
| [TeamSwordphin/ShapecastHitbox](https://github.com/TeamSwordphin/ShapecastHitbox) | 22 | Shapecast-gebaseerde melee-hitboxes (opvolger RaycastHitbox) |
| [Vel136/Vetra](https://github.com/Vel136/Vetra) | 10 | Analytische baan-projectielen: pierce, bounce, hi-fi raycasting |
| [skyriverstudios/Zoner](https://github.com/skyriverstudios/Zoner) | 10 | Gebruiksvriendelijke zone-queries |
| [howmanysmall/fast-rotated-region3](https://github.com/howmanysmall/fast-rotated-region3) | 5 | Snellere GJK rotated region3 (collisie-checks) |
| [vbaumel1337/central](https://github.com/vbaumel1337/central) | 4 | Server-authoritative hitbox/ray/shapecast queries met latency-compensatie |
| [shmove/roblox-melee-movement-system](https://github.com/shmove/roblox-melee-movement-system) | 4 | Melee- en movement-scripts |
| [datlass/Turret-Controller](https://github.com/datlass/Turret-Controller) | 3 | Turret-controller (richten met constraints) |
| [TheRealUwie/OpenRBLXFightEngine](https://github.com/TheRealUwie/OpenRBLXFightEngine) | 3 | Open-source fighting-game engine |
| [weebweeb/ParticleGun_rbx](https://github.com/weebweeb/ParticleGun_rbx) | 2 | Projectielen gevisualiseerd met ParticleEmitters (goedkoop, veel kogels) |
| [Lolekic/HomingCast](https://github.com/Lolekic/HomingCast) | 2 | Gesimuleerde homing-projectielen zonder Roblox-physics |
| [WBlair1/roblox-bg-system](https://github.com/WBlair1/roblox-bg-system) | 2 | Battlegrounds-systeem met skills en effects (op WCS) |
| [Gskartwii/roblox-sf-analysis](https://github.com/Gskartwii/roblox-sf-analysis) | 2 | Analytische engine voor sword fighting (declaratief) |
| [dodisteigmeier807-coder/RollbackNet](https://github.com/dodisteigmeier807-coder/RollbackNet) | 1 | Experimenteel: rollback lag-compensatie + recoil-validatie met buffers |
| [REALEncryptal/Hindsight](https://github.com/REALEncryptal/Hindsight) | 1 | Gegeneraliseerde hit-detectie met lag-compensated rollback voor guns |
| [monobrov1234/CombatSystems](https://github.com/monobrov1234/CombatSystems) | 1 | Voertuig- en wapen-library |
| [Khann05/Roblox-Tool-Prison-ShowCase](https://github.com/Khann05/Roblox-Tool-Prison-ShowCase) | 1 | Unieke tools: BlackHole, Telekinesis, LaserBeam e.a. |
| [a04855089-hash/RobloxCombatSystem](https://github.com/a04855089-hash/RobloxCombatSystem) | 1 | Server-authoritative combat: combo's, parry, dodge, anti-exploit (typed Luau) |
| [Mythus-Z/Roblox-Combat-System](https://github.com/Mythus-Z/Roblox-Combat-System) | 1 | Server-side combat met combo's en status-effecten |
| [unnixu/ZO-like-Combat-System](https://github.com/unnixu/ZO-like-Combat-System) | 1 | Zwaardvecht-systeem gebaseerd op ZO Samurai |
| [jasonconba/CIA-SAC-ACS](https://github.com/jasonconba/CIA-SAC-ACS) | 1 | Verbeterde fork van Advanced Combat System (ACS) |
| [jiwonz/bump.luau](https://github.com/jiwonz/bump.luau) | 1 | Collision-detectie library (bump.lua) |
| [nsawill1405/Hitbox-Plus](https://github.com/nsawill1405/Hitbox-Plus) | 1 | Spatial-query hitboxes met lag-compensatie hooks en debug-visualisatie |
| [Kyr4vex/predictive-bullet-path](https://github.com/Kyr4vex/predictive-bullet-path) | 1 | Kogel-ricochet voorspellen en tonen, met glas dat breekt |
| [jun-ro/SCF](https://github.com/jun-ro/SCF) | 1 | Simple Combat Framework voor combat-games |
| [banowey/roblox-server-authoritative-gun-system](https://github.com/banowey/roblox-server-authoritative-gun-system) | 0 | Raycast-guns met lag-compensatie en wapen-inheritance |
| [Synphrax/roblox-combat-system](https://github.com/Synphrax/roblox-combat-system) | 0 | Rojo combat-prototype: blocking, combo's, state management |
| [jjophoven/ProtomainsOfEastAndWest](https://github.com/jjophoven/ProtomainsOfEastAndWest) | 0 | Pokémon-achtig battle-systeem |
| [Vasco888888/sword-duelists](https://github.com/Vasco888888/sword-duelists) | 0 | Zwaardduel-game |
| [text21/Rewind](https://github.com/text21/Rewind) | 0 | Lag-compensatie framework voor hit-validatie, projectielen en melee |
| [tralfa42real/roblox-combat-framework](https://github.com/tralfa42real/roblox-combat-framework) | 0 | Server-authoritative combat: combo's, cooldowns, stamina |
| [voidxz9999/roblox-skill-system](https://github.com/voidxz9999/roblox-skill-system) | 0 | Modulair skill-systeem |
| [DanieiR/Roblox-Fishing-Fight-System](https://github.com/DanieiR/Roblox-Fishing-Fight-System) | 0 | Deterministische vis-minigame (server-authoritative) |
| [Aeronautiac/ffRpgLuau](https://github.com/Aeronautiac/ffRpgLuau) | 0 | Fighting/RPG-core met client prediction en ping-compensatie |

## AI, NPC's & machine learning

Neurale netwerken, behavior trees, pathfinding, boids en LLM-NPC's. (25 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [ahmicy/simplepath](https://github.com/ahmicy/simplepath) | 70 | Pathfinding voor humanoids en non-humanoids in een paar regels |
| [prooheckcp/RobloxStateMachine](https://github.com/prooheckcp/RobloxStateMachine) | 41 | State machines met states en transitions (NPC/game-flow) |
| [Kironte/Roblox-Neural-Network-Library](https://github.com/Kironte/Roblox-Neural-Network-Library) | 39 | Object-georiënteerde neurale netwerken |
| [AqwamCreates/DataPredict](https://github.com/AqwamCreates/DataPredict) | 23 | Machine learning library: 100+ modellen incl. reinforcement learning |
| [bstummer/openskill.lua](https://github.com/bstummer/openskill.lua) | 22 | Weng-Lin rating (TrueSkill-alternatief) voor matchmaking/ranked |
| [boatbomber/AIConversation](https://github.com/boatbomber/AIConversation) | 18 | Praten met LLM-chatbots vanuit Roblox |
| [snipcola/Roblox-AI](https://github.com/snipcola/Roblox-AI) | 17 | Word een AI in Roblox (LLM bestuurt een character) |
| [littensy/nanoai](https://github.com/littensy/nanoai) | 9 | Minimale library voor neurale netwerken |
| [Project-Ptolemy/ProjectUAI](https://github.com/Project-Ptolemy/ProjectUAI) | 9 | Universele AI-agent die in Roblox draait (Claude Code-achtige loop) |
| [Axp3cter/Arbor](https://github.com/Axp3cter/Arbor) | 3 | Composable, getypeerde behavior trees voor NPC-AI |
| [Echolewron/rbx-enemy-ai](https://github.com/Echolewron/rbx-enemy-ai) | 3 | Vijand-AI: patrouilleren, achtervolgen, verstoppen |
| [elcapykkzxd/NavPathX](https://github.com/elcapykkzxd/NavPathX) | 3 | Geoptimaliseerde fork van SimplePath |
| [StephenSHorton/navigate](https://github.com/StephenSHorton/navigate) | 3 | Composable pathfinding-suite voor roblox-ts |
| [Daemon6109/AStarPathfinding](https://github.com/Daemon6109/AStarPathfinding) | 2 | A* zoekalgoritme in Luau (eigen grids) |
| [glindberg2000/roblox_ai](https://github.com/glindberg2000/roblox_ai) | 2 | AI-gestuurd NPC-systeem (LLM) |
| [ProtonDev-sys/StridePath](https://github.com/ProtonDev-sys/StridePath) | 2 | Strict pathfinding met cached navgrid en jump-aware waypoints |
| [regibus361/AIBusPassengers](https://github.com/regibus361/AIBusPassengers) | 1 | NPC-passagiers voor bus-games |
| [luandrew66-ctrl/SmartNPC](https://github.com/luandrew66-ctrl/SmartNPC) | 1 | AI-NPC's met gesprekken, geheugen en behavior trees |
| [nsawill1405/Pathfinding-Plus](https://github.com/nsawill1405/Pathfinding-Plus) | 1 | Crowd-aware pathfinding met replanning en agent-coördinatie |
| [gdr1461/GPath](https://github.com/gdr1461/GPath) | 1 | Tool voor makkelijke pathfinding-systemen |
| [Escalate17/samskriti-luau](https://github.com/Escalate17/samskriti-luau) | 1 | NPC's die onthouden hoe je ze behandelde (emotionele staat, zonder LLM) |
| [treebarkbr/RoNet](https://github.com/treebarkbr/RoNet) | 0 | Tensors, transformer-modellen en BPE-tokenizer in pure Luau |
| [TuneScotty/TinyMNIST](https://github.com/TuneScotty/TinyMNIST) | 0 | Cijferherkenning (MNIST) die volledig in Roblox draait |
| [sebastianboscan/roblox-ai-npc](https://github.com/sebastianboscan/roblox-ai-npc) | 0 | NPC's die natuurlijke taal via TextGenerator omzetten in acties |
| [Murned/roblox-boid-flocking](https://github.com/Murned/roblox-boid-flocking) | 0 | Drone-zwerm met Reynolds' boids + spatial grid |

## Procedurele generatie & wiskunde

Voxels, dungeons, doolhoven, wave function collapse, noise en curves. (22 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [real2nix/mineblox](https://github.com/real2nix/mineblox) | 68 | Uitbreidbare voxel-engine (Minecraft-achtig) |
| [Sleitnick/rbxts-octo-tree](https://github.com/Sleitnick/rbxts-octo-tree) | 29 | Octree voor snelle ruimtelijke lookups |
| [EgoMooseOldProjects/Dungeon-generator](https://github.com/EgoMooseOldProjects/Dungeon-generator) | 19 | Dungeon-generatie module |
| [EgoMoose/PolyBool-Lua](https://github.com/EgoMoose/PolyBool-Lua) | 16 | Boolean-operaties op polygonen (union, intersect, difference) |
| [Sleitnick/RDC2019-Procedural-Generation](https://github.com/Sleitnick/RDC2019-Procedural-Generation) | 14 | Materiaal van de RDC2019 talk over procedurele generatie |
| [bstummer/bezier](https://github.com/bstummer/bezier) | 12 | Bézier-curves van elke graad met arc-length parametrisatie |
| [vocksel/geo](https://github.com/vocksel/geo) | 12 | Geometrische vormherkenning (gebaren tekenen → vorm) |
| [bstummer/matrix](https://github.com/bstummer/matrix) | 4 | Matrix-wiskunde (determinant, inverse, transformaties) |
| [sammy0127/WavyRobloxObby](https://github.com/sammy0127/WavyRobloxObby) | 4 | Obby procedureel gegenereerd met Python |
| [AshR-03/Greedy-Procedural-Maze-Generation-in-Lua](https://github.com/AshR-03/Greedy-Procedural-Maze-Generation-in-Lua) | 3 | Stack-gebaseerde procedurele doolhoven |
| [RyanChang25/Dungeon-Generation-Service](https://github.com/RyanChang25/Dungeon-Generation-Service) | 3 | Semi-procedurele dungeon-layouts |
| [nightcycle/node](https://github.com/nightcycle/node) | 3 | Node-netwerken + wave function collapse generatie |
| [nightcycle/noise](https://github.com/nightcycle/noise) | 3 | Meerdere noise-stijlen (Perlin, Simplex...) met seeds |
| [ffrostfall/polybool-luau](https://github.com/ffrostfall/polybool-luau) | 2 | Polygon boolean-operaties in Luau |
| [AidenTran900/markov-luau](https://github.com/AidenTran900/markov-luau) | 1 | MarkovJunior / Wave Function Collapse in Luau |
| [Mythus-Z/Procedural-Dungeon-Generation-Roblox-](https://github.com/Mythus-Z/Procedural-Dungeon-Generation-Roblox-) | 1 | Voxel-dungeons: 2000 kamers / 100k voxels in < 1 seconde |
| [Bryan0-0AG/Procedural-Dungeon-Generator_Roblox-Studio](https://github.com/Bryan0-0AG/Procedural-Dungeon-Generator_Roblox-Studio) | 1 | Vertakkende dungeons met gewogen kamer-templates en collision-checks |
| [MingauRM/noisepp](https://github.com/MingauRM/noisepp) | 1 | Extra noise-types voorbij math.noise |
| [ddavness/curve](https://github.com/ddavness/curve) | 1 | Analytisch gedefinieerde 3D-curves maken en beheren |
| [D3-4D/MGen](https://github.com/D3-4D/MGen) | 0 | Backtracking doolhof-algoritme |
| [noahssjursen-code/proceduralObbyRobloxStudio](https://github.com/noahssjursen-code/proceduralObbyRobloxStudio) | 0 | Procedureel gegenereerde obby's |
| [Arav-ThewebMaker/Roblox-Maze-System](https://github.com/Arav-ThewebMaker/Roblox-Maze-System) | 0 | Doolhoven genereren én oplossen |

## Networking & replicatie

Buffer-netcode, IDL-compilers, encryptie en eigen replicatie. (37 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [red-blox/zap](https://github.com/red-blox/zap) | 188 | IDL-compiler (Rust) die razendsnelle buffer-netcode genereert |
| [1Axen/blink](https://github.com/1Axen/blink) | 184 | IDL-compiler in Luau voor buffer-networking met type-safety |
| [ffrostfall/ByteNet](https://github.com/ffrostfall/ByteNet) | 181 | Moderne buffer-gebaseerde networking-library |
| [roblox-aurora/rbx-net](https://github.com/roblox-aurora/rbx-net) | 108 | Geavanceerd multi-language networking-framework |
| [MadStudioRoblox/Replica](https://github.com/MadStudioRoblox/Replica) | 75 | Server-naar-client state-replicatie (opvolger ReplicaService) |
| [ffrostfall/BridgeNet2](https://github.com/ffrostfall/BridgeNet2) | 72 | Razendsnelle networking-library |
| [boatbomber/EncryptedNet](https://github.com/boatbomber/EncryptedNet) | 59 | Versleutelde remotes: ECDH key-exchange + ChaCha20 |
| [RoSocket/rosocket](https://github.com/RoSocket/rosocket) | 52 | WebSocket-ondersteuning in Roblox via een relay-server |
| [littensy/remo](https://github.com/littensy/remo) | 45 | Simpele, getypeerde remote-library |
| [YetAnotherClown/YetAnotherNet](https://github.com/YetAnotherClown/YetAnotherNet) | 27 | Data-driven networking voor ECS (deprecated, goede referentie) |
| [Axp3cter/Lync](https://github.com/Axp3cter/Lync) | 21 | Gebatchte binaire networking: delta-encoded, 1 RemoteEvent per frame |
| [playcurrent/shards](https://github.com/playcurrent/shards) | 13 | Spelers in regio's indelen voor lagere matchmaking-latency |
| [Reselim/rbx-engine.io](https://github.com/Reselim/rbx-engine.io) | 13 | Engine.IO (Socket.IO) client voor Roblox |
| [EgoMoose/Rbx-Replication](https://github.com/EgoMoose/Rbx-Replication) | 12 | Eigen replicatie-systeem los van Roblox' standaard replicatie |
| [R-unic/tether](https://github.com/R-unic/tether) | 12 | Message-based networking met binaire serialisatie en validatie |
| [AlexanderLindholt/PacketPlus](https://github.com/AlexanderLindholt/PacketPlus) | 8 | Verbeterde versie van de Packet networking-library |
| [vocksel/matter-replication](https://github.com/vocksel/matter-replication) | 7 | Replicatie voor Matter ECS |
| [dig1t/red](https://github.com/dig1t/red) | 6 | Event-driven server↔client en server↔server communicatie |
| [optimisticside/messenger](https://github.com/optimisticside/messenger) | 6 | Lichtgewicht cross-server messaging |
| [CavefulGames/HandyNet](https://github.com/CavefulGames/HandyNet) | 5 | Handigere ByteNet-fork |
| [tacheometry/SimpleSignals](https://github.com/tacheometry/SimpleSignals) | 5 | RemoteEvents zonder boilerplate |
| [Mullets-Gavin/Network](https://github.com/Mullets-Gavin/Network) | 5 | Wrapper rond remotes en bindables |
| [iconmaster5326/RbxRPC](https://github.com/iconmaster5326/RbxRPC) | 4 | RemoteEvents automatisch beheren (RPC) |
| [Stratiz/DataStream](https://github.com/Stratiz/DataStream) | 4 | Data-replicatie-oplossing |
| [cg955gtr/SwitchNet](https://github.com/cg955gtr/SwitchNet) | 3 | Snelle networking die bandbreedte en overhead verlaagt |
| [walksanatora/WorldQL_RBXL](https://github.com/walksanatora/WorldQL_RBXL) | 3 | Servers syncen met WorldQL (gedeelde wereld over servers) |
| [8ch32bit/ReplicatedTweening](https://github.com/8ch32bit/ReplicatedTweening) | 3 | Tweens op de server maken die soepel op clients afspelen |
| [HylianBasement/netbuilder](https://github.com/HylianBasement/netbuilder) | 3 | Declaratieve networking-library |
| [demi-dog/duplecs](https://github.com/demi-dog/duplecs) | 2 | Gegeneraliseerde high-performance replicatie voor jecs (ECS) |
| [rbxxaxa/replicant](https://github.com/rbxxaxa/replicant) | 2 | Server-authoritative gerepliceerde componenten |
| [isoopod/PakNet](https://github.com/isoopod/PakNet) | 1 | Geschematiseerde networking-library |
| [andrian-syh/rblx-twill](https://github.com/andrian-syh/rblx-twill) | 1 | Modulair framework: boot order, bewaakte networking, state-replicatie |
| [bainchild/rpc2-rs](https://github.com/bainchild/rpc2-rs) | 1 | Bidirectionele RPC tussen Roblox en Rust |
| [debugasync/FogWar](https://github.com/debugasync/FogWar) | 0 | Fog-of-war replicatie: clients krijgen alleen posities die ze echt kunnen zien (anti-wallhack) |
| [ujji-k06/remotelens](https://github.com/ujji-k06/remotelens) | 0 | Remote-activiteit meten (netwerk-instrumentatie) |
| [thekingofspace/Reflect](https://github.com/thekingofspace/Reflect) | 0 | Sync-systeem |
| [ocauapaz/BTYN](https://github.com/ocauapaz/BTYN) | 0 | Networking-compiler: schema naar gebatchte, delta-encoded Luau |

## ECS & game-architectuur

Entity Component Systems en frameworks voorbij Knit. (21 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [Ukendio/jecs](https://github.com/Ukendio/jecs) | 467 | Snelle, data-oriented ECS voor Luau (relaties, archetypes) |
| [rbxts-flamework/core](https://github.com/rbxts-flamework/core) | 159 | Flamework: uitbreidbaar game-framework met decorators/DI (roblox-ts) |
| [matter-ecs/matter](https://github.com/matter-ecs/matter) | 116 | Moderne ECS met hot-reloading en debugger |
| [centau/ecr](https://github.com/centau/ecr) | 60 | Sparse-set gebaseerde ECS |
| [rbxts-flamework/jecs](https://github.com/rbxts-flamework/jecs) | 49 | jecs-wrapper voor Flamework (roblox-ts) |
| [teamfireworks/gargantuan](https://github.com/teamfireworks/gargantuan) | 46 | Onafhankelijke game-engine voor Roblox-devs (SDL3) |
| [welcomestohell/prvdmwrong](https://github.com/welcomestohell/prvdmwrong) | 36 | Uitbreidbaar provider-framework (Knit-alternatief) |
| [Sleitnick/rbxts-proton](https://github.com/Sleitnick/rbxts-proton) | 23 | Experimenteel game-framework voor roblox-ts |
| [Iron-Stag-Games/Pronghorn](https://github.com/Iron-Stag-Games/Pronghorn) | 15 | Direct module-framework voor snelle ontwikkeling |
| [sayhisam1/Stitch](https://github.com/sayhisam1/Stitch) | 15 | Simpele, uitbreidbare ECS |
| [ItipatS/RPGJECS](https://github.com/ItipatS/RPGJECS) | 14 | Server-authoritative RPG-framework gebouwd op jecs |
| [featherfall-org/quill](https://github.com/featherfall-org/quill) | 14 | Strikt getypeerd singletons & components framework |
| [LDGerrits/Bootstrapper](https://github.com/LDGerrits/Bootstrapper) | 10 | Module-loader/scheduler: bepaal exact wat elke frame draait en in welke volgorde |
| [baxoplenty/quebec](https://github.com/baxoplenty/quebec) | 10 | Modulair framework met services, controllers en opt-in dependencies |
| [AetherInteractiveLtd/Tina](https://github.com/AetherInteractiveLtd/Tina) | 9 | High-tech framework voor experiences |
| [SecondNewtonLaw/VEngine](https://github.com/SecondNewtonLaw/VEngine) | 9 | Type-safe game-development framework |
| [OverlineJunior/toucan](https://github.com/OverlineJunior/toucan) | 8 | Opinionated ECS-framework (roblox-ts) |
| [Stratiz/Eden](https://github.com/Stratiz/Eden) | 7 | Lichtgewicht, flexibel game-framework |
| [ryancundiff/chief](https://github.com/ryancundiff/chief) | 2 | Volledig getypeerd, getest module-framework |
| [zblox164/Scrypt](https://github.com/zblox164/Scrypt) | 1 | Scrypt-framework |
| [ZacharyVanier/VZNCore-Template](https://github.com/ZacharyVanier/VZNCore-Template) | 0 | Batteries-included ECS-framework template |

## UI & interface

Reactieve UI, custom tekst, inventories, 2D-engines en mobiele controls. (88 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [SirMallard/Iris](https://github.com/SirMallard/Iris) | 352 | Immediate-mode GUI (Dear ImGui) voor debug- en dev-tools |
| [centau/vide](https://github.com/centau/vide) | 330 | Reactieve UI-library (Fusion-alternatief, heel snel) |
| [ryanlua/satchel](https://github.com/ryanlua/satchel) | 132 | Moderne vervanging van de standaard backpack |
| [flipbook-labs/flipbook](https://github.com/flipbook-labs/flipbook) | 125 | Storybook voor Roblox UI (componenten los bekijken) |
| [boatbomber/Highlighter](https://github.com/boatbomber/Highlighter) | 99 | Syntax highlighting van Lua-code in RichText |
| [loneka/onyx-ui](https://github.com/loneka/onyx-ui) | 59 | Kant-en-klare componenten voor Fusion |
| [notreux/UpsideEngine](https://github.com/notreux/UpsideEngine) | 46 | 2D game-engine voor Roblox |
| [ffrostfall/fluid](https://github.com/ffrostfall/fluid) | 40 | Declaratief UI-framework |
| [nightcycle/synthetic](https://github.com/nightcycle/synthetic) | 40 | Google Material Design UI-library voor Fusion |
| [cascadeui/Cascade](https://github.com/cascadeui/Cascade) | 39 | UI-library in macOS Sequoia-stijl |
| [loneka/avalog](https://github.com/loneka/avalog) | 37 | Complete avatar-catalogus (avatar-editor) in Fusion |
| [AlexanderLindholt/TextPlus](https://github.com/AlexanderLindholt/TextPlus) | 32 | Eigen tekst-rendering met custom fonts |
| [EgoMooseOldProjects/Rbx_CustomFont](https://github.com/EgoMooseOldProjects/Rbx_CustomFont) | 32 | Custom fonts via sprite-sheets |
| [latte-soft/lucide-roblox](https://github.com/latte-soft/lucide-roblox) | 31 | De Lucide icon-set in Roblox |
| [7kayoh/Lydie](https://github.com/7kayoh/Lydie) | 29 | Mooie UI-componenten voor Fusion |
| [cxmeel/colour-utils](https://github.com/cxmeel/colour-utils) | 25 | Kleurmanipulatie-library |
| [inurentto/grid-pack](https://github.com/inurentto/grid-pack) | 24 | Grid/Tetris-stijl inventories (zoals Resident Evil/Tarkov) |
| [kohltastrophe/flux](https://github.com/kohltastrophe/flux) | 20 | Lazy fine-grained reactivity |
| [Perthys/chalk](https://github.com/Perthys/chalk) | 19 | RichText-styling done right |
| [Bytebit-Org/roblox-TouchScreenJoysticks](https://github.com/Bytebit-Org/roblox-TouchScreenJoysticks) | 19 | Meerdere custom touch-joysticks voor mobiele games |
| [creepersaur/quark](https://github.com/creepersaur/quark) | 19 | Simpele reactieve UI-library |
| [ok-nick/LayoutUtil](https://github.com/ok-nick/LayoutUtil) | 19 | UILayouts beheren |
| [encodedlux/sling](https://github.com/encodedlux/sling) | 19 | Moderne reactieve backpack-UI |
| [MiaGobble/ExpressivePrompts](https://github.com/MiaGobble/ExpressivePrompts) | 18 | Volledig aanpasbare ProximityPrompt-UI |
| [MiaGobble/Figma-Import-Assistant](https://github.com/MiaGobble/Figma-Import-Assistant) | 18 | Figma-designs importeren naar Roblox |
| [simplynoni/roblox-material-ui](https://github.com/simplynoni/roblox-material-ui) | 17 | Material Design 3 componenten voor Roact |
| [cameronpcampbell/supercorner](https://github.com/cameronpcampbell/supercorner) | 16 | Figma-achtige smooth corners (squircles) als UICorner-alternatief |
| [seaofvoices/chroma-luau](https://github.com/seaofvoices/chroma-luau) | 16 | Kleurmanipulatie-library |
| [ryanlua/purse](https://github.com/ryanlua/purse) | 16 | Standaard backpack losgekoppeld van CoreGui |
| [evaera/RadialSpriteSheetGenerator](https://github.com/evaera/RadialSpriteSheetGenerator) | 15 | Radiale progress-indicator spritesheets genereren |
| [lopi-py/figblox](https://github.com/lopi-py/figblox) | 15 | Figma → Roblox converter (react-lua) |
| [seaofvoices/react-lua-hooks](https://github.com/seaofvoices/react-lua-hooks) | 15 | Hook-collecties voor React Lua |
| [Zyn-ic/Stoway](https://github.com/Zyn-ic/Stoway) | 13 | Geavanceerd inventory/hotbar-systeem met item-tracking |
| [satyanto/rblxGlassUI](https://github.com/satyanto/rblxGlassUI) | 13 | Glassmorphism UI-library |
| [frappedevs/FusionRouter](https://github.com/frappedevs/FusionRouter) | 12 | Stateful UI-routing in Fusion |
| [rimuy/hook-bag](https://github.com/rimuy/hook-bag) | 11 | Custom Roact-hooks |
| [Reselim/roact-flipper](https://github.com/Reselim/roact-flipper) | 11 | Roact + Flipper animatie-hooks |
| [alexmercier25/Enoria](https://github.com/alexmercier25/Enoria) | 10 | Snel, lichtgewicht UI-framework |
| [TheNexusAvenger/Module3D](https://github.com/TheNexusAvenger/Module3D) | 9 | 3D-modellen in GUI-frames tonen |
| [jammees/Rethink-Engine](https://github.com/jammees/Rethink-Engine) | 9 | Veelzijdige 2D game-engine voor Roblox |
| [RadiatedExodus/LuaTextBox](https://github.com/RadiatedExodus/LuaTextBox) | 8 | Tekstveld met Lua-syntax highlighting + autocomplete (in-game code-editor) |
| [boatbomber/SmoothScroll](https://github.com/boatbomber/SmoothScroll) | 7 | Smooth scrolling voor ScrollingFrames |
| [daimond113/lexi](https://github.com/daimond113/lexi) | 7 | Lokalisatie/vertaling voor Vide |
| [roblox-aurora/roact-dnd](https://github.com/roblox-aurora/roact-dnd) | 7 | Drag & drop voor Roact |
| [kotdes/Koute](https://github.com/kotdes/Koute) | 7 | Router-library voor Fusion |
| [Blupo/Color](https://github.com/Blupo/Color) | 7 | Kleurbeheer en -manipulatie library |
| [Shadercloud/rbxts-react-clean-ui](https://github.com/Shadercloud/rbxts-react-clean-ui) | 7 | Nette React-componentenbibliotheek voor roblox-ts |
| [twinrbx/donation-board](https://github.com/twinrbx/donation-board) | 7 | Donatie-bord met strakke UI |
| [TenebrisNoctua/FusionFoundation](https://github.com/TenebrisNoctua/FusionFoundation) | 6 | Roblox' Foundation UI-library geport naar Fusion |
| [Vvshenok/SpotlightUI](https://github.com/Vvshenok/SpotlightUI) | 6 | Tutorials maken met een "spotlight" die focus legt op UI-elementen |
| [qwreey/quad](https://github.com/qwreey/quad) | 6 | Reactieve rendering-library voor Roblox en GTK |
| [TheNexusAvenger/Nexus-Button](https://github.com/TheNexusAvenger/Nexus-Button) | 5 | Multi-input knop (muis, touch, gamepad) |
| [AlexanderLindholt/LuauXML](https://github.com/AlexanderLindholt/LuauXML) | 5 | XML naar Luau converter (fonts voor TextPlus) |
| [OMouta/Rex](https://github.com/OMouta/Rex) | 5 | Declaratief UI-framework in React/Vue-stijl |
| [DestinEcarma/draggable](https://github.com/DestinEcarma/draggable) | 5 | Vervanging voor de verouderde Draggable-property |
| [AwesomePossum212/nametag-plus](https://github.com/AwesomePossum212/nametag-plus) | 5 | Modulaire nametags met titels en healthbars |
| [TheNexusAvenger/Nexus-Virtual-List](https://github.com/TheNexusAvenger/Nexus-Virtual-List) | 4 | Lange lijsten efficiënt tonen (virtualisatie) |
| [voxelcrw/Zeno3D](https://github.com/voxelcrw/Zeno3D) | 4 | 3D-objecten in 2D-perspectief tonen (herschrijving van Module3D) |
| [btc7274/control-hints](https://github.com/btc7274/control-hints) | 4 | Genereert control-hints UI op basis van het Input Action System |
| [imacodr/Construct](https://github.com/imacodr/Construct) | 4 | Componentenbibliotheek voor Fusion met geavanceerde theming |
| [Mt-roblox/Mt](https://github.com/Mt-roblox/Mt) | 4 | Window manager + extra GUI-objecten |
| [Kilozen/DragonPaint](https://github.com/Kilozen/DragonPaint) | 4 | Tool om character-kleuren te plannen |
| [visualized-node/nebulous-framework](https://github.com/visualized-node/nebulous-framework) | 4 | UI-framework met events via attributes |
| [Ukuroks-games/2d-adventure](https://github.com/Ukuroks-games/2d-adventure) | 3 | "Engine" voor 2D-games in Roblox |
| [AstonishedLiker/HyperText](https://github.com/AstonishedLiker/HyperText) | 3 | RichText veilig manipuleren |
| [evilbocchi/decillion](https://github.com/evilbocchi/decillion) | 3 | Million.js-achtige optimalisatie voor React in roblox-ts |
| [unrooot/keyframes](https://github.com/unrooot/keyframes) | 3 | Compacte UI-animatielibrary met keyframes |
| [gaymeowing/quantize-luau](https://github.com/gaymeowing/quantize-luau) | 2 | MMCQ kleur-kwantisatie (dominante kleuren uit afbeeldingen) |
| [spin-the-hexagon/rover](https://github.com/spin-the-hexagon/rover) | 2 | Next-gen UI-framework |
| [project-aether-ui/aether](https://github.com/project-aether-ui/aether) | 2 | Headless UI: één component draait in Roblox, desktop en CI |
| [CavefulGames/i18nom](https://github.com/CavefulGames/i18nom) | 1 | Lokalisatie voor reactieve UI-libraries |
| [gdr1461/GEditor](https://github.com/gdr1461/GEditor) | 1 | In-game script-editor interface |
| [Novaly-Studios/UIParticle](https://github.com/Novaly-Studios/UIParticle) | 1 | Particles in de UI |
| [nebula-neru/rbxVN](https://github.com/nebula-neru/rbxVN) | 1 | Visual novels maken in Roblox |
| [ZyCrypticz/HoverFX](https://github.com/ZyCrypticz/HoverFX) | 1 | Hover-animaties en interactieve effecten voor knoppen |
| [optimisticside/ronaco](https://github.com/optimisticside/ronaco) | 1 | De Monaco-editor (VS Code-editor) geport naar Roblox |
| [debxylen/Rui](https://github.com/debxylen/Rui) | 1 | Reactief-declaratief UI-framework |
| [ImDragonxd07/Screenlab](https://github.com/ImDragonxd07/Screenlab) | 1 | GUI-gebaseerde 2D game-engine |
| [Alexpoopy1/HTMLuau](https://github.com/Alexpoopy1/HTMLuau) | 1 | HTML direct in Roblox Luau bouwen |
| [port22exposed/rbxcreate](https://github.com/port22exposed/rbxcreate) | 1 | Syntactic sugar om Instances te declareren met strikte types |
| [Vvshenok/ContextUI](https://github.com/Vvshenok/ContextUI) | 0 | Context- en hover-panelen met docking en pinning |
| [AnotherSubatomo/pii](https://github.com/AnotherSubatomo/pii) | 0 | Pico-size pseudo-immediate-mode UI |
| [rvila94/SimpleToasts](https://github.com/rvila94/SimpleToasts) | 0 | Toast-notificaties zonder dependencies |
| [ninjaninja140/sailboat](https://github.com/ninjaninja140/sailboat) | 0 | Tailwind CSS voor Roblox (roblox-ts React) |
| [RenovateEnv/rblx-lao-renderer](https://github.com/RenovateEnv/rblx-lao-renderer) | 0 | Laotiaans schrift en fonts renderen |
| [spavdigital/roblox-r6-character-creation](https://github.com/spavdigital/roblox-r6-character-creation) | 0 | R6 character-creatie |
| [mmdj04/Luau2DWorld](https://github.com/mmdj04/Luau2DWorld) | 0 | 2D UI game-engine: procedurele wereld, chunks, inventory, fog-of-war |
| [jaipack17/roblox-verlet](https://github.com/jaipack17/roblox-verlet) | 0 | Verlet-integratie projecten in GUI's (touw, doek) |

## Camera & cutscenes

Camera-shake, custom camera's, cutscene-tools en timelines. (13 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [Sleitnick/RbxCameraShaker](https://github.com/Sleitnick/RbxCameraShaker) | 123 | Camera-shake presets en eigen shakes |
| [rduoDevs/CameraService](https://github.com/rduoDevs/CameraService) | 36 | Alternatieve game-camera met veel controle |
| [EgoMoose/patch-roblox-cameramodule](https://github.com/EgoMoose/patch-roblox-cameramodule) | 21 | Patch zodat de camera-API van PlayerModule runtime bereikbaar is |
| [bstummer/CutsceneService](https://github.com/bstummer/CutsceneService) | 11 | Vloeiende cutscenes met Bézier-curves |
| [valutekat/CutsceneStudio-v1.7](https://github.com/valutekat/CutsceneStudio-v1.7) | 2 | Cutscenes maken in Studio |
| [mlwre-off/RoPlay](https://github.com/mlwre-off/RoPlay) | 2 | Replay-recorder en editor (zoals Minecraft Replay Mod) met camera-keyframes |
| [Reapimus/grims-cutscene-engine](https://github.com/Reapimus/grims-cutscene-engine) | 1 | Cutscene-systeem + plugin |
| [nilleniumrust/SpringShaker](https://github.com/nilleniumrust/SpringShaker) | 1 | Camera-shaker met springs + Perlin noise |
| [Seftube/RobloxCameraSystem](https://github.com/Seftube/RobloxCameraSystem) | 1 | Realistisch camerasysteem (volledig lokaal) |
| [Studio713/direct](https://github.com/Studio713/direct) | 0 | Cutscene-director plugin |
| [emdomanus/pulse](https://github.com/emdomanus/pulse) | 0 | Timeline-runtime voor VFX, skill-timelines en cutscenes |
| [netslashh/EasyCutscene2](https://github.com/netslashh/EasyCutscene2) | 0 | Cinematische camera-sequences met cinematic bars |
| [NikMusy/apex-cinematic-cam](https://github.com/NikMusy/apex-cinematic-cam) | 0 | Cinematic camera: freecam, tracking, keyframe-paden, auto-regie |

## Audio

3D-audio, occlusie/reverb, adaptieve muziek en radio. (12 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [Redon-Tech/radio-system](https://github.com/Redon-Tech/radio-system) | 7 | Radiosysteem met de nieuwe voice/sound API's |
| [Interfiber/rbxmidi](https://github.com/Interfiber/rbxmidi) | 6 | Speel Roblox-piano's met een echt MIDI-keyboard |
| [Jupiter-Development-Revamp/PhantomComms](https://github.com/Jupiter-Development-Revamp/PhantomComms) | 3 | Proximity-chat voor RP- en horrorgames |
| [Mullets-Gavin/DiceSound](https://github.com/Mullets-Gavin/DiceSound) | 2 | Loops, playlists en soft stops zonder memory leaks |
| [Nazuh2/Team-VC-Module](https://github.com/Nazuh2/Team-VC-Module) | 1 | Team-voicechat module |
| [therealbytecore/BetterSound](https://github.com/therealbytecore/BetterSound) | 0 | 3D-audio, fades, adaptieve muziek, ducking, reverb-zones, soundscapes in één API |
| [8ava/insono](https://github.com/8ava/insono) | 0 | Wiskundig geluid dempen en laten galmen rond de speler (occlusie/reverb) |
| [scrpt2r/soundHandler](https://github.com/scrpt2r/soundHandler) | 0 | Modulair audio-framework |
| [Accutrix/SoundStablizer](https://github.com/Accutrix/SoundStablizer) | 0 | Voorkomt dat geluiden te hard worden |
| [ryleighhhhhh/Score](https://github.com/ryleighhhhhh/Score) | 0 | Dynamische muziek-handler |
| [DebianCatt/Dynamic-Footsteps-for-Roblox](https://github.com/DebianCatt/Dynamic-Footsteps-for-Roblox) | 0 | Dynamische voetstappen per materiaal |
| [danijayvv/Erika](https://github.com/danijayvv/Erika) | 0 | Audio-visualizer library |

## VR & motion tracking

Full-body VR, SteamVR-trackers en webcam-tracking. (14 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [TheNexusAvenger/Nexus-VR-Character-Model](https://github.com/TheNexusAvenger/Nexus-VR-Character-Model) | 90 | Roblox-characters mappen op VR-input (volledig lichaam in VR) |
| [saucekid/sauceVR](https://github.com/saucekid/sauceVR) | 28 | Universeel full-body VR |
| [TheNexusAvenger/Nexus-VR-Core](https://github.com/TheNexusAvenger/Nexus-VR-Core) | 20 | Utilities voor VR-games en -systemen |
| [TheNexusAvenger/Enigma](https://github.com/TheNexusAvenger/Enigma) | 20 | SteamVR-trackers (full-body tracking) naar de Roblox-client |
| [mmbaguette/Roblox-VR-with-Webcam](https://github.com/mmbaguette/Roblox-VR-with-Webcam) | 8 | Avatar bootst je bewegingen na met alleen een webcam (pose-tracking) |
| [Quenty/vrpresentation2022](https://github.com/Quenty/vrpresentation2022) | 7 | Broncode van Quenty's VR-fundamentals presentatie |
| [TheNexusAvenger/Nexus-VR-Backpack](https://github.com/TheNexusAvenger/Nexus-VR-Backpack) | 6 | Backpack om Tools te gebruiken in VR |
| [TheNexusAvenger/Nexus-VR-Compatibility-Tester](https://github.com/TheNexusAvenger/Nexus-VR-Compatibility-Tester) | 5 | Detecteert veelvoorkomende VR-problemen in je game |
| [IITPP-Roblox/VR-Bottom-Bar](https://github.com/IITPP-Roblox/VR-Bottom-Bar) | 4 | Extra VR-balk voor eigen knoppen |
| [twhlynch/Roblox2Grab](https://github.com/twhlynch/Roblox2Grab) | 3 | Roblox-map exporteren naar de VR-game Grab |
| [hakusoda/HAKUREALITY](https://github.com/hakusoda/HAKUREALITY) | 2 | Experimenteel VR-systeem |
| [4x8Matrix/Hoku](https://github.com/4x8Matrix/Hoku) | 1 | VR-overlay engine in Luau |
| [mathken029/vr-roblox-kit](https://github.com/mathken029/vr-roblox-kit) | 0 | Open-source VR game-development kit |
| [Metatable-Games/MetaVR](https://github.com/Metatable-Games/MetaVR) | 0 | VR-framework in Luau |

## Data, opslag & serialisatie

DataStores, serialisatie, compressie, state en big numbers. (48 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [MadStudioRoblox/ProfileStore](https://github.com/MadStudioRoblox/ProfileStore) | 338 | Session-locked DataStore saving (opvolger ProfileService) |
| [littensy/charm](https://github.com/littensy/charm) | 261 | Atomic state management (Jotai-stijl) |
| [paradoxum-games/lyra](https://github.com/paradoxum-games/lyra) | 151 | Geavanceerd player-data beheer met simpele API |
| [cxmeel/sift](https://github.com/cxmeel/sift) | 92 | Immutable data library |
| [buildthomas/MockDataStoreService](https://github.com/buildthomas/MockDataStoreService) | 84 | DataStoreService emuleren voor offline testen |
| [cipharius/msgpack-luau](https://github.com/cipharius/msgpack-luau) | 51 | MessagePack binaire serialisatie |
| [pinehappi/DataDelve](https://github.com/pinehappi/DataDelve) | 49 | Grafische interface voor de DataStore API |
| [Dekkonot/bitbuffer](https://github.com/Dekkonot/bitbuffer) | 45 | Binaire data packen in pure Lua |
| [MadStudioRoblox/Sera](https://github.com/MadStudioRoblox/Sera) | 43 | Low-level geschematiseerde serialisatie naar buffers |
| [chadhyatt/LuaEncode](https://github.com/chadhyatt/LuaEncode) | 41 | Snelle table-serialisatie naar Lua-code |
| [Dekkonot/int64-luau](https://github.com/Dekkonot/int64-luau) | 29 | Unsigned 64-bit integers in pure Luau via vectors |
| [alonefact/RBLX-UGC-Emotes](https://github.com/alonefact/RBLX-UGC-Emotes) | 28 | API-dump van alle UGC-emotes |
| [KdudeDev/InfiniteMath](https://github.com/KdudeDev/InfiniteMath) | 25 | Voorbij het 10^308 getal-limiet |
| [EgoMoose/rbx-bufferize](https://github.com/EgoMoose/rbx-bufferize) | 24 | Roblox-datatypes lossless naar/van buffers encoderen |
| [evilbocchi/alyanum](https://github.com/evilbocchi/alyanum) | 20 | High-performance big numbers (incremental/simulator games) |
| [Gem-API/Rose](https://github.com/Gem-API/Rose) | 17 | Volledige Roblox Instance-serializer (instances opslaan/laden) |
| [duckarmor/Freeze](https://github.com/duckarmor/Freeze) | 16 | Immutable datastructuren |
| [RiskoZS/llz4](https://github.com/RiskoZS/llz4) | 14 | LZ4-compressie in pure Lua (data kleiner maken) |
| [XoifaiI/Ledger](https://github.com/XoifaiI/Ledger) | 13 | Lock-free, event-sourced datastore zonder session locks |
| [Dekkonot/base91-luau](https://github.com/Dekkonot/base91-luau) | 13 | Base91 encoderen/decoderen (compacter dan Base64) |
| [R-unic/serio](https://github.com/R-unic/serio) | 11 | Buffer-serialisatie library |
| [howmanysmall/FastBitBuffer](https://github.com/howmanysmall/FastBitBuffer) | 10 | Snelste Roblox BitBuffer |
| [CrabGuy/APInt](https://github.com/CrabGuy/APInt) | 10 | Arbitrary-precision integers |
| [fosterchild1/AptInt](https://github.com/fosterchild1/AptInt) | 10 | Snelste BigInteger-implementatie in Luau |
| [TheNexusAvenger/Nexus-Data-Store](https://github.com/TheNexusAvenger/Nexus-Data-Store) | 9 | DataStore-requests bufferen en wijzigingen naar andere servers sturen |
| [LastTalon/Monolith](https://github.com/LastTalon/Monolith) | 9 | Collecties-library (sets, queues, etc.) |
| [NotDSF/leopard](https://github.com/NotDSF/leopard) | 8 | "Snelste" serializer voor Lua en Roblox |
| [NotReeceHarris/DataStore3](https://github.com/NotReeceHarris/DataStore3) | 7 | Modulaire externe SQL-opslag voor Roblox |
| [seaofvoices/luau-character](https://github.com/seaofvoices/luau-character) | 7 | Unicode-tekenclassificatie en conversie |
| [romdotdog/BigInteger.lua](https://github.com/romdotdog/BigInteger.lua) | 7 | BigInteger-library getranspileerd naar Luau |
| [wrello/Plums](https://github.com/wrello/Plums) | 6 | Table-wijzigingen server → client repliceren |
| [olmescode/DataModule](https://github.com/olmescode/DataModule) | 6 | DataStore-library voor games |
| [rimuy/roselect](https://github.com/rimuy/roselect) | 4 | Composable data-selectors |
| [Khaomi/bson.luau](https://github.com/Khaomi/bson.luau) | 3 | BSON-dataformaat in Luau |
| [isoopod/Pack](https://github.com/isoopod/Pack) | 2 | Geschematiseerde buffer-serialisatie |
| [star-alice/ordered-store-manager](https://github.com/star-alice/ordered-store-manager) | 2 | OrderedDataStores beheren met sync naar clients |
| [9q7n/luau-snowflake](https://github.com/9q7n/luau-snowflake) | 2 | Snowflake-ID's in Luau |
| [ThatTimothy/ordered-datastore-backup-tool](https://github.com/ThatTimothy/ordered-datastore-backup-tool) | 2 | Back-up van OrderedDataStore naar CSV via Open Cloud |
| [nightcycle/compression-util](https://github.com/nightcycle/compression-util) | 1 | Roblox-types comprimeren |
| [text21/SlotCore](https://github.com/text21/SlotCore) | 1 | Multi-slot saves met migraties, middleware, admin-console en globale leaderboards |
| [Distracted-Games/ProfileStore2](https://github.com/Distracted-Games/ProfileStore2) | 1 | Modulaire, type-safe, async refactor van ProfileStore |
| [retaunoir/squishy](https://github.com/retaunoir/squishy) | 1 | Buffers packen |
| [cxmeel/packager](https://github.com/cxmeel/packager) | 1 | Instance-bomen verpakken in één table |
| [peterhellberg/brickcolor](https://github.com/peterhellberg/brickcolor) | 1 | Alle BrickColor-codes als Go-package |
| [ordac/keystone](https://github.com/ordac/keystone) | 0 | Betrouwbare session-locked data-persistentie |
| [R-unic/diff](https://github.com/R-unic/diff) | 0 | Verschillen tussen objecten berekenen en toepassen |
| [ElixNoir/Roblox-Codec](https://github.com/ElixNoir/Roblox-Codec) | 0 | Bytes efficiënt in buffers packen |
| [Dinojan-D/NDArrayLuau](https://github.com/Dinojan-D/NDArrayLuau) | 0 | NumPy-achtige multi-dimensionale arrays voor Luau |

## Game-systemen & utilities

Quests, dialogen, input, trading, admin, signals en meer. (124 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [evaera/Cmdr](https://github.com/evaera/Cmdr) | 525 | Uitbreidbare command-console voor developers (types, autocomplete) |
| [Epix-Incorporated/Adonis](https://github.com/Epix-Incorporated/Adonis) | 499 | Uitgebreid open-source server-administratiesysteem |
| [1ForeverHD/TopbarPlus](https://github.com/1ForeverHD/TopbarPlus) | 236 | Dynamische topbar-iconen met thema's, dropdowns en menu's |
| [howmanysmall/Janitor](https://github.com/howmanysmall/Janitor) | 149 | Opruimen van connections/instances (Maid-alternatief) |
| [nanoblox/hd-admin](https://github.com/nanoblox/hd-admin) | 82 | Broncode van HD Admin (Nanoblox): rollen, commands, management |
| [stravant/goodsignal](https://github.com/stravant/goodsignal) | 70 | Signal met volledige RBXScriptSignal-pariteit |
| [MaximumADHD/Roblox-Parallel-Worker](https://github.com/MaximumADHD/Roblox-Parallel-Worker) | 60 | Parallel Luau zonder gedoe: taken verdelen over Actors |
| [paradoxuum/centurion](https://github.com/paradoxuum/centurion) | 58 | Uitbreidbaar command-framework (roblox-ts) |
| [Sleitnick/RbxObservers](https://github.com/Sleitnick/RbxObservers) | 57 | Observer-functies (tags, attributes, players) |
| [kohls-admin/kohls-admin](https://github.com/kohls-admin/kohls-admin) | 48 | Kohl's Admin herschreven: complete experience-moderatie |
| [AlexanderLindholt/SignalPlus](https://github.com/AlexanderLindholt/SignalPlus) | 37 | Zeer snelle signal-library |
| [EgoMoose/Rbx-PSD-UI](https://github.com/EgoMoose/Rbx-PSD-UI) | 36 | Photoshop PSD-bestanden omzetten naar Roblox GUI |
| [MaximumADHD/Roblox-Utils](https://github.com/MaximumADHD/Roblox-Utils) | 35 | Collectie Wally-packages |
| [TheNexusAvenger/Nexus-Admin](https://github.com/TheNexusAvenger/Nexus-Admin) | 32 | Admin-systeem voor gewone spelers, gebouwd op Cmdr |
| [Nicell/alien-signals-luau](https://github.com/Nicell/alien-signals-luau) | 30 | Lichtste reactieve signals-library |
| [decimalcubed/luau-thread](https://github.com/decimalcubed/luau-thread) | 28 | Parallel Luau zo simpel mogelijk |
| [Blupo/ColorPane](https://github.com/Blupo/ColorPane) | 27 | Kleur-tools voor Studio-plugins |
| [ffrostfall/luausignal](https://github.com/ffrostfall/luausignal) | 26 | Cross-runtime signal-implementatie |
| [evaera/Aurora](https://github.com/evaera/Aurora) | 23 | Status-effecten ("auras") beheren: buffs, debuffs, stacking |
| [zblox164/PlacementService](https://github.com/zblox164/PlacementService) | 21 | Bouw/placement-systeem (tycoon/sandbox) |
| [prooheckcp/RoQuest](https://github.com/prooheckcp/RoQuest) | 20 | Uitgebreid quest-systeem |
| [administer-org/administer](https://github.com/administer-org/administer) | 20 | Modulair admin-paneel |
| [loneka/moonlets](https://github.com/loneka/moonlets) | 19 | Unopinionated utility-modules |
| [Asiandayboy/InventoryMaker](https://github.com/Asiandayboy/InventoryMaker) | 17 | Framework om je eigen inventory-systeem te bouwen |
| [rimuy/GameJoy](https://github.com/rimuy/GameJoy) | 17 | Composable input-library (combo's, sequences, holds) |
| [RBLXUtils/FastSignal](https://github.com/RBLXUtils/FastSignal) | 16 | Signal-library gelijk aan RBXScriptSignal |
| [Cosmental/Social-Chat-V2](https://github.com/Cosmental/Social-Chat-V2) | 15 | Complete chat-overhaul: bubbles, effecten, tags |
| [AdamMillsy/Inputter](https://github.com/AdamMillsy/Inputter) | 14 | Cross-platform input-manager |
| [DialogueMaker/plugin](https://github.com/DialogueMaker/plugin) | 13 | RPG-dialogen voor NPC's |
| [Redon-Tech/Emergency-Vehicle-Creator](https://github.com/Redon-Tech/Emergency-Vehicle-Creator) | 13 | Zwaailichten/sirenes voor hulpdienstvoertuigen (ELS) |
| [mkargus/PartToTerrain](https://github.com/mkargus/PartToTerrain) | 12 | Parts omzetten naar terrain |
| [YetAnotherClown/luau-futures](https://github.com/YetAnotherClown/luau-futures) | 12 | Rust-achtige Futures voor Luau |
| [lukadev-0/util.luau](https://github.com/lukadev-0/util.luau) | 12 | Verzameling nuttige Luau-utilities |
| [lukadev-0/rbx-typed-promise](https://github.com/lukadev-0/rbx-typed-promise) | 12 | Promise-library met volledige types |
| [TheNexusAvenger/Nexus-Instance](https://github.com/TheNexusAvenger/Nexus-Instance) | 10 | Eigen custom instance-classes maken in Luau |
| [Ultray-Studios/RBXConnectionManager](https://github.com/Ultray-Studios/RBXConnectionManager) | 10 | Connections beheren met auto-cleanup en debugging |
| [averlyst/NamedSignal](https://github.com/averlyst/NamedSignal) | 10 | Signal-implementatie met goede balans tussen ergonomie en snelheid |
| [IllusionAC/Illusion-InputActionSystem](https://github.com/IllusionAC/Illusion-InputActionSystem) | 9 | Input Action System library (acties i.p.v. toetsen) |
| [vocksel/context-controls](https://github.com/vocksel/context-controls) | 9 | Makkelijke wrapper rond ContextActionService |
| [FarFromLittle/Questline](https://github.com/FarFromLittle/Questline) | 9 | Quest-creatie module |
| [Dionysusnu/rbxts-rust-classes](https://github.com/Dionysusnu/rbxts-rust-classes) | 9 | Rust's Option/Result/Vec als TypeScript-classes |
| [welcomestohell/boba](https://github.com/welcomestohell/boba) | 8 | Type-safe runtime typechecker |
| [HuotChu/roblox-pubsub](https://github.com/HuotChu/roblox-pubsub) | 8 | PubSub-module |
| [gdr1461/GAdmin](https://github.com/gdr1461/GAdmin) | 8 | Zeer aanpasbaar admin-systeem |
| [blorbee1/ComputeLua](https://github.com/blorbee1/ComputeLua) | 7 | Parallel Luau makkelijker (compute-shader stijl) |
| [R-unic/mechanism](https://github.com/R-unic/mechanism) | 7 | Elegante input-wrapper |
| [mvyasu/TeleportQueue](https://github.com/mvyasu/TeleportQueue) | 6 | Teleport-queue voor lobbies/matchmaking |
| [Team-Snowdust/feature-flags](https://github.com/Team-Snowdust/feature-flags) | 6 | Feature-flags library |
| [Reselim/cmdr-additions](https://github.com/Reselim/cmdr-additions) | 6 | Extra commands voor Cmdr |
| [omrezkeypie/OmrezKeyBind](https://github.com/omrezkeypie/OmrezKeyBind) | 5 | Declaratieve, actie-gebaseerde input-library |
| [dig/roblox-lua-parallel](https://github.com/dig/roblox-lua-parallel) | 5 | Simpele parallelle uitvoering |
| [Bytebit-Org/roblox-RewardContainers](https://github.com/Bytebit-Org/roblox-RewardContainers) | 5 | Type-safe beloningen geven aan spelers |
| [Bytebit-Org/roblox-PlayerStatisticAchievements](https://github.com/Bytebit-Org/roblox-PlayerStatisticAchievements) | 5 | Achievements op basis van speler-statistieken |
| [jammees/Threader](https://github.com/jammees/Threader) | 5 | Promise-gebaseerde Actor-wrapper (Parallel Luau) |
| [Beastslash/Roblox-RhythmService](https://github.com/Beastslash/Roblox-RhythmService) | 5 | Ritme van de speler meten (rhythm games) |
| [gaymeowing/catboygirl-maid](https://github.com/gaymeowing/catboygirl-maid) | 5 | Snelste en simpelste maid voor Luau/Roblox |
| [opDavi1/Obby-Engine](https://github.com/opDavi1/Obby-Engine) | 5 | Engine voor obby's: checkpoints, killparts, stages |
| [bstummer/PartyService](https://github.com/bstummer/PartyService) | 4 | Party-systemen, globale matchmaking-queues en teleport via MessagingService |
| [metatablecatgames/catwork](https://github.com/metatablecatgames/catwork) | 4 | Declaratieve runtime en object-framework |
| [R-unic/action-journal](https://github.com/R-unic/action-journal) | 4 | State-changes opnemen en replay/rollback doen |
| [nontkph/ArcLight-Input](https://github.com/nontkph/ArcLight-Input) | 4 | Input-module manager |
| [0jewell/td-kit](https://github.com/0jewell/td-kit) | 4 | Tower-defense toolkit: paden, waves, torens |
| [tplaygd/Custom-Chat-System](https://github.com/tplaygd/Custom-Chat-System) | 4 | Volledig eigen chatsysteem |
| [A-Ricemusic/RPG-Template](https://github.com/A-Ricemusic/RPG-Template) | 3 | RPG-template: quests, spawning, inventory, wapens, abilities |
| [TheNexusAvenger/Nexus-Feature-Flags](https://github.com/TheNexusAvenger/Nexus-Feature-Flags) | 3 | Feature flags beheren en synchroniseren in je game |
| [NotKisoMomo/Mitt](https://github.com/NotKisoMomo/Mitt) | 3 | Full-stack input: action registry, combo's, shortcuts, context-filtering |
| [stardustdtm/combo](https://github.com/stardustdtm/combo) | 3 | Input-sequences (vechtgame-combo's) |
| [Skekdog/RoundHandler](https://github.com/Skekdog/RoundHandler) | 3 | Rondes en gamemodes beheren |
| [Distracted-Games/LeanPromise](https://github.com/Distracted-Games/LeanPromise) | 3 | Moderne refactor van evaera's Promise |
| [EkoDy/SimpleMatchmaking](https://github.com/EkoDy/SimpleMatchmaking) | 3 | Simpele matchmaking-module |
| [glitchifyed/Tunicus-Placement-v3](https://github.com/glitchifyed/Tunicus-Placement-v3) | 3 | Grid-placement systeem (bouwen/plaatsen) |
| [Zyrakia/rbxts-fsm](https://github.com/Zyrakia/rbxts-fsm) | 3 | Simpele finite state machine |
| [YetAnotherClown/ThreadPool](https://github.com/YetAnotherClown/ThreadPool) | 3 | Thread pools voor betere performance en minder latency |
| [nightcycle/value-sequence](https://github.com/nightcycle/value-sequence) | 2 | NumberSequence/ColorSequence voor elk datatype |
| [DialogueMaker/kit](https://github.com/DialogueMaker/kit) | 2 | Tools voor dialoog-systemen: templates, triggers, effecten |
| [funwolf7/JumpButton](https://github.com/funwolf7/JumpButton) | 2 | Jump-knop detectie met input-buffering |
| [RomanHein/luau-result](https://github.com/RomanHein/luau-result) | 2 | Type-safe Result-type |
| [Hex-Interactive/ChainLink](https://github.com/Hex-Interactive/ChainLink) | 2 | DataModel-gedreven logic- en besturingssysteem |
| [CavefulGames/luau-rng](https://github.com/CavefulGames/luau-rng) | 2 | Random-utilities (gewogen random e.d.) |
| [MrRoblick/platform-luau](https://github.com/MrRoblick/platform-luau) | 2 | Platform van de speler detecteren (pc/mobiel/console/VR) |
| [ReRand/RbxRevared](https://github.com/ReRand/RbxRevared) | 2 | Toolkit met module manager en values-systeem |
| [RadiatedExodus/Builder](https://github.com/RadiatedExodus/Builder) | 2 | Systeem om instances te bouwen |
| [AlexeyLegasov63/RobloxRegistry](https://github.com/AlexeyLegasov63/RobloxRegistry) | 2 | Type-safe registry-systeem |
| [DavidXu1721/Roblox_GridBasedInventorySystem](https://github.com/DavidXu1721/Roblox_GridBasedInventorySystem) | 1 | Grid-based inventory (tutorial-reeks) |
| [sam4922/Roblox-ServerClientTradeFramework](https://github.com/sam4922/Roblox-ServerClientTradeFramework) | 1 | Server-framework voor een trade-systeem |
| [MrBlueMW/GameStarter](https://github.com/MrBlueMW/GameStarter) | 1 | Plugin: één-klik dialogen, matchmaking, shops, leaderboards, loot boxes |
| [Redon-Tech/Fire-System](https://github.com/Redon-Tech/Fire-System) | 1 | Brand-systeem voor roleplay (brandweer) |
| [samnewmn/RoRx](https://github.com/samnewmn/RoRx) | 1 | RxJS reactive programming in Roblox |
| [Yuzkkj/cashier](https://github.com/Yuzkkj/cashier) | 1 | Gamepasses, developer products en gifting gestroomlijnd |
| [OK-ORCO/roblox-feedback](https://github.com/OK-ORCO/roblox-feedback) | 1 | In-game feedback-box met Discord-webhook |
| [Distracted-Games/LootTable](https://github.com/Distracted-Games/LootTable) | 1 | Gewogen random selectie (loot tables) |
| [Danonienko/Clearance-System](https://github.com/Danonienko/Clearance-System) | 1 | Keycard/clearance-systeem |
| [exelarios/infinitum](https://github.com/exelarios/infinitum) | 1 | Framework voor roleplay-community management |
| [XolborGames/FuzzyString](https://github.com/XolborGames/FuzzyString) | 1 | Fuzzy string-matching (Levenshtein) voor zoekfuncties |
| [Sleitnick/rbxts-clack](https://github.com/Sleitnick/rbxts-clack) | 1 | Input-helperklassen (roblox-ts) |
| [itssRetro/RngService](https://github.com/itssRetro/RngService) | 1 | Beloningen en kansen berekenen |
| [Mullets-Gavin/DiceMsgService](https://github.com/Mullets-Gavin/DiceMsgService) | 1 | Andere servers pingen om spelers te vinden |
| [Hinikaa/luaukit](https://github.com/Hinikaa/luaukit) | 1 | Acht geteste utility-modules in één Wally-kit |
| [bobthegodhaha-ui/RobloxGatchaSystem](https://github.com/bobthegodhaha-ui/RobloxGatchaSystem) | 1 | Gacha/spin-machine systeem |
| [9q7n/Vote-System](https://github.com/9q7n/Vote-System) | 1 | Open-source stemsysteem |
| [MafuSaku/robloxbadwordfilter](https://github.com/MafuSaku/robloxbadwordfilter) | 1 | Lijst met bekende filter-bypasses voor eigen chatfilters |
| [Lukako-zabijak/TradingSystem](https://github.com/Lukako-zabijak/TradingSystem) | 0 | Server-authoritative trading met durable transacties en recovery |
| [insop1/Roblox-Dialogue-System-Script](https://github.com/insop1/Roblox-Dialogue-System-Script) | 0 | Vertakkende dialogen geïnspireerd op Disco Elysium |
| [MarioChao/FlyingBroom](https://github.com/MarioChao/FlyingBroom) | 0 | Vliegende bezem (Wandering Witch-stijl) |
| [thecreare/roblox-visual-scripting-language](https://github.com/thecreare/roblox-visual-scripting-language) | 0 | Visuele scriptingtaal voor in-game gebruik |
| [notllog1c/sourceenginechat](https://github.com/notllog1c/sourceenginechat) | 0 | Source Engine-achtige chat |
| [AlexeyLegasov63/weightedrandom](https://github.com/AlexeyLegasov63/weightedrandom) | 0 | Gewogen random met dynamische kansen (pity-systemen) |
| [MarioChao/client-movement-detector](https://github.com/MarioChao/client-movement-detector) | 0 | Jump-requests en bewegingsrichting van de lokale speler detecteren |
| [CavefulGames/stringdiff-luau](https://github.com/CavefulGames/stringdiff-luau) | 0 | String-similarity voor chatbots |
| [Ou1cK5CoP3/hook-registry](https://github.com/Ou1cK5CoP3/hook-registry) | 0 | Event-hook dispatcher voor combat- en ability-systemen |
| [gue-hub/roblox-tycoon-kit](https://github.com/gue-hub/roblox-tycoon-kit) | 0 | Modulair tycoon-framework: plots, droppers, knoppen |
| [nrbx-ts/rbxts-cron](https://github.com/nrbx-ts/rbxts-cron) | 0 | Cron-service voor herhalende events |
| [tralfa42real/roblox-round-framework](https://github.com/tralfa42real/roblox-round-framework) | 0 | Rondes met map-voting, team-balancing en match-state |
| [tralfa42real/roblox-ghost-runner-framework](https://github.com/tralfa42real/roblox-ghost-runner-framework) | 0 | Time-trials met gevalideerde checkpoints en ghost-replays |
| [DevSmoke1/rng-spinner-engine](https://github.com/DevSmoke1/rng-spinner-engine) | 0 | Gewogen RNG/spinner-engine met luck-multipliers |
| [MarioChao/text-typewriter](https://github.com/MarioChao/text-typewriter) | 0 | Tekst karakter-voor-karakter tonen (typewriter) |
| [spavdigital/roblox-liveops-patching](https://github.com/spavdigital/roblox-liveops-patching) | 0 | Live-ops patching (game aanpassen zonder te herstarten) |
| [spavdigital/roblox-economy-service](https://github.com/spavdigital/roblox-economy-service) | 0 | Server-authoritative economy-service |
| [SuperInstance/luau-recipe](https://github.com/SuperInstance/luau-recipe) | 0 | Crafting-recepten systeem |
| [MarioChao/dreamers-dialog-system](https://github.com/MarioChao/dreamers-dialog-system) | 0 | Uitgebreid dialoog-systeem |
| [QuroDev/Roblox-Wanted-System](https://github.com/QuroDev/Roblox-Wanted-System) | 0 | Wanted-systeem (politie/sterren) |
| [ryanleem/Roblox-Building-and-Placement-System](https://github.com/ryanleem/Roblox-Building-and-Placement-System) | 0 | Bouwsysteem: roteren, plaatsen en aan elkaar snappen |
| [Frieda-VI/building-system](https://github.com/Frieda-VI/building-system) | 0 | Open-source placement-systeem |
| [emdomanus/tempo](https://github.com/emdomanus/tempo) | 0 | Low-overhead phase-aware scheduler met task-ID's en pooling |

## Security & anticheat

Hashing, encryptie, logins, permissies, rate limiting en anticheat. (18 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [Dekkonot/luau-hashing](https://github.com/Dekkonot/luau-hashing) | 35 | Hash-algoritmes (SHA, MD5, CRC...) in pure Luau |
| [PossiblePanda/QueryAuth](https://github.com/PossiblePanda/QueryAuth) | 27 | Type-safe permissie-checks met complexe logica |
| [boatbomber/HashLib](https://github.com/boatbomber/HashLib) | 18 | Cryptografische hashes (SHA, MD5...) in pure Lua |
| [EgoMoose/rbx-captcha](https://github.com/EgoMoose/rbx-captcha) | 13 | Captcha's in Roblox (anti-bot) |
| [BrookenRecord/Rodentify](https://github.com/BrookenRecord/Rodentify) | 11 | Roblox game-servers authenticeren bij je eigen backend |
| [boatbomber/LoginSystem](https://github.com/boatbomber/LoginSystem) | 8 | Veilige login-accounts binnen een game |
| [TheNexusAvenger/Sovereign](https://github.com/TheNexusAvenger/Sovereign) | 7 | Bans centraal beheren over meerdere games en groepen |
| [bytexenon/luau-rng-cracker](https://github.com/bytexenon/luau-rng-cracker) | 6 | Toont hoe Luau's Random voorspelbaar is (RNG-cracker) |
| [Shambi-0/Luau-Sha256](https://github.com/Shambi-0/Luau-Sha256) | 4 | Geoptimaliseerde SHA-256 voor Luau |
| [ssynical/triplesec](https://github.com/ssynical/triplesec) | 3 | Triple-cascade encryptie (VeraCrypt-stijl) in Luau |
| [janisfox/marble](https://github.com/janisfox/marble) | 3 | Role-based access control met DataStore-persistentie |
| [MrRoblick/chacha20-luau](https://github.com/MrRoblick/chacha20-luau) | 3 | ChaCha20-encryptie in Luau |
| [Shambi-0/crypto](https://github.com/Shambi-0/crypto) | 3 | Cryptografie-library (hashing, encryptie) |
| [0xmortuex/roblox-anticheat-the-hard-way](https://github.com/0xmortuex/roblox-anticheat-the-hard-way) | 2 | Tutorial: server-side anticheat bouwen, elke regel uitgelegd |
| [alexandervonarx/RoScanner](https://github.com/alexandervonarx/RoScanner) | 1 | Static analysis: vindt servercode die de client vertrouwt |
| [Jeremy84100/RateLimiter](https://github.com/Jeremy84100/RateLimiter) | 0 | Zero-allocation O(1) rate limiter |
| [Word30210/luau-confusables](https://github.com/Word30210/luau-confusables) | 0 | Lijkende tekens detecteren (anti-impersonatie in namen/chat) |
| [kentiers/anvil](https://github.com/kentiers/anvil) | 0 | Server-authoritative basis: acties, schema's en veilige remote-grenzen |

## Next-level / experimenteel

Luau-in-Luau, emulators, DOOM, N64, video, Python-in-Luau en game-ports. (101 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [bliporg/blip](https://github.com/bliporg/blip) | 284 | Blip: cross-platform scriptbare game-engine en platform (Luau) |
| [iErcann/NotBlox](https://github.com/iErcann/NotBlox) | 184 | Roblox-achtige multiplayer game-engine in Three.js/Node.js met auto's en physics |
| [vanyle/vectarine](https://github.com/vanyle/vectarine) | 135 | Game-engine voor snel prototypen met Luau-scripting |
| [Manonox/GDLuau](https://github.com/Manonox/GDLuau) | 105 | Luau-bindings voor de Godot Engine |
| [roblox-csharp/roblox-cs](https://github.com/roblox-csharp/roblox-cs) | 101 | C#-naar-Luau transpiler |
| [MaximumADHD/Source2Roblox](https://github.com/MaximumADHD/Source2Roblox) | 91 | Source Engine-maps (Half-Life/CS) automatisch naar Roblox porten |
| [MaximumADHD/Rbx2Source](https://github.com/MaximumADHD/Rbx2Source) | 88 | Roblox-assets naar Source Engine compileren |
| [MaximumADHD/Super-Nostalgia-Zone](https://github.com/MaximumADHD/Super-Nostalgia-Zone) | 65 | Broncode van Super Nostalgia Zone (oude Roblox nagebouwd) |
| [kosuke14/vLuau](https://github.com/kosuke14/vLuau) | 63 | Luau VM + compiler die in Luau draait (loadstring-alternatief) |
| [RadiatedExodus/LuauCeption](https://github.com/RadiatedExodus/LuauCeption) | 56 | Luau draaien in Luau (via Wasynth/WebAssembly) |
| [jackhexed/luaup](https://github.com/jackhexed/luaup) | 56 | Lossless Luau-parser in Luau |
| [roblox-rs/roblox-rs](https://github.com/roblox-rs/roblox-rs) | 56 | Rust-bindings voor Roblox (Rust → WebAssembly → Luau) |
| [MaximumADHD/Roblox-PNG-Library](https://github.com/MaximumADHD/Roblox-PNG-Library) | 55 | PNG-bestanden lezen in Luau |
| [StayBlue/librebox-demo](https://github.com/StayBlue/librebox-demo) | 51 | Librebox: open-source, Roblox-compatibele game-engine |
| [roblox-compilers/roblox-py](https://github.com/roblox-compilers/roblox-py) | 42 | Python-naar-Luau compiler |
| [PhoenixWhitefire/PhoenixEngine](https://github.com/PhoenixWhitefire/PhoenixEngine) | 41 | Game-engine met Luau-scripting |
| [GameabillityOnYt/obbying-revival-project](https://github.com/GameabillityOnYt/obbying-revival-project) | 41 | Roblox-obby's nagebouwd in Godot |
| [Atmerek/CrossplayProject](https://github.com/Atmerek/CrossplayProject) | 37 | Minecraft ↔ Roblox crossplay (beide kanten) |
| [edunad/rawrbox](https://github.com/edunad/rawrbox) | 34 | PSX-achtige game-engine met Luau-modding |
| [sircfenner/png-luau](https://github.com/sircfenner/png-luau) | 32 | PNG-bestanden lezen/schrijven in Luau |
| [Scythe-Technology/luau-roblox](https://github.com/Scythe-Technology/luau-roblox) | 30 | Roblox place/model-bestanden bewerken vanuit Luau |
| [OMouta/PyLua](https://github.com/OMouta/PyLua) | 27 | Python-interpreter embedded in Luau (Python draaien in Roblox) |
| [KumoCorp/shingetsu](https://github.com/KumoCorp/shingetsu) | 27 | Rust-native Lua/Luau implementatie |
| [uniquadev/LuauVM](https://github.com/uniquadev/LuauVM) | 26 | Luau-bytecode interpreter in Luau |
| [roblox-aurora/zirconium](https://github.com/roblox-aurora/zirconium) | 26 | Runtime scriptingtaal voor Roblox |
| [ActualMasterOogway/Iridium](https://github.com/ActualMasterOogway/Iridium) | 23 | Luau bytecode-toolkit/deserializer in Luau |
| [Nicell/lynx](https://github.com/Nicell/lynx) | 23 | Webframework in Luau (websites bouwen met Lune/Lute) |
| [KazuOfficial/Roblox-Unity](https://github.com/KazuOfficial/Roblox-Unity) | 22 | Roblox nagebouwd in Unity |
| [optimisticside/luaul](https://github.com/optimisticside/luaul) | 21 | Luau-compiler geschreven in Luau |
| [MaximumADHD/cage-mesh-deformer](https://github.com/MaximumADHD/cage-mesh-deformer) | 19 | Reverse-engineering van Roblox' cage mesh deformer (layered clothing) |
| [vantoanvh/LuauParser](https://github.com/vantoanvh/LuauParser) | 18 | Volledige Luau-parser (AST + CST) in Luau |
| [secondlife/slua](https://github.com/secondlife/slua) | 18 | Luau-fork van Second Life (Luau buiten Roblox in een virtuele wereld) |
| [rbx-loom/loom](https://github.com/rbx-loom/loom) | 18 | Roblox DSL |
| [RadiatedExodus/LuauInLuau](https://github.com/RadiatedExodus/LuauInLuau) | 17 | Luau-compiler/VM in Luau (voorganger van LuauCeption) |
| [vantoanvh/LuauNES](https://github.com/vantoanvh/LuauNES) | 16 | Snelle, accurate NES-emulator in Roblox |
| [fuse-lang/fuse](https://github.com/fuse-lang/fuse) | 16 | Statisch getypeerde taal die compileert naar Lua/Luau |
| [wizevaxel/picguin](https://github.com/wizevaxel/picguin) | 15 | High-performance image codecs (PNG e.d.) in Luau |
| [Nicell/htmluau](https://github.com/Nicell/htmluau) | 15 | HTML-templating in Luau |
| [Heliodex/coputer](https://github.com/Heliodex/coputer) | 15 | Collaboratieve Luau-uitvoeromgeving |
| [vinterbell/cart](https://github.com/vinterbell/cart) | 14 | Embedbare, sandboxed Luau-runtime |
| [ayulang/ayu](https://github.com/ayulang/ayu) | 14 | Statisch getypeerde taal die compileert naar Luau |
| [SovereignSatellite/Fin](https://github.com/SovereignSatellite/Fin) | 14 | Lua-achtige bytecode-interpreter in Luau |
| [thecreare/CatWebCompiler](https://github.com/thecreare/CatWebCompiler) | 14 | Compileert eigen programmeertaal naar CatWeb-scripts (in-game websites) |
| [PizzaLvr49/bevy-luau](https://github.com/PizzaLvr49/bevy-luau) | 13 | Luau-scripting voor de Bevy engine |
| [mayari-org/mayari](https://github.com/mayari-org/mayari) | 12 | Adaptief web-backend framework in Luau |
| [Plasmism/RoVM](https://github.com/Plasmism/RoVM) | 12 | Eigen 32-bit virtuele computer + besturingssysteem volledig in Roblox |
| [vantoanvh/LuauDOOM](https://github.com/vantoanvh/LuauDOOM) | 11 | De originele DOOM-engine geport naar Luau |
| [mokiros/luau_term](https://github.com/mokiros/luau_term) | 11 | Terminal-emulator (xterm-achtig) in Luau |
| [vantoanvh/LuauPorts](https://github.com/vantoanvh/LuauPorts) | 11 | Ports naar Luau: LZAV, Zlib, rANS, Base85, GIF, JPEG, PNG |
| [thekingofspace/Ruzit](https://github.com/thekingofspace/Ruzit) | 11 | Luau game-engine oplossing (Rust) |
| [Fumohouse/shadowblox](https://github.com/Fumohouse/shadowblox) | 10 | Roblox DataModel/API emuleren in Godot |
| [MaximumADHD/Roblox-VMF-Toolset](https://github.com/MaximumADHD/Roblox-VMF-Toolset) | 9 | Roblox-levels porten naar Garry's Mod |
| [vanyle/ASG](https://github.com/vanyle/ASG) | 9 | Statische website-generator in Rust + Luau |
| [Word30210/luau-hangul](https://github.com/Word30210/luau-hangul) | 8 | Koreaans (Hangul) verwerken in Luau |
| [TigersUniverse/LuauSharp](https://github.com/TigersUniverse/LuauSharp) | 8 | C#-interpreter voor Luau |
| [SovereignSatellite/LuauJBC](https://github.com/SovereignSatellite/LuauJBC) | 8 | Luau-bytecode naar Java-bytecode vertalen |
| [yoits9090/plumber](https://github.com/yoits9090/plumber) | 7 | Nintendo 64-emulator in Roblox (R4300 + Fast3D op EditableImage) |
| [wizevaxel/pnguin](https://github.com/wizevaxel/pnguin) | 7 | Snelle PNG-library in pure Luau |
| [mrparkerlol/script-builder](https://github.com/mrparkerlol/script-builder) | 7 | Complete script-builder in één ModuleScript |
| [lode-luau/LodeRuntime](https://github.com/lode-luau/LodeRuntime) | 7 | Snelle, modulaire Luau-runtime |
| [keplerHaloxx/roblox-chess-script](https://github.com/keplerHaloxx/roblox-chess-script) | 7 | Stockfish-schaakzetten tonen in Roblox |
| [UtoECat/miniLuau](https://github.com/UtoECat/miniLuau) | 7 | Luau-broncode in twee bestanden om makkelijk te embedden |
| [SPOOKEXE/atomic-game-engine](https://github.com/SPOOKEXE/atomic-game-engine) | 7 | C++-engine met ingebedde Luau en TypeScript |
| [TornadoCookie/OpenRBLX](https://github.com/TornadoCookie/OpenRBLX) | 6 | Open-source kloon van Roblox Studio/Player |
| [schphe/embrik](https://github.com/schphe/embrik) | 6 | Scriptbare server-first 2D-game-engine |
| [Yumacide/yum](https://github.com/Yumacide/yum) | 6 | Rust-achtige getypeerde taal die compileert naar Luau |
| [nrmu9/Ro2DEngine](https://github.com/nrmu9/Ro2DEngine) | 5 | Software-renderer + physics-engine op EditableImage |
| [nightcycle/editable-clothing-util](https://github.com/nightcycle/editable-clothing-util) | 5 | Klassieke clothing naar EditableImages vertalen |
| [Zytharian/RbxStargate](https://github.com/Zytharian/RbxStargate) | 5 | Stargates (werkende poorten) in Roblox, v20 |
| [magicoal-nerb/luvm](https://github.com/magicoal-nerb/luvm) | 5 | Lua 5.1 opnieuw geïmplementeerd in getypeerde Luau |
| [LUSharp/LUSharp](https://github.com/LUSharp/LUSharp) | 5 | C# compileren naar Luau |
| [boatbomber/Decant](https://github.com/boatbomber/Decant) | 4 | Decompressie in pure Luau |
| [Pimpoli/GodotLuau](https://github.com/Pimpoli/GodotLuau) | 4 | Luau in Godot 4, programmeren zoals in Roblox Studio |
| [not-nullptr/Ropen-Backend](https://github.com/not-nullptr/Ropen-Backend) | 4 | Open-source, reverse-engineered Roblox-backend |
| [littensy/logify](https://github.com/littensy/logify) | 4 | Minimalistische logic-gate simulator |
| [R-unic/ion](https://github.com/R-unic/ion) | 4 | Statisch getypeerde taal die naar Luau compileert |
| [pon331/qr-luau](https://github.com/pon331/qr-luau) | 3 | QR-codes genereren in Luau |
| [decompi/Pixel-Stream-Player](https://github.com/decompi/Pixel-Stream-Player) | 3 | Video afspelen in Roblox: frames als pixeldata streamen via Node.js |
| [travisdmathis/quake-3-arena-engine-luau-roblox](https://github.com/travisdmathis/quake-3-arena-engine-luau-roblox) | 3 | Quake 3 Arena-engine geport naar Luau voor Roblox |
| [Dekkonot/rbx-binary-luau](https://github.com/Dekkonot/rbx-binary-luau) | 2 | Roblox binair bestandsformaat (.rbxm) lezen in pure Luau |
| [filoxen/workspace-detector](https://github.com/filoxen/workspace-detector) | 2 | .rbxm-bestanden analyseren om oude games te vinden |
| [AnotherSubatomo/luau_qoi](https://github.com/AnotherSubatomo/luau_qoi) | 2 | QOI-afbeeldingsformaat encoder/decoder |
| [AegisLua/AegisVM](https://github.com/AegisLua/AegisVM) | 2 | Volledig sandboxed Luau-interpreter in Luau |
| [Ukuroks-games/giflib](https://github.com/Ukuroks-games/giflib) | 2 | GIFs maken in Luau |
| [shrjrd/rbxcad](https://github.com/shrjrd/rbxcad) | 2 | JSCAD (CSG/3D-modelleren in code) geport naar roblox-ts |
| [FXDuke/Lua2D](https://github.com/FXDuke/Lua2D) | 2 | 2D game-editor geïnspireerd op Roblox Studio |
| [ntech-org/Nova07](https://github.com/ntech-org/Nova07) | 2 | Clean-room herimplementatie van de Roblox-engine anno 2007 |
| [pon331/luau-vm](https://github.com/pon331/luau-vm) | 1 | Moderne Luau VM in Luau |
| [PhantomShift/rbx-pen-showcase](https://github.com/PhantomShift/rbx-pen-showcase) | 1 | Tablet-pen druk in Roblox via een geëmuleerde controller |
| [crownaintanoob/VideoToRobloxPlayer](https://github.com/crownaintanoob/VideoToRobloxPlayer) | 1 | Video naar frames/pixels omzetten en in Roblox tonen |
| [fak3Conde/CondeCodeStudio](https://github.com/fak3Conde/CondeCodeStudio) | 1 | Eigen game-engine + editor met Roblox-getrouwe Luau-API |
| [Asphaltian/OpenRBX](https://github.com/Asphaltian/OpenRBX) | 1 | Decompilatie en open reimplementatie van Roblox (dec. 2007) |
| [gigabyteworkstation/gta5-roblox-vehicles](https://github.com/gigabyteworkstation/gta5-roblox-vehicles) | 0 | GTA5-voertuigmeshes runtime in Roblox laden (Rust-backend + EditableMesh) |
| [pon331/unzip-luau](https://github.com/pon331/unzip-luau) | 0 | ZIP-bestanden decoderen in Luau |
| [pon331/GIFDecoder-Luau](https://github.com/pon331/GIFDecoder-Luau) | 0 | GIFs decoderen en afspelen in Roblox |
| [MingauRM/fobos-framework](https://github.com/MingauRM/fobos-framework) | 0 | Game-framework geïnspireerd op LÖVE2D en Roblox, met Luau |
| [ermak-dev/kubaria](https://github.com/ermak-dev/kubaria) | 0 | Open-source engine compatibel met Roblox, gebouwd op Godot |
| [Crazyblox/DUAUM](https://github.com/Crazyblox/DUAUM) | 0 | Luau DOOM-engine (doomgeneric), platform-agnostisch |
| [coolguy65161/QuBlox](https://github.com/coolguy65161/QuBlox) | 0 | Quantumcomputer-simulator in Luau |
| [Builder-Pals/native-legacy](https://github.com/Builder-Pals/native-legacy) | 0 | Restauratieproject voor Roblox 2006-2014 |
| [KartzRbx/CLPP](https://github.com/KartzRbx/CLPP) | 0 | CL++: C++-achtige taal die naar Luau compileert |

## API's & externe integraties

Open Cloud, web-API's, Discord, databases en analytics. (64 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [matthewdean/roblox-web-apis](https://github.com/matthewdean/roblox-web-apis) | 725 | Lijst van (ongedocumenteerde) Roblox web-API's |
| [noblox/noblox.js](https://github.com/noblox/noblox.js) | 308 | Node.js-wrapper voor Roblox web-API (groepen, ranks) — gearchiveerd |
| [Sleitnick/rbxcloud](https://github.com/Sleitnick/rbxcloud) | 140 | CLI + Rust-library voor de Open Cloud API |
| [DiscordLuau/discord-luau](https://github.com/DiscordLuau/discord-luau) | 79 | Discord-bots schrijven in Luau |
| [LengoLabs/qbot](https://github.com/LengoLabs/qbot) | 78 | Discord ↔ Roblox ranking-bot |
| [focalorrr/roblox-moderation-bot](https://github.com/focalorrr/roblox-moderation-bot) | 62 | Moderatie-bot voor Roblox-games |
| [skriken/bloxy](https://github.com/skriken/bloxy) | 57 | Roblox-website en API aanspreken (Node.js) |
| [BrookenRecord/studio-activity](https://github.com/BrookenRecord/studio-activity) | 52 | Laat live op Discord zien waar je in Studio aan werkt |
| [BrookenRecord/playfab-luau](https://github.com/BrookenRecord/playfab-luau) | 50 | PlayFab SDK voor Luau (externe backend/economie) |
| [treeben77/rblx-open-cloud](https://github.com/treeben77/rblx-open-cloud) | 39 | Python-wrapper voor Open Cloud |
| [cameronpcampbell/openblox](https://github.com/cameronpcampbell/openblox) | 39 | Volledig typesafe Roblox API-wrapper (TypeScript) |
| [AlroviOfficial/RoZod](https://github.com/AlroviOfficial/RoZod) | 39 | TypeScript-wrapper voor de Roblox API |
| [pat-dill/roblox-requests](https://github.com/pat-dill/roblox-requests) | 34 | Elegante HTTP-requests (Python requests-stijl) |
| [RbxAPI/Pyblox](https://github.com/RbxAPI/Pyblox) | 32 | Python-wrapper voor de Roblox API |
| [fekie/roboat](https://github.com/fekie/roboat) | 30 | High-performance Rust-interface voor de Roblox REST API |
| [Quenty/roblox-group-autoranker](https://github.com/Quenty/roblox-group-autoranker) | 24 | Node.js-server die automatisch ranks geeft in groepen |
| [RoSeal-Extension/Roblox-DeepLink-Parser](https://github.com/RoSeal-Extension/Roblox-DeepLink-Parser) | 23 | Roblox (deep)links parsen |
| [relatiocc/opencloud](https://github.com/relatiocc/opencloud) | 21 | Getypeerde SDK voor Open Cloud |
| [devSparkle/sentry-roblox](https://github.com/devSparkle/sentry-roblox) | 19 | Sentry.io crash-reporting voor je game |
| [boatbomber/GitHubUtil](https://github.com/boatbomber/GitHubUtil) | 16 | GitHub-API's aanroepen vanuit een Roblox-game |
| [Sleitnick/RbxAWS](https://github.com/Sleitnick/RbxAWS) | 15 | AWS SDK voor Roblox (in ontwikkeling) |
| [thegalaxydev/Aloha](https://github.com/thegalaxydev/Aloha) | 14 | Discord-API in Luau via Lune (bots die met je game praten) |
| [Jodenee/Voyager](https://github.com/Jodenee/Voyager) | 14 | Discord-webhook API-wrapper voor Roblox |
| [dynabloxjs/dynablox_opencloud](https://github.com/dynabloxjs/dynablox_opencloud) | 14 | Open Cloud wrapper voor Deno/Node |
| [BrookenRecord/sentry-luau](https://github.com/BrookenRecord/sentry-luau) | 13 | Volledige Sentry SDK voor Luau |
| [grand-hawk/action-roblox-luau-execution](https://github.com/grand-hawk/action-roblox-luau-execution) | 13 | GitHub Action die Luau uitvoert via Open Cloud |
| [chteau/Roblox-Supabase](https://github.com/chteau/Roblox-Supabase) | 12 | Type-safe Supabase-client (Postgres, storage, edge functions) |
| [MilkFrame/MilkBox](https://github.com/MilkFrame/MilkBox) | 12 | Database met info en leaderboards van Roblox-games |
| [TheNexusAvenger/Nexus-Clearing](https://github.com/TheNexusAvenger/Nexus-Clearing) | 11 | Server voor Roblox GDPR-webhooks (data-verwijderverzoeken) |
| [TheEpicFace007/roblox-domino-pizza-api](https://github.com/TheEpicFace007/roblox-domino-pizza-api) | 11 | Echt pizza bestellen bij Domino's vanuit Roblox (!) |
| [itsfrank/lune-cloud-luau-client](https://github.com/itsfrank/lune-cloud-luau-client) | 10 | Luau op Roblox-servers uitvoeren via Open Cloud (vanuit Lune) |
| [datalinkhq/datalink](https://github.com/datalinkhq/datalink) | 10 | Analytics/data-platform voor Roblox-games |
| [LFS6502/roblox-trello](https://github.com/LFS6502/roblox-trello) | 10 | Trello-API (OOP) vanuit Roblox |
| [vsenger/aws-roblox](https://github.com/vsenger/aws-roblox) | 10 | Integraties tussen Roblox en AWS Cloud |
| [Sightem/RoPP](https://github.com/Sightem/RoPP) | 9 | Roblox web-API wrapper in C++ |
| [ValiantWind/cloudblox](https://github.com/ValiantWind/cloudblox) | 8 | Promise-based wrapper voor web-API + Open Cloud |
| [chansoo-kr/Roblox-Supabase](https://github.com/chansoo-kr/Roblox-Supabase) | 8 | Type-safe Supabase/PostgREST-client voor Roblox-servers (roblox-ts) |
| [boatbomber/RbxSlack](https://github.com/boatbomber/RbxSlack) | 6 | Slack-API's vanuit Roblox |
| [GamebeastGG/RobloxSDK](https://github.com/GamebeastGG/RobloxSDK) | 6 | SDK voor het Gamebeast analytics-platform |
| [guidojw/arora-api](https://github.com/guidojw/arora-api) | 6 | Backend voor de Roblox Web API met extra features |
| [plainenglishh/remote-image-library](https://github.com/plainenglishh/remote-image-library) | 5 | Afbeeldingen van externe URL's laden in Roblox |
| [nightcycle/midas](https://github.com/nightcycle/midas) | 5 | Uitgebreide analytics-suite voor je game |
| [roblox-js/core](https://github.com/roblox-js/core) | 5 | Roblox web-API makkelijk aanspreken (JS) |
| [typical-developers/goblox](https://github.com/typical-developers/goblox) | 5 | Go-library voor Roblox- en Open Cloud-API's |
| [devsarim/roblox-catalog-proxy-server](https://github.com/devsarim/roblox-catalog-proxy-server) | 4 | Template voor een eigen catalog-proxy webserver |
| [WhitehillGroup/RankCache](https://github.com/WhitehillGroup/RankCache) | 4 | Actuele groepsranks cachen over servers |
| [KhanPython/Analytics-Service-Wrapper](https://github.com/KhanPython/Analytics-Service-Wrapper) | 4 | Rate-limited AnalyticsService-wrapper met event coalescing |
| [RefinedDev/rbx-ds-cloud](https://github.com/RefinedDev/rbx-ds-cloud) | 4 | Rust CLI + wrapper voor DataStore Open Cloud |
| [Stratiz/rbx-open-cloud](https://github.com/Stratiz/rbx-open-cloud) | 4 | OOP-wrapper voor Open Cloud |
| [FxllenCode/HttpServiceWrapper](https://github.com/FxllenCode/HttpServiceWrapper) | 3 | HttpService-wrapper in Axios-stijl met promises en proxying |
| [DataGrout/tether](https://github.com/DataGrout/tether) | 3 | DataGrout-client: game koppelen aan externe logica/tools |
| [Neura-Studios/recombee-sdk-luau](https://github.com/Neura-Studios/recombee-sdk-luau) | 3 | Recombee aanbevelings-engine SDK voor Luau |
| [elde-n/roblox-api](https://github.com/elde-n/roblox-api) | 3 | Roblox web-API bindings voor Rust |
| [thegamerbay/roblox-luau-execution-action](https://github.com/thegamerbay/roblox-luau-execution-action) | 2 | GitHub Action: place uploaden en tests draaien op Roblox-servers |
| [Corecii/ROBLOX-GameAnalytics-API](https://github.com/Corecii/ROBLOX-GameAnalytics-API) | 2 | GameAnalytics-integratie voor Roblox |
| [memorycode/cirrus](https://github.com/memorycode/cirrus) | 2 | Luau-library voor Open Cloud (vanuit Lune) |
| [exurd/roblox_wb_proxy](https://github.com/exurd/roblox_wb_proxy) | 1 | De Wayback Machine als Roblox API-proxy |
| [G0tzya/RoNexo](https://github.com/G0tzya/RoNexo) | 1 | Friend-tracking en playtime-analytics (Chrome-extensie + Rust-server) |
| [dinevolence/roblox-stats-tracker](https://github.com/dinevolence/roblox-stats-tracker) | 1 | Logt visits, favorites en spelers van games/groepen naar CSV |
| [ernisto/ro-cloud](https://github.com/ernisto/ro-cloud) | 1 | Open Cloud-utilities in Luau |
| [Naymmmm/openai.luau](https://github.com/Naymmmm/openai.luau) | 0 | OpenAI API-wrapper voor Lune en Roblox |
| [Kylaaa/TwitchBlox](https://github.com/Kylaaa/TwitchBlox) | 0 | Twitch-stream events in Roblox |
| [vweatherstation/vweatherstation-roblox](https://github.com/vweatherstation/vweatherstation-roblox) | 0 | Echt weer van de wereld live in je game syncen |
| [top-stats/analytics-roblox-integration](https://github.com/top-stats/analytics-roblox-integration) | 0 | TopStats analytics-integratie met track-API |

## AI-tools voor Roblox-development

MCP-servers, AI-agents en skills die in Studio kunnen bouwen. (34 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [boshyxd/robloxstudio-mcp](https://github.com/boshyxd/robloxstudio-mcp) | 486 | MCP-server: agentic AI-workflows in Roblox Studio |
| [Chrrxs/robloxstudio-mcp](https://github.com/Chrrxs/robloxstudio-mcp) | 253 | MCP-server: AI-agents laten debuggen, playtesten en screenshots maken in Studio |
| [hope1026/weppy-roblox-mcp](https://github.com/hope1026/weppy-roblox-mcp) | 61 | MCP-server + plugin: AI-assistenten scripts, terrain, lighting laten maken |
| [TabooHarmony/roblox-brain](https://github.com/TabooHarmony/roblox-brain) | 56 | Skill-library met Roblox Studio-kennis voor AI-coding agents |
| [MSayib/roblox-dev-skill](https://github.com/MSayib/roblox-dev-skill) | 25 | Kennisbank die AI-assistenten Roblox-experts maakt |
| [nonlooped/roblox-suite](https://github.com/nonlooped/roblox-suite) | 16 | Skill-set voor AI-agents met accurate Roblox-richtlijnen |
| [luumenlabs/luau-skills](https://github.com/luumenlabs/luau-skills) | 12 | Agent-skills voor Luau en Roblox-development |
| [AshExplained/roblox-skills](https://github.com/AshExplained/roblox-skills) | 10 | 34 Claude Code skills voor Roblox-gamedev |
| [CodePhobiia/claude-roblox-game-studio](https://github.com/CodePhobiia/claude-roblox-game-studio) | 9 | Claude Code als Roblox-studio: 36 agents, 50 skills, Luau-wiki |
| [Pugbread/ro-sync](https://github.com/Pugbread/ro-sync) | 8 | Local-first Studio control plane voor mensen en coding agents |
| [princeofscale/bloxforge](https://github.com/princeofscale/bloxforge) | 7 | Open-source AI-agent toolkit voor Studio |
| [andrian-syh/roblox-best-practices-skill](https://github.com/andrian-syh/roblox-best-practices-skill) | 7 | Roblox/Luau best-practices skill voor AI-agents |
| [JustineDevs/roblox-ai-os](https://github.com/JustineDevs/roblox-ai-os) | 7 | Roblox AI OS: skills voor Codex, Claude, Cursor |
| [EL4CTEO/rbx-studio-mcp](https://github.com/EL4CTEO/rbx-studio-mcp) | 6 | Gratis MCP-server voor Studio (35 tools, coding agents in een console-paneel) |
| [iamthebestts/RoDocs-MCP](https://github.com/iamthebestts/RoDocs-MCP) | 5 | MCP die je AI de juiste Roblox-docs geeft |
| [dig1t/skills](https://github.com/dig1t/skills) | 5 | AI-agent skills voor Roblox-development |
| [Onur45500/blockforge](https://github.com/Onur45500/blockforge) | 3 | Desktop-app om Roblox-games te bouwen met AI-agents |
| [EL4CTEO/roblox-devforum-mcp](https://github.com/EL4CTEO/roblox-devforum-mcp) | 3 | Geeft je AI-agent toegang tot de DevForum en docs |
| [Underscoretime/OpenBlox](https://github.com/Underscoretime/OpenBlox) | 3 | AI-systemen koppelen aan Roblox Studio |
| [OK-ORCO/roblox-portfolio-mcp](https://github.com/OK-ORCO/roblox-portfolio-mcp) | 3 | MCP-server: game-portfolio, Open Cloud analytics, Discord-feedback voor Claude |
| [aliboIly/Tripwire](https://github.com/aliboIly/Tripwire) | 3 | Agentic MCP: tests draaien en exploits in je eigen game vinden |
| [dillydog580/animate-roblox-characters](https://github.com/dillydog580/animate-roblox-characters) | 3 | AI-skill: R6/R15-animaties maken via Blender-rigs met GIF-preview |
| [gogolumo/rbsmithy-roblox-claude-skill](https://github.com/gogolumo/rbsmithy-roblox-claude-skill) | 3 | Claude-skill voor Luau, Rojo, multiplayer, QA en releases |
| [IvanKuria/bloxscout](https://github.com/IvanKuria/bloxscout) | 2 | MCP-server + CLI voor Roblox game-analytics |
| [frrazer/roblox-analytics-mcp](https://github.com/frrazer/roblox-analytics-mcp) | 1 | MCP-server voor experience-analytics (DAU, revenue, retentie) |
| [egwmiadg/luau-gemini](https://github.com/egwmiadg/luau-gemini) | 1 | Google Gemini in Roblox |
| [rbxrootx/roxo-mcp](https://github.com/rbxrootx/roxo-mcp) | 1 | MCP-native Rojo: filesystem-sync die AI-agents kunnen besturen |
| [MosheBarami/forgebridge](https://github.com/MosheBarami/forgebridge) | 1 | Brug tussen bijna elk AI-model en Roblox Studio (gratis) |
| [ShiroKSH/skills](https://github.com/ShiroKSH/skills) | 1 | Studio-skill + lokale MCP-bridge voor coding agents |
| [rengcor/SwordFactory-LuauAI](https://github.com/rengcor/SwordFactory-LuauAI) | 1 | Open-source multiplayer game als testbed voor AI-coding agents |
| [BokX1/RbxLuauLLM](https://github.com/BokX1/RbxLuauLLM) | 1 | LLM-wrapper: natuurlijke taal naar Luau/admin-acties via proxy |
| [szlay/roblox-base](https://github.com/szlay/roblox-base) | 1 | Claude Code starter: Rojo, Luau-checks, Studio-MCP en 32 skills |
| [10kkyvl/studioforge](https://github.com/10kkyvl/studioforge) | 0 | Project-workflow voor Claude Code + Studio: context, orchestratie, validatie |
| [cortex-rbx/roblox-ai-kit](https://github.com/cortex-rbx/roblox-ai-kit) | 0 | Plugin: Engels naar Luau + SDK voor pratende NPC's en moderatie |

## Tooling & workflow

Runtimes, sync-tools, package managers, asset-pipelines, CI en docs. (203 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [lune-org/lune](https://github.com/lune-org/lune) | 952 | Standalone Luau-runtime (scripts, place-files bewerken, CI) |
| [vinegarhq/vinegar](https://github.com/vinegarhq/vinegar) | 769 | Roblox Studio draaien op Linux |
| [MaximumADHD/Roblox-Client-Tracker](https://github.com/MaximumADHD/Roblox-Client-Tracker) | 546 | Automatisch bijgehouden info over elke Roblox-versie (API-dumps, FFlags) |
| [MaximumADHD/Roblox-Studio-Mod-Manager](https://github.com/MaximumADHD/Roblox-Studio-Mod-Manager) | 383 | Studio-bootstrapper: bestanden overriden, dev-branches, Fast Flags |
| [luau-lang/lute](https://github.com/luau-lang/lute) | 346 | Officiële standalone Luau-runtime voor algemeen gebruik |
| [rojo-rbx/rbxlx-to-rojo](https://github.com/rojo-rbx/rbxlx-to-rojo) | 297 | Bestaande Roblox-place eenmalig omzetten naar een Rojo-project |
| [stravant/LuaMinify](https://github.com/stravant/LuaMinify) | 276 | Lua-code minifier |
| [komaruworld/mocktail](https://github.com/komaruworld/mocktail) | 259 | Experimentele Roblox-compatibiliteitsruntime voor Linux/FreeBSD |
| [evaera/moonwave](https://github.com/evaera/moonwave) | 246 | Documentatie genereren uit commentaar in Luau-code |
| [rojo-rbx/rbx-dom](https://github.com/rojo-rbx/rbx-dom) | 197 | Roblox DOM + (de)serialisatie in Rust |
| [MaximumADHD/Roblox-FFlag-Tracker](https://github.com/MaximumADHD/Roblox-FFlag-Tracker) | 191 | Houdt wijzigingen in Roblox' publieke FFlags bij (zie nieuwe features vroeg) |
| [rojo-rbx/remodel](https://github.com/rojo-rbx/remodel) | 176 | Scriptbare multitool: instances, model-files, places en assets bewerken |
| [jackTabsCode/asphalt](https://github.com/jackTabsCode/asphalt) | 160 | Assets-as-files: afbeeldingen/audio automatisch uploaden |
| [LorettaDevs/Loretta](https://github.com/LorettaDevs/Loretta) | 152 | C# parser/analyse/transformatie voor Lua en Luau |
| [MaximumADHD/Roblox-File-Format](https://github.com/MaximumADHD/Roblox-File-Format) | 149 | C#-library om .rbxl/.rbxm te maken en bewerken |
| [Anaminus/rbxmk](https://github.com/Anaminus/rbxmk) | 134 | Tool om Roblox-bestanden te verwerken (scriptbaar) |
| [pesde-pkg/pesde](https://github.com/pesde-pkg/pesde) | 124 | Package manager voor Luau (Roblox + Lune) |
| [Ransomwave/azul](https://github.com/Ransomwave/azul) | 122 | Two-way sync waarbij Studio de bron van waarheid is |
| [blake-mealey/mantle](https://github.com/blake-mealey/mantle) | 116 | Infrastructure-as-code en deployment voor Roblox |
| [Kampfkarren/kampfkarren-luau-guidelines](https://github.com/Kampfkarren/kampfkarren-luau-guidelines) | 99 | Luau code-richtlijnen van een ervaren dev |
| [lopi-py/luau-lsp.nvim](https://github.com/lopi-py/luau-lsp.nvim) | 93 | Luau-LSP voor Neovim |
| [luohoa97/cordial](https://github.com/luohoa97/cordial) | 91 | Draait de Roblox-client native op Linux (geen Wine/emulator) |
| [Pseudoreality/Roblox-Identities](https://github.com/Pseudoreality/Roblox-Identities) | 73 | Uitleg van Roblox' script-identities en security-levels |
| [AeEn123/RoExtract](https://github.com/AeEn123/RoExtract) | 65 | Assets veilig extraheren uit je Roblox-installatie |
| [tiffany352/Roblox-Tag-Editor](https://github.com/tiffany352/Roblox-Tag-Editor) | 63 | CollectionService-tags beheren in Studio |
| [typeforge-luau/typeforge](https://github.com/typeforge-luau/typeforge) | 54 | Type-function utilities voor de nieuwe Luau type-solver |
| [prepsure/team-create-hats](https://github.com/prepsure/team-create-hats) | 52 | Character-customization voor Team Create |
| [MaximumADHD/Roblox-API-Dump-Tool](https://github.com/MaximumADHD/Roblox-API-Dump-Tool) | 48 | API-dumps bekijken en vergelijken (nieuwe API's ontdekken) |
| [revolutionxk/roblox-modloader](https://github.com/revolutionxk/roblox-modloader) | 46 | Mod-loader voor Studio met native C++ mods |
| [pjankiewicz/luaur](https://github.com/pjankiewicz/luaur) | 41 | Luau (compiler, VM, type-checker) volledig vertaald naar Rust, draait op wasm |
| [latte-soft/maui](https://github.com/latte-soft/maui) | 39 | Modules bundelen tot uitvoerbare Luau-scripts |
| [LDGerrits/rogen](https://github.com/LDGerrits/rogen) | 37 | CLI voor feature-based architectuur in Roblox-projecten |
| [gaymeowing/luauberries](https://github.com/gaymeowing/luauberries) | 37 | Collectie libraries voor Lune, Luau en Roblox |
| [tacheometry/Rostar](https://github.com/tacheometry/Rostar) | 37 | Volledig beheerde Rojo-helper |
| [roblox-aurora/zircon](https://github.com/roblox-aurora/zircon) | 36 | Geavanceerde debug-console met eigen scriptingtaal |
| [photobooth-rbx/photobooth-plugin](https://github.com/photobooth-rbx/photobooth-plugin) | 35 | Screenshots/afbeeldingen maken in Studio (icons, thumbnails) |
| [Bottersnike/eryx](https://github.com/Bottersnike/eryx) | 34 | Standalone Luau-runtime met standaard libraries |
| [filiptibell/roblox-ui](https://github.com/filiptibell/roblox-ui) | 33 | Roblox-explorer in VS Code (externe editor) |
| [Sleitnick/luau-api](https://github.com/Sleitnick/luau-api) | 33 | Onofficiële documentatie van de Luau C API |
| [dphfox/tiniest](https://github.com/dphfox/tiniest) | 31 | Minimale, draagbare test-library |
| [wolfgangmeyers/bloxcode](https://github.com/wolfgangmeyers/bloxcode) | 31 | Roblox-scripts maken met visuele programmeerblokken |
| [freeway-rbx/freeway](https://github.com/freeway-rbx/freeway) | 28 | 3D-modellen en afbeeldingen live linken van een map naar Studio (voor artists) |
| [luau-lang/playground](https://github.com/luau-lang/playground) | 28 | Web-playground: Luau type-checken, compileren en bytecode inspecteren |
| [CavefulGames/dalbit](https://github.com/CavefulGames/dalbit) | 28 | Luau-naar-Lua transpiler |
| [tacheometry/testez-companion](https://github.com/tacheometry/testez-companion) | 27 | TestEZ-tests draaien vanuit VS Code |
| [christopher-buss/jest-roblox-cli](https://github.com/christopher-buss/jest-roblox-cli) | 25 | CLI om Jest-tests in Roblox te draaien |
| [evaera/vscode-roblox-api-explorer](https://github.com/evaera/vscode-roblox-api-explorer) | 24 | Roblox API-explorer in VS Code |
| [seaofvoices/npmluau](https://github.com/seaofvoices/npmluau) | 23 | npm gebruiken voor Luau-projecten |
| [roblox-aurora/rbx-log](https://github.com/roblox-aurora/rbx-log) | 23 | Structured logging library |
| [fewkz/studio-wally](https://github.com/fewkz/studio-wally) | 23 | Wally-packages installeren vanuit Studio |
| [emppu-dev/roblox-decal-mass-uploader](https://github.com/emppu-dev/roblox-decal-mass-uploader) | 23 | Massaal afbeeldingen als decals uploaden |
| [polychromatist/tree-sitter-luau](https://github.com/polychromatist/tree-sitter-luau) | 21 | Tree-sitter grammar voor Luau (editors) |
| [devSparkle/Overture](https://github.com/devSparkle/Overture) | 21 | Source-code management engine voor Roblox |
| [Dekkonot/rbx-api-dump](https://github.com/Dekkonot/rbx-api-dump) | 20 | Werken met de Roblox API-dump |
| [0neShot101/rbxdev-ls](https://github.com/0neShot101/rbxdev-ls) | 19 | Luau language server + VS Code extensie met live-game tooling |
| [fiveman1/rbxm-parser-ts](https://github.com/fiveman1/rbxm-parser-ts) | 19 | .rbxm-bestanden parsen in TypeScript |
| [nidorx/roblox-rojo-bundle](https://github.com/nidorx/roblox-rojo-bundle) | 18 | Rojo-template die bestanden bundelt/concatenatie |
| [tapple/pyrxbm](https://github.com/tapple/pyrxbm) | 18 | Python-library om model/place-bestanden te maken en bewerken |
| [seaofvoices/generator-luau](https://github.com/seaofvoices/generator-luau) | 17 | Project-generator voor Luau |
| [pwnwrkz/tungsten](https://github.com/pwnwrkz/tungsten) | 16 | Nog een asset-tool (Tarmac/Asphalt-alternatief) |
| [sircfenner/AutoImport](https://github.com/sircfenner/AutoImport) | 16 | Autocomplete voor require en GetService |
| [vurvdev/rluau](https://github.com/vurvdev/rluau) | 16 | Idiomatische Luau-bindings in Rust |
| [vocksel/prefabs](https://github.com/vocksel/prefabs) | 16 | Herbruikbare assets die gesynchroniseerd blijven door je hele game |
| [christopher-buss/bedrock](https://github.com/christopher-buss/bedrock) | 15 | Infrastructure-as-code voor Roblox |
| [argon-rbx/argon-roblox](https://github.com/argon-rbx/argon-roblox) | 14 | Argon: Rojo-alternatief voor two-way sync |
| [Bytebit-Org/fitumi](https://github.com/Bytebit-Org/fitumi) | 14 | Dependencies faken voor unit tests |
| [larvae-luau/larvae](https://github.com/larvae-luau/larvae) | 14 | Formatter + linter voor Luau |
| [bookek/roblox-slang](https://github.com/bookek/roblox-slang) | 13 | Type-safe i18n/vertaling code-generator |
| [brightluau/bright](https://github.com/brightluau/bright) | 13 | Scriptbare tool om Luau-code te transformeren/transpileren |
| [Vexot/CustomEmoteThumbnail](https://github.com/Vexot/CustomEmoteThumbnail) | 13 | Volledig eigen emote-thumbnails maken |
| [lest-luau/lest](https://github.com/lest-luau/lest) | 12 | Test-toolchain voor Luau |
| [Barocena/RBX-Fileview](https://github.com/Barocena/RBX-Fileview) | 12 | Leesbare, diff-vriendelijke dumps van place/model-bestanden |
| [ArvidSilverlock/Pilot.lua-Luau-LSP](https://github.com/ArvidSilverlock/Pilot.lua-Luau-LSP) | 12 | LSP-definities generator voor Waste of Space (in-game programmeren) |
| [typeforge-luau/typebrick](https://github.com/typeforge-luau/typebrick) | 11 | Type-function utilities voor Roblox-types |
| [vocksel/studio-bridge](https://github.com/vocksel/studio-bridge) | 11 | Automatisch bestanden syncen naar Studio |
| [seaofvoices/luau-path](https://github.com/seaofvoices/luau-path) | 11 | Bestandspad-library voor Luau |
| [iLynkk/roblox-assets-extractor](https://github.com/iLynkk/roblox-assets-extractor) | 11 | Gecachte Roblox-assets extraheren |
| [stravant/DevComment](https://github.com/stravant/DevComment) | 10 | 3D-commentaren in je wereld, gesynced tussen Edit, test en live |
| [Parritz/LuaCompact](https://github.com/Parritz/LuaCompact) | 10 | Lua-bundler die meerdere bestanden samenvoegt |
| [DexxterDax/rbxlx-to-rojo-py](https://github.com/DexxterDax/rbxlx-to-rojo-py) | 10 | Python-port van rbxlx-to-rojo |
| [32bitx64bit/Tipsy](https://github.com/32bitx64bit/Tipsy) | 10 | Open-source Roblox-runtime voor Linux (Go/C) |
| [Quenty/ClassConverterPlugin](https://github.com/Quenty/ClassConverterPlugin) | 9 | Instances naar een andere class converteren |
| [KinderBarrel/AutoCompletePlus](https://github.com/KinderBarrel/AutoCompletePlus) | 9 | Instant imports van services/modules/instances |
| [filiptibell/wally-utilities-extension](https://github.com/filiptibell/wally-utilities-extension) | 9 | Autocomplete en diagnostics voor Wally |
| [CompeyDev/lune-packaging](https://github.com/CompeyDev/lune-packaging) | 9 | Cross-platform packaging voor Lune |
| [stravant/roblox-geometry](https://github.com/stravant/roblox-geometry) | 8 | getGeometry en closest-mesh-edge helpers |
| [OssieNomae/Blueprint](https://github.com/OssieNomae/Blueprint) | 8 | Standaard script-template vervangen |
| [lutest-dev/lutest](https://github.com/lutest-dev/lutest) | 8 | Moderne test-runner voor Luau |
| [cxmeel/dump-parser](https://github.com/cxmeel/dump-parser) | 8 | Roblox API-dump parsen |
| [IconPippi/MockMessagingService](https://github.com/IconPippi/MockMessagingService) | 8 | Lokale MessagingService voor testen |
| [ericplane/Luix](https://github.com/ericplane/Luix) | 8 | VS Code: prop-hints en docs voor React-Luau, Roact, Fusion en Vide |
| [jiwonz/lune-pathfs](https://github.com/jiwonz/lune-pathfs) | 8 | Path + filesystem utilities voor Lune |
| [Cobbdevv/luau-grader](https://github.com/Cobbdevv/luau-grader) | 8 | Statische analyse en beoordeling van Luau-code (desktop + CLI) |
| [dubit/roblox-dubit-tools](https://github.com/dubit/roblox-dubit-tools) | 8 | Monorepo met studio-tools van Dubit |
| [Unreal-Works/jest-roblox-assassin](https://github.com/Unreal-Works/jest-roblox-assassin) | 7 | Jest-lua laten voelen als echte Jest |
| [benbrimeyer/rbx-plugin-testServiceWatcher](https://github.com/benbrimeyer/rbx-plugin-testServiceWatcher) | 7 | Automatisch tests draaien bij code-wijziging |
| [cxmeel/resurface-plugin](https://github.com/cxmeel/resurface-plugin) | 7 | Surfaces naar studs converteren (retro-look) |
| [WaviestBalloon/RobloxFLogArchive](https://github.com/WaviestBalloon/RobloxFLogArchive) | 7 | Plaintext FLogs uit de Roblox-binary extraheren |
| [RadiatedExodus/RunLSC](https://github.com/RadiatedExodus/RunLSC) | 7 | Scripts uitvoeren in server- of client-context vanuit Studio |
| [DervexDev/setup-roblox-studio](https://github.com/DervexDev/setup-roblox-studio) | 7 | Roblox Studio installeren in CI/CD |
| [pesde-pkg/scripts](https://github.com/pesde-pkg/scripts) | 7 | Scripts en utilities voor pesde (Rojo-integratie) |
| [tree-sitter-grammars/tree-sitter-luau](https://github.com/tree-sitter-grammars/tree-sitter-luau) | 7 | Tree-sitter grammar voor Luau |
| [BrookenRecord/unicode-segmentation](https://github.com/BrookenRecord/unicode-segmentation) | 7 | Grapheme/word/sentence-segmentatie (UAX#29) |
| [MineBill/odin-luau](https://github.com/MineBill/odin-luau) | 7 | Luau-bindings voor Odin |
| [Mullets-Gavin/Loader](https://github.com/Mullets-Gavin/Loader) | 7 | Library loader met lazy-loading |
| [sircfenner/CollisionGroupsEditor](https://github.com/sircfenner/CollisionGroupsEditor) | 6 | Alternatieve collision-groups editor |
| [EgoMoose/better-view-selector](https://github.com/EgoMoose/better-view-selector) | 6 | Betere view-selector |
| [Wharkk/RoGit-Plugin](https://github.com/Wharkk/RoGit-Plugin) | 6 | Git (push/pull/diff/branch) in Studio |
| [GooglyBlox/rbxlx-explorer](https://github.com/GooglyBlox/rbxlx-explorer) | 6 | Web-based explorer en editor voor .rbxlx |
| [patangation/roblox-script-exporter](https://github.com/patangation/roblox-script-exporter) | 6 | Scripts uit .rbxl-bestanden extraheren en ordenen (Lune) |
| [jiwonz/pesde-multitarget](https://github.com/jiwonz/pesde-multitarget) | 6 | Build-script voor meerdere pesde-targets |
| [techs-sus/azalea](https://github.com/techs-sus/azalea) | 6 | Modellen omzetten naar grote scripts (encode in Rust, decode in Luau) |
| [l3dotdev/EzSpec](https://github.com/l3dotdev/EzSpec) | 6 | Eenvoudig unit-testing framework |
| [cxmeel/roblox-font-list-generator](https://github.com/cxmeel/roblox-font-list-generator) | 6 | Genereert automatisch lijst van lokale en cloud-fonts |
| [AstolfoBrew/SimpleBench](https://github.com/AstolfoBrew/SimpleBench) | 6 | Simpele benchmarking-tool |
| [nokogoat/Rowork](https://github.com/nokogoat/Rowork) | 6 | Meta-framework CLI: zet Rojo/roblox-ts/Flamework op en genereert boilerplate |
| [filiptibell/roblox-studio-utils](https://github.com/filiptibell/roblox-studio-utils) | 6 | Cross-platform library om met Roblox Studio te communiceren |
| [Bytebit-Org/event-log-roblox-plugin](https://github.com/Bytebit-Org/event-log-roblox-plugin) | 5 | Alle RemoteEvents/BindableEvents monitoren |
| [morgann1/studio-discover](https://github.com/morgann1/studio-discover) | 5 | Wally- en Pesde-packages browsen/installeren |
| [SadCivilian/luauMacros](https://github.com/SadCivilian/luauMacros) | 5 | Macro-systeem voor Luau |
| [ssynical/luau-parser](https://github.com/ssynical/luau-parser) | 5 | Snelle Luau lexer/parser met volledige AST |
| [Paficent/Dex](https://github.com/Paficent/Dex) | 5 | Devtools voor Roblox |
| [verde-rbx/verde](https://github.com/verde-rbx/verde) | 5 | Bestanden syncen tussen Studio en je editor |
| [OMouta/Jelly](https://github.com/OMouta/Jelly) | 5 | npm-achtige package manager bovenop Wally |
| [NotDSF/LuauDissasembler](https://github.com/NotDSF/LuauDissasembler) | 5 | Luau-bytecode disassembler |
| [Conikku/ClassicHeadConversion](https://github.com/Conikku/ClassicHeadConversion) | 5 | Zet dynamic heads om naar classic heads |
| [OnaticDev/Roblox-Luau-Reference](https://github.com/OnaticDev/Roblox-Luau-Reference) | 4 | Minder bekende Luau-features, syntax en patterns met voorbeelden |
| [KSAGlory/KSA-Accessibility-Preflight](https://github.com/KSAGlory/KSA-Accessibility-Preflight) | 4 | Toegankelijkheid-check: contrast, tekstgrootte, reduced motion |
| [suscersal/roblox-studio-web](https://github.com/suscersal/roblox-studio-web) | 4 | .rbxl-parser + web-viewer (Studio in de browser) |
| [jaipack17/Gizmo2D](https://github.com/jaipack17/Gizmo2D) | 4 | Visuele debugging voor GUI's |
| [nightcycle/file-to-luau](https://github.com/nightcycle/file-to-luau) | 4 | Bestanden naar Luau-script converteren |
| [Dekkonot/run-in-roblox](https://github.com/Dekkonot/run-in-roblox) | 4 | Scripts in Roblox Studio uitvoeren vanaf de command line (CI) |
| [flipbook-labs/storyteller](https://github.com/flipbook-labs/storyteller) | 4 | Engine achter Flipbook: UI-stories ontdekken en renderen |
| [CompeyDev/rojo-build-action](https://github.com/CompeyDev/rojo-build-action) | 4 | GitHub Action die Rojo-builds automatiseert |
| [zilibobi/luau-tree.nvim](https://github.com/zilibobi/luau-tree.nvim) | 4 | Roblox DataModel in Neovim tonen |
| [SequesteredOne/wally-vendor](https://github.com/SequesteredOne/wally-vendor) | 4 | Wally-dependencies overal vendoren |
| [amirfarzamnia/json-schema-to-luau](https://github.com/amirfarzamnia/json-schema-to-luau) | 4 | JSON Schema omzetten naar Luau-types |
| [Avant-Rbx/Avant-Plugin](https://github.com/Avant-Rbx/Avant-Plugin) | 3 | Unit tests draaien in Studio |
| [bstummer/benchmarking](https://github.com/bstummer/benchmarking) | 3 | Code-snelheid meten en vergelijken |
| [Dekkonot/open-cloud-execute-gui](https://github.com/Dekkonot/open-cloud-execute-gui) | 3 | GUI-app om Luau via Open Cloud uit te voeren |
| [foxjetstudios/sheetsync-plugin](https://github.com/foxjetstudios/sheetsync-plugin) | 3 | Google Sheets data importeren in Studio |
| [depthso/Luau-StringBuilder](https://github.com/depthso/Luau-StringBuilder) | 3 | 800x snellere string-concatenatie |
| [Unreal-Works/roblox-coverage](https://github.com/Unreal-Works/roblox-coverage) | 3 | Code-coverage voor Roblox Luau |
| [this-fifo/DataStoria](https://github.com/this-fifo/DataStoria) | 3 | DataStores bekijken/bewerken vanuit VS Code met revisie-geschiedenis |
| [luumenlabs/luumen](https://github.com/luumenlabs/luumen) | 3 | Unified CLI voor Luau-development |
| [vocksel/mock](https://github.com/vocksel/mock) | 3 | Jest-achtige mocks voor unit tests |
| [ewd3v/lune_darklua_build](https://github.com/ewd3v/lune_darklua_build) | 3 | darklua build-script voor Lune |
| [intervinn/indium](https://github.com/intervinn/indium) | 3 | Minimalistische backend voor Lune |
| [SirBepy/mc_skin_to_roblox_clothing](https://github.com/SirBepy/mc_skin_to_roblox_clothing) | 3 | Minecraft-skin omzetten naar Roblox-kleding |
| [cortesi/luau-analyze](https://github.com/cortesi/luau-analyze) | 3 | In-process Luau type checker voor Rust |
| [ddavness/scoop-roblox](https://github.com/ddavness/scoop-roblox) | 3 | Scoop-bucket met Roblox dev-CLI's voor Windows |
| [TheNexusAvenger/Pulse](https://github.com/TheNexusAvenger/Pulse) | 2 | Debug-library met geheugenstatistieken |
| [nightcycle/spreadsheet-to-luau](https://github.com/nightcycle/spreadsheet-to-luau) | 2 | Google Sheets/CSV/XLSX naar Luau-modules (game-balancing data!) |
| [Name-hw/MeshConvert](https://github.com/Name-hw/MeshConvert) | 2 | Meshes op allerlei manieren converteren |
| [YusufVyce/Vyce-Luau-ErrorAnalyzer](https://github.com/YusufVyce/Vyce-Luau-ErrorAnalyzer) | 2 | AST-gebaseerde runtime-diagnostics in Studio |
| [include-marcy/luau-class-generator](https://github.com/include-marcy/luau-class-generator) | 2 | VS Code-extensie die OOP-boilerplate genereert |
| [peyton2465/rbx-merge](https://github.com/peyton2465/rbx-merge) | 2 | Modules samenvoegen tot één script |
| [astriaInight/LuauLexer](https://github.com/astriaInight/LuauLexer) | 2 | Luau-lexer voor Roblox |
| [Carlitos999yt/RobloxScriptExplorer](https://github.com/Carlitos999yt/RobloxScriptExplorer) | 2 | C#-tool om Luau-scripts in Roblox-binaries te parsen, bewerken en exporteren |
| [cvipdebug/roblox-outfit-studio](https://github.com/cvipdebug/roblox-outfit-studio) | 2 | Desktop-editor voor shirts/pants met live 3D R6-preview |
| [afterl1ght/BloxClothViewer](https://github.com/afterl1ght/BloxClothViewer) | 2 | Godot-app om classic shirts/pants te previewen |
| [TakuKitamura/rbxlx-to-rojo-json](https://github.com/TakuKitamura/rbxlx-to-rojo-json) | 2 | Zet .rbxlx om naar Rojo project-JSON |
| [Esocietyhere/rit](https://github.com/Esocietyhere/rit) | 2 | CLI voor Roblox-projectbeheer |
| [lunarlattice0/sifter](https://github.com/lunarlattice0/sifter) | 2 | Haalt je game-assets terug uit Wireshark PCAP-captures |
| [stravant/roblox-gripedit](https://github.com/stravant/roblox-gripedit) | 1 | Tool-grip editor |
| [RullzVyline/VectorFlow](https://github.com/RullzVyline/VectorFlow) | 1 | Realtime sync tussen Blender en Roblox Studio (EditableMesh) |
| [ewd3v/roblox_graft](https://github.com/ewd3v/roblox_graft) | 1 | Hot reloading voor Roblox |
| [cayasde/rbxperf](https://github.com/cayasde/rbxperf) | 1 | CLI voor performance-regressies |
| [Kiborgik/TasteTest](https://github.com/Kiborgik/TasteTest) | 1 | Jest-achtige tests in Studio én onder Lune in CI |
| [vskstudio/naht](https://github.com/vskstudio/naht) | 1 | Bidirectionele, conflict-veilige sync tussen filesystem en Studio (Rust) |
| [Paryx-Labs/rbxlx-extractor](https://github.com/Paryx-Labs/rbxlx-extractor) | 1 | Lune-extensie die .rbxlx naar Rojo-formaat extraheert |
| [R-unic/rbxm-to-ts](https://github.com/R-unic/rbxm-to-ts) | 1 | TypeScript-types genereren uit een .rbxm-bestand |
| [daymxn/rLog](https://github.com/daymxn/rLog) | 1 | Context-gebaseerde server-logging |
| [Kooraseru/Arbor](https://github.com/Kooraseru/Arbor) | 1 | Instance-hiërarchieën zichtbaar maken voor het Luau-typesysteem |
| [chemiclast/rasorite](https://github.com/chemiclast/rasorite) | 1 | Rust-tool om Roblox-analytics benchmarks te plotten |
| [Plumvery/rocas](https://github.com/Plumvery/rocas) | 1 | Open Cloud asset-sync |
| [Glladiator29/RbxRuntimeTest](https://github.com/Glladiator29/RbxRuntimeTest) | 1 | Lichte runtime-tests alleen in Studio |
| [notmagniill/tungsten](https://github.com/notmagniill/tungsten) | 1 | Asset-CLI zoals Tarmac/Asphalt |
| [RoGrid-HQ/rogrid](https://github.com/RoGrid-HQ/rogrid) | 1 | Framework om games vanuit je editor te bouwen |
| [robinskaba/roge](https://github.com/robinskaba/roge) | 1 | CLI voor package-versiebeheer |
| [SpaceSquare640/RB_Skin_Forge](https://github.com/SpaceSquare640/RB_Skin_Forge) | 1 | Afbeeldingen en OBJ-meshes omzetten naar kledingtemplates |
| [morgann1/studio-theme](https://github.com/morgann1/studio-theme) | 0 | VS Code-thema's gebruiken in Studio |
| [morgann1/waldo](https://github.com/morgann1/waldo) | 0 | Het "add"-commando dat Wally mist |
| [Hawakiki/roblox-rarn](https://github.com/Hawakiki/roblox-rarn) | 0 | Package manager voor het Wally-register zonder Rojo, met types |
| [rib3ye/RoInit](https://github.com/rib3ye/RoInit) | 0 | Productieklaar Roblox-project in één commando |
| [revvy02/rbx-iconify](https://github.com/revvy02/rbx-iconify) | 0 | Iconify-iconen: sprite sheets + Luau-index genereren |
| [Daemon6109/roblox-forge](https://github.com/Daemon6109/roblox-forge) | 0 | Local-first visuele systeem-editor voor Roblox |
| [Borritomes/vconsole](https://github.com/Borritomes/vconsole) | 0 | Developer-console backend (Source Engine-stijl) |
| [IanKang678/roblox-engine-scaling-study](https://github.com/IanKang678/roblox-engine-scaling-study) | 0 | Onderzoek: hoe frame time en geheugen schalen met aantal projectielen |
| [LiamRousselle/Fracture](https://github.com/LiamRousselle/Fracture) | 0 | Sorteert gamebestanden volgens feature-based architectuur |
| [memothelemo/trail](https://github.com/memothelemo/trail) | 0 | Event-based diagnostics/tracing (zoals tokio-rs/tracing) |
| [ujji-k06/rojo-doctor](https://github.com/ujji-k06/rojo-doctor) | 0 | Structurele diagnostiek voor Rojo-projecten |
| [rbx-dev-tools/luau-lsp-boundary](https://github.com/rbx-dev-tools/luau-lsp-boundary) | 0 | Filtert auto-imports die client/server-grens overschrijden |
| [ASecondOne/nyjo](https://github.com/ASecondOne/nyjo) | 0 | Rojo-achtige file-syncer voor Linux |
| [afrxo/feago](https://github.com/afrxo/feago) | 0 | Code per feature organiseren, genereert Rojo-projectbestanden |
| [hautajoki/tessera](https://github.com/hautajoki/tessera) | 0 | TypeScript-first asset-, deploy- en Open Cloud-workflow |
| [robinskaba/rbxpmux](https://github.com/robinskaba/rbxpmux) | 0 | Games met meerdere places die dezelfde instances delen publiceren |
| [robinskaba/rslnk](https://github.com/robinskaba/rslnk) | 0 | Persistente, place-specifieke Studio-shortcuts |
| [svvly2/lettuce](https://github.com/svvly2/lettuce) | 0 | Veilig assets vervangen in Studio via OAuth |
| [StephenSHorton/biome-plugin-roblox-ts](https://github.com/StephenSHorton/biome-plugin-roblox-ts) | 0 | roblox-ts lintregels voor Biome (i.p.v. ESLint) |
| [projectx667/bloxcode-plus](https://github.com/projectx667/bloxcode-plus) | 0 | Visueel programmeren: Luau schrijven met Blockly-blokken |
| [rbx-forge/rbx-cli](https://github.com/rbx-forge/rbx-cli) | 0 | Declaratieve deploy + live-ops (servers, data, spelers) via Open Cloud |
| [Qoxu/Beep](https://github.com/Qoxu/Beep) | 0 | Test-toolkit: performance-analyse, visuele debugging, physics-tests |

## Studio-plugins

Handige plugins voor bouwen, terrain, UI en workflow. (25 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [MaximumADHD/Roblox-Plugins](https://github.com/MaximumADHD/Roblox-Plugins) | 137 | Collectie Studio-plugins van MaximumADHD |
| [welcomestohell/rocket](https://github.com/welcomestohell/rocket) | 26 | Command-launcher plugin voor Studio |
| [SovereignSatellite/Binja-Luau](https://github.com/SovereignSatellite/Binja-Luau) | 18 | Binary Ninja plugin voor Luau-bytecode analyse |
| [stravant/roblox-redupe](https://github.com/stravant/roblox-redupe) | 15 | Array/herhaal-geometrie plugin |
| [Dekkonot/rbx-instance-serializer](https://github.com/Dekkonot/rbx-instance-serializer) | 11 | Instances naar Luau-code serialiseren (plugin) |
| [Anaminus/hotswap](https://github.com/Anaminus/hotswap) | 9 | Plugin-ontwikkeling versnellen (hot reload) |
| [Ultrasonic1209/Zappy](https://github.com/Ultrasonic1209/Zappy) | 8 | Zap-playground als Studio-plugin |
| [Neohertz/comet](https://github.com/Neohertz/comet) | 7 | Framework voor Studio-plugins (roblox-ts) |
| [Rawblocky/RobloxPlugin-SubwaySurfers](https://github.com/Rawblocky/RobloxPlugin-SubwaySurfers) | 7 | Grap-plugin: Subway Surfers in Studio |
| [seaofvoices/react-roblox-studio-plugin](https://github.com/seaofvoices/react-roblox-studio-plugin) | 6 | React-componenten voor plugins |
| [evaera/roblox-image-size](https://github.com/evaera/roblox-image-size) | 6 | Pixelgrootte van image-assets opvragen |
| [stravant/draggerframework](https://github.com/stravant/draggerframework) | 4 | Studio's DraggerFramework draaiend buiten plugin-security (in-game bouwtools!) |
| [stravant/roblox-gapfill](https://github.com/stravant/roblox-gapfill) | 3 | GapFill plugin (gaten tussen parts vullen) |
| [stravant/roblox-materialflip](https://github.com/stravant/roblox-materialflip) | 3 | MaterialFlip plugin (textures draaien) |
| [stravant/roblox-resizealign](https://github.com/stravant/roblox-resizealign) | 2 | ResizeAlign plugin |
| [mattqdev/Performance-Heatmap](https://github.com/mattqdev/Performance-Heatmap) | 2 | Plugin: heatmap van performance-problemen in je map |
| [KhanPython/LoopCut](https://github.com/KhanPython/LoopCut) | 2 | Loop-cut zoals in Blender, voor Studio |
| [Blupo/PropertiesMod](https://github.com/Blupo/PropertiesMod) | 2 | Alternatief Properties-venster voor Studio |
| [ivadsiulsgames/tycooncreator](https://github.com/ivadsiulsgames/tycooncreator) | 2 | Tycoon-maker tool |
| [rbxxaxa/RopeMaster](https://github.com/rbxxaxa/RopeMaster) | 2 | Plugin: snel touwen maken |
| [morgann1/stylua-for-roblox](https://github.com/morgann1/stylua-for-roblox) | 1 | StyLua als Studio-plugin |
| [makwira/makwira](https://github.com/makwira/makwira) | 1 | Package manager zonder plugin |
| [stravant/roblox-ropetool](https://github.com/stravant/roblox-ropetool) | 0 | RopeTool plugin |
| [stravant/roblox-adhoc](https://github.com/stravant/roblox-adhoc) | 0 | Veel micro-tools in één plugin |
| [Apisalam/BloxQA](https://github.com/Apisalam/BloxQA) | 0 | Plugin voor geautomatiseerde QA en gameplay-tests |

## Leren, open-source games & collecties

Artikelen, complete open-source games, templates en curated lijsten. (117 repos)

| Repo | ⭐ | Wat het doet |
|---|---:|---|
| [Quenty/NevermoreEngine](https://github.com/Quenty/NevermoreEngine) | 612 | Enorme verzameling herbruikbare game-modules |
| [Kampfkarren/Roblox](https://github.com/Kampfkarren/Roblox) | 393 | Scripts uit een echte game (o.a. DataStore2) |
| [littensy/slither](https://github.com/littensy/slither) | 202 | Complete open-source game (roblox-ts + React) |
| [elevenpassin/awesome-roblox](https://github.com/elevenpassin/awesome-roblox) | 196 | Curated lijst van resources, plugins en frameworks |
| [EgoMoose/Articles](https://github.com/EgoMoose/Articles) | 147 | Diepgaande artikelen over wiskunde/CFrames/physics in Roblox |
| [loominatrx/useful-roblox-resources](https://github.com/loominatrx/useful-roblox-resources) | 114 | Curated lijst met nuttige Roblox-resources |
| [awesome-roblox/awesome-roblox](https://github.com/awesome-roblox/awesome-roblox) | 81 | Curated lijst van Roblox OSS |
| [littensy/fishing-minigame](https://github.com/littensy/fishing-minigame) | 77 | Minimale recreatie van Fisch (vis-minigame) |
| [Anaminus/roblox-library](https://github.com/Anaminus/roblox-library) | 73 | Collectie modules, scripts en snippets |
| [MonzterDev/Roblox-TS-Template](https://github.com/MonzterDev/Roblox-TS-Template) | 70 | roblox-ts template met Flamework + ProfileService |
| [Sleitnick/RbxCookbook](https://github.com/Sleitnick/RbxCookbook) | 69 | Handige Lua-snippets voor Roblox |
| [MiaGobble/Open-Sourced-Projects](https://github.com/MiaGobble/Open-Sourced-Projects) | 54 | Oude/onafgemaakte/geannuleerde games en projecten open-source (.rbxl) |
| [MaximumADHD/Roblox-Boilerplate](https://github.com/MaximumADHD/Roblox-Boilerplate) | 49 | Handige fragmenten voor het maken van Roblox-games |
| [Coyenn/awesome-roblox-ts](https://github.com/Coyenn/awesome-roblox-ts) | 43 | Alle packages voor roblox-ts |
| [EgoMooseOldProjects/ExampleDump](https://github.com/EgoMooseOldProjects/ExampleDump) | 37 | Voorbeeldcode bij EgoMoose's video's en artikelen (CFrame-wiskunde) |
| [MayGo/maze-world](https://github.com/MayGo/maze-world) | 35 | Open-source doolhof-game |
| [B-Ricey763/Roblox-Studio-Tycoon](https://github.com/B-Ricey763/Roblox-Studio-Tycoon) | 35 | Tycoon-code met uitleg (tutorialserie) |
| [YetAnotherClown/awesome-react-lua](https://github.com/YetAnotherClown/awesome-react-lua) | 30 | Awesome-lijst voor React-lua |
| [littensy/charm-example](https://github.com/littensy/charm-example) | 29 | Voorbeeldgame gebouwd met Charm (state management) |
| [EgoMooseOldProjects/Vector3-and-CFrame](https://github.com/EgoMooseOldProjects/Vector3-and-CFrame) | 25 | Vector3 en CFrame nagebouwd in pure Lua en C# (leer hoe ze werken) |
| [evaera/LuaAlgorithms](https://github.com/evaera/LuaAlgorithms) | 22 | Generieke algoritmes voor Roblox |
| [seaofvoices/awesome-luau](https://github.com/seaofvoices/awesome-luau) | 22 | Handpicked lijst met kwaliteits-Luau-packages (npm) |
| [BrookenRecord/tabletop-island](https://github.com/BrookenRecord/tabletop-island) | 22 | Open-source sociale game met tafelspellen |
| [jaipack17/write-ups](https://github.com/jaipack17/write-ups) | 21 | Artikelen en onderzoek over Roblox-physics/wiskunde |
| [evilbocchi/eternal-empire](https://github.com/evilbocchi/eternal-empire) | 17 | Complete tycoon/incremental game open-source (roblox-ts) |
| [MonzterDev/Roblox-Game-Template](https://github.com/MonzterDev/Roblox-Game-Template) | 16 | Luau game-template met Module Framework + ProfileService |
| [Xyraniz/VaultUI](https://github.com/Xyraniz/VaultUI) | 16 | Collectie van 15+ gratis UI-libraries |
| [Emancyphur/Roblox-Studio-Tutorials](https://github.com/Emancyphur/Roblox-Studio-Tutorials) | 15 | Broncode en modellen van Roblox Studio tutorials |
| [LPGhatguy/roads](https://github.com/LPGhatguy/roads) | 15 | Rojo tech-demo |
| [Bytebit-Org/lua-statistics](https://github.com/Bytebit-Org/lua-statistics) | 14 | Statistische functies voor Lua |
| [LastTalon/sentinel-core](https://github.com/LastTalon/sentinel-core) | 13 | Complete co-op horde-survival game open-source |
| [Fizzyhex/price-point](https://github.com/Fizzyhex/price-point) | 12 | Complete open-source game: raad marketplace-prijzen |
| [ffrostfall/roblox-writeups](https://github.com/ffrostfall/roblox-writeups) | 11 | Diepgaande technische writeups over Roblox |
| [MiaGobble/Praxis](https://github.com/MiaGobble/Praxis) | 11 | Collectie libraries en utilities |
| [howmanysmall/DataStructures](https://github.com/howmanysmall/DataStructures) | 10 | Datastructuren in Lua |
| [rghv234/pokemonbrickbronze](https://github.com/rghv234/pokemonbrickbronze) | 10 | Bestanden van de Pokémon Brick Bronze game |
| [elomala/Fighting-game](https://github.com/elomala/Fighting-game) | 8 | Open-source vechtgame |
| [spotco/RobeatsCustomServerTemplate](https://github.com/spotco/RobeatsCustomServerTemplate) | 8 | Open-source Robeats rhythm-game server-template |
| [devsarim/roblox-project-template](https://github.com/devsarim/roblox-project-template) | 7 | Boilerplate: synced state, data saving, synced UI |
| [B-Ricey763/Roblox-Snowball-Fight](https://github.com/B-Ricey763/Roblox-Snowball-Fight) | 7 | Open-source sneeuwbalgevecht-game |
| [ethangtkt/Outrageous-Blades](https://github.com/ethangtkt/Outrageous-Blades) | 6 | Multiplayer melee-toernooi game (open-source) |
| [replier0/open-source-games](https://github.com/replier0/open-source-games) | 6 | Collectie open-source Roblox-games |
| [rsource-open-source/map-scripts](https://github.com/rsource-open-source/map-scripts) | 5 | Scripts voor bhop/surf-maps |
| [colbert2677/Roblox-Code-Samples](https://github.com/colbert2677/Roblox-Code-Samples) | 5 | Gratis code-voorbeelden |
| [NirlekaPlay/asymptote-engine](https://github.com/NirlekaPlay/asymptote-engine) | 5 | Engine voor stealth-games (Entry Point / Payday-stijl) |
| [ConMur/StonkSimulator](https://github.com/ConMur/StonkSimulator) | 5 | Aandelen-simulatie game |
| [Dekkonot/crossroads-rojo](https://github.com/Dekkonot/crossroads-rojo) | 4 | De klassieke Crossroads-game als Rojo-project |
| [evilbocchi/bocchi-upgrade-tree](https://github.com/evilbocchi/bocchi-upgrade-tree) | 4 | Open-source upgrade-tree game |
| [T-R-I-X/Jorik-TS](https://github.com/T-R-I-X/Jorik-TS) | 4 | Open-source MMORPG in roblox-ts |
| [Nimblz/MineStuff](https://github.com/Nimblz/MineStuff) | 4 | Open-source mijnbouw-game |
| [EnigmaDevelopmentGroup/Industry-Tycoon](https://github.com/EnigmaDevelopmentGroup/Industry-Tycoon) | 4 | Open-source fabriek-game |
| [homomorphist/factorial-defence-rbx](https://github.com/homomorphist/factorial-defence-rbx) | 4 | Factory + tower defense hybride, open-source |
| [knownasrazi/roblox-tycoon-clean](https://github.com/knownasrazi/roblox-tycoon-clean) | 4 | Opgeschoonde tycoon-architectuur |
| [cubacadabra/first-game](https://github.com/cubacadabra/first-game) | 4 | Draagbaar voorbeeldspel als Luau-package |
| [dwmk/RobloxGames](https://github.com/dwmk/RobloxGames) | 3 | Backup van games, open-source |
| [Aarav2709/TheLastVisit](https://github.com/Aarav2709/TheLastVisit) | 3 | Award-winnende narrative game, open-source |
| [Ar4ujo009/Last-Ember](https://github.com/Ar4ujo009/Last-Ember) | 3 | Soulslike RPG-prototype (Rojo + Luau) |
| [RenderingByte/ROMania](https://github.com/RenderingByte/ROMania) | 3 | Open-source rhythm game (osu!mania-stijl) |
| [AqwamCreates/Roblox-Source-Codes](https://github.com/AqwamCreates/Roblox-Source-Codes) | 3 | Code uit AqwamCreates' YouTube-video's (ML/AI) |
| [loneka/rbx-stack](https://github.com/loneka/rbx-stack) | 3 | Game-template (Fusion + OnyxUI) |
| [singharaj-usai/OpenBronze](https://github.com/singharaj-usai/OpenBronze) | 3 | Pokémon Brick Bronze starter kit |
| [JustSorvak/Quantum](https://github.com/JustSorvak/Quantum) | 3 | Open-source Forsaken-achtige game |
| [cataclysmic-studios/music-hero](https://github.com/cataclysmic-studios/music-hero) | 3 | Ritmegame geïnspireerd op Fortnite Festival |
| [cataclysmic-studios/neanderthals](https://github.com/cataclysmic-studios/neanderthals) | 3 | Survival-game geïnspireerd op Booga Booga |
| [ClementeAbarzua/Dragon-RNG-Genetic-Supremacy](https://github.com/ClementeAbarzua/Dragon-RNG-Genetic-Supremacy) | 2 | Complete game: draken verzamelen, RNG-hatching, genetische eigenschappen |
| [yoelthewhale/brickblast-roblox](https://github.com/yoelthewhale/brickblast-roblox) | 2 | Complete block-puzzle game (Rojo, StyLua, Selene) |
| [Unreal-Works/monsters-awakening](https://github.com/Unreal-Works/monsters-awakening) | 2 | Broncode van Monsters Awakening |
| [LockpickInteractive/GearDB](https://github.com/LockpickInteractive/GearDB) | 2 | Vergeten Roblox-gears opnieuw gescript |
| [vanshrana21/AbyssalDive](https://github.com/vanshrana21/AbyssalDive) | 2 | Co-op extraction boss-battler in drie oceaanzones |
| [Silverside-Developers/Silverside](https://github.com/Silverside-Developers/Silverside) | 2 | Open-source city-roleplay game |
| [OverDsh/SwordfightTS](https://github.com/OverDsh/SwordfightTS) | 2 | Open-source zwaardvecht-game (roblox-ts) |
| [cataclysmic-studios/spellbreak](https://github.com/cataclysmic-studios/spellbreak) | 2 | Turn-based kaart-RPG geïnspireerd op Wizard101 |
| [TheNickmaster21/Forever](https://github.com/TheNickmaster21/Forever) | 2 | Tech-demo client-side rendering |
| [ReRand/RENTED_old_rbx](https://github.com/ReRand/RENTED_old_rbx) | 2 | First-person survival-horror game |
| [depthso/Game-Scripts](https://github.com/depthso/Game-Scripts) | 2 | Game-scripts om van te leren |
| [knettia/BEYW](https://github.com/knettia/BEYW) | 2 | Open-source bouwgame "Build Everything You Want" |
| [Yonugy/Roblox-Racing-Game](https://github.com/Yonugy/Roblox-Racing-Game) | 2 | Open-source racegame |
| [Blupo/ATDG](https://github.com/Blupo/ATDG) | 2 | Open-source tower defense game |
| [RazonIn4K/l4d2-roblox-game](https://github.com/RazonIn4K/l4d2-roblox-game) | 2 | Left 4 Dead-achtige co-op zombie game |
| [aseemsahoocodes/roblox-simulator-engine](https://github.com/aseemsahoocodes/roblox-simulator-engine) | 1 | Simulator-engine: pets, eieren, ascensions, trading |
| [3xpluto/roblox-clean-architecture-template](https://github.com/3xpluto/roblox-clean-architecture-template) | 1 | Clean-architecture template: DI, veilige netlaag, rate limiting, migraties |
| [MarioChao/HeartPie](https://github.com/MarioChao/HeartPie) | 1 | Klassiek pie-hiking gear herbouwd |
| [TemujinCalidius/SurvivorCore](https://github.com/TemujinCalidius/SurvivorCore) | 1 | Uitbreidbaar survival-game framework |
| [cataclysmic-studios/tdz](https://github.com/cataclysmic-studios/tdz) | 1 | Tower Defense Z (open-source) |
| [cataclysmic-studios/tabletop-lounge](https://github.com/cataclysmic-studios/tabletop-lounge) | 1 | Hangout-game met tafelspellen |
| [strawbberrys/fable](https://github.com/strawbberrys/fable) | 1 | Verhaal-/game-maker (roblox-ts) |
| [Vexx3/Ascent](https://github.com/Vexx3/Ascent) | 1 | Template voor Eternal Towers of Hell-fangames |
| [saulmontealvo/Wordle](https://github.com/saulmontealvo/Wordle) | 1 | Wordle in Roblox met Fusion |
| [ReRand/ACE-ULTRA_old](https://github.com/ReRand/ACE-ULTRA_old) | 1 | PvP-shooter geïnspireerd op ULTRAKILL (movement) |
| [dig1t/slime-defense](https://github.com/dig1t/slime-defense) | 1 | 24-uurs coding-challenge game |
| [kalebtaylor3/RobloxCoopHorror-NetcodeFramework](https://github.com/kalebtaylor3/RobloxCoopHorror-NetcodeFramework) | 1 | 4-speler co-op horror met eigen netcode en movement |
| [Dad-0ps/TD-OpenSourced](https://github.com/Dad-0ps/TD-OpenSourced) | 1 | Open-source tower defense |
| [phantomfills/fantasy-tower-defense](https://github.com/phantomfills/fantasy-tower-defense) | 1 | Open-source fantasy tower defense |
| [rushikeshgoud19/nightdesk](https://github.com/rushikeshgoud19/nightdesk) | 1 | Co-op anomaly-horror + Rojo/Blender-pipeline |
| [faranontheway/HollowWard](https://github.com/faranontheway/HollowWard) | 1 | Open-source horror game |
| [MarkExKiana/ProjectStarFallCodebase](https://github.com/MarkExKiana/ProjectStarFallCodebase) | 1 | Volledige codebase van een Roblox-game |
| [gievano/map-voice](https://github.com/gievano/map-voice) | 1 | Social hangout met voicechat, wardrobe, emotes en dag/nacht |
| [tralfa42real/roblox-rpg-core-systems](https://github.com/tralfa42real/roblox-rpg-core-systems) | 0 | RPG-backend: profielen, equipment, economie, loot, guilds, enemy AI |
| [lukas-mikalainis/roblox-precision-framework](https://github.com/lukas-mikalainis/roblox-precision-framework) | 0 | Server-authoritative movement + combat framework |
| [Sworddao/ascendant-mortal](https://github.com/Sworddao/ascendant-mortal) | 0 | Xianxia cultivation MMORPG |
| [B0LLEX/card-factory-tycoon](https://github.com/B0LLEX/card-factory-tycoon) | 0 | Complete tycoon volledig autonoom gebouwd door Claude via Studio MCP |
| [thegamerbay/super-coin-world](https://github.com/thegamerbay/super-coin-world) | 0 | 3D-platformer met bolvormige zwaartekracht |
| [DestinEcarma/roblox-ts-demo](https://github.com/DestinEcarma/roblox-ts-demo) | 0 | Demo met chunk-gebaseerde wereldgeneratie (Flamework) |
| [FilteredAsync/fusion-framework-blueprint](https://github.com/FilteredAsync/fusion-framework-blueprint) | 0 | Architectuurgids voor code-first UI met Fusion 0.3 |
| [pastadudes/colorando](https://github.com/pastadudes/colorando) | 0 | Flood-escape game met Geometry Dash-elementen |
| [UltimateBattleSandbox/UBS](https://github.com/UltimateBattleSandbox/UBS) | 0 | Broncode van een gratis sandbox-game |
| [rgwl1tv69/Open-Source-Industrialist](https://github.com/rgwl1tv69/Open-Source-Industrialist) | 0 | Poging om Industrialist (fabrieksgame) open-source na te bouwen |
| [matt-lunsford/Obby_Arena_Source](https://github.com/matt-lunsford/Obby_Arena_Source) | 0 | Open-source Obby Arena |
| [coolpeter98/bridge-duel](https://github.com/coolpeter98/bridge-duel) | 0 | Bridge Duel open-source (GPLv3) |
| [Khangaroooooo/studs](https://github.com/Khangaroooooo/studs) | 0 | Game van 27k regels Luau: battle, trade, quests, saves |
| [voximity/brick-building-game](https://github.com/voximity/brick-building-game) | 0 | Open-source Blockland-achtige brick builder |
| [DLinacre/slime-factory-tycoon](https://github.com/DLinacre/slime-factory-tycoon) | 0 | Productieklare idle-tycoon template met CI balance-simulator |
| [kipuki/grid-based-tactical-rpg](https://github.com/kipuki/grid-based-tactical-rpg) | 0 | Fire Emblem-achtige tactische grid-RPG |
| [AliSultanbekov/The-Dungeons](https://github.com/AliSultanbekov/The-Dungeons) | 0 | Dungeon-RPG met ECS-combat, lag-compensatie en ServiceBag |
| [mkepg/body-swap-royale](https://github.com/mkepg/body-swap-royale) | 0 | Party-game waarin spelers periodiek van avatar wisselen |
| [CorixDev/roblox-tycoon-framework](https://github.com/CorixDev/roblox-tycoon-framework) | 0 | Server-authoritative restaurant/tycoon-backend in strict Luau |
| [SofiSubbotina/BridgeRun](https://github.com/SofiSubbotina/BridgeRun) | 0 | Multiplayer bruggenbouw-runner met object pooling |

## Uitbreiden

1. Voeg een regel toe aan [`data/repos.tsv`](data/repos.tsv) (`categorie<TAB>eigenaar/repo<TAB>sterren<TAB>omschrijving`).
2. Draai `python3 scripts/generate.py` — README en categoriepagina's worden opnieuw gegenereerd.

> Let op: controleer altijd de licentie van een repo voordat je code in je eigen game gebruikt.
