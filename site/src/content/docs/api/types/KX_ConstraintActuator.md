---
title: "KX_ConstraintActuator"
description: "Referência da classe Range.types.KX_ConstraintActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Um atuador Constraint limita a posição, rotação, distância ou orientação de um objeto.

### damp

Constante de tempo da constraint, em frames (não usada pela constraint Force field).

**Tipo:** integer

### rotDamp

Constante de tempo da rotação, em frames (só para a constraint de distância); 0 = usa damp também na rotação.

**Tipo:** integer

### direction

A direção de referência, em coordenadas do mundo, da constraint de orientação.

**Tipo:** `mathutils.Vector`

### option

Combinação binária `destas constantes`

**Tipo:** integer

### time

tempo de ativação do atuador. O atuador se desliga depois desse número de frames. Com 0, o atuador não tem limite de tempo.

**Tipo:** integer

### propName

o nome da propriedade ou material para a detecção por raio da constraint de distância.

**Tipo:** string

### min

O limite inferior da constraint. Nas constraints de rotação e orientação, é em radianos.

**Tipo:** float

### distance

a distância alvo da constraint de distância.

**Tipo:** float

### max

o limite superior da constraint. Nas constraints de rotação e orientação, é em radianos.

**Tipo:** float

### rayLength

o comprimento do raio da constraint de distância.

**Tipo:** float

### limit

tipo de constraint. Use uma `destas constantes`

**Tipo:** integer.

