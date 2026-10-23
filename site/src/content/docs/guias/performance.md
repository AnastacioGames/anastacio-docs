---
title: Menu Performance (relatório e otimização)
description: Meça o jogo com um clique e receba um relatório visual dizendo o que pesa e o que fazer. Inclui Scene Doctor, LODs, colisão e preparo para exportar.
---

O botão **Performance**, na barra de cima ao lado de **Game**, junta as ferramentas para descobrir o que deixa o jogo lento e corrigir. Funciona em qualquer jogo, sem instalar nada.

## Performance Report

1. Clique em **Performance > Measure**.
2. O jogo abre no `AnastacioRuntime` com a gravação ligada. Jogue normalmente pelas partes que quer medir.
3. Feche o jogo. O relatório (`report.html`) abre sozinho no navegador.

Se a cena tiver mudanças não salvas, a engine roda uma cópia temporária e apaga no fim. Seu arquivo não é alterado.

**Last** reabre o último relatório e **Folder** abre a pasta com todos eles.

### O que tem no relatório

- **Veredito no topo**: roda liso, vale olhar ou precisa de ajustes.
- **Cartões coloridos** (verde, amarelo, vermelho) com os números principais.
- **O que fazer**: recomendações automáticas a partir do que foi medido.
- **Comparação** com o relatório anterior do mesmo jogo, para ver se a mudança ajudou.
- **Gráfico do frame** com os picos marcados, junto com as cenas e os sons de cada momento.
- **Onde vai o tempo** de cada frame: lógica, física, render e outros.
- **Scripts**: tempo de cada componente Python (por classe) e de cada controller Python (por script).
- **Picos**: o script mais pesado e o que estava carregando em cada travada.
- **Memória** do processo a cada segundo.
- **Cargas durante o jogo**, **shaders** compilados e **carregamento por cena**.
- **Carregado mas nunca desenhado**: o que ocupa memória sem aparecer.
- **Sons** iniciados (Sound actuator, speaker, World Sound) e contadores por frame.

A abertura do jogo (até 60 frames seguidos sem pico) aparece separada no topo e não entra nos números.

O relatório tem tema claro e escuro (segue o sistema, com botão no canto) e sai no idioma da interface do editor.

:::tip
Meça, mude uma coisa e meça de novo. A seção de comparação mostra na hora se ficou melhor ou pior.
:::

## Scene Doctor

**Performance > Scene Doctor** analisa a cena aberta sem rodar o jogo e lista o que custa carregamento, memória ou tempo de frame. Vários itens têm correção com um clique, como gerar LODs para malhas pesadas ou trocar colisão estática densa por um proxy.

## Otimizar a cena

- **Generate LODs**: cria níveis de detalhe em lote, com as distâncias calculadas pelo tamanho de cada objeto. O **X** ao lado remove os LODs gerados.
- **Collision Proxies**: cria colisão simplificada para cenário estático denso. O **X** remove.

## Preparar para exportar

- **Textures (DDS)**: prepara as texturas em DDS BC1/BC3 para o jogo exportado no desktop. A seta desfaz.
- **Audio (OGG)**: prepara os sons em OGG para o pacote exportado.

Os originais ficam intactos; as versões preparadas são usadas só na exportação.
