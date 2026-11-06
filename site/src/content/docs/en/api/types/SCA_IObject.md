---
title: "SCA_IObject"
description: "Range.types.SCA_IObject class reference"
---

Base class: [`EXP_Value`](../exp_value/)



This class has no python functions

```python

# Every game object is also a SCA_IObject.
import Range

obj = Range.logic.getCurrentController().owner
print(isinstance(obj, Range.types.SCA_IObject))
```

