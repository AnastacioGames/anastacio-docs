---
title: Minimap
description: Crie um minimapa no HUD com um comando, com radar, mapa inteiro ou GPS 3D, e marque jogadores e itens.
---

O **Minimap** é um nó do HUD na [UI Tree](../ui-tree/). Ele não redesenha a cena: mostra uma imagem do mapa, por isso custa pouco.

## Criar com um comando

1. Salve o `.range`. **Add > Minimap** com Bake e **Bake Map Image** recusam cena nunca salva.
2. Na 3D View, selecione o jogador e use **Add > Minimap**.
3. Escolha o estilo: **Radar** (círculo que gira), **Whole Map** (quadrado parado) ou **GPS 3D** (retângulo inclinado).

O comando cria o HUD, o nó que segue o objeto, a foto do mapa e a lógica da UI.

## Marcar objetos

Selecione o objeto e abra a aba **Object**, painel **Minimap**. Ligue **Show on Minimap**. **Own Color** dá uma cor própria; sem ela, vale a cor **Markers** do nó.

Por script, a cor fica em `minimap_color`, no formato `#rrggbb`:

```python
own["minimap_color"] = "#ff3030"
```

Sem o painel, use a propriedade de jogo `minimap` ou o **Marker Prefix** no nome do objeto. Marcadores fora da área ficam presos na borda.

## Ajustes do nó

| Opção | O que faz |
|---|---|
| **World Min / Max** | Área do mundo coberta pela imagem. **Fit to Scene** mede sozinho. |
| **Zoom Radius** | `0` mostra o mapa inteiro parado; maior que 0 segue o jogador. |
| **Rotate with Player** | Gira o mapa com o jogador. |
| **Camera Tilt** | Inclina a vista de 0 a 60°, como um GPS 3D. |
| **Shape** | Circle, Square, Rectangle ou Ellipse. |
| **Border Style** | None, Solid ou Soft. |

**Bake Map Image** tira uma foto de cima das malhas visíveis, salva `<arquivo>_minimap.png` ao lado do `.range` e acerta World Min/Max.
