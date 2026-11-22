# SCA_IObject

Base class: [`EXP_Value`](EXP_Value.md)

This class has no python functions

```python

# Every game object is also a SCA_IObject.
import Range

obj = Range.logic.getCurrentController().owner
print(isinstance(obj, Range.types.SCA_IObject))
```
