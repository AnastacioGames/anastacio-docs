---
title: "KX_LibLoadStatus"
description: "Referência da classe Range.types.KX_LibLoadStatus"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



An object providing information about a LibLoad() operation.

```python

# Print a message when an async LibLoad is done
import Range

def finished_cb(status):
    print("Library (%s) loaded in %.2fms." % (status.libraryName, status.timeTaken))

Range.logic.LibLoad('myblend.blend', 'Scene', asynchronous=True).onFinish = finished_cb
```

### onFinish

A callback that gets called when the lib load is done.

**Tipo:** callable

### finished

The current status of the lib load.

**Tipo:** boolean

### progress

The current progress of the lib load as a normalized value from 0.0 to 1.0.

**Tipo:** float

### libraryName

The name of the library being loaded (the first argument to LibLoad).

**Tipo:** string

### timeTaken

The amount of time, in seconds, the lib load took (0 until the operation is complete).

**Tipo:** float

