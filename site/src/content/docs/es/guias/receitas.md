---
title: Recetas rápidas
description: Fragmentos cortos para las tareas más comunes con objetos, escena, tiempo y teclado.
---

Fragmentos listos para copiar. Todos suponen que se ejecutan dentro de un componente (`self.object` es el objeto dueño) y que el archivo empieza con:

```python
import Range
from Range import logic, events
```

Algunos nombres están en portugués porque el código es el mismo probado en la página en portugués (`alvo` = objetivo, `vida` = vida, `cena` = escena, `tiro` = disparo, `inimigo` = enemigo, `pontos` = puntos).

## Objetos ([`KX_GameObject`](../../api/types/kx_gameobject/))

**Mover y rotar** (`True` usa los ejes propios del objeto):

```python
self.object.applyMovement((0.0, 0.1, 0.0), True)
self.object.applyRotation((0.0, 0.0, 0.05), True)
```

**Distancia a otro objeto:**

```python
alvo = self.object.scene.objects["Jogador"]
if self.object.getDistanceTo(alvo) < 5.0:
    print("cerca")
```

**Mirar hacia un objeto** (el eje Y apunta al objetivo):

```python
vetor = self.object.getVectTo(alvo)[1]
self.object.alignAxisToVect(vetor, 1, 0.1)
```

**Propiedad de juego:**

```python
self.object["vida"] = self.object.get("vida", 100) - 10
```

**Rayo hacia adelante** (qué hay hasta 10 m al frente):

```python
frente = self.object.worldPosition + self.object.worldOrientation.col[1] * 10.0
atingido = self.object.rayCastTo(frente, 10.0)
if atingido:
    print("chocó con", atingido.name)
```

**Eliminar** (tiene efecto al final del frame):

```python
self.object.endObject()
```

## Escena ([`KX_Scene`](../../api/types/kx_scene/))

**Crear un objeto de una capa inactiva** en la posición de otro objeto, durante 120 frames (0 = para siempre):

```python
cena = self.object.scene
tiro = cena.addObject("Tiro", self.object, 120)
```

**Buscar objetos por propiedad:**

```python
inimigos = [o for o in self.object.scene.objects if "inimigo" in o]
```

**Cambiar de escena y reiniciar:**

```python
self.object.scene.replace("Fase2")
self.object.scene.restart()
```

## Tiempo y teclado ([`Range.logic`](../../api/modulos/logic/))

**Tecla recién presionada / mantenida:**

```python
teclas = logic.keyboard.inputs
if teclas[events.SPACEKEY].activated:
    print("saltó")
if teclas[events.WKEY].active:
    print("caminando")
```

**Clic y posición del mouse:**

```python
mouse = logic.mouse
if mouse.inputs[events.LEFTMOUSE].activated:
    print("clic en", mouse.position)
```

**Tiempo:** movimiento independiente de los FPS.

```python
dt = 1.0 / max(logic.getAverageFrameRate(), 1.0)
self.object.applyMovement((0.0, 2.0 * dt, 0.0), True)
```

**Conservar datos entre escenas:**

```python
logic.globalDict["pontos"] = logic.globalDict.get("pontos", 0) + 1
```
