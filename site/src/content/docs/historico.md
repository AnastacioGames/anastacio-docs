---
title: O que já foi feito
description: Tudo que a Anastacio Engine ganhou desde o fork da Range Engine 1.6, mês a mês.
sidebar:
  label: O que já foi feito
---

<div class="ae-h-hero">
<span class="ae-h-eyebrow">Diário de bordo · ago → out 2026</span>
<p class="ae-h-lead">Cada linha abaixo saiu do diário técnico da engine. Aqui está a versão curta: o que mudou para quem faz jogos.</p>
<dl class="ae-h-odo">
<div><dt>entradas no diário</dt><dd>716</dd></div>
<div><dt>versões publicadas</dt><dd>13</dd></div>
<div><dt>plataformas</dt><dd>4</dd></div>
</dl>
</div>

<section class="ae-h-month">
<header><span class="ae-h-num">08</span><div><h2>Agosto</h2><p>A base: mais rápido e com partículas novas</p></div></header>
<div class="ae-h-grid">
<article><h3>Desempenho</h3><ul>
<li>Personagens animados calculados na placa de vídeo (GPU Skinning).</li>
<li>Folhagem recortada desenha mais rápido: 28 → 21 ms por quadro no teste.</li>
<li>Árvores distantes viram impostores (uma imagem plana) automaticamente.</li>
</ul></article>
<article><h3>Efeitos</h3><ul>
<li>Sistema de partículas na GPU: fogo, fumaça, poeira e faíscas prontos.</li>
<li>Primeiros filtros de tela (escala de cinza, negativo, sépia).</li>
</ul></article>
<article><h3>Editor</h3><ul>
<li>Escolha entre os ícones da Range e da UPBGE.</li>
<li>Menus em ImGui organizados como componentes.</li>
</ul></article>
</div>
</section>

<section class="ae-h-month">
<header><span class="ae-h-num">09</span><div><h2>Setembro</h2><p>A engine sai do Windows</p></div></header>
<div class="ae-h-grid">
<article><h3>Web e celular</h3><ul>
<li>O jogo roda no navegador: luzes, sombras, filtros, som, save e Python.</li>
<li>Validação e "Abrir no navegador" direto do editor.</li>
<li>Exporte para Android (APK e AAB), com controles na tela e sensores de movimento.</li>
</ul></article>
<article><h3>Linux</h3><ul>
<li>Editor e player nativos, com pacote portátil que roda em várias distros.</li>
<li>Cycles com placas NVIDIA (CUDA) e AMD (OpenCL).</li>
</ul></article>
<article><h3>Jogo</h3><ul>
<li>Cutscenes nativas com linha do tempo.</li>
<li>Destruição e explosões, câmera com foco e tremor, chuva e nuvens no World.</li>
<li>Áreas de eco (Reverb Area), eventos de animação e navmesh que desvia de obstáculos.</li>
<li>Scripts antigos de BGE/UPBGE rodam sem mudar os imports.</li>
</ul></article>
<article><h3>Editor</h3><ul>
<li>Barra flutuante na 3D View, coleções no Outliner e Asset Browser.</li>
<li>Interface em English, Português, Español e Русский.</li>
<li>Logic Bricks viram Python com um botão.</li>
</ul></article>
<article><h3>Por dentro</h3><ul>
<li>O núcleo do jogo foi reorganizado em 11 etapas, com medidores de desempenho.</li>
<li>Passo de física fixo opcional, para o jogo andar igual em qualquer FPS.</li>
</ul></article>
</div>
<p class="ae-h-rel">Versões 0.3.0 a 0.4.6</p>
</section>

<section class="ae-h-month">
<header><span class="ae-h-num">10</span><div><h2>Outubro</h2><p>Gráficos novos, lógica sem código e multiplayer</p></div></header>
<div class="ae-h-grid">
<article><h3>Gráficos</h3><ul>
<li>Os nós de material do Cycles funcionam no jogo: vidro, cabelo, volume, céu.</li>
<li>Reflexos (probes e espelho planar), sombra colorida de vitral e sombras em cascata.</li>
<li>Sombra de sol com cascatas (CSM) e sombras suaves com penumbra (PCSS).</li>
<li>Efeitos de pós-processo no jogo: Directional Blur, Color Correction, Tonemap, Glare, Crop e outros.</li>
<li>Nuvens volumétricas, névoa volumétrica e iluminação indireta (bake e SSGI).</li>
<li>Shaders por nós com vento, ondas, pelo e contorno toon.</li>
</ul></article>
<article><h3>Carregamento</h3><ul>
<li>Arquivo "cozido" (<code>.cooked</code>): física, shaders e malhas já prontos ao abrir.</li>
<li>Tela de loading com progresso real e texturas DDS comprimidas.</li>
<li>Escolha o que carrega com a cena e o que carrega só quando precisar.</li>
</ul></article>
<article><h3>Desempenho</h3><ul>
<li>Static Batch: com ele ligado empatamos com a ThunderPlayer no benchmark.</li>
<li>Cerca de 100 pontos de trabalho repetido revisados no motor.</li>
<li>Range Trace, Performance Report e Scene Doctor mostram onde o jogo pesa.</li>
<li>Auto Static Batch, contador de FPS compacto e uma API Python mais barata.</li>
</ul></article>
<article><h3>Lógica sem código</h3><ul>
<li>Logic Bricks 2.0 e Logic Tree: lógica por nós que vira bricks nativos.</li>
<li>Smart Components com assistente, e filtros 2D com campos no painel.</li>
<li>UI Tree: menus e HUD montados no editor de nós.</li>
</ul></article>
<article><h3>Jogo</h3><ul>
<li>Multiplayer nativo (LAN, internet e navegador) e complemento Steam.</li>
<li>World Sound com música, ambiente, chuva e trovão.</li>
<li>VR no celular, ragdoll, amassados por batida e veículos arcade.</li>
<li>Idiomas do jogo e gravação de tela com som.</li>
<li><code>Range.types.TrackLine</code>: pista para a IA de corrida seguir.</li>
</ul></article>
<article><h3>Texto e diálogos</h3><ul>
<li>Text Boxes no jogo: quebra de linha, páginas e efeito de máquina de escrever.</li>
<li>Diálogos sem código: nó Dialogue Box na UI Tree.</li>
</ul></article>
<article><h3>Tempo e estabilidade</h3><ul>
<li>Relógio único com escala de tempo; a cutscene pausa junto com a cena.</li>
<li>Revisão geral de cena, objetos, joystick, LibLoad e multiplayer, com vários travamentos corrigidos.</li>
<li>Exportação: Compile Scripts funciona e o <code>.range</code> aberto não vai mais no pacote.</li>
</ul></article>
</div>
<p class="ae-h-rel">Versões 0.5.0 a 0.5.4</p>
</section>

<p class="ae-h-foot">Quer o detalhe de alguma coisa? O diário completo fica no repositório da engine, em <code>docs/changelog.md</code>. O que ainda falta está no <code>docs/roadmap.md</code>.</p>
