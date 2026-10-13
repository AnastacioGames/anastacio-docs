---
title: Carregamento rápido (Load Mode e Cook)
description: Deixar objetos de fora do carregamento, criá-los só quando precisar e cozinhar a cena para abrir mais rápido.
---

Uma cena grande demora para abrir porque a engine converte todos os objetos antes do primeiro quadro. A Anastacio tem duas ferramentas para isso:

- **Load Mode**: escolhe quais objetos entram no carregamento e quais ficam para depois.
- **Cook**: guarda num arquivo `.cooked` o que a conversão calcula (física, malhas, shaders), para não calcular de novo.

## Load Mode

Selecione um objeto e abra **Properties > Object**, painel **Load Object with Scene**. São três modos:

| Modo | O que acontece |
|---|---|
| **With Scene** | Padrão. O objeto é criado junto com a cena. |
| **On Demand** | Fica de fora no carregamento. É criado quando um script pede ou quando um Add Object o usa pela primeira vez. |
| **Editor Only** | Nunca vai para o jogo. Bom para objetos de referência, câmeras de trabalho, blocagem. |

O modo vale para os objetos selecionados e seus filhos.

<!-- PRINT: painel Load Object with Scene com On Demand selecionado -->

### Criar um objeto On Demand pelo script

```python
import Range

cena = Range.logic.getCurrentScene()
chefe = cena.convertObject("Chefe")
```

Se `Chefe` estiver numa camada ativa, ele aparece na cena. Se estiver numa camada inativa, vai para `objectsInactive` e fica pronto para `addObject`:

```python
cena.convertObject("Tiro")
tiro = cena.addObject("Tiro", cena.objects["Arma"], 120)
```

`cena.unconvertedObjects` lista os nomes que ainda podem ser criados assim.

### Com Logic Bricks

O atuador **Add Object** já entende On Demand: o objeto é criado na primeira vez que o atuador dispara, e as vezes seguintes só fazem cópias. Não precisa de script.

## Cook

O botão **Cook** fica no painel Render e ao lado do Play no cabeçalho. Ele roda a cena uma vez e grava, ao lado do `.blend`, um arquivo `.cooked` com:

- formas de colisão (Convex Hull e Triangle Mesh) já calculadas;
- buffers de malha, normais e tangentes;
- shaders compilados para a sua placa de vídeo.

Na próxima abertura, a engine lê o arquivo em vez de calcular. Em testes, carregar uma cena caiu de cerca de 2,4 s para menos de 0,5 s.

- O `.blend` precisa estar salvo (sem arquivo salvo o botão fica apagado).
- **Clear Cooked** apaga o cache. Se mudar uma malha, não precisa limpar: a parte mudada é recalculada.
- No jogo exportado, o `.cooked` vai junto. Os shaders são guardados no computador do jogador na primeira abertura, que mostra uma tela de preparação.

<!-- PRINT: botão Cook no cabeçalho -->

## Medir

`Range.logic.getLoadLog()` mostra quanto tempo cada etapa da carga levou. Use antes e depois do Cook para ver o ganho.

```python
import Range

for etapa in Range.logic.getLoadLog():
    print(etapa)
```
