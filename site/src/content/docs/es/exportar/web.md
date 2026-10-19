---
title: Exportar al navegador (Web)
description: Paso a paso para generar la versión WebGL 2 del juego, probarla en el navegador y publicarla en un sitio web.
---

La exportación Web crea una carpeta que ejecuta el juego **dentro del navegador** (Chrome, Edge, Firefox y navegadores de teléfono), usando WebGL 2 y WebAssembly. El jugador abre un enlace, hace clic en **Play** y listo: no hay nada que instalar.

:::note
El runtime Web ya viene en el zip del motor, en la carpeta `web/` junto a `AnastacioEngine.exe` (o `AnastacioEngine` en Linux). No hace falta descargar nada más.
:::

## 1. Abrir el panel

**Properties > Export Game > Web**. El panel empieza contraído; haz clic en su título para abrirlo.

![Panel web](../../../../assets/exportar/web_en.png)

## 2. Paquete

| Campo | Qué hace |
|---|---|
| **Web runtime** | Qué runtime usar. Deja `web-runtime-release`. |
| **Entry scene** | Primera escena del juego. Vacío usa la escena actual. |
| **Destination** | Carpeta de salida. El valor predeterminado `//web/` crea una carpeta `web` junto al `.range`. |

## 3. Controles táctiles (Touch Controls)

Los teléfonos y tabletas no tienen teclado. Aquí eliges el control virtual que aparece **solo en pantallas táctiles**. También aplica a Android.

| Diseño | Para juegos que leen... |
|---|---|
| **Stick + 2 buttons** | Gamepad: stick izquierdo y botones A/B |
| **D-pad + 4 buttons** | Gamepad: cruceta y A/B/X/Y |
| **Two sticks** | Gamepad: dos sticks |
| **Stick as WASD + Space** | Teclado: el stick presiona W/A/S/D y el botón presiona Espacio |
| **D-pad as arrows + Space/Enter** | Teclado: flechas, Espacio y Enter |
| **First person (WASD + look)** | Teclado y mouse: moverse con WASD, mirar alrededor con el stick derecho |
| **Racing (steer + pedals)** | Gamepad: dirección en el stick, pedales en los gatillos; el jugador puede cambiar a flechas o a inclinar el dispositivo |
| **None** | Sin controles; los toques se convierten en clics del mouse |

**Stick mode** elige si el stick aparece donde toca el dedo (**Where the finger touches**) o queda fijo en la esquina (**In the corner**).

:::tip
Elige el diseño que coincida con lo que lee tu juego. Si el juego usa un sensor **Keyboard**, usa *WASD* o *flechas*; si usa **Joystick**, usa un diseño de gamepad. **Validate Web** te avisa (regla `WEB-INPUT-001`) cuando el diseño no presiona una tecla que el juego usa.
:::

Para ver los controles en una PC, abre el juego con `?touch=1` al final de la dirección y usa el mouse como dedo.

## 4. Validar

Haz clic en **Validate Web**. El motor revisa escenas, logic bricks, scripts y archivos y lista los problemas:

- **Error** (icono ✖): bloquea la exportación. Hay que corregirlo.
- **Advertencia** (icono ⚠): exporta, pero algo puede no funcionar en el navegador.
- **Info**: solo información.

Muchos elementos tienen un botón **Locate** que selecciona el objeto con el problema. Después de corregir, valida de nuevo.

## 5. Exportar

1. Guarda el archivo (`Ctrl+S`).
2. Opciones:
   - **Preflight after export**: después de exportar, abre el paquete en un Chrome/Edge oculto durante unos 15 s y agrega al informe los errores que vio el navegador. Déjalo activado.
   - **Open after export**: abre el juego en el navegador al terminar.
3. Haz clic en **Export Web**.

La exportación valida de nuevo antes de generar. Si falla, se conserva el paquete anterior.

## 6. Probar en el navegador

No basta con hacer doble clic en `index.html`: los navegadores bloquean WebAssembly cargado desde archivos locales. Usa el servidor del motor:

- **Browser Test > Open in browser**: inicia un servidor local y abre el juego. Haz clic en **Play** en la página.
- **Stop server** apaga el servidor (también se cierra con el motor).

:::caution
Presionar **P** en el editor **no** es una prueba Web. El navegador tiene límites que la PC no tiene; prueba siempre con **Open in browser**.
:::

Consejo: `?debug=1` al final de la dirección muestra el log del runtime en la página.

## 7. Publicar

La carpeta de destino es un sitio web listo (`index.html`, `RangeRuntime.*`, `game/`, `manifest.json`...). Incluye un `HOSTING.md` con recetas para cada servicio.

- **itch.io**: comprime en zip el *contenido* de la carpeta (`index.html` debe estar en la raíz del zip), crea un proyecto **HTML** y marca *This file will be played in the browser*.
- **GitHub Pages, Netlify, tu propio servidor**: sube la carpeta completa.

Requisitos del servidor:

- Servir `.wasm` como `application/wasm`.
- Activar compresión gzip o brotli: la descarga baja de ~46 MB a ~17 MB.
- No se necesitan los encabezados COOP/COEP.

Cuando publiques una versión nueva, cambia la versión del paquete para que los navegadores no usen la antigua en caché.

## Bueno saber

- El **sonido** solo empieza después de que el jugador hace clic en **Play** (una regla del navegador). Formatos: WAV, MP3 y OGG. Los efectos de sonido OpenAL no existen en Web.
- Las **partidas guardadas** (`saveGlobalDict`) se guardan en el navegador, por sitio. Cambiar de dominio o borrar los datos del sitio elimina la partida.
- La página tiene un botón de **pantalla completa**. En Android intenta fijar la orientación horizontal; en iPhone el botón está oculto (Safari no lo permite).
- Gráficos mínimos: **WebGL 2**.
