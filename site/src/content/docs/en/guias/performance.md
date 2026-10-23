---
title: Performance menu (report and optimization)
description: Measure your game in one click and get a visual report of what is heavy and what to do. Includes Scene Doctor, LODs, collision and export preparation.
---

The **Performance** button, in the top bar next to **Game**, gathers the tools to find what makes the game slow and fix it. It works for any game, nothing to install.

## Performance Report

1. Click **Performance > Measure**.
2. The game opens in `AnastacioRuntime` with recording on. Play through the parts you want to measure.
3. Close the game. The report (`report.html`) opens in your browser.

If the scene has unsaved changes, the engine runs a temporary copy and deletes it at the end. Your file is not touched.

**Last** reopens the latest report and **Folder** opens the folder with all of them.

### What the report shows

- **Verdict at the top**: runs smoothly, worth a look, or needs work.
- **Colored cards** (green, yellow, red) with the key numbers.
- **What to do**: automatic recommendations based on what was measured.
- **Comparison** with the previous report of the same game, to see whether a change helped.
- **Frame chart** with spikes marked, plus the scenes and sounds at each moment.
- **Where the time goes** in each frame: logic, physics, render and more.
- **Scripts**: time of each Python component (per class) and each Python controller (per script).
- **Spikes**: the heaviest script and what was loading at each hitch.
- **Memory** of the process every second.
- **Loads during play**, compiled **shaders** and **loading per scene**.
- **Loaded but never drawn**: what takes memory without showing up.
- **Sounds** started (Sound actuator, speaker, World Sound) and per-frame counters.

Start-up (up to 60 frames in a row without spikes) is shown separately at the top and does not count in the numbers.

The report has light and dark themes (follows the system, with a toggle in the corner) and uses the editor interface language.

:::tip
Measure, change one thing and measure again. The comparison section shows right away whether it got better or worse.
:::

## Scene Doctor

**Performance > Scene Doctor** analyzes the open scene without running the game and lists what costs load time, memory or frame time. Many items have a one-click fix, such as generating LODs for heavy meshes or replacing dense static collision with a proxy.

## Optimize the scene

- **Generate LODs**: creates levels of detail in batch, with distances computed from each object's size. The **X** next to it removes generated LODs.
- **Collision Proxies**: creates simplified collision for dense static scenery. The **X** removes them.

## Prepare for export

- **Textures (DDS)**: prepares textures as DDS BC1/BC3 for the exported desktop game. The arrow reverts.
- **Audio (OGG)**: prepares sounds as OGG for the exported package.

Originals stay untouched; prepared versions are only used on export.
