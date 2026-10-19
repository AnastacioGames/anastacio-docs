---
title: Range y bge
description: Los dos nombres del módulo principal y por qué Range lleva R mayúscula.
---

La API del motor vive en el módulo **`Range`**, con **R mayúscula**. Range Engine eligió la mayúscula para que no se confunda con la función `range()` de Python.

```python
import Range
from Range import logic, events
```

El nombre antiguo **`bge`** también funciona. El motor registra cada submódulo con ambos nombres, así que `Range.logic` y `bge.logic` son el mismo objeto:

```python
import bge
from bge import logic
```

Esta documentación usa `Range` en todos los ejemplos.

| Range | bge | Para qué sirve |
|---|---|---|
| `Range.logic` | `bge.logic` | Escena, objetos, tiempo, propiedades globales y carga de archivos |
| `Range.types` | `bge.types` | Clases de objetos del juego: objetos, cámaras, luces, sensores, actuadores |
| `Range.render` | `bge.render` | Ventana, resolución, VSync, cursor del mouse y dibujo de depuración |
| `Range.events` | `bge.events` | Constantes de teclas, botones del mouse y estados de entrada |
| `Range.constraints` | `bge.constraints` | Uniones físicas, vehículos y ajustes del motor de física |
| `Range.application` | `bge.application` | Información de la aplicación, como versión y plataforma |
| `Range.texture` | `bge.texture` | Texturas dinámicas: video, imagen, cámara y render a textura |
| `Range.imgui` | `bge.imgui` | Ventanas y controles de interfaz para depuración |
| `Range.network` | `bge.network` | Multijugador: conexión, mensajes y replicación de objetos |

:::caution[Exportación Web]
El validador Web avisa `WEB-PY-001` cuando encuentra `import bge` y sugiere cambiarlo por `import Range`.
:::
