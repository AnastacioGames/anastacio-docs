---
title: "SCA_DelaySensor"
description: "Referência da classe Range.types.SCA_DelaySensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



O sensor Delay gera disparos positivos e negativos em momentos precisos, contados em frames. O parâmetro delay define a duração do período OFF inicial. Um disparo positivo é gerado no fim desse período.

O parâmetro duration define a duração do período ON que vem depois do OFF. Há um disparo negativo no fim do período ON. Se duration for 0, o sensor fica ON e não há disparo negativo.

O sensor roda o ciclo OFF-ON uma vez, a menos que a opção repeat esteja ligada: aí o ciclo OFF-ON se repete sem parar (ou só o OFF, se duration for 0).

Use `SCA_ISensor.reset` a qualquer momento para reiniciar o sensor.

### delay

duração do período OFF inicial em número de frames; 0 para disparar na hora.

**Tipo:** integer.

### duration

duração do período ON em número de frames, depois do período OFF inicial.

Se duration for maior que 0, um disparo negativo é enviado no fim do pulso ON.

**Tipo:** integer

### repeat

1 se o ciclo OFF-ON deve se repetir sem parar, 0 se deve rodar uma vez.

**Tipo:** integer

### repeatTimes

Número de vezes que o atuador vai repetir.

**Tipo:** integer.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### useDelta

 <small>atributo</small>

Conta o atraso em segundos (tempo real) em vez de frames lógicos.

