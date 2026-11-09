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

### Automatic Occluders

Na aba **Scene**, em **Game Settings > Physics**, caixa **Culling**, embaixo de **Occlusion Culling**, marque **Automatic Occluders**. Paredes, pisos e prédios grandes passam a esconder o que está atrás deles, e a engine deixa de desenhar esses objetos.

- **Escolha sozinha, no carregamento:** malhas paradas (física Static ou No Collision), opacas, com até 2048 triângulos e grandes (o segundo maior lado com pelo menos 1,5 m e a maior face com pelo menos 6 m²). Elas **continuam com colisão**. O tipo de física **Occluder** da aba Physics, ao contrário, tira a colisão do objeto.
- **Liga e desliga sozinha, no jogo:** a cada 30 quadros a engine conta quantos objetos a oclusão está escondendo para a câmera ativa. Em campo aberto, onde ela esconde pouco, fica desligada e não gasta nada; em interiores, liga.
- **Quando vale:** interiores com muitas salas e PCs com GPU fraca. Num prédio de 36 salas com GPU fraca simulada, o tempo de quadro caiu de 5,1 para 3,75 ms. Em PC bom a diferença é pequena, porque o Auto Static Batch já junta os draw calls.
- Vem **desligada**. O **Scene Doctor** sugere ligar quando a cena tem 150 malhas ou mais e pelo menos 8 paredes ou prédios que serviriam.
- Objetos carregados por `LibLoad` não entram na escolha automática.

:::tip[Medir sem limite de FPS]
O jogo sempre segue o FPS de lógica da cena (**Scene > Game Settings > Physics > Steps & Timing > FPS**, 60 por padrão). Desmarcar **Use Frame Rate** (aba Render, **System**) não solta o FPS: essa opção só escolhe como a física avança. Para comparar duas versões pelo tempo de quadro, suba o FPS de lógica numa cópia da cena de teste (por exemplo, 1000) e olhe o tempo de trabalho no Performance Report.
:::

## Scripts mais rápidos

Medido no RolimaRacer com 20 pilotos. Cada chamada da API custa de 0,2 a 0,6 µs só para ir do Python ao C++, e um laço por objeto multiplica isso pelo número de objetos a cada quadro.

- **Calcule uma vez, leia muitas.** Se cada carro precisa de um valor dos outros (faixa, distância na pista), quem é dono calcula no próprio `update()` e guarda; os outros só leem. No Rolima isso cortou metade do custo da IA.
- **Entrada compartilhada.** Teclas de debug ou atalhos lidos em todos os objetos: leia o teclado uma vez por quadro (guarde junto de `Range.logic.getFrameTime()`) e pule o resto quando nada está apertado.
- **Use o que já é nativo.** Contas repetidas sobre listas grandes (seguir uma linha de pista, achar o ponto mais perto) ficam bem mais rápidas em C++. Para IA de corrida existe [`TrackLine`](../../api/types/trackline/): achar o carro na linha cai de ~128 µs para ~3 µs.
- **Prefira `obj.get("x", padrão)`** para ler propriedades, e guarde em variável local o que usa várias vezes no mesmo `update()`.
- **Não faça a cada quadro o que não muda.** Esconder objetos, ler configurações e procurar filhos podem rodar no `start()` ou a cada poucos quadros.

Para achar o script que pesa, use o **Performance Report** acima: ele lista o tempo de cada componente.

## Preparar para exportar

- **Textures (DDS)**: prepara as texturas em DDS BC1/BC3 para o jogo exportado no desktop. A seta desfaz.
- **Audio (OGG)**: prepara os sons em OGG para o pacote exportado.

Os originais ficam intactos; as versões preparadas são usadas só na exportação.

## Web e Android

A GPU do celular é bem mais fraca que a do PC, e efeitos de tela cheia pesam muito mais lá. O menu **Performance** tem uma seção **Web / Android** com estas dicas.

### Sky Quality

O céu **Atmospheric** calcula a atmosfera em cada pixel. No **World**, a opção **Sky Quality** escolhe quanto ele custa:

| Opção | Uso | Medido num celular Android |
|---|---|---|
| **Auto** (padrão) | Low na Web e no Android, High no PC | ~11 ms por frame |
| **High** | céu completo | 41 ms (~24 FPS) |
| **Low** | celular e vídeo integrado | ~11 ms |
| **Very Low** | celular fraco ou cena cheia de efeitos | 3 ms |

### Medir no celular

1. Exporte para Web e rode o `serve.py` do pacote no PC.
2. No celular (mesmo Wi-Fi), abra `http://<IP do PC>:8080/?report=1`. Com cabo USB: `adb reverse tcp:8080 tcp:8080` e abra `http://localhost:8080/?report=1`.
3. Jogue. A cada 10 segundos e ao sair, o celular manda os dados ao PC, que gera `reports/<data>/report.html` na pasta do pacote.

:::tip
Na Web, o tempo que aparece como **Overhead** é o navegador esperando a GPU. Se ele domina, o gargalo são pixels e efeitos, não scripts.
:::
