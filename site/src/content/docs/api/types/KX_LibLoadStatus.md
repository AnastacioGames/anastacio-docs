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

```python

# Tela de carregamento: mostra o progresso. Rode update a cada frame (sensor Always com True Pulse).
import Range

status = Range.logic.LibLoad("//level2.range", "Scene", asynchronous=True)

def update(cont):
    cont.owner.text = "Loading %d%%" % (status.progress * 100)

    if status.finished:
        cont.owner.text = "Ready"
```

```python

# Adiciona um objeto assim que o arquivo dele termina de carregar.
import Range

def finished(status):
    print(status.libraryName, status.timeTaken)
    Range.logic.getCurrentScene().addObject("Enemy")

status = Range.logic.LibLoad("//enemies.range", "Scene", asynchronous=True)
status.onFinish = finished
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

