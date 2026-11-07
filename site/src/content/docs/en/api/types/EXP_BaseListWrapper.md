---
title: "EXP_BaseListWrapper"
description: "Range.types.EXP_BaseListWrapper class reference"
---

Class `Range.types.EXP_BaseListWrapper`.

```python
# These lists work by name or by index, like sensors or channels.
import Range

armature = Range.logic.getCurrentController().owner

head = armature.channels.get("Head")
first = armature.channels[0]
print(head, first)
```



## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### get(key, default=None)

 <small>method</small>

Item with that name, or `default` if it doesn't exist.

**Returns:** `object`

