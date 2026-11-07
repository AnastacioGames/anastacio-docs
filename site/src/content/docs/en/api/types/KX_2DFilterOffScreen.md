---
title: "KX_2DFilterOffScreen"
description: "Range.types.KX_2DFilterOffScreen class reference"
---

Base class: [`EXP_Value`](../exp_value/)



2D filter custom off screen.

```python
# Read the size of the image a filter writes to.
import Range

manager = Range.logic.getCurrentScene().filterManager
offScreen = manager.getFilter(0).offScreen

if offScreen is not None:
    print(offScreen.width, offScreen.height)
    print(offScreen.colorBindCodes, offScreen.depthBindCode)
```

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

