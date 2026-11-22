# KX_PlanarMap

Base class: [`KX_TextureRenderer`](KX_TextureRenderer.md)

> **See also:**
[`KX_CubeMap`](KX_CubeMap.md), [`KX_TextureRenderer`](KX_TextureRenderer.md)

Python API for realtime planar map textures.

```python
# Update a mirror only when needed.
import Range

own = Range.logic.getCurrentController().owner
mirror = own.meshes[0].materials[0].textures[0].renderer

mirror.autoUpdate = False
mirror.update()
print(mirror.normal)
```

## normal

Plane normal used to compute the reflection or refraction orientation of the render camera.

**Type:** `mathutils.Vector`
