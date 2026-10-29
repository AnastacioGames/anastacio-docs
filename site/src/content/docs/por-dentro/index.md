---
title: Por dentro da engine
description: O caminho que o seu jogo faz, do editor até a tela, em cinco paradas.
sidebar:
  label: Mapa
  order: 0
fontes:
  - docs/diagramas-arquitetura.md
  - docs/architecture.md
conferido: d17e1b23
---

<div class="ae-x">
<div class="ae-x-plate">
<span class="ae-x-eyebrow">Planta da Anastacio Engine</span>
<h2>Do clique no Play até a imagem na tela</h2>
<p>A engine tem duas metades: o <strong>editor</strong> (Blender 2.79 modificado), onde você monta o jogo, e o <strong>runtime</strong> (Ketsji, herdado do BGE), que roda o jogo. As duas só conversam por um arquivo: o <code>.range</code>. Clique numa parada para ver aquela parte de perto.</p>
<ol class="ae-x-route">
<li><a href="/anastacio-docs/por-dentro/repositorio/"><span class="ae-x-dot">1</span><div><strong>Repositório</strong><span>Onde está cada coisa</span></div></a></li>
<li><a href="/anastacio-docs/por-dentro/editor-para-jogo/"><span class="ae-x-dot">2</span><div><strong>Editor → jogo</strong><span>Painel, RNA, DNA, conversor</span></div></a></li>
<li><a href="/anastacio-docs/por-dentro/modulos/"><span class="ae-x-dot">3</span><div><strong>Módulos</strong><span>As peças do runtime</span></div></a></li>
<li><a href="/anastacio-docs/por-dentro/frame/"><span class="ae-x-dot">4</span><div><strong>Um frame</strong><span>Simulação e render</span></div></a></li>
<li><a href="/anastacio-docs/por-dentro/plataformas/"><span class="ae-x-dot">5</span><div><strong>Plataformas</strong><span>Windows, Linux, Web, Android</span></div></a></li>
</ol>
</div>
<p class="ae-x-cap">O pulso dourado segue a ordem em que um jogo nasce: o código-fonte vira editor, o editor grava a cena, o conversor monta os objetos, o loop roda frame a frame e o mesmo código é compilado para cada plataforma.</p>
</div>

## Em uma frase cada

- **Editor e runtime são dois programas.** `AnastacioEngine.exe` é o editor; `AnastacioRuntime.exe` é o player que vai junto com o jogo exportado. O botão Play do editor roda o mesmo runtime dentro da janela.
- **O jogo nunca lê o editor.** Tudo o que você configura num painel é gravado no `.range` e convertido em objetos de jogo quando a cena abre.
- **Lógica por nós vira lógica nativa.** A Logic Tree compila em Logic Bricks e a UI Tree grava um texto que o runtime lê. Nenhuma das duas cria um formato que o jogo precise entender à parte.
- **Cada frame tem duas metades.** Primeiro a simulação (lógica, física, rede, partículas), depois o desenho (sombras, câmeras, filtros 2D).
- **Um código, quatro destinos.** Windows e Linux compilam o editor e o player; a Web compila só o player em WebAssembly; o Android leva o pacote Web dentro de um app.

<div><a class="ae-x ae-x-next" href="/anastacio-docs/por-dentro/repositorio/"><div><span class="ae-x-eyebrow">Começar pela parada 1</span><strong>Repositório</strong></div><span class="ae-x-go">abrir →</span></a></div>
