---
title: Vehículos
description: Arma un auto con el panel Vehicle y manéjalo con el componente listo o desde Python.
---

:::note
El código es el mismo probado en la página en portugués, por eso nombres como `carro` (auto) y `volante` (volante) están en portugués.
:::

Anastacio arma el vehículo por ti desde el panel **Physics > Vehicle**. Solo configuras las ruedas y asignas un controlador.

## 1. Armar el auto

Necesitas un chasis (la carrocería) y un objeto por rueda.

1. Selecciona el chasis. En **Properties > Physics**, usa **Rigid Body** y activa el vehículo en el panel **Vehicle**.
2. En la lista de ruedas, agrega una entrada por rueda y elige su objeto.
3. Para cada rueda, ajusta **radio**, **suspensión**, si **gira** (ruedas delanteras) y si es **motriz**.

<!-- PRINT: Physics > Vehicle panel with four wheels -->

:::tip
La demo **Vehicle** que viene con el motor (carpeta `demos/Vehicle`) ya tiene un auto configurado. Ábrela para ver valores que funcionan.
:::

## 2. Manejar con el componente listo

Asigna el componente `VehiclePlayerComponent` (archivo `vehicle_player_component.py` de la demo) al chasis.

- **W** acelera, **S** da reversa, **A/D** giran;
- **Espacio** frena, **Shift izquierdo** es el freno de mano;
- con marchas registradas en el panel Vehicle, el cambio es automático (o E/Q en manual).

El componente publica las propiedades `vehicle_speed_kmh`, `vehicle_rpm` y `vehicle_gear` en el chasis, útiles para un velocímetro.

:::tip
Por convención del proyecto, el frente del chasis apunta hacia **+Y**. Si el auto va en reversa al presionar W, activa **Invert Direction** en las propiedades de `VehiclePlayerComponent`.
:::

## 3. O controlarlo desde Python

`getVehicle()` devuelve el vehículo del chasis ([`KX_VehicleWrapper`](../../api/types/kx_vehiclewrapper/)). Un controlador mínimo:

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

Asígnalo al chasis. Las ruedas 0 y 1 son las dos primeras de la lista del panel (las que giran).

:::note
El signo de la fuerza depende de hacia dónde mira el chasis. Si el auto va en reversa con W, invierte los signos.
:::

## Guardar el ajuste del auto

`vehicle.savePreset("//acerto.json")` escribe masa, suspensión, fricción y ruedas en un archivo. `vehicle.loadPreset(...)` vuelve a aplicar el ajuste al mismo auto, por ejemplo para alternar entre "asfalto" y "tierra".

:::caution
`savePreset()` falla si el campo **Ray Cast Mask** del vehículo queda en su valor predeterminado (0): el motor guarda internamente -1, y su propia validación rechaza ese valor. Ajusta el Ray Cast Mask manualmente en el panel Vehicle antes de guardar el ajuste.
:::
