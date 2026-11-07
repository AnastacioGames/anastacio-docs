---
title: "EXP_Value"
description: "Referência da classe Range.types.EXP_Value"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Esta classe é a base de outras classes.

```python
# Todo valor com nome tem o atributo name.
import Range

cont = Range.logic.getCurrentController()

print(cont.owner.name)
print(cont.name)
```

### name

O nome deste objeto derivado de EXP_Value (somente leitura).

**Tipo:** string

