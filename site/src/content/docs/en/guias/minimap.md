---
title: Minimap
description: Create a HUD minimap with one command, as radar, whole map or 3D GPS, and mark players and items.
---

**Minimap** is a HUD node in [UI Tree](../ui-tree/). It does not redraw the scene: it shows a map image, so it costs little.

## Create it with one command

1. Save the `.range`. **Add > Minimap** with Bake and **Bake Map Image** refuse a scene that was never saved.
2. In the 3D View, select the player and use **Add > Minimap**.
3. Pick the style: **Radar** (rotating circle), **Whole Map** (still square) or **GPS 3D** (tilted rectangle).

The command creates the HUD, the node that follows the object, the map image and the UI logic.

## Mark objects

Select the object and open the **Object** tab, **Minimap** panel. Enable **Show on Minimap**. **Own Color** gives it its own color; without it, the node's **Markers** color applies.

From a script, the color is in `minimap_color`, as `#rrggbb`:

```python
own["minimap_color"] = "#ff3030"
```

Without the panel, use the `minimap` game property or the **Marker Prefix** in the object's name. Markers outside the area stick to the edge.

## Node settings

| Option | What it does |
|---|---|
| **World Min / Max** | World area covered by the image. **Fit to Scene** measures it for you. |
| **Zoom Radius** | `0` shows the whole map, still; above 0 follows the player. |
| **Rotate with Player** | Rotates the map with the player. |
| **Camera Tilt** | Tilts the view from 0 to 60°, like a 3D GPS. |
| **Shape** | Circle, Square, Rectangle or Ellipse. |
| **Border Style** | None, Solid or Soft. |

**Bake Map Image** takes a top-down picture of the visible meshes, saves `<file>_minimap.png` next to the `.range` and sets World Min/Max.
