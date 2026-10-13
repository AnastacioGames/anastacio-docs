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

| Range | bge | Para que serve |
|---|---|---|
| `Range.logic` | `bge.logic` | Cena, objetos, tempo, propriedades globais e carregamento de arquivos |
| `Range.types` | `bge.types` | Classes dos objetos do jogo: objetos, câmeras, luzes, sensores, atuadores |
| `Range.render` | `bge.render` | Janela, resolução, VSync, cursor do mouse e desenho de debug |
| `Range.events` | `bge.events` | Constantes de teclas, botões do mouse e estados de entrada |
| `Range.constraints` | `bge.constraints` | Juntas físicas, veículos e configurações do motor de física |
| `Range.application` | `bge.application` | Informações da aplicação, como versão e plataforma |
| `Range.texture` | `bge.texture` | Texturas dinâmicas: vídeo, imagem, câmera e render para textura |
| `Range.imgui` | `bge.imgui` | Janelas e controles de interface para depuração |
| `Range.network` | `bge.network` | Multiplayer: conexão, mensagens e replicação de objetos |

:::caution[Exportação para Web]
O validador Web avisa `WEB-PY-001` quando encontra `import bge` e sugere trocar por `import Range`.
:::
