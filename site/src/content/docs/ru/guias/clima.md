---
title: Погода (дождь, молнии, облака и туман)
description: Включайте и меняйте погоду World во время игры с помощью setWeather и strikeLightning.
---

Погода в Anastacio живёт в **World**: дождь, брызги, лужи, молнии, облака, Sky Layers, объёмные облака и объёмный туман. Всё настраивается в редакторе, а во время игры значения меняются из Python через [`setWeather`](../../api/types/kx_worldinfo/).

:::note
Код тот же, что проверен на португальской странице, поэтому имена вроде `mundo` (мир) и `tempestade` (гроза) на португальском.
:::

## 1. Настройка в редакторе

1. Откройте вкладку **World** в свойствах.
2. В панели **Weather** включите **Rain** и подберите интенсивность, пока во вьюпорте не будет выглядеть как надо.
3. Если будете использовать облака, сразу включите в редакторе **Clouds** (или Sky Layers / Volumetric Clouds).

:::caution
Облакам нужен проход, создаваемый при загрузке. Если при старте игры ни один из них не включён в World, `setWeather("clouds", True)` негде рисовать. Включите их в редакторе, а если хотите начать без облаков, обнулите покрытие из скрипта.
:::

## 2. Смена погоды из скрипта

Создайте `clima.py` в Text Editor, прикрепите его как компонент к любому объекту сцены (например, к Cube) и зарегистрируйте, как в руководстве [Первый скрипт](../primeiro-script/).

```python
import Range
from collections import OrderedDict


class Clima(Range.types.KX_PythonComponent):
    args = OrderedDict([
        ("Segundos ate a tempestade", 5.0),
    ])

    def start(self, args):
        self.espera = args["Segundos ate a tempestade"]
        self.tempo = 0.0
        self.tempestade = False
        mundo = self.object.scene.world
        mundo.setWeather("rain", True)
        mundo.setWeather("rain_intensity", 0.2)

    def update(self):
        self.tempo += 1.0 / Range.logic.getAverageFrameRate()
        if not self.tempestade and self.tempo >= self.espera:
            self.tempestade = True
            mundo = self.object.scene.world
            mundo.setWeather("rain_intensity", 1.0)
            mundo.setWeather("puddles", True)
            mundo.setWeather("lightning", True)
            mundo.strikeLightning()
```

Что происходит:

- в начале идёт лёгкий дождь;
- через 5 секунд дождь усиливается, появляются лужи и сразу бьёт молния; дальше автоматические молнии продолжаются с интервалами.

## Имена, которые можно менять

Имена принимают префикс `weather.` (необязательно). Самые используемые:

| Имя | Тип | Что делает |
|---|---|---|
| `rain` | bool | Включает дождь |
| `rain_intensity` | float | Сила дождя |
| `rain_wind` | float | Наклон дождя от ветра |
| `puddles` | bool | Лужи на земле |
| `lightning` | bool | Автоматические молнии |
| `clouds` | bool | Облака (нужен проход, см. предупреждение выше) |
| `cloud_coverage` | float | Какая часть неба закрыта |
| `vfog` | bool | Объёмный туман |
| `vfog_density` | float | Плотность тумана |

Полный список — в [`KX_WorldInfo.setWeather`](../../api/types/kx_worldinfo/). Неверное имя вызывает ошибку, что помогает ловить опечатки.

## Без скрипта: Logic Bricks

Актуатор **Weather Effects** делает те же изменения без Python. Подключите к нему сенсор (Keyboard, Delay, Property) и выберите, что менять.
