---
title: "KX_InputTable"
description: "Referência da classe Range.types.KX_InputTable"
---

:::tip[Veja também]
[`KX_InputSystem`](../../types/kx_inputsystem/)
:::

Classe `Range.types.KX_InputTable`.

```python
# Usa uma ação sem saber qual tecla está ligada a ela.
import Range

maps = Range.logic.inputSystem.inputMaps
jump = maps["Player"]["Jump"]

if jump.activated:
    print("Jump")
```

```python
# Lê um eixo.
import Range

move = Range.logic.inputSystem.inputMaps["Player"]["Move"]

if move.active:
    print(move.values)
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### activated

 <small>atributo · só leitura</small>

`True` no frame em que a ação acabou de ser acionada.

### active

 <small>atributo · só leitura</small>

`True` enquanto a ação está acionada.

### released

 <small>atributo · só leitura</small>

`True` no frame em que a ação acabou de ser solta.

### values

 <small>atributo · só leitura</small>

Valores atuais da ação: tupla com 1, 2 ou 3 números, conforme o tipo (botão, eixo 2D ou 3D).

