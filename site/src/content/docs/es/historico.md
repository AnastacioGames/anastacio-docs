---
title: Lo que ya se hizo
description: Todo lo que Anastacio Engine ha ganado desde el fork de Range Engine 1.6, mes a mes.
sidebar:
  label: Lo que ya se hizo
---

<div class="ae-h-hero">
<span class="ae-h-eyebrow">Diario de a bordo · ago → oct 2026</span>
<p class="ae-h-lead">Cada línea de abajo sale del diario técnico del motor. Esta es la versión corta: qué cambió para quien hace juegos.</p>
<dl class="ae-h-odo">
<div><dt>entradas en el diario</dt><dd>716</dd></div>
<div><dt>versiones publicadas</dt><dd>15</dd></div>
<div><dt>plataformas</dt><dd>4</dd></div>
</dl>
</div>

<section class="ae-h-month">
<header><span class="ae-h-num">08</span><div><h2>Agosto</h2><p>La base: más rápido y con partículas nuevas</p></div></header>
<div class="ae-h-grid">
<article><h3>Rendimiento</h3><ul>
<li>Personajes animados calculados en la tarjeta gráfica (GPU Skinning).</li>
<li>El follaje recortado se dibuja más rápido: 28 → 21 ms por fotograma en la prueba.</li>
<li>Los árboles lejanos se convierten automáticamente en impostores (una imagen plana).</li>
</ul></article>
<article><h3>Efectos</h3><ul>
<li>Sistema de partículas en la GPU: fuego, humo, polvo y chispas listos para usar.</li>
<li>Primeros filtros de pantalla (escala de grises, negativo, sepia).</li>
</ul></article>
<article><h3>Editor</h3><ul>
<li>Elige entre los iconos de Range y de UPBGE.</li>
<li>Menús de ImGui organizados como componentes.</li>
</ul></article>
</div>
</section>

<section class="ae-h-month">
<header><span class="ae-h-num">09</span><div><h2>Septiembre</h2><p>El motor sale de Windows</p></div></header>
<div class="ae-h-grid">
<article><h3>Web y móvil</h3><ul>
<li>El juego corre en el navegador: luces, sombras, filtros, sonido, guardado y Python.</li>
<li>Validación y "Abrir en el navegador" directo desde el editor.</li>
<li>Exporta a Android (APK y AAB), con controles en pantalla y sensores de movimiento.</li>
</ul></article>
<article><h3>Linux</h3><ul>
<li>Editor y reproductor nativos, con un paquete portátil que corre en varias distros.</li>
<li>Cycles con tarjetas NVIDIA (CUDA) y AMD (OpenCL).</li>
</ul></article>
<article><h3>Juego</h3><ul>
<li>Cinemáticas nativas con línea de tiempo.</li>
<li>Destrucción y explosiones, cámara con enfoque y temblor, lluvia y nubes en el World.</li>
<li>Áreas de eco (Reverb Area), eventos de animación y navmesh que esquiva obstáculos.</li>
<li>Los scripts antiguos de BGE/UPBGE corren sin cambiar los imports.</li>
</ul></article>
<article><h3>Editor</h3><ul>
<li>Barra flotante en la 3D View, colecciones en el Outliner y Asset Browser.</li>
<li>Interfaz en English, Português, Español y Русский.</li>
<li>Los Logic Bricks se convierten en Python con un botón.</li>
</ul></article>
<article><h3>Por dentro</h3><ul>
<li>El núcleo del juego se reorganizó en 11 etapas, con medidores de rendimiento.</li>
<li>Paso de física fijo opcional, para que el juego se comporte igual a cualquier FPS.</li>
</ul></article>
</div>
<p class="ae-h-rel">Versiones 0.3.0 a 0.4.6</p>
</section>

<section class="ae-h-month">
<header><span class="ae-h-num">10</span><div><h2>Octubre</h2><p>Gráficos nuevos, lógica sin código y multijugador</p></div></header>
<div class="ae-h-grid">
<article><h3>Gráficos</h3><ul>
<li>Los nodos de material de Cycles funcionan en el juego: vidrio, pelo, volumen, cielo.</li>
<li>Reflejos (probes y espejo plano), sombra de color de vitral y sombras en cascada.</li>
<li>Sombra de sol con cascadas (CSM) y sombras suaves con penumbra (PCSS).</li>
<li>Efectos de posprocesado en el juego: Directional Blur, Color Correction, Tonemap, Glare, Crop y más.</li>
<li>Nubes volumétricas, niebla volumétrica e iluminación indirecta (bake y SSGI).</li>
<li>Shaders por nodos con viento, olas, pelo y contorno toon.</li>
</ul></article>
<article><h3>Carga</h3><ul>
<li>Archivo "cocido" (<code>.cooked</code>): física, shaders y mallas listos al abrir.</li>
<li>Pantalla de carga con progreso real y texturas DDS comprimidas.</li>
<li>Elige qué carga con la escena y qué carga solo cuando hace falta.</li>
</ul></article>
<article><h3>Rendimiento</h3><ul>
<li>Static Batch: con él activado empatamos con ThunderPlayer en el benchmark.</li>
<li>Cerca de 100 puntos de trabajo repetido revisados en el motor.</li>
<li>Range Trace, Performance Report y Scene Doctor muestran dónde pesa el juego.</li>
<li>Auto Static Batch, un contador de FPS compacto y una API de Python más barata.</li>
</ul></article>
<article><h3>Lógica sin código</h3><ul>
<li>Logic Bricks 2.0 y Logic Tree: lógica por nodos que se convierte en bricks nativos.</li>
<li>Smart Components con asistente, y filtros 2D con campos en el panel.</li>
<li>UI Tree: menús y HUD montados en el editor de nodos.</li>
</ul></article>
<article><h3>Juego</h3><ul>
<li>Multijugador nativo (LAN, internet y navegador) y complemento de Steam.</li>
<li>World Sound con música, ambiente, lluvia y trueno.</li>
<li>VR en el móvil, ragdoll, abolladuras por golpes y vehículos arcade.</li>
<li>Idiomas del juego y grabación de pantalla con sonido.</li>
<li><code>Range.types.TrackLine</code>: una pista para que siga la IA de carreras.</li>
</ul></article>
<article><h3>Texto y diálogos</h3><ul>
<li>Text Boxes en el juego: salto de línea, páginas y efecto de máquina de escribir.</li>
<li>Diálogos sin código: nodo Dialogue Box en la UI Tree.</li>
</ul></article>
<article><h3>Tiempo y estabilidad</h3><ul>
<li>Un único reloj con escala de tiempo; la cinemática se pausa junto con la escena.</li>
<li>Revisión general de escena, objetos, joystick, LibLoad y multijugador, con varios cuelgues corregidos.</li>
<li>Exportación: Compile Scripts funciona y el <code>.range</code> abierto ya no va en el paquete.</li>
<li>Fixed Timestep con dibujo interpolado, activado por defecto en escenas nuevas (0.6.1).</li>
</ul></article>
</div>
<p class="ae-h-rel">Versiones 0.5.0 a 0.6.1</p>
</section>

<p class="ae-h-foot">¿Quieres el detalle de algo? El diario completo está en el repositorio del motor, en <code>docs/changelog.md</code>. Lo que aún falta está en <code>docs/roadmap.md</code>.</p>
