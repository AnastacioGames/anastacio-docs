---
title: Plataformas
description: Como o mesmo código vira editor e player para Windows, Linux, Web e Android.
sidebar:
  label: 5 · Plataformas
  order: 5
fontes:
  - source/CMakePresets.json
  - source/release/scripts/modules/range_web/android.py
  - source/release/scripts/modules/range_web/__init__.py
  - source/source/blender/gpu/intern/gpu_shader.c
  - source/intern/ghost/intern/GHOST_WindowWin32.cpp
  - source/CMakeLists.txt
conferido: f0b2506f
---

<div class="ae-x">
<span class="ae-x-eyebrow">Parada 5 de 5</span>
<div class="ae-x-flow">
<div class="ae-x-row">
<span class="ae-x-chip"><b>Mesmo código-fonte</b><code>source/</code></span><i>preset v142-ninja</i>
<span class="ae-x-chip"><b>Windows x64</b><code>AnastacioEngine + AnastacioRuntime · Cycles: Embree, CUDA, OpenCL</code></span>
</div>
<div class="ae-x-row">
<span class="ae-x-chip"><b>Mesmo código-fonte</b><code>source/</code></span><i>linux-editor / linux-runtime</i>
<span class="ae-x-chip"><b>Linux x86_64</b><code>AnastacioEngine + AnastacioRuntime</code></span>
</div>
<div class="ae-x-row">
<span class="ae-x-chip"><b>Mesmo código-fonte</b><code>source/</code></span><i>web-runtime-release</i>
<span class="ae-x-chip"><b>Runtime Web</b><code>WebAssembly + WebGL2</code></span><i>Exportar Web</i>
<a class="ae-x-chip" href="/anastacio-docs/exportar/web/"><b>Pacote do navegador</b><code>o seu jogo + runtime</code></a><i>android.py</i>
<a class="ae-x-chip" href="/anastacio-docs/exportar/android/"><b>Android</b><code>APK/AAB com WebView</code></a>
</div>
</div>
<p class="ae-x-cap">Windows e Linux compilam editor e player nativos. A Web compila só o player; o jogo é exportado pelo editor e empacotado com ele. O Android aproveita esse pacote Web dentro de um app com WebView, então não existe build C++ próprio para celular.</p>
</div>

## Versão do OpenGL

O renderizador do jogo (`RangeRuntime`) é compilado com `WITH_GL_PROFILE_CORE_RANGERUNTIME`: não usa mais a pilha
fixa do OpenGL antigo e todos os shaders saem com `#version 330 core`. Por isso o jogo no PC precisa de
**OpenGL 3.3**. A janela continua pedindo um contexto compatibility, e o driver entrega a versão mais alta que
tiver, normalmente 4.6.

O editor fica em compatibility de propósito, porque `editors/` e `bf_rna` ainda dependem do OpenGL antigo.
`gpu_shader_version()` escolhe o maior `#version ... compatibility` que o driver aceitar, até 4.50.

A Web compila o mesmo renderizador para WebGL 2, com `#version 300 es`. Sem geometry shader em WebGL, esse estágio
é ignorado.

| Build | Contexto | Shaders |
|---|---|---|
| Jogo no PC | compatibility, versão máxima do driver | `#version 330 core` |
| Editor | compatibility, versão máxima do driver | `#version 4x0 compatibility` |
| Web e Android | WebGL 2 | `#version 300 es` |

## Para exportar o seu jogo

- [Visão geral da exportação](/anastacio-docs/exportar/visao-geral/)
- [RangeArmor](/anastacio-docs/exportar/rangearmor/), para proteger o jogo no desktop
- [Web](/anastacio-docs/exportar/web/) e [Android](/anastacio-docs/exportar/android/)

<div><a class="ae-x ae-x-next" href="/anastacio-docs/por-dentro/"><div><span class="ae-x-eyebrow">Fim do percurso</span><strong>Voltar ao mapa</strong></div><span class="ae-x-go">abrir →</span></a></div>
