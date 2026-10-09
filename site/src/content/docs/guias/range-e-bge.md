---
title: Range e bge
description: Os dois nomes do módulo principal e por que Range tem R maiúsculo.
---

A API da engine fica no módulo **`Range`**, com **R maiúsculo**. A Range Engine escolheu a maiúscula para não confundir com a função `range()` do Python.

```python
import Range
from Range import logic, events
```

O nome antigo **`bge`** também funciona. A engine registra cada submódulo nos dois nomes, então `Range.logic` e `bge.logic` são o mesmo objeto:

```python
import bge
from bge import logic
```

Esta documentação usa `Range` em todos os exemplos.

| Range | bge |
|---|---|
| `Range.logic` | `bge.logic` |
| `Range.types` | `bge.types` |
| `Range.render` | `bge.render` |
| `Range.events` | `bge.events` |
| `Range.constraints` | `bge.constraints` |
| `Range.application` | `bge.application` |
| `Range.texture` | `bge.texture` |
| `Range.imgui` | `bge.imgui` |
| `Range.network` | `bge.network` |

:::caution[Exportação para Web]
O validador Web avisa `WEB-PY-001` quando encontra `import bge` e sugere trocar por `import Range`.
:::
