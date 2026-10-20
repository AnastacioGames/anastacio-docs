---
title: Smart Components (Range.args y la clase Editor)
description: Campos con slider, ayuda y selector de objeto, avisos y botones en el editor, sin cambiar nada en el juego.
---

Un componente Python normal tiene `args` y el código del juego. El **Smart Component** es el mismo componente con dos recursos más, ambos opcionales:

1. **Campos mejores** con `Range.args`: slider con límites, ayuda al pasar el ratón, secciones, lista en orden y elegir un objeto o una escena con el ratón.
2. **Una clase `Editor`** que solo corre en el editor: prepara el objeto al añadirlo, muestra avisos en los campos, crea botones y dibuja guías en el viewport.

El juego no cambia: `args["Velocidad"]` sigue siendo un `float`, y el juego exportado corre sin `bpy`. Los componentes antiguos funcionan igual.

:::tip[Ejemplo listo]
En el Text Editor, **Templates > Components > 04 Smart Component** abre un perseguidor completo con todo lo de esta guía.
:::

## 1. Campos con Range.args

```python
from collections import OrderedDict
from Range import types
from Range.args import Float, Int, Bool, Text, Choice, Object, Scene, Header

class Perseguidor(types.KX_PythonComponent):
    args = OrderedDict([
        Header("Objetivo", icon="OBJECT_DATA"),
        ("Objetivo", Object(tip="Objeto que persigue")),
        ("Distancia de parada", Float(1.5, min=0, max=10, tip="Se detiene a esta distancia")),

        Header("Movimiento", icon="AUTO"),
        ("Velocidad", Float(3.0, min=0, max=20, tip="Metros por segundo")),
        ("Modo", Choice("Caminar", "Caminar", "Correr", "Saltar")),
        ("Mirar al objetivo", Bool(True, tip="Gira el cuerpo hacia el objetivo")),
        ("Escena al atrapar", Scene(tip="Escena que se añade encima al atrapar al jugador")),
    ])

    def start(self, args):
        self.objetivo = args["Objetivo"]    # KX_GameObject o None
        self.velocidad = args["Velocidad"]
```

| Campo | En el editor | Llega al juego como |
|---|---|---|
| `Float(valor, min, max, tip)` | número; slider cuando tiene `min` y `max` | `float` |
| `Int(valor, min, max, tip)` | entero; slider cuando tiene `min` y `max` | `int` |
| `Bool(valor, tip)` | casilla | `bool` |
| `Text(valor, tip)` | campo de texto | `str` |
| `Choice(defecto, item1, item2, ..., tip)` | lista en el orden escrito | `str` |
| `Object(tip)` | elegir un objeto de la escena | `KX_GameObject`, o `None` |
| `Scene(tip)` | elegir una escena del archivo | `str` con el nombre (`""` si está vacío), listo para `logic.addScene` |
| `Header(nombre, icon, open)` | título de sección plegable | (no es un campo) |

Los valores fuera del límite se recortan: escribir 50 en un `Float(max=20)` queda en 20. El formato antiguo (`("Nombre", 1.0)`) sigue valiendo en la misma lista, solo que sin ayuda.

## 2. Pedir cosas al añadir: `requires`

```python
class Perseguidor(types.KX_PythonComponent):
    requires = {"physics": "NO_COLLISION", "components": ["vida.Vida"]}
```

Al añadir el componente, el editor ajusta el tipo de física del objeto y añade los otros componentes de la lista.

## 3. La clase Editor

Va dentro del componente. El juego nunca la ejecuta. Puede usar `bpy`, pero impórtalo solo dentro de los métodos. Dentro, `self.object` es el objeto y `self.args["Campo"]` lee y escribe los campos.

```python
class Perseguidor(types.KX_PythonComponent):
    # ... args, start, update ...

    class Editor:
        buttons = [
            ("Poner en el suelo", "poner_en_suelo", "TRIA_DOWN_BAR"),
        ]

        def on_attach(self, obj):
            # una vez, justo cuando el componente entra en el objeto
            self.args["Nombre"] = obj.name

        def on_change(self, obj, nombre, valor):
            # corre para cada campo cuando algo cambia y al abrir el archivo;
            # devolver un texto muestra un aviso debajo del campo
            if nombre == "Velocidad" and valor > 15:
                return "Demasiado rápido: puede atravesar paredes"
            if nombre == "Objetivo" and valor is None:
                return "Sin objetivo: se quedará quieto"

        def poner_en_suelo(self, obj, context):
            context.scene.update()
            z_min = min((obj.matrix_world * v.co).z for v in obj.data.vertices)
            obj.location.z -= z_min

        def draw_gizmo(self, obj, args, g, selected):
            # dibujo en el viewport, no aparece en el juego
            pos = obj.matrix_world.translation
            g.circle(pos, args["Distancia de parada"], "GREEN")
            if args["Objetivo"] is not None:
                g.arrow(pos, args["Objetivo"].matrix_world.translation, "YELLOW", width=2)
```

| Elemento | Cuándo corre |
|---|---|
| `on_attach(self, obj)` | Una vez, cuando se añade el componente. |
| `on_change(self, obj, nombre, valor)` | Cuando cambia un campo y al abrir el archivo. El texto devuelto se vuelve un aviso. |
| `buttons = [(texto, metodo, icono)]` | Botones al final de la caja del componente; el método recibe `(obj, context)` y admite deshacer. |
| `draw_gizmo(self, obj, args, g, selected)` | En cada redibujado del viewport. `g` tiene `line`, `path`, `circle`, `sphere`, `box`, `arrow` y `text`; colores por nombre (`"RED"`) o `(r, g, b)`, posiciones en el mundo. |

Por defecto los gizmos solo aparecen con el objeto seleccionado. La opción **Overlay > Component Gizmos** cambia eso.

Los errores en el código del `Editor` aparecen en rojo en la caja del componente y no afectan al juego.
