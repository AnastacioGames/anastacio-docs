---
title: Receitas rápidas
description: Trechos curtos para as tarefas mais comuns com objetos, cena, tempo e teclado.
draft: true
---

Trechos prontos para copiar. Todos supõem que estão dentro de um componente (`self.object` é o objeto dono) e que o arquivo começa com:

```python
import Range
from Range import logic, events
```

## Objetos ([`KX_GameObject`](../../api/types/kx_gameobject/))

**Mover e girar** (o `True` usa os eixos do próprio objeto):

```python
self.object.applyMovement((0.0, 0.1, 0.0), True)
self.object.applyRotation((0.0, 0.0, 0.05), True)
```

**Distância até outro objeto:**

```python
alvo = self.object.scene.objects["Jogador"]
if self.object.getDistanceTo(alvo) < 5.0:
    print("perto")
```

**Olhar para um objeto** (eixo Y aponta para o alvo):

```python
vetor = self.object.getVectTo(alvo)[1]
self.object.alignAxisToVect(vetor, 1, 0.1)
```

**Propriedade de jogo:**

```python
self.object["vida"] = self.object.get("vida", 100) - 10
```

**Raio à frente** (o que está até 10 m na frente):

```python
frente = self.object.worldPosition + self.object.worldOrientation.col[1] * 10.0
atingido = self.object.rayCastTo(frente, 10.0)
if atingido:
    print("bateu em", atingido.name)
```

**Remover:**

```python
self.object.endObject()
```

## Cena ([`KX_Scene`](../../api/types/kx_scene/))

**Criar um objeto de uma camada inativa** na posição de outro, por 120 quadros (0 = para sempre):

```python
cena = self.object.scene
tiro = cena.addObject("Tiro", self.object, 120)
```

**Achar objetos pela propriedade:**

```python
inimigos = [o for o in self.object.scene.objects if "inimigo" in o]
```

**Trocar de cena e reiniciar:**

```python
self.object.scene.replace("Fase2")
self.object.scene.restart()
```

## Tempo e teclado ([`Range.logic`](../../api/modulos/logic/))

**Tecla apertada agora / segurada:**

```python
teclas = logic.keyboard.inputs
if teclas[events.SPACEKEY].activated:
    print("pulou")
if teclas[events.WKEY].active:
    print("andando")
```

**Clique do mouse e posição:**

```python
mouse = logic.mouse
if mouse.inputs[events.LEFTMOUSE].activated:
    print("clicou em", mouse.position)
```

**Tempo:** movimento independente do FPS.

```python
dt = 1.0 / max(logic.getAverageFrameRate(), 1.0)
self.object.applyMovement((0.0, 2.0 * dt, 0.0), True)
```

**Guardar dados entre cenas:**

```python
logic.globalDict["pontos"] = logic.globalDict.get("pontos", 0) + 1
```
