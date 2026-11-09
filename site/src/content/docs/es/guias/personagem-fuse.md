---
title: Personaje automático (Fuse)
description: Convierte un OBJ exportado de Fuse en un personaje con esqueleto, LODs y ragdoll, sin Mixamo.
---

El motor convierte el OBJ de un personaje de Fuse en un personaje listo para el juego, sin pasar por Mixamo.

## Importar

Abre **File > Import > Fuse Character (.obj)**, elige el archivo y ajusta:

| Opción | Qué hace |
|---|---|
| **Skeleton** | Esqueleto de la biblioteca usado como base. |
| **Name** | Nombre del personaje; el grupo se llama `Group<Nombre>`. Vacío usa el nombre del archivo. |
| **Ragdoll** | Añade cajas de ragdoll en los huesos grandes, sin manos ni dedos. |
| **Output Folder** | Dónde quedan `Group<Nombre>.range` y `textures/`. Vacío crea una carpeta junto al archivo abierto. |
| **Game Folder** | Raíz del proyecto del juego, para conectar el componente de ragdoll. Vacío usa la carpeta del archivo abierto. |
| **Add to Scene** | Coloca el grupo terminado en la escena actual, en el cursor 3D. |

El proceso se ejecuta en segundo plano y no toca el archivo abierto.

## Qué obtienes

- Cuerpo reducido a 9000 triángulos en el nivel 0, preservando cabeza y pecho.
- LODs de 2500 triángulos a 10 m y 900 triángulos a 25 m.
- Un grupo con armature, cuerpo y ragdoll, guardado para entrar con `LibLoad`.

:::caution
Revisa la licencia de las mallas de Fuse antes de distribuir el juego.
:::
