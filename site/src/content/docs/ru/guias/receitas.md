---
title: Быстрые рецепты
description: Короткие фрагменты для самых частых задач с объектами, сценой, временем и клавиатурой.
---

Готовые к копированию фрагменты. Все предполагают выполнение внутри компонента (`self.object` — объект-владелец) и что файл начинается так:

```python
import Range
from Range import logic, events
```

Некоторые имена на португальском, потому что код тот же, что проверен на португальской странице (`alvo` = цель, `vida` = здоровье, `cena` = сцена, `tiro` = выстрел, `inimigo` = враг, `pontos` = очки).

## Объекты ([`KX_GameObject`](../../api/types/kx_gameobject/))

**Перемещение и вращение** (`True` использует собственные оси объекта):

```python
self.object.applyMovement((0.0, 0.1, 0.0), True)
self.object.applyRotation((0.0, 0.0, 0.05), True)
```

**Расстояние до другого объекта:**

```python
alvo = self.object.scene.objects["Jogador"]
if self.object.getDistanceTo(alvo) < 5.0:
    print("perto")
```

**Смотреть на объект** (ось Y направлена на цель):

```python
vetor = self.object.getVectTo(alvo)[1]
self.object.alignAxisToVect(vetor, 1, 0.1)
```

**Игровое свойство:**

```python
self.object["vida"] = self.object.get("vida", 100) - 10
```

**Луч вперёд** (что находится в пределах 10 м впереди):

```python
frente = self.object.worldPosition + self.object.worldOrientation.col[1] * 10.0
atingido = self.object.rayCastTo(frente, 10.0)
if atingido:
    print("bateu em", atingido.name)
```

**Удаление** (срабатывает в конце кадра):

```python
self.object.endObject()
```

## Сцена ([`KX_Scene`](../../api/types/kx_scene/))

**Создать объект с неактивного слоя** в позиции другого объекта на 120 кадров (0 = навсегда):

```python
cena = self.object.scene
tiro = cena.addObject("Tiro", self.object, 120)
```

**Найти объекты по свойству:**

```python
inimigos = [o for o in self.object.scene.objects if "inimigo" in o]
```

**Сменить сцену и перезапустить:**

```python
self.object.scene.replace("Fase2")
self.object.scene.restart()
```

## Время и клавиатура ([`Range.logic`](../../api/modulos/logic/))

**Клавиша только что нажата / удерживается:**

```python
teclas = logic.keyboard.inputs
if teclas[events.SPACEKEY].activated:
    print("pulou")
if teclas[events.WKEY].active:
    print("andando")
```

**Щелчок и позиция мыши:**

```python
mouse = logic.mouse
if mouse.inputs[events.LEFTMOUSE].activated:
    print("clicou em", mouse.position)
```

**Время:** движение, не зависящее от FPS.

```python
dt = 1.0 / max(logic.getAverageFrameRate(), 1.0)
self.object.applyMovement((0.0, 2.0 * dt, 0.0), True)
```

**Сохранение данных между сценами:**

```python
logic.globalDict["pontos"] = logic.globalDict.get("pontos", 0) + 1
```
