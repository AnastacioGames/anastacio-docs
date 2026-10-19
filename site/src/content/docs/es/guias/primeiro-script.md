---
title: Primer script
description: Un script de Python que mueve un objeto al presionar una tecla.
---

1. Selecciona un objeto de la escena y agrega un sensor **Always** (con *True Level Triggering* activado) conectado a un controlador **Python**.
2. Crea un texto llamado `mover.py` en el editor de texto y elígelo en el controlador.
3. Pega el código y presiona **P** para jugar.

![Sensor Always conectado al controlador Python con el script mover.py, y el código en el editor de texto](../../../../assets/guias/logic-bricks-mover.png)

```python
import Range
from Range import logic, events

cont = logic.getCurrentController()
own = cont.owner
teclado = logic.keyboard

if teclado.inputs[events.WKEY].active:
    own.applyMovement((0, 0.1, 0), True)   # avanza hacia adelante
if teclado.inputs[events.SKEY].active:
    own.applyMovement((0, -0.1, 0), True)
```

El código usa nombres en portugués, los mismos que aparecen en las capturas: `mover` = mover, `teclado` = teclado, `Velocidade` = velocidad.

- `logic.getCurrentController()` devuelve el controlador que ejecuta el script.
- `own` es el objeto dueño del controlador, un [`KX_GameObject`](../../api/types/kx_gameobject/).
- `applyMovement(vector, local)` mueve el objeto; `True` usa los ejes propios del objeto.

## Lo mismo con un componente

Un componente hace el mismo trabajo sin logic bricks. Es una clase de Python asignada al objeto, y puedes cambiar sus parámetros en el panel sin tocar el código.

1. Crea un texto llamado `mover_componente.py` en el editor de texto (el nombre debe terminar en `.py`) y pega el código de abajo.
2. Selecciona el objeto y abre la pestaña de componentes (icono de Python) en las propiedades. En **Existing Components**, elige **In .Range File** en *Modules*, luego la clase **Mover** en *Classes*, y haz clic en **Register**. Si la clase no aparece, haz clic en el botón de actualizar en la esquina del panel.
3. El componente aparece en **Object's Components**, con el campo **Velocidade**. Ajústalo si quieres y presiona **P** para jugar.

![Componente Mover registrado en el objeto, con el campo Velocidade, y el código en el editor de texto](../../../../assets/guias/componente-mover.png)

```python
import Range
from Range import logic, events
from collections import OrderedDict


class Mover(Range.types.KX_PythonComponent):
    # parámetros que aparecen en el panel Components
    args = OrderedDict([
        ("Velocidade", 0.1),
    ])

    def start(self, args):
        # se ejecuta una vez, cuando empieza el juego
        self.velocidade = args["Velocidade"]

    def update(self):
        # se ejecuta en cada frame
        teclado = logic.keyboard
        if teclado.inputs[events.WKEY].active:
            self.object.applyMovement((0, self.velocidade, 0), True)   # avanza hacia adelante
        if teclado.inputs[events.SKEY].active:
            self.object.applyMovement((0, -self.velocidade, 0), True)
```

- La clase hereda de [`KX_PythonComponent`](../../api/types/kx_pythoncomponent/).
- `args` define los parámetros del panel. El orden del `OrderedDict` es el orden en que aparecen.
- `start(args)` recibe los valores del panel; `update()` se ejecuta en cada frame, antes de los logic bricks.
- `self.object` es el objeto dueño del componente, en lugar del `cont.owner` del script.

**¿Script o componente?** Usa un script con logic bricks para conectar sensores y actuadores de forma visual. Usa un componente cuando la lógica es toda en Python y quieres reutilizar la misma clase en varios objetos, cada uno con sus propios valores.
