---
title: "KX_NetworkMessageSensor"
description: "Referência da classe Range.types.KX_NetworkMessageSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



O logic brick do sensor Message.

Por enquanto só redes loopback (locais) são suportadas.

### subject

O assunto que o sensor procura.

**Tipo:** string

### frameMessageCount

O número de mensagens recebidas desde o último frame (somente leitura).

**Tipo:** integer

### subjects

A lista dos assuntos das mensagens recebidas (somente leitura).

**Tipo:** list of strings

### bodies

A lista dos corpos das mensagens recebidas (somente leitura).

**Tipo:** list of strings

