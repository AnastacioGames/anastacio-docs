---
title: "SCA_WaitActuator"
description: "Referência da classe Range.types.SCA_WaitActuator"
---

Classe `Range.types.SCA_WaitActuator`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### duration

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Tempo de espera em segundos (0 a 100000). Ao receber pulso positivo o actuator começa a contar; quando o tempo passa, ele termina e um sensor **Actuator** em modo Finished dispara.

### elapsed

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Segundos já passados desde o início da espera atual.

### useRestart

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Se `True`, um novo pulso positivo durante a espera reinicia a contagem do zero.

### waiting

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

`True` enquanto o actuator está contando.

