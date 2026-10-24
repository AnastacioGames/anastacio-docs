---
title: Módulos do runtime
description: As peças do runtime em camadas, da aplicação até a base.
sidebar:
  label: 3 · Módulos
  order: 3
fontes:
  - source/source/gameengine/CMakeLists.txt
  - source/source/gameengine/Network/CMakeLists.txt
  - source/source/gameengine/Ketsji/KX_NetworkManager.cpp
conferido: 3ec78347
---

<div class="ae-x">
<span class="ae-x-eyebrow">Parada 3 de 5</span>
<div class="ae-x-stack">
<div class="ae-x-layer"><span class="ae-x-eyebrow">Entrada</span>
<div class="ae-x-chips">
<span class="ae-x-chip"><b>GamePlayer</b><code>AnastacioRuntime</code></span>
<span class="ae-x-chip"><b>BlenderRoutines</b><code>Play no editor</code></span>
<span class="ae-x-chip"><b>Launcher</b><code>LA_Launcher</code></span>
</div>
</div>
<p class="ae-x-down">dirige ↓</p>
<div class="ae-x-layer hot"><span class="ae-x-eyebrow">Maestro</span>
<div class="ae-x-chips">
<a class="ae-x-chip" href="/anastacio-docs/por-dentro/frame/"><b>Ketsji</b><code>KX_KetsjiEngine, KX_Scene, KX_GameObject, API Python, ImGui</code></a>
</div>
</div>
<p class="ae-x-down">usa ↓</p>
<div class="ae-x-layer"><span class="ae-x-eyebrow">Sistemas</span>
<div class="ae-x-chips">
<a class="ae-x-chip" href="/anastacio-docs/por-dentro/editor-para-jogo/"><b>Converter</b><code>.range → objetos</code></a>
<span class="ae-x-chip"><b>GameLogic</b><code>sensores, controladores, atuadores</code></span>
<span class="ae-x-chip"><b>Physics</b><code>Bullet</code></span>
<span class="ae-x-chip"><b>Rasterizer</b><code>OpenGL / WebGL2, filtros 2D</code></span>
<a class="ae-x-chip novo" href="/anastacio-docs/guias/multiplayer/"><b>Network</b><code>sessão, réplica, ENet, Steam, WebSocket</code></a>
<span class="ae-x-chip"><b>VideoTexture</b><code>bge.texture</code></span>
</div>
</div>
<p class="ae-x-down">apoiados em ↓</p>
<div class="ae-x-layer"><span class="ae-x-eyebrow">Base</span>
<div class="ae-x-chips">
<span class="ae-x-chip"><b>SceneGraph</b><code>SG_Node, hierarquia</code></span>
<span class="ae-x-chip"><b>Device</b><code>teclado, mouse, joystick</code></span>
<span class="ae-x-chip"><b>Expressions</b><code>valores, ponte C++/Python</code></span>
<span class="ae-x-chip"><b>Common</b><code>clock, log, refcount</code></span>
</div>
</div>
</div>
<p class="ae-x-cap">As camadas mostram papéis, de cima (quem manda) para baixo (quem serve). No código real os <code>#include</code> cruzam camadas em várias direções, herança do BGE, então leia como mapa de responsabilidades e não como regra de dependência.</p>
</div>

## O que cada um faz

- **Ketsji** é o maior módulo: guarda as cenas e os objetos, expõe a API Python (`Range.*`, `bge.*`) e contém o loop principal.
- **Converter** só trabalha quando uma cena ou objeto é carregado.
- **GameLogic** avalia os Logic Bricks a cada frame, inclusive os que a Logic Tree gerou.
- **Network** é o multiplayer nativo. Ele entra no loop por `KX_NetworkManager`: aplica o que chegou antes do passo e envia o estado depois. Guia: [Multiplayer](/anastacio-docs/guias/multiplayer/).
- **Rasterizer** desenha em OpenGL no desktop e em WebGL2 no navegador, com os mesmos filtros 2D.

<div><a class="ae-x ae-x-next" href="/anastacio-docs/por-dentro/frame/"><div><span class="ae-x-eyebrow">Próxima parada</span><strong>4 · Um frame do jogo</strong></div><span class="ae-x-go">abrir →</span></a></div>
