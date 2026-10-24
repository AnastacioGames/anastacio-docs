---
title: Do editor para o jogo
description: Como uma opção marcada num painel chega ao jogo rodando.
sidebar:
  label: 2 · Editor → jogo
  order: 2
fontes:
  - source/release/scripts/startup/range_logic_tree.py
  - source/release/scripts/startup/range_ui_tree.py
  - source/release/scripts/modules/range_ui_runtime.py
  - source/source/gameengine/Converter/BL_BlenderDataConversion.cpp
  - source/source/gameengine/Converter/BL_Converter.cpp
  - source/source/gameengine/Physics/Bullet/CcdCookedData.cpp
  - source/source/blender/blenloader/intern/versioning_range.c
  - source/release/scripts/startup/bl_ui/properties_game.py
conferido: 3ec78347
---

<div class="ae-x">
<span class="ae-x-eyebrow">Parada 2 de 5</span>
<div class="ae-x-flow">
<div class="ae-x-row">
<span class="ae-x-chip"><b>Painel Python</b><code>startup/bl_ui</code></span><i>lê e grava</i>
<span class="ae-x-chip"><b>Propriedade RNA</b><code>makesrna/rna_*.c</code></span><i>aponta para</i>
<span class="ae-x-chip"><b>Struct DNA</b><code>makesdna/DNA_*_types.h</code></span><i>salva</i>
<span class="ae-x-chip"><b>Arquivo .range</b><code>a cena inteira</code></span>
</div>
<div class="ae-x-row side">
<span class="ae-x-eyebrow">Autoria por nós · chega ao mesmo arquivo</span>
<span class="ae-x-chip novo"><b>Logic Tree</b><code>range_logic_tree.py</code></span><i>P, salvar ou Compile</i>
<span class="ae-x-chip"><b>Logic Bricks</b><code>grupo "Tree: nome"</code></span>
</div>
<div class="ae-x-row side">
<span class="ae-x-chip novo"><b>UI Tree</b><code>range_ui_tree.py</code></span><i>Bake UI</i>
<span class="ae-x-chip"><b>Texto ui_tree_data.py</b><code>dentro do .range</code></span>
</div>
<div class="ae-x-row">
<span class="ae-x-chip"><b>Arquivo .range</b><code>ao abrir a cena</code></span><i>converte</i>
<span class="ae-x-chip"><b>Converter</b><code>BL_BlenderDataConversion.cpp</code></span><i>cria</i>
<span class="ae-x-chip"><b>Objetos de jogo</b><code>KX_GameObject, SCA_*, física, GLSL</code></span>
</div>
<div class="ae-x-row side">
<span class="ae-x-eyebrow">Atalho de carregamento</span>
<span class="ae-x-chip novo"><b>.cooked</b><code>colisão, shaders, buffers de malha</code></span><i>o conversor pula esse trabalho</i>
<span class="ae-x-chip"><b>Cena abre mais rápido</b><code>sem .cooked, refaz tudo</code></span>
</div>
</div>
<p class="ae-x-cap">As faixas tracejadas são caminhos extras que terminam no mesmo trilho principal. O runtime nunca vê os nós da Logic Tree, só os bricks que ela gerou; o texto da UI Tree é lido por <code>range_ui_runtime.py</code> durante o jogo.</p>
</div>

## O que isso muda para você

- **Uma opção nova de jogo toca cinco lugares:** painel, RNA, DNA, versioning (para arquivos antigos abrirem certo) e conversor.
- **Opções só do editor param antes do conversor:** Asset Browser, pastas do Outliner, temas e o Scene Doctor não chegam ao jogo.
- **Arquivos antigos** passam pelo versioning (`versioning_range.c`) ao abrir, que preenche os campos novos com valores seguros.
- **Load Mode** decide se um objeto é convertido quando a cena abre ou só quando é chamado. Veja [Load Mode](/anastacio-docs/guias/load-mode/).

<div><a class="ae-x ae-x-next" href="/anastacio-docs/por-dentro/modulos/"><div><span class="ae-x-eyebrow">Próxima parada</span><strong>3 · Módulos do runtime</strong></div><span class="ae-x-go">abrir →</span></a></div>
