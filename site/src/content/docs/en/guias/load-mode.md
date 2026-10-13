---
title: Fast loading (Load Mode and Cook)
description: Leave objects out of loading, create them only when needed and cook the scene so it opens faster.
---

A large scene takes time to open because the engine converts every object before the first frame. Anastacio has two tools for that:

- **Load Mode**: chooses which objects are loaded with the scene and which wait until later.
- **Cook**: stores in a `.cooked` file what the conversion computes (physics, meshes, shaders), so it is not computed again.

## Load Mode

Select an object and open **Properties > Object**, panel **Load Object with Scene**. There are three modes:

| Mode | What happens |
|---|---|
| **With Scene** | Default. The object is created with the scene. |
| **On Demand** | Left out at load. Created when a script asks for it or when an Add Object uses it for the first time. |
| **Editor Only** | Never goes into the game. Good for reference objects, work cameras, blockout. |

The mode applies to the selected objects and their children.

### Creating an On Demand object from a script

(`cena` = scene, `chefe` = boss, `tiro` = shot, `arma` = weapon: the code is the one tested on the Portuguese page.)

```python
import Range

cena = Range.logic.getCurrentScene()
chefe = cena.convertObject("Chefe")
```

If `Chefe` is on an active layer, it appears in the scene. If it is on an inactive layer, it goes to `objectsInactive` and is ready for `addObject`:

```python
cena.convertObject("Tiro")
tiro = cena.addObject("Tiro", cena.objects["Arma"], 120)
```

`cena.unconvertedObjects` lists the names that can still be created this way.

### With Logic Bricks

The **Add Object** actuator already understands On Demand: the object is created the first time the actuator fires, and later times only make copies. No script needed.

## Cook

The **Cook** button is in the Render panel and next to Play in the header. It runs the scene once and writes, next to the `.blend`, a `.cooked` file with:

- collision shapes (Convex Hull and Triangle Mesh) already computed;
- mesh buffers, normals and tangents;
- shaders compiled for your graphics card.

On the next load, the engine reads the file instead of computing. In tests, loading a scene dropped from about 2.4 s to under 0.5 s.

- The `.blend` must be saved (without a saved file the button is greyed out).
- **Clear Cooked** deletes the cache. If you change a mesh you don't need to clear it: the changed part is recomputed.
- In the exported game, the `.cooked` goes along. Shaders are stored on the player's computer on first launch, which shows a preparation screen.

## Measuring

`Range.logic.getLoadLog()` shows how long each loading stage took. Use it before and after Cook to see the gain.

```python
import Range

for etapa in Range.logic.getLoadLog():
    print(etapa)
```
