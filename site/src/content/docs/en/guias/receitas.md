---
title: Quick recipes
description: Short snippets for the most common tasks with objects, scene, time and keyboard.
---

Ready-to-copy snippets. All of them assume they run inside a component (`self.object` is the owner object) and that the file starts with:

```python
import Range
from Range import logic, events
```

Some names are in Portuguese because the code is the same one tested on the Portuguese page (`alvo` = target, `vida` = health, `cena` = scene, `tiro` = shot, `inimigo` = enemy, `pontos` = score).

## Objects ([`KX_GameObject`](../../api/types/kx_gameobject/))

**Move and rotate** (`True` uses the object's own axes):

```python
self.object.applyMovement((0.0, 0.1, 0.0), True)
self.object.applyRotation((0.0, 0.0, 0.05), True)
```

**Distance to another object:**

```python
alvo = self.object.scene.objects["Jogador"]
if self.object.getDistanceTo(alvo) < 5.0:
    print("perto")
```

**Look at an object** (the Y axis points at the target):

```python
vetor = self.object.getVectTo(alvo)[1]
self.object.alignAxisToVect(vetor, 1, 0.1)
```

**Game property:**

```python
self.object["vida"] = self.object.get("vida", 100) - 10
```

**Ray ahead** (what is up to 10 m in front):

```python
frente = self.object.worldPosition + self.object.worldOrientation.col[1] * 10.0
atingido = self.object.rayCastTo(frente, 10.0)
if atingido:
    print("bateu em", atingido.name)
```

**Remove** (takes effect at the end of the frame):

```python
self.object.endObject()
```

## Scene ([`KX_Scene`](../../api/types/kx_scene/))

**Create an object from an inactive layer** at another object's position, for 120 frames (0 = forever):

```python
cena = self.object.scene
tiro = cena.addObject("Tiro", self.object, 120)
```

**Find objects by property:**

```python
inimigos = [o for o in self.object.scene.objects if "inimigo" in o]
```

**Switch scene and restart:**

```python
self.object.scene.replace("Fase2")
self.object.scene.restart()
```

## Time and keyboard ([`Range.logic`](../../api/modulos/logic/))

**Key just pressed / held:**

```python
teclas = logic.keyboard.inputs
if teclas[events.SPACEKEY].activated:
    print("pulou")
if teclas[events.WKEY].active:
    print("andando")
```

**Mouse click and position:**

```python
mouse = logic.mouse
if mouse.inputs[events.LEFTMOUSE].activated:
    print("clicou em", mouse.position)
```

**Time:** movement independent of FPS.

```python
dt = 1.0 / max(logic.getAverageFrameRate(), 1.0)
self.object.applyMovement((0.0, 2.0 * dt, 0.0), True)
```

**Keep data between scenes:**

```python
logic.globalDict["pontos"] = logic.globalDict.get("pontos", 0) + 1
```
