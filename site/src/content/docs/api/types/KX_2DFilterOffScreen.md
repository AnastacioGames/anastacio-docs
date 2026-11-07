---
title: "KX_2DFilterOffScreen"
description: "Referência da classe Range.types.KX_2DFilterOffScreen"
---

Classe base: [`EXP_Value`](../exp_value/)



Off screen personalizado de filtro 2D.

```python
# Lê o tamanho da imagem em que um filtro escreve.
import Range

manager = Range.logic.getCurrentScene().filterManager
offScreen = manager.getFilter(0).offScreen

if offScreen is not None:
    print(offScreen.width, offScreen.height)
    print(offScreen.colorBindCodes, offScreen.depthBindCode)
```

### width

A largura do off screen; -1 se o off screen pode ser redimensionado dinamicamente (somente leitura).

**Tipo:** integer

### height

A altura do off screen; -1 se o off screen pode ser redimensionado dinamicamente (somente leitura).

**Tipo:** integer

### colorBindCodes

O bind code das texturas de cor ligadas ao off screen (somente leitura).

:::caution
Se o off screen pode ser redimensionado dinamicamente (`width` ou `height` igual a -1), os bind codes podem mudar.
:::

**Tipo:** list of 8 integers

### depthBindCode

O bind code da textura de profundidade ligada ao off screen (somente leitura).

:::caution
Se o off screen pode ser redimensionado dinamicamente (`width` ou `height` igual a -1), o bind code pode mudar.
:::

**Tipo:** integer

