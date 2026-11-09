---
title: Minimap
description: Crea un minimapa en el HUD con un comando, como radar, mapa completo o GPS 3D, y marca jugadores y objetos.
---

**Minimap** es un nodo del HUD en la [UI Tree](../ui-tree/). No vuelve a dibujar la escena: muestra una imagen del mapa, así que cuesta poco.

## Crear con un comando

1. Guarda el `.range`. **Add > Minimap** con Bake y **Bake Map Image** rechazan una escena nunca guardada.
2. En la 3D View, selecciona al jugador y usa **Add > Minimap**.
3. Elige el estilo: **Radar** (círculo que gira), **Whole Map** (cuadrado fijo) o **GPS 3D** (rectángulo inclinado).

El comando crea el HUD, el nodo que sigue al objeto, la imagen del mapa y la lógica de la UI.

## Marcar objetos

Selecciona el objeto y abre la pestaña **Object**, panel **Minimap**. Activa **Show on Minimap**. **Own Color** le da un color propio; sin él, se usa el color **Markers** del nodo.

Por script, el color está en `minimap_color`, con formato `#rrggbb`:

```python
own["minimap_color"] = "#ff3030"
```

Sin el panel, usa la propiedad de juego `minimap` o el **Marker Prefix** en el nombre del objeto. Los marcadores fuera del área quedan sujetos al borde.

## Ajustes del nodo

| Opción | Qué hace |
|---|---|
| **World Min / Max** | Zona del mundo cubierta por la imagen. **Fit to Scene** la mide sola. |
| **Zoom Radius** | `0` muestra todo el mapa fijo; mayor que 0 sigue al jugador. |
| **Rotate with Player** | Gira el mapa con el jugador. |
| **Camera Tilt** | Inclina la vista de 0 a 60°, como un GPS 3D. |
| **Shape** | Circle, Square, Rectangle o Ellipse. |
| **Border Style** | None, Solid o Soft. |

**Bake Map Image** toma una imagen desde arriba de las mallas visibles, guarda `<archivo>_minimap.png` junto al `.range` y ajusta World Min/Max.
