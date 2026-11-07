---
title: "EXP_PyObjectPlus"
description: "Range.types.EXP_PyObjectPlus class reference"
---

EXP_PyObjectPlus base class of most other types in the Game Engine.

```python
# Check that an object was not removed before using a saved reference.
import Range

own = Range.logic.getCurrentController().owner
target = own.get("target")

if target is not None and not target.invalid:
    print(target.worldPosition)
```

### invalid

Test if the object has been freed by the game engine and is no longer valid.

Normally this is not a problem but when storing game engine data in the GameLogic module,
KX_Scenes or other KX_GameObjects its possible to hold a reference to invalid data.
Calling an attribute or method on an invalid object will raise a SystemError.

The invalid attribute allows testing for this case without exception handling.

**Type:** boolean

