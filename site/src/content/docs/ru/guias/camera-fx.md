---
title: Игровая камера (фокус, эффекты и тряска)
description: Автофокус, камера, следящая за целью, размытие скорости, DOF и тряска — без фильтров на Python.
---

У камеры Anastacio есть встроенные эффекты: фокус, следующий за объектом, слежение (камера поворачивается вслед за целью), DOF, размытие скорости, хроматическая аберрация, виньетка и тряска. Всё настраивается в свойствах камеры и может меняться из Python через [`KX_Camera`](../../api/types/kx_camera/).

По умолчанию всё выключено. Обновляется только активная камера сцены.

:::note
Код тот же, что проверен на португальской странице, поэтому некоторые имена на португальском (`TremerNoEspaco` = тряска по пробелу, `cena` = сцена).
:::

## 1. Фокус и слежение в редакторе

Выберите камеру и откройте **Properties > Camera** (с движком Range Game).

В панели **Focus & Tracking**:

1. В **Focus** выберите **Object** и укажите объект, за которым должна следить камера (машина, игрок).
2. В **Tracking** выберите **Look At**. Камера остаётся на месте, но плавно поворачивается, удерживая цель в кадре.
3. **Track Smooth** задаёт плавность (в секундах). **Framing Offset** с отрицательным Y держит цель чуть ниже центра.

## 2. Эффекты

В панели **Camera Effects**:

- **DOF**: размывает всё, что вне фокусного расстояния. Работает вместе с фокусом из предыдущего шага.
- **Speed Blur**: радиальное размытие, растущее со скоростью камеры. **Full Speed** — скорость (м/с), при которой эффект достигает максимума.
- **Protect Focus**: исключает цель из размытия (машина остаётся чёткой).
- **Vignette / Fisheye**: тёмные углы и искажение объектива.

Каждый эффект расходует производительность, только пока он включён.

## 3. Тряска из скрипта

`shake(trauma, duration)` трясёт камеру. `trauma` — от 0 до 1, несколько встрясок складываются. Пример: тряска по нажатию пробела, как при взрыве.

```python
import Range
from Range import events, logic


class TremerNoEspaco(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        pass

    def update(self):
        teclado = logic.keyboard.inputs[events.SPACEKEY]
        if teclado.activated:
            camera = self.object.scene.active_camera
            camera.shake(0.8, 0.6)
```

Прикрепите его к любому объекту сцены. Сила и частота тряски задаются в панели камеры **Camera Shake** (или в `shakeAmplitude` и `shakeFrequency`).

## 4. Включение эффектов из игрового меню

Меню настроек может включать и выключать эффекты во время игры:

```python
camera = Range.logic.getCurrentScene().active_camera
camera.useSpeedBlur = True
camera.speedBlurStrength = 0.5
camera.useDof = False
```

## Зерно плёнки

Зерно относится к сцене, а не к камере: **Render > Post Processing**, опция Film Grain. В игре:

```python
cena = Range.logic.getCurrentScene()
cena.filterManager.changeGrainValues(True, 0.3)
```
