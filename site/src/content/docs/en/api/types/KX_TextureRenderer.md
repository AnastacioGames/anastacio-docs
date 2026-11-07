---
title: "KX_TextureRenderer"
description: "Range.types.KX_TextureRenderer class reference"
---

Base class: [`EXP_Value`](../exp_value/)



Python API for object doing a render stored in a texture.

```python
# Update a reflection only every few frames to save time.
import Range

own = Range.logic.getCurrentController().owner
renderer = own.meshes[0].materials[0].textures[0].renderer

renderer.autoUpdate = False
own["frames"] = own.get("frames", 0) + 1

if own["frames"] % 10 == 0:
    renderer.update()
```

```python
# Use another point of view and a shorter distance.
import Range

own = Range.logic.getCurrentController().owner
renderer = own.meshes[0].materials[0].textures[0].renderer

renderer.viewpointObject = Range.logic.getCurrentScene().objects["Probe"]
renderer.clipEnd = 50.0
```

### autoUpdate

Choose to update automatically each frame the texture renderer or not.

**Type:** boolean

### viewpointObject

The object where the texture renderer will render the scene.

**Type:** `KX_GameObject`

### enabled

Enable the texture renderer to render the scene.

**Type:** boolean

### ignoreLayers

The layers to ignore when rendering.

**Type:** bitfield

### clipStart

The projection view matrix near plane, used for culling.

**Type:** float

### clipEnd

The projection view matrix far plane, used for culling.

**Type:** float

### lodDistanceFactor

The factor to multiply distance to camera to adjust levels of detail.
A float < 1.0f will make the distance to camera used to compute
levels of detail decrease.

**Type:** float

### update()

Request to update this texture renderer during the rendering stage. This function is effective only when `autoUpdate` is disabled.

