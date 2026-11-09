---
title: Rec Play (record scenes while playing)
description: Record actors into Takes while you play, in layers, and use them in cutscenes, video or Python.
---

**Rec Play** records what happens while you play. Each recording becomes a **Take**, with the pose of each actor. A Take can then become a video, go into a cutscene or play from a script.

## Record in Rec Studio

1. Open **Window > Rec Studio**. If you have no library of your own, it opens on a kit with 3 characters, 6 actions and 4 sceneries.
2. In **Scenery**, drag a scenery into the scene.
3. In **Characters**, drag a character. It becomes an actor right away.
4. In **Actions**, drag an action onto the actor.
5. Click **Record**, move the actor and stop with **F10**. The Take shows up in the list.

## Buttons

| Button | What it does |
|---|---|
| **Watch** | Plays all Takes in the game, without recording. |
| **Rerecord** | Records the actors of the selected Take again and replaces it. |
| **Undo** | Undoes the last recording. |
| **Movie** | Plays the Takes and saves a video with sound in the file's folder. |

## Record in layers

While recording, unmarked actors repeat their latest Take, so you can record one actor at a time. **Play Other Takes** enables this replay, and **Collide on Replay** sets whether replayed actors collide.

## Send it to a cutscene

1. In the **Render** tab, open **Motion Recording (Experimental)**.
2. Select the Take and click **Add to Cutscene**. Recording does not create the event by itself.
3. A Play Take event appears in **Cutscene Sequences**. Renaming the Take updates the event.

## Play from Python

```python
import Range

scene = Range.logic.getCurrentScene()
door = scene.objects["Door"]
if not door.is_playing_take():
    door.play_take("Take 1")
```

`scene.takes` lists the names, `scene.play_take(name)` plays all actors and `obj.stop_take()` stops at the current point. While playing, the actor has no logic or physics; both return at the end. See [`KX_Scene`](../../api/types/kx_scene/) / [`KX_GameObject`](../../api/types/kx_gameobject/).

:::note
Per-bone pose is not recorded yet, so IK and scripts that move bones do not go into the Take. Body movement and Actions do.
:::
