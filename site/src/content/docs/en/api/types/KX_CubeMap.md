---
title: "KX_CubeMap"
description: "Range.types.KX_CubeMap class reference"
---

Base class: [`KX_TextureRenderer`](../kx_texturerenderer/)

:::tip[See also]
[`KX_PlanarMap`](../../types/kx_planarmap/), [`KX_TextureRenderer`](../../types/kx_texturerenderer/)
:::



Python API for realtime cube map textures.

```python

import Range

scene = Range.logic.getCurrentScene()
# The object using a realtime cube map in its material.
obj = scene.objects["Suzanne"]

mat = obj.meshes[0].materials[0]
# Obtain the realtime cube map from the material texture.
cubemap = mat.textures[0].renderer

# Set the render position to the "Cube" object position.
cubemap.viewpointObject = scene.objects["Cube"]

# Change the culling clip start and clip end.
cubemap.clipStart = 5.0
cubemap.clipEnd = 20.0

# Disable render on third layer.
cubemap.ignoreLayers = (1 << 2)

# Disable per frame update.
cubemap.autoUpdate = False
# Ask to update for this frame only.
cubemap.update()
```

