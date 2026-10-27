---
title: What's been done
description: Everything Anastacio Engine has gained since forking Range Engine 1.6, month by month.
sidebar:
  label: What's been done
---

<div class="ae-h-hero">
<span class="ae-h-eyebrow">Dev log · Aug → Oct 2026</span>
<p class="ae-h-lead">Every line below comes from the engine's technical log. Here is the short version: what changed for people who make games.</p>
<dl class="ae-h-odo">
<div><dt>log entries</dt><dd>716</dd></div>
<div><dt>releases published</dt><dd>14</dd></div>
<div><dt>platforms</dt><dd>4</dd></div>
</dl>
</div>

<section class="ae-h-month">
<header><span class="ae-h-num">08</span><div><h2>August</h2><p>The base: faster, with new particles</p></div></header>
<div class="ae-h-grid">
<article><h3>Performance</h3><ul>
<li>Animated characters computed on the graphics card (GPU Skinning).</li>
<li>Cutout foliage draws faster: 28 → 21 ms per frame in the test.</li>
<li>Distant trees automatically become impostors (a flat image).</li>
</ul></article>
<article><h3>Effects</h3><ul>
<li>GPU particle system: fire, smoke, dust and sparks ready to use.</li>
<li>First screen filters (grayscale, negative, sepia).</li>
</ul></article>
<article><h3>Editor</h3><ul>
<li>Choose between the Range and UPBGE icons.</li>
<li>ImGui menus organized as components.</li>
</ul></article>
</div>
</section>

<section class="ae-h-month">
<header><span class="ae-h-num">09</span><div><h2>September</h2><p>The engine leaves Windows</p></div></header>
<div class="ae-h-grid">
<article><h3>Web and mobile</h3><ul>
<li>The game runs in the browser: lights, shadows, filters, sound, saves and Python.</li>
<li>Validation and "Open in browser" straight from the editor.</li>
<li>Export to Android (APK and AAB), with on-screen controls and motion sensors.</li>
</ul></article>
<article><h3>Linux</h3><ul>
<li>Native editor and player, with a portable package that runs on many distros.</li>
<li>Cycles on NVIDIA (CUDA) and AMD (OpenCL) cards.</li>
</ul></article>
<article><h3>Game</h3><ul>
<li>Native cutscenes with a timeline.</li>
<li>Destruction and explosions, camera focus and shake, rain and clouds in the World.</li>
<li>Echo areas (Reverb Area), animation events and a navmesh that avoids obstacles.</li>
<li>Old BGE/UPBGE scripts run without changing the imports.</li>
</ul></article>
<article><h3>Editor</h3><ul>
<li>Floating bar in the 3D View, collections in the Outliner and Asset Browser.</li>
<li>Interface in English, Português, Español and Русский.</li>
<li>Logic Bricks turn into Python with one button.</li>
</ul></article>
<article><h3>Under the hood</h3><ul>
<li>The game core was reorganized into 11 stages, with performance meters.</li>
<li>Optional fixed physics step, so the game plays the same at any FPS.</li>
</ul></article>
</div>
<p class="ae-h-rel">Versions 0.3.0 to 0.4.6</p>
</section>

<section class="ae-h-month">
<header><span class="ae-h-num">10</span><div><h2>October</h2><p>New graphics, no-code logic and multiplayer</p></div></header>
<div class="ae-h-grid">
<article><h3>Graphics</h3><ul>
<li>Cycles material nodes work in the game: glass, hair, volume, sky.</li>
<li>Reflections (probes and planar mirror), colored stained-glass shadow and cascaded shadows.</li>
<li>Sun shadow with cascades (CSM) and soft penumbra shadows (PCSS).</li>
<li>Post-processing effects in the game: Directional Blur, Color Correction, Tonemap, Glare, Crop and more.</li>
<li>Volumetric clouds, volumetric fog and indirect lighting (bake and SSGI).</li>
<li>Node shaders with wind, waves, fur and toon outline.</li>
</ul></article>
<article><h3>Loading</h3><ul>
<li>"Cooked" file (<code>.cooked</code>): physics, shaders and meshes ready on open.</li>
<li>Loading screen with real progress and compressed DDS textures.</li>
<li>Choose what loads with the scene and what loads only when needed.</li>
</ul></article>
<article><h3>Performance</h3><ul>
<li>Static Batch: with it on, we tie with ThunderPlayer in the benchmark.</li>
<li>About 100 spots of repeated work reviewed in the engine.</li>
<li>Range Trace, Performance Report and Scene Doctor show where the game is heavy.</li>
<li>Auto Static Batch, a compact FPS counter and a cheaper Python API.</li>
</ul></article>
<article><h3>No-code logic</h3><ul>
<li>Logic Bricks 2.0 and Logic Tree: node logic that becomes native bricks.</li>
<li>Smart Components with a wizard, and 2D filters with fields in the panel.</li>
<li>UI Tree: menus and HUD built in the node editor.</li>
</ul></article>
<article><h3>Game</h3><ul>
<li>Native multiplayer (LAN, internet and browser) and a Steam add-on.</li>
<li>World Sound with music, ambience, rain and thunder.</li>
<li>VR on the phone, ragdoll, crash dents and arcade vehicles.</li>
<li>Game languages and screen recording with sound.</li>
<li><code>Range.types.TrackLine</code>: a track for the racing AI to follow.</li>
</ul></article>
<article><h3>Text and dialogue</h3><ul>
<li>Text Boxes in the game: line wrapping, pages and a typewriter effect.</li>
<li>No-code dialogue: Dialogue Box node in the UI Tree.</li>
</ul></article>
<article><h3>Time and stability</h3><ul>
<li>A single clock with time scale; the cutscene pauses along with the scene.</li>
<li>Full review of scene, objects, joystick, LibLoad and multiplayer, with several crashes fixed.</li>
<li>Export: Compile Scripts works and the open <code>.range</code> no longer ships in the package.</li>
</ul></article>
</div>
<p class="ae-h-rel">Versions 0.5.0 to 0.6.0</p>
</section>

<p class="ae-h-foot">Want the detail on something? The full log lives in the engine repository, in <code>docs/changelog.md</code>. What is still missing is in <code>docs/roadmap.md</code>.</p>
