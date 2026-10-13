---
title: "SCA_ISensor"
description: "Referência da classe Range.types.SCA_ISensor"
---

Classe base: [`SCA_ILogicBrick`](../sca_ilogicbrick/)



Classe base de todos os logic bricks de sensor.

### usePosPulseMode

Flag que liga e desliga o modo de pulso positivo.

**Tipo:** boolean

### useNegPulseMode

Flag que liga e desliga o modo de pulso negativo.

**Tipo:** boolean

### frequency

A frequência dos sensores em modo de pulso. (Obsoleto: use SCA_ISensor.skippedTicks)

**Tipo:** integer

### skippedTicks

Número de ticks de lógica pulados entre 2 pulsos ativos

**Tipo:** integer

### level

level: opção que define se detecta o nível ou a transição de borda ao entrar num estado. Só faz diferença em transições de estado de lógica (atuador State). Um detector de nível gera um pulso na hora, negativo ou positivo conforme a condição do sensor, assim que o estado é ativado. Um detector de borda espera uma mudança de estado antes de gerar um pulso. nota: exclusivo com `tap`; ligar este desliga `tap`.

**Tipo:** boolean

### tap

Quando ligado, só sensores que acabaram de ativar mandam um evento positivo; depois disso os controladores os veem como negativos. Assim, uma tecla segura age como se fosse tocada só por um instante. nota: exclusivo com `level`; ligar este desliga `level`.

**Tipo:** boolean

### invert

Flag que define se este sensor ativa com eventos positivos ou negativos.

**Tipo:** boolean

### triggered

True se este sensor está em estado positivo (somente leitura).

**Tipo:** boolean

### positive

True se este sensor está em estado positivo (somente leitura).

**Tipo:** boolean

### pos_ticks

O número de ticks desde o último pulso positivo (somente leitura).

**Tipo:** int

### neg_ticks

O número de ticks desde o último pulso negativo (somente leitura).

**Tipo:** int

### status

O status do sensor (somente leitura): pode ser uma `destas constantes`.

**Tipo:** int

:::note
Este atributo prático combina os valores dos atributos triggered e positive.
:::

### reset()

Reinicia o estado interno do sensor; o efeito depende do tipo de sensor e das configurações.

O sensor volta ao estado inicial, como se tivesse acabado de ser ativado.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### useDeltaTime

 <small>atributo</small>

Usa o tempo real (delta time) para os intervalos do sensor em vez de contar frames.

