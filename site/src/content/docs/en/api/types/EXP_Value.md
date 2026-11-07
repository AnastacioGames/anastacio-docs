---
title: "EXP_Value"
description: "Range.types.EXP_Value class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



This class is a basis for other classes.

```python
# Every value with a name has the name attribute.
import Range

cont = Range.logic.getCurrentController()

print(cont.owner.name)
print(cont.name)
```

### name

The name of this EXP_Value derived object (read-only).

**Type:** string

