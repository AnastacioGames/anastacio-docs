---
title: "KX_LibLoadStatus"
description: "Referência da classe Range.types.KX_LibLoadStatus"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Um objeto com informações sobre uma operação LibLoad().

```python

# Mostra uma mensagem quando um LibLoad assíncrono termina
import Range

def finished_cb(status):
    print("Library (%s) loaded in %.2fms." % (status.libraryName, status.timeTaken))

Range.logic.LibLoad('myblend.blend', 'Scene', asynchronous=True).onFinish = finished_cb
```

### onFinish

Um callback chamado quando o carregamento da lib termina.

**Tipo:** callable

### finished

O status atual do carregamento da lib.

**Tipo:** boolean

### progress

O progresso atual do carregamento da lib, como valor normalizado de 0.0 a 1.0.

**Tipo:** float

### libraryName

O nome da biblioteca sendo carregada (o primeiro argumento de LibLoad).

**Tipo:** string

### timeTaken

O tempo, em segundos, que o carregamento levou (0 até a operação terminar).

**Tipo:** float

