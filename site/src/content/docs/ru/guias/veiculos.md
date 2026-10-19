---
title: Транспорт
description: Соберите машину через панель Vehicle и управляйте ей готовым компонентом или из Python.
---

:::note
Код тот же, что проверен на португальской странице, поэтому имена вроде `carro` (машина) и `volante` (руль) на португальском.
:::

Anastacio собирает транспортное средство за вас через панель **Physics > Vehicle**. Нужно только настроить колёса и прикрепить контроллер.

## 1. Сборка машины

Нужны шасси (кузов) и по объекту на каждое колесо.

1. Выберите шасси. В **Properties > Physics** используйте **Rigid Body** и включите транспорт в панели **Vehicle**.
2. В списке колёс добавьте по записи на каждое колесо и выберите его объект.
3. Для каждого колеса задайте **радиус**, **подвеску**, является ли оно **рулевым** (передние колёса) и **ведущим**.

<!-- PRINT: Physics > Vehicle panel with four wheels -->

:::tip
В демо **Vehicle**, поставляемом с движком (папка `demos/Vehicle`), уже есть настроенная машина. Откройте его, чтобы увидеть рабочие значения.
:::

## 2. Управление готовым компонентом

Прикрепите к шасси компонент `VehiclePlayerComponent` (файл демо `vehicle_player_component.py`).

- **W** — газ, **S** — задний ход, **A/D** — руление;
- **Space** — тормоз, **Left Shift** — ручник;
- если в панели Vehicle заданы передачи, переключение автоматическое (или E/Q для ручного).

Компонент публикует на шасси свойства `vehicle_speed_kmh`, `vehicle_rpm` и `vehicle_gear` — пригодятся для спидометра.

:::tip
По соглашению проекта перед шасси смотрит в сторону **+Y**. Если машина едет назад при нажатии W, включите **Invert Direction** в свойствах `VehiclePlayerComponent`.
:::

## 3. Или управление из Python

`getVehicle()` возвращает транспорт шасси ([`KX_VehicleWrapper`](../../api/types/kx_vehiclewrapper/)). Минимальный контроллер:

```python
import Range
from Range import events, logic


class DirigirSimples(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        self.carro = self.object.getVehicle()

    def update(self):
        if self.carro is None:
            return
        tecla = logic.keyboard.inputs
        forca = 0.0
        if tecla[events.WKEY].active:
            forca = -1500.0
        elif tecla[events.SKEY].active:
            forca = 800.0
        volante = 0.0
        if tecla[events.AKEY].active:
            volante = 0.4
        elif tecla[events.DKEY].active:
            volante = -0.4

        for roda in range(self.carro.getNumWheels()):
            self.carro.applyEngineForce(forca, roda)
            self.carro.applyBraking(0.0, roda)
        self.carro.setSteeringValue(volante, 0)
        self.carro.setSteeringValue(volante, 1)
```

Прикрепите его к шасси. Колёса 0 и 1 — первые два в списке панели (рулевые).

:::note
Знак силы зависит от того, куда смотрит шасси. Если машина едет назад по W, поменяйте знаки.
:::

## Сохранение настроек машины

`vehicle.savePreset("//acerto.json")` записывает в файл массу, подвеску, трение и колёса. `vehicle.loadPreset(...)` заново применяет настройки к той же машине, например чтобы переключаться между «асфальтом» и «грунтом».

:::caution
`savePreset()` завершается ошибкой, если поле **Ray Cast Mask** транспорта оставлено со значением по умолчанию (0): движок внутренне хранит -1, и его же проверка отвергает это значение. Задайте Ray Cast Mask вручную в панели Vehicle перед сохранением настроек.
:::
