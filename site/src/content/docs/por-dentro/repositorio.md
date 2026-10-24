---
title: Repositório
description: Onde fica cada parte da engine no código-fonte.
sidebar:
  label: 1 · Repositório
  order: 1
---

<div class="ae-x">
<span class="ae-x-eyebrow">Parada 1 de 5</span>
<pre class="ae-x-tree"><b>AnastacioEngine/</b>
├─ <b>source/</b>                     <em>raiz do CMake e dos presets</em>
│  ├─ <b>source/</b>
│  │  ├─ gameengine/            <em>runtime do jogo (Ketsji)</em>
│  │  ├─ blender/               <em>editor herdado do Blender 2.79</em>
│  │  ├─ creator/               <em>main() do editor → AnastacioEngine.exe</em>
│  │  └─ blenderplayer/         <em>player → AnastacioRuntime.exe</em>
│  ├─ intern/                   <em>cycles, ghost (janela), audaspace (som)</em>
│  ├─ extern/                   <em>Bullet, ImGui, Recast, SDL2</em>
│  └─ release/
│     ├─ scripts/startup/       <em>painéis, operadores, Logic Tree, UI Tree</em>
│     ├─ scripts/modules/       <em>range_web, range_locale, range_ui_runtime</em>
│     └─ datafiles/             <em>startup.blend, splash, ícones</em>
├─ <b>tools/</b>                      <em>web, android, linux, debug, modelagem</em>
├─ <b>docs/</b>                       <em>documentação técnica</em>
└─ build*/                    <em>saída dos builds (fora do git)</em></pre>
<p class="ae-x-cap">O jogo roda a partir de <code>gameengine/</code>. Quase toda a interface do editor é Python, em <code>release/scripts/</code>, por isso muita coisa nova (Logic Tree, UI Tree, idiomas, export Web) nasce lá sem tocar em C++.</p>
</div>

## Por onde começar a ler

| Quero mexer em… | Comece por |
|---|---|
| Um painel ou botão do editor | `release/scripts/startup/bl_ui/` |
| Uma propriedade nova salva no arquivo | `blender/makesdna/` e `blender/makesrna/` |
| Como um objeto vira objeto de jogo | `gameengine/Converter/` |
| O loop do jogo, cenas e objetos | `gameengine/Ketsji/` |
| Rede | `gameengine/Network/` |
| Shaders dos materiais | `blender/gpu/shaders/` |

Os executáveis se chamam `AnastacioEngine` e `AnastacioRuntime`, mas os alvos de build continuam `RangeEngine` e `RangeRuntime`, herança da Range Engine.

<div><a class="ae-x ae-x-next" href="/anastacio-docs/por-dentro/editor-para-jogo/"><div><span class="ae-x-eyebrow">Próxima parada</span><strong>2 · Editor → jogo</strong></div><span class="ae-x-go">abrir →</span></a></div>
