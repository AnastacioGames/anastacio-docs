---
title: Automatic character (Fuse)
description: Turn an OBJ exported from Fuse into a character with skeleton, LODs and ragdoll, without Mixamo.
---

The engine turns the OBJ of a Fuse character into a game-ready character, without going through Mixamo.

## Import

Open **File > Import > Fuse Character (.obj)**, pick the file and adjust:

| Option | What it does |
|---|---|
| **Skeleton** | Library skeleton used as the base. |
| **Name** | Character name; the group is called `Group<Name>`. Empty uses the file name. |
| **Ragdoll** | Adds ragdoll boxes on the big bones, without hands and fingers. |
| **Output Folder** | Where `Group<Name>.range` and `textures/` go. Empty creates a folder next to the open file. |
| **Game Folder** | Game project root, to attach the ragdoll component. Empty uses the open file's folder. |
| **Add to Scene** | Places the finished group in the current scene, at the 3D cursor. |

Processing runs in the background and does not touch the open file.

## What you get

- Body reduced to 9000 triangles at level 0, preserving head and chest.
- LODs of 2500 triangles at 10 m and 900 triangles at 25 m.
- A group with armature, body and ragdoll, saved to be brought in with `LibLoad`.

:::caution
Check the license of the Fuse meshes before distributing your game.
:::
