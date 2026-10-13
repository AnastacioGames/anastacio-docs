---
title: Exportar o jogo
description: Como transformar o seu .range num jogo que outras pessoas podem jogar, no PC, no navegador ou no celular.
---

Todas as opções de exportação ficam na mesma aba: **Propriedades > Export Game** (o ícone de caixa, na coluna de abas à direita). Lá há três painéis, um para cada destino.

| Destino | Painel | O que sai | Quando usar |
|---|---|---|---|
| PC (Windows e Linux) | **Export (RangeArmor)** | Pasta `release/` com o executável do jogo | Para distribuir no itch.io, Steam ou num zip |
| Navegador | **Web** | Pasta com `index.html` e o runtime WebGL 2 | Para jogar no site, sem instalar nada |
| Celular Android | **Android (Web)** | Arquivo `.apk` (e `.aab` para a Google Play) | Para instalar no celular ou publicar na loja |

O Android reaproveita o pacote Web: o APK é um app que roda a versão Web do jogo por dentro. Por isso, **tudo que funciona no Web funciona no Android**, e os avisos do Web valem para os dois.

## Antes de exportar, sempre

1. **Salve o arquivo** (`Ctrl+S`). Os três exports usam o `.range` salvo em disco, não o que está aberto na tela.
2. **Teste com P** no editor. Se o jogo não roda no editor, não vai rodar exportado.
3. Use **caminhos relativos** para texturas, sons e scripts (`//textures/...`). Caminho absoluto (`C:\Users\...`) só existe no seu PC.

## Guias

- [Exportar para PC com RangeArmor](../rangearmor/)
- [Exportar para o navegador (Web/WebGL)](../web/)
- [Exportar para Android (APK e chave .jks)](../android/)
