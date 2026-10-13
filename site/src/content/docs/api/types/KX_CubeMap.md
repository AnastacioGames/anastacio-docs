---
title: "KX_CubeMap"
description: "Referência da classe Range.types.KX_CubeMap"
---

Classe base: [`KX_TextureRenderer`](../kx_texturerenderer/)

:::tip[Veja também]
[`KX_PlanarMap`](../../types/kx_planarmap/), [`KX_TextureRenderer`](../../types/kx_texturerenderer/)
:::



API Python para texturas de cube map em tempo real.

```python

import Range

scene = Range.logic.getCurrentScene()
# O objeto que usa um cube map em tempo real no material.
obj = scene.objects["Suzanne"]

mat = obj.meshes[0].materials[0]
# Pega o cube map em tempo real a partir da textura do material.
cubemap = mat.textures[0].renderer

# Põe a posição de render na posição do objeto "Cube".
cubemap.viewpointObject = scene.objects["Cube"]

# Muda o clip start e o clip end do culling.
cubemap.clipStart = 5.0
cubemap.clipEnd = 20.0

# Desliga o render na terceira layer.
cubemap.ignoreLayers = (1 << 2)

# Desliga a atualização por frame.
cubemap.autoUpdate = False
# Pede atualização só neste frame.
cubemap.update()
```

