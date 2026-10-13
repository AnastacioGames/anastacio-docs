---
title: Vehicles
description: Build a car with the Vehicle panel and drive it with the ready-made component or from Python.
---

:::note
The code is the same one tested on the Portuguese page, so names such as `carro` (car) and `volante` (steering) are in Portuguese.
:::

Anastacio builds the vehicle for you from the **Physics > Vehicle** panel. You only configure the wheels and attach a controller.

## 1. Build the car

You need a chassis (the body) and one object per wheel.

1. Select the chassis. Under **Properties > Physics**, use **Rigid Body** and turn on the vehicle in the **Vehicle** panel.
2. In the wheel list, add one entry per wheel and pick its object.
3. For each wheel, set **radius**, **suspension**, whether it **steers** (front wheels) and whether it is **driven**.

<!-- PRINT: Physics > Vehicle panel with four wheels -->

:::tip
The **Vehicle** demo that ships with the engine (`demos/Vehicle` folder) already has a car set up. Open it to see working values.
:::

## 2. Drive with the ready-made component

Attach the `VehiclePlayerComponent` component (the demo's `vehicle_player_component.py` file) to the chassis.

- **W** accelerates, **S** reverses, **A/D** steer;
- **Space** brakes, **Left Shift** is the handbrake;
- with gears registered in the Vehicle panel, shifting is automatic (or E/Q for manual).

The component publishes the `vehicle_speed_kmh`, `vehicle_rpm` and `vehicle_gear` properties on the chassis, useful for a speedometer.

:::tip
By project convention, the chassis' front points toward **+Y**. If the car reverses when you press W, turn on **Invert Direction** in the `VehiclePlayerComponent` properties.
:::

## 3. Or control it from Python

`getVehicle()` returns the chassis' vehicle ([`KX_VehicleWrapper`](../../api/types/kx_vehiclewrapper/)). A minimal controller:

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

Attach it to the chassis. Wheels 0 and 1 are the first two in the panel's list (the steering ones).

:::note
The force's sign depends on which way the chassis faces. If the car reverses with W, flip the signs.
:::

## Saving the car setup

`vehicle.savePreset("//acerto.json")` writes mass, suspension, friction and wheels to a file. `vehicle.loadPreset(...)` reapplies the setup to the same car, for example to switch between "asphalt" and "dirt".

:::caution
`savePreset()` fails if the vehicle's **Ray Cast Mask** field is left at its default value (0): the engine internally stores -1, and its own validation rejects that value. Set the Ray Cast Mask manually in the Vehicle panel before saving the setup.
:::
