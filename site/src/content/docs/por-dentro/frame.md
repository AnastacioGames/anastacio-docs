---
title: Um frame do jogo
description: O que a engine faz, em ordem, a cada frame.
sidebar:
  label: 4 · Um frame
  order: 4
---

<div class="ae-x">
<span class="ae-x-eyebrow">Parada 4 de 5</span>
<p class="ae-x-cap">Os três caminhos de entrada (player, Play no editor e navegador) chegam ao mesmo <code>LA_Launcher::EngineNextFrame()</code>. No desktop um laço chama cada frame; na Web quem chama é o navegador, um frame por vez.</p>
<div class="ae-x-lanes">
<div class="ae-x-lane">
<span class="ae-x-eyebrow">Trilha A</span>
<span class="ae-x-title">NextFrame()</span>
<ol class="ae-x-steps">
<li>ImGui e eventos de joystick</li>
<li>Roda a simulação<small>trilha B, uma vez por frame</small></li>
<li>Limpa input e mensagens</li>
<li>Carrega e libera libs, troca de cena<small>KX_SceneScheduler</small></li>
<li>Decide se desenha<small>m_doRender</small></li>
</ol>
<span class="ae-x-go">KX_KetsjiEngine.cpp</span>
</div>
<div class="ae-x-lane hot">
<span class="ae-x-eyebrow">Trilha B · para cada cena</span>
<span class="ae-x-title">Simulação</span>
<ol class="ae-x-steps"><i class="ae-x-pulse" aria-hidden="true"></i>
<li class="opt novo">Rede: aplica o que chegou<small>só com sessão multiplayer</small></li>
<li>Atividade dos objetos</li>
<li>Animações e deformação</li>
<li>Cutscene e seus eventos</li>
<li>Lógica: sensores e controladores</li>
<li>Atuadores</li>
<li>Terremoto e física Bullet</li>
<li class="novo">Trilho do Range Trace, LOD/HLOD, sol automático</li>
<li>Hierarquia e Game FX da câmera</li>
<li class="novo">Partículas GPU, chuva, raios, flicker das luzes</li>
<li class="opt novo">Rede: servidor envia o estado<small>só com sessão multiplayer</small></li>
</ol>
<span class="ae-x-go">KX_SimulationPipeline.cpp</span>
</div>
<div class="ae-x-lane">
<span class="ae-x-eyebrow">Trilha C · se m_doRender</span>
<span class="ae-x-title">Render()</span>
<ol class="ae-x-steps">
<li>Começa o frame</li>
<li>Sombras<small>KX_ShadowRenderer</small></li>
<li>Render-to-texture</li>
<li>Cada câmera: culling, LOD/HLOD, céu e desenho<small>Static Batch junta malhas</small></li>
<li>Filtros 2D da cena</li>
<li>ImGui, debug e troca de buffers</li>
</ol>
<span class="ae-x-go">KX_RenderPipeline.cpp</span>
</div>
</div>
<p class="ae-x-legend"><span>sempre roda</span><span class="opt">só em certas condições</span><span class="novo">acrescentado pela Anastacio</span></p>
</div>

## Detalhes que importam

- **A simulação sempre roda; o desenho, não.** Quando o jogo está adiantado, a engine só calcula quanto dormir e pula o render.
- **Passo fixo só com multiplayer.** O acumulador de passo fixo fica desligado. Com uma sessão de rede aberta ele liga sozinho, e cada passo vira um tick de rede.
- **A hierarquia é atualizada várias vezes:** depois da lógica, dos atuadores e da física. A trilha B resume isso numa etapa.
- **Medir cada etapa:** o menu Performance mostra o tempo de cada trecho do frame. Veja [Performance](/anastacio-docs/guias/performance/).

<div><a class="ae-x ae-x-next" href="/anastacio-docs/por-dentro/plataformas/"><div><span class="ae-x-eyebrow">Última parada</span><strong>5 · Plataformas</strong></div><span class="ae-x-go">abrir →</span></a></div>
