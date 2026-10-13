---
title: "KX_2DFilterOffScreen"
description: "Range.types.KX_2DFilterOffScreen class reference"
---

Base class: [`EXP_Value`](../exp_value/)



2D filter custom off screen.

### width

The off screen width, -1 if the off screen can be resized dynamically (read-only).

**Type:** integer

### height

The off screen height, -1 if the off screen can be resized dynamically (read-only).

**Type:** integer

### colorBindCodes

The bind code of the color textures attached to the off screen (read-only).

:::caution
If the off screen can be resized dynamically (:data:`width` of :data:`height` equal to -1), the bind codes may change.
:::

**Type:** list of 8 integers

### depthBindCode

The bind code of the depth texture attached to the off screen (read-only).

:::caution
If the off screen can be resized dynamically (:data:`width` of :data:`height` equal to -1), the bind code may change.
:::

**Type:** integer

