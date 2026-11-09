---
title: Rec Play (grave cenas jogando)
description: Grave atores em Takes enquanto joga, em camadas, e use o resultado em cutscenes, vídeo ou Python.
---

O **Rec Play** grava o que acontece enquanto você joga. Cada gravação vira um **Take**, com a pose de cada ator. Depois, o Take pode virar vídeo, entrar numa cutscene ou tocar por script.

## Gravar no Rec Studio

1. Abra **Window > Rec Studio**. Se você não tem biblioteca própria, ele abre num kit com 3 personagens, 6 ações e 4 cenários.
2. Em **Scenery**, arraste um cenário para a cena.
3. Em **Characters**, arraste um personagem. Ele já vira ator.
4. Em **Actions**, arraste uma ação sobre o ator.
5. Clique em **Record**, mova o ator e pare com **F10**. O Take aparece na lista.

## Botões

| Botão | O que faz |
|---|---|
| **Watch** | Toca todos os Takes no jogo, sem gravar. |
| **Rerecord** | Grava de novo os atores do Take selecionado e o substitui. |
| **Undo** | Desfaz a última gravação. |
| **Movie** | Toca os Takes e salva o vídeo com som na pasta do arquivo. |

## Gravar em camadas

Ao gravar, quem não está marcado repete o Take mais recente dele. Assim, dá para gravar um ator de cada vez. **Play Other Takes** liga essa repetição, e **Collide on Replay** define se os atores repetidos colidem.

## Levar para a cutscene

1. Na aba **Render**, abra **Motion Recording (Experimental)**.
2. Selecione o Take e clique em **Add to Cutscene**. A gravação não cria o evento sozinha.
3. Em **Cutscene Sequences**, aparece um evento Play Take. Renomear o Take atualiza o evento.

## Tocar por Python

```python
import Range

scene = Range.logic.getCurrentScene()
door = scene.objects["Door"]
if not door.is_playing_take():
    door.play_take("Take 1")
```

`scene.takes` lista os nomes, `scene.play_take(nome)` toca todos os atores, e `obj.stop_take()` para no ponto atual. Enquanto toca, o ator fica sem lógica e sem física; as duas voltam no fim. Veja [`KX_Scene`](../../api/types/kx_scene/) / [`KX_GameObject`](../../api/types/kx_gameobject/).

:::note
A pose por osso ainda não é gravada, então IK e scripts que mexem em ossos não entram no Take. O corpo e as Actions entram.
:::
