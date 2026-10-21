---
title: Logic Editor
description: A janela dos logic bricks. Cada painel em poucas linhas, com destaque para o que é novo na Anastacio.
---

O Logic Editor é onde você monta a lógica do jogo com **sensores**, **controladores** e **atuadores**, sem escrever código. Abaixo, cada parte da janela em poucas linhas. O selo **Novo** marca o que não existe na Range original.

<!-- PRINT: Logic Editor inteiro, com a barra lateral aberta -->

## Barra superior

### Highlight Active <span class="ae-badge novo">Novo</span>
Com o jogo rodando, acende os bricks que estão disparando naquele momento. Assim dá para ver a lógica funcionando ao vivo e achar o brick que não reage.

### Convert to Python <span class="ae-badge novo">Novo</span>
Transforma os bricks do objeto num script Python (Smart Component). Bom ponto de partida quando a lógica cresce demais para ser feita só com bricks. Veja [Smart Components](/anastacio-docs/guias/smart-components/).

### Add
Menu para criar sensores, controladores e atuadores.

## Barra lateral (tecla N)

### Properties
As variáveis do objeto (Game Properties): nome, tipo e valor. O botão **i** mostra o valor na tela durante o jogo. Em objetos de texto, aparece um atalho para a propriedade **Text**, que define o texto exibido.

### Brick Groups <span class="ae-badge novo">Novo</span>
Organiza os bricks em grupos com nome, como "Movimento" ou "Tiro". Renomear um grupo com clique duplo renomeia também os bricks que estão nele. Se algum brick usa um grupo que ainda não está na lista, o botão **Add Groups Used by Bricks** cria esse grupo.

### States
Os 30 estados do objeto. **Visible** mostra ou esconde os bricks de cada estado, e **Initial** escolhe com quais estados o jogo começa. Dá para dar um nome a cada estado.

### Brick Inspector <span class="ae-badge novo">Novo</span>
Confere os bricks do objeto e aponta erros antes de você dar Play: tecla não escolhida, script vazio, brick sem ligação, sensor com alcance zero e outros.

- **Viewport (Off / Selected / All):** desenha na viewport o alcance de Near, Radar e Ray, além do alvo de Steering e Track To.
- **Show Tips:** mostra também as dicas leves. Desligado, o painel mostra só erros e avisos.
- **Other objects with problems:** lista outros objetos da cena com problemas. Clicar no nome leva até o objeto.

<!-- PRINT: Brick Inspector mostrando um erro -->
