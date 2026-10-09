---
title: "KX_2DFilterOffScreen"
description: "Referência da classe Range.types.KX_2DFilterOffScreen"
---

Classe base: [`EXP_Value`](../exp_value/)



2D filter custom off screen.

### width

The off screen width, -1 if the off screen can be resized dynamically (read-only).

**Tipo:** integer

### height

The off screen height, -1 if the off screen can be resized dynamically (read-only).

**Tipo:** integer

### colorBindCodes

The bind code of the color textures attached to the off screen (read-only).

:::caution
If the off screen can be resized dynamically (`width` of `height` equal to -1), the bind codes may change.
:::

**Tipo:** list of 8 integers

### depthBindCode

The bind code of the depth texture attached to the off screen (read-only).

:::caution
If the off screen can be resized dynamically (`width` of `height` equal to -1), the bind code may change.
:::

**Tipo:** integer

