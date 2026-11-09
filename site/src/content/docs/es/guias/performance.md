---
title: Menú Performance (informe y optimización)
description: Mide tu juego con un clic y recibe un informe visual de lo que pesa y qué hacer. Incluye Scene Doctor, LODs, colisión y preparación para exportar.
---

El botón **Performance**, en la barra superior junto a **Game**, reúne las herramientas para encontrar lo que vuelve lento el juego y corregirlo. Funciona con cualquier juego, sin instalar nada.

## Performance Report

1. Haz clic en **Performance > Measure**.
2. El juego se abre en `AnastacioRuntime` con la grabación activada. Juega las partes que quieras medir.
3. Cierra el juego. El informe (`report.html`) se abre en el navegador.

Si la escena tiene cambios sin guardar, el motor ejecuta una copia temporal y la borra al final. Tu archivo no se toca.

**Last** vuelve a abrir el último informe y **Folder** abre la carpeta con todos.

### Qué muestra el informe

- **Veredicto arriba**: funciona bien, conviene mirar o necesita trabajo.
- **Tarjetas de colores** (verde, amarillo, rojo) con los números clave.
- **Qué hacer**: recomendaciones automáticas según lo medido.
- **Comparación** con el informe anterior del mismo juego, para ver si un cambio ayudó.
- **Gráfico de fotogramas** con los picos marcados, además de las escenas y sonidos de cada momento.
- **A dónde va el tiempo** de cada fotograma: lógica, física, render y más.
- **Scripts**: tiempo de cada componente Python (por clase) y de cada controlador Python (por script).
- **Picos**: el script más pesado y lo que se estaba cargando en cada tirón.
- **Memoria** del proceso a cada segundo.
- **Cargas durante el juego**, **shaders** compilados y **carga por escena**.
- **Cargado pero nunca dibujado**: lo que ocupa memoria sin aparecer.
- **Sonidos** iniciados (actuador Sound, altavoz, World Sound) y contadores por fotograma.

El inicio (hasta 60 fotogramas seguidos sin picos) se muestra aparte arriba y no cuenta en los números.

El informe tiene tema claro y oscuro (sigue el sistema, con un interruptor en la esquina) y usa el idioma de la interfaz del editor.

:::tip
Mide, cambia una cosa y vuelve a medir. La sección de comparación muestra enseguida si mejoró o empeoró.
:::

## Scene Doctor

**Performance > Scene Doctor** analiza la escena abierta sin ejecutar el juego y lista lo que cuesta tiempo de carga, memoria o tiempo de fotograma. Muchos elementos se corrigen con un clic, como generar LODs para mallas pesadas o sustituir una colisión estática densa por un proxy.

## Optimizar la escena

- **Generate LODs**: crea niveles de detalle en lote, con distancias calculadas según el tamaño de cada objeto. La **X** de al lado elimina los LODs generados.
- **Collision Proxies**: crea colisión simplificada para escenario estático denso. La **X** los elimina.

### Automatic Occluders

En la pestaña **Scene**, en **Game Settings > Physics**, recuadro **Culling**, debajo de **Occlusion Culling**, marca **Automatic Occluders**. Las paredes, suelos y edificios grandes empiezan a ocultar lo que tienen detrás, y el motor deja de dibujar esos objetos.

- **Elegidos automáticamente al cargar:** mallas inmóviles (física Static o No Collision), opacas, de hasta 2048 triángulos y grandes (segundo lado mayor de al menos 1,5 m y cara mayor de al menos 6 m²). **Conservan su colisión**. En cambio, el tipo de física **Occluder** de la pestaña Physics elimina la colisión del objeto.
- **Se enciende y se apaga solo en el juego:** cada 30 fotogramas el motor cuenta cuántos objetos oculta la oclusión a la cámara activa. En zonas abiertas, donde oculta poco, sigue apagado y no cuesta nada; en interiores se enciende.
- **Cuándo ayuda:** interiores con muchas habitaciones y PCs con GPU débil. En un edificio de 36 habitaciones con una GPU débil simulada, el tiempo de fotograma bajó de 5,1 a 3,75 ms. En un buen PC la diferencia es pequeña, porque Auto Static Batch ya une las llamadas de dibujo.
- Viene **apagado**. El **Scene Doctor** lo sugiere cuando la escena tiene 150 mallas o más y al menos 8 paredes o edificios que cumplan los requisitos.
- Los objetos cargados con `LibLoad` no entran en la elección automática.

:::tip[Medir sin límite de FPS]
El juego siempre sigue los FPS de lógica de la escena (**Scene > Game Settings > Physics > Steps & Timing > FPS**, 60 por defecto). Desmarcar **Use Frame Rate** (pestaña Render, **System**) no quita el límite: esa opción solo elige cómo avanza la física. Para comparar dos versiones por tiempo de fotograma, sube los FPS de lógica en una copia de la escena de prueba (por ejemplo, a 1000) y lee el tiempo de trabajo en el Performance Report.
:::

## Scripts más rápidos

Medido en RolimaRacer con 20 pilotos. Cada llamada a la API cuesta de 0,2 a 0,6 µs solo por pasar de Python a C++, y un bucle por objeto multiplica eso por el número de objetos en cada fotograma.

- **Calcula una vez, lee muchas.** Si cada coche necesita un valor de los demás (carril, distancia en la pista), el dueño lo calcula en su propio `update()` y lo guarda; los demás solo lo leen. En RolimaRacer esto redujo a la mitad el coste de la IA.
- **Entrada compartida.** Teclas de depuración o atajos que lee cada objeto: lee el teclado una vez por fotograma (con `Range.logic.getFrameTime()` como clave) y omite el resto cuando no se pulsa nada.
- **Usa lo que ya es nativo.** Las operaciones matemáticas repetidas sobre listas grandes (seguir una línea de pista, buscar el punto más cercano) son mucho más rápidas en C++. Para la IA de carreras existe [`TrackLine`](../../api/types/trackline/): ubicar un coche en la línea baja de ~128 µs a ~3 µs.
- **Prefiere `obj.get("x", default)`** para leer propiedades y guarda en una variable local lo que uses varias veces en el mismo `update()`.
- **No repitas en cada fotograma lo que no cambia.** Ocultar objetos, leer ajustes y buscar hijos puede ir en `start()` o cada varios fotogramas.

Para encontrar el script pesado, usa el **Performance Report** de arriba: lista el tiempo de cada componente.

## Preparar para exportar

- **Textures (DDS)**: prepara las texturas como DDS BC1/BC3 para el juego de escritorio exportado. La flecha revierte.
- **Audio (OGG)**: prepara los sonidos como OGG para el paquete exportado.

Los originales no se tocan; las versiones preparadas solo se usan al exportar.

## Web y Android

Las GPU de los teléfonos son mucho más débiles que las de escritorio, y los efectos a pantalla completa cuestan bastante más. El menú **Performance** tiene una sección **Web / Android** con estos consejos.

### Sky Quality

El cielo **Atmospheric** calcula la atmósfera en cada píxel. En el **World**, **Sky Quality** elige su coste:

| Opción | Uso | Medido en un teléfono Android |
|---|---|---|
| **Auto** (predeterminada) | Low en Web y Android, High en escritorio | ~11 ms por fotograma |
| **High** | cielo completo | 41 ms (~24 FPS) |
| **Low** | teléfonos y GPU integradas | ~11 ms |
| **Very Low** | teléfonos débiles o escenas con muchos efectos | 3 ms |

### Medir en el teléfono

1. Exporta a Web y ejecuta el `serve.py` del paquete en el PC.
2. En el teléfono (misma Wi-Fi), abre `http://<IP del PC>:8080/?report=1`. Con cable USB: `adb reverse tcp:8080 tcp:8080` y abre `http://localhost:8080/?report=1`.
3. Juega. Cada 10 segundos y al salir, el teléfono envía los datos al PC, que escribe `reports/<fecha>/report.html` en la carpeta del paquete.

:::tip
En la Web, el tiempo mostrado como **Overhead** es el navegador esperando a la GPU. Si domina, el cuello de botella son los píxeles y los efectos, no los scripts.
:::
