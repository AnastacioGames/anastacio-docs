---
title: Exportar a PC (RangeArmor)
description: Paso a paso para generar el ejecutable del juego para Windows y Linux con RangeArmor.
---

**RangeArmor** es la herramienta que empaqueta el juego para PC. Junta el runtime del motor, tu `.range` protegido y un lanzador en un ejecutable que el jugador abre con doble clic. Una sola exportación puede generar las versiones **Windows 64-bit** y **Linux 64-bit**.

:::note
El panel de RangeArmor funciona en Windows y Linux (desde la 0.5.3). En ambos sistemas exporta para Windows y Linux.
:::

## 1. Instalar RangeArmor

RangeArmor se descarga aparte del motor, en la misma página de la versión: `RangeArmor-<versión>-windows-x64.zip` en Windows o `RangeArmor-<versión>-linux-x86_64.tar.xz` en Linux.

1. Extrae el archivo.
2. Renombra la carpeta extraída a **`rangearmor`** y ponla **dentro de la carpeta del motor**, junto a `AnastacioEngine.exe` (en Linux, junto a `AnastacioEngine`):

```
AnastacioEngine-0.6.1-windows-x64/
├── AnastacioEngine.exe
├── AnastacioRuntime.exe
└── rangearmor/
    ├── RangeArmor Panel.exe
    └── release/
```

El motor busca exactamente `rangearmor/RangeArmor Panel.exe` (en Linux, `rangearmor/RangeArmor Panel`) en ese lugar. Si la carpeta tiene otro nombre, los botones de exportación no encuentran la herramienta.

## 2. Crear el proyecto

RangeArmor trabaja con una carpeta de proyecto con estructura fija. La forma más fácil de crear una es desde el motor:

![Menú File](../../../../assets/exportar/menu_file.png)

El menú **File** tiene **Create Project**, **Export Game With RANGEARMOR** y **Save .Range Protected File**.

1. **File > Create Project**.
2. Elige dónde crearlo y dale un nombre (sin `< > : " / \ | ? *`).
3. El motor crea esta estructura y abre el nuevo `.range`:

```
MiJuego/
├── data/            ← el .range del juego va AQUÍ
│   ├── MiJuego.range
│   ├── scripts/  textures/  models/  audio/  fonts/  scenes/  libloads/
├── engine/          ← runtime copiado al exportar
├── launcher/        ← config.json y lanzador
├── icons/
└── release/         ← salida de la exportación
```

:::caution[Regla más importante]
El `.range` principal debe estar **dentro de la carpeta `data/` del proyecto**. Si está en otro lugar, la exportación dice: *"Current file is not inside a RangeArmor project"*.
:::

¿Ya tienes un juego terminado? Crea el proyecto y luego copia tu `.range` y sus archivos (texturas, sonidos, scripts) dentro de `data/`, manteniendo las mismas subcarpetas para que las rutas relativas sigan funcionando.

![Panel rangearmor](../../../../assets/exportar/armor_en.png)

## 3. Configurar el panel Export (RangeArmor)

En **Properties > Export Game > Export (RangeArmor)**:

| Campo | Qué hace |
|---|---|
| **Windows 64-bit / Linux 64-bit** | Plataformas a generar. Puedes activar ambas. |
| **Product Name** | Nombre del juego, usado en el ejecutable y en el paquete. |
| **Version** | Versión del paquete, por ejemplo `1.0.0`. |
| **Company Name** | Tu nombre o estudio. |
| **Icon** | Archivo `.ico` del ejecutable. Vacío mantiene el icono predeterminado. |
| **Cook before export** | Genera la caché "cocida" (física y shaders listos) para que el juego abra más rápido. Déjalo activado. |

Los campos vacíos mantienen los valores predeterminados de RangeArmor.

## 4. Exportar

Hay dos botones:

- **Export Game (1 Click)**: guarda una copia protegida, cocina la caché y genera todo directamente en `MiJuego/release/`. La carpeta se abre al terminar. **Este es el camino recomendado.**
  También genera el paquete **Universal**: una carpeta (y un zip) con Windows y Linux juntos. El jugador abre `MiJuego.exe` en Windows o `MiJuego` en Linux. *(desde la 0.6.0)*
- **Open RangeArmor Panel**: abre la herramienta completa, con más opciones. Los ajustes del panel del motor se le pasan.

El mismo panel también se abre desde **File > Export Game With RANGEARMOR**.

:::tip
Si ves *"Could not find a Python interpreter for the export"*, abre RangeArmor Panel una vez, haz clic en **Get RanGE** e intenta 1 Click de nuevo.
:::

## Otra forma: usar RangeArmor Panel por separado

También puedes exportar sin los botones del motor, abriendo la herramienta externa directamente. Es útil para exportar un proyecto antiguo o cambiar opciones que el panel del motor no muestra.

![Pantalla inicial de RangeArmor Panel](../../../../assets/exportar/rangearmor_inicio.png)

Pantalla inicial de RangeArmor Panel: **Open Project**, **New Project** y la lista **Recent projects**.

1. Abre **`rangearmor/RangeArmor Panel.exe`** (en Linux, `rangearmor/RangeArmor Panel`) en la carpeta del motor. También se abre desde el botón **Open RangeArmor Panel** o **File > Export Game With RANGEARMOR**.
2. En la pantalla inicial, haz clic en **New Project** para crear una carpeta de proyecto nueva, o en **Open Project** para abrir una existente (por ejemplo, la creada con **File > Create Project**). Los proyectos abiertos antes aparecen en **Recent projects**.
3. En el motor, abre tu `.range` y guarda la copia protegida con **File > Save .Range Protected File** dentro de la carpeta `data/` del proyecto. Tiene la extensión `.rasec`.
4. De vuelta en el panel, en la pestaña **Project**:

| Campo | Qué hace |
|---|---|
| **Game Name** | Nombre del juego. |
| **Version** | Versión del juego. |
| **Main File** | El archivo `.rasec` del paso 3. Mientras siga siendo el archivo de ejemplo, la exportación está bloqueada. |
| **Data Source** | Carpeta con los archivos del juego (normalmente `data`). |
| **Compile Python scripts** | Incluye los scripts compilados en lugar del código fuente. |

5. En la pestaña **Paths**, revisa **Engine executables** (el runtime de cada plataforma) y **Python for authoring tools**. Si están vacíos, usa **Copy Available Range Engine Files** en la pestaña **Tasks**, que copia el runtime del motor a la carpeta `engine/` del proyecto.
   ![Pestaña Paths de RangeArmor Panel](../../../../assets/exportar/rangearmor_paths.png)

   Las rutas en **rojo** con la casilla vacía son archivos que aún no existen en la carpeta `engine/` del proyecto. Después de **Copy Available Range Engine Files**, quedan marcadas (✓) y la plataforma cuenta como lista en la parte inferior.

6. Haz clic en **Save** para guardar los ajustes.
7. En la pestaña **Tasks**:
   - **Run game**: ejecuta el juego como lo verá el jugador, para probar primero.
   - **Set Icons**: elige los iconos `.ico` del lanzador y del ejecutable.
   - **Export to**: exporta una plataforma o **All Platforms**. **Compress targets after export** crea el zip.
   - **Universal (Win + Linux)**: además de la carpeta de cada plataforma, crea `MiJuego-<versión>-Universal/`, una sola carpeta para los dos sistemas. Necesita los dos runtimes en la pestaña **Paths**. *(desde la 0.6.0)*
   ![Pestaña Tasks de RangeArmor Panel](../../../../assets/exportar/rangearmor_tasks.png)

   Los botones de plataforma en gris y la nota *0/2 platform(s) ready* en la parte inferior indican que falta el runtime. Haz clic en **Copy Available Range Engine Files** (paso 5) y revisa **Main File** y **Data Source**; los botones se encienden cuando la plataforma está lista.

8. La salida va a la carpeta `release/` del proyecto. **Explore** abre la carpeta y **Copy Log** copia el log si algo sale mal.

:::note
El botón **Export Game (1 Click)** del motor hace los pasos 3 a 7 por sí solo, y además cocina la caché. Usa el panel externo cuando necesites control manual.
:::

## 5. Probar y publicar

1. Abre `release/` y **extrae el zip generado en cualquier carpeta fuera del proyecto**.
2. Ejecuta el ejecutable del juego y juégalo de principio a fin.
3. Si funciona, ese zip es lo que envías a los jugadores (itch.io, Steam, Google Drive...).

Probar fuera del proyecto es importante: dentro de él, el juego puede encontrar archivos que nunca entraron al paquete.

## Protección del archivo

El juego exportado usa una copia **protegida** del `.range` (extensión `.rasec`), que no se abre en el editor. También puedes crear esta copia manualmente con **File > Save .Range Protected File**. Conserva siempre el `.range` original: es el único que puedes editar.

## Problemas comunes

| Mensaje | Solución |
|---|---|
| *Save the .blend file inside the project's data/ folder first* | Guarda el archivo dentro de `data/`. |
| *Current file is not inside a RangeArmor project* | El `.range` no está en `<proyecto>/data/`. Usa **File > Create Project**. |
| *build_release.py not found next to RangeArmor Panel* | Falta la carpeta `rangearmor/` o tiene otro nombre. Ver el paso 1. |
| *Export finished with errors* | Abre la consola (**Window > Toggle System Console**) para ver el error completo. |
| *Universal package skipped: no runtime for ...* | Falta el runtime de una plataforma. Configura Windows y Linux en la pestaña **Paths** (o usa **Copy Available Range Engine Files**). |
