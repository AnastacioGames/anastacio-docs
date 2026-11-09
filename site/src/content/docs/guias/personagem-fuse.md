---
title: Personagem automático (Fuse)
description: Transforme um OBJ exportado do Fuse num personagem com esqueleto, LODs e ragdoll, sem usar o Mixamo.
---

A engine transforma o OBJ de um personagem do Fuse num personagem pronto para o jogo, sem passar pelo Mixamo.

## Importar

Abra **File > Import > Fuse Character (.obj)**, escolha o arquivo e ajuste:

| Opção | O que faz |
|---|---|
| **Skeleton** | Esqueleto da biblioteca usado como base. |
| **Name** | Nome do personagem; o grupo se chama `Group<Nome>`. Vazio usa o nome do arquivo. |
| **Ragdoll** | Adiciona caixas de ragdoll nos ossos grandes, sem mãos e dedos. |
| **Output Folder** | Onde ficam `Group<Nome>.range` e `textures/`. Vazio cria uma pasta ao lado do arquivo aberto. |
| **Game Folder** | Raiz do projeto do jogo, para ligar o componente de ragdoll. Vazio usa a pasta do arquivo aberto. |
| **Add to Scene** | Coloca o grupo pronto na cena atual, no cursor 3D. |

O processamento roda em segundo plano e não mexe no arquivo aberto.

## O que sai

- Corpo reduzido a 9000 triângulos no nível 0, preservando cabeça e peito.
- LODs de 2500 triângulos a 10 m e 900 triângulos a 25 m.
- Grupo com armature, corpo e ragdoll, salvo para entrar por `LibLoad`.

:::caution
Confira a licença das malhas do Fuse antes de distribuir o jogo.
:::
