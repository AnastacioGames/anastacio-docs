---
title: Exportar tu juego
description: Cómo convertir tu .range en un juego que otras personas puedan jugar, en PC, en el navegador o en el teléfono.
---

Todas las opciones de exportación están en la misma pestaña: **Properties > Export Game** (el icono de caja en la columna de pestañas a la derecha). Tiene tres paneles, uno por destino.

| Destino | Panel | Salida | Cuándo usarlo |
|---|---|---|---|
| PC (Windows y Linux) | **Export (RangeArmor)** | Carpeta `release/` con el ejecutable del juego | Para publicar en itch.io, Steam o como zip |
| Navegador | **Web** | Carpeta con `index.html` y el runtime WebGL 2 | Para jugar en un sitio web, sin instalar nada |
| Teléfono Android | **Android (Web)** | Archivo `.apk` (más `.aab` para Google Play) | Para instalar en un teléfono o publicar en la tienda |

Android reutiliza el paquete Web: el APK es una app que ejecuta dentro la versión Web del juego. Por eso **todo lo que funciona en Web funciona en Android**, y los avisos de Web aplican a ambos.

## Siempre, antes de exportar

1. **Guarda el archivo** (`Ctrl+S`). Las tres exportaciones usan el `.range` guardado en disco, no lo que está abierto en pantalla.
2. **Prueba con P** en el editor. Si el juego no funciona en el editor, no funcionará exportado.
3. Usa **rutas relativas** para texturas, sonidos y scripts (`//textures/...`). Una ruta absoluta (`C:\Users\...`) solo existe en tu PC.

## Guías

- [Exportar a PC con RangeArmor](../rangearmor/)
- [Exportar al navegador (Web/WebGL)](../web/)
- [Exportar a Android (APK y clave .jks)](../android/)
