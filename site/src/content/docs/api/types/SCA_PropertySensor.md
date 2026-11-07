---
title: "SCA_PropertySensor"
description: "Referência da classe Range.types.SCA_PropertySensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



Ativa quando a propriedade do game object corresponde.

```python
# Dispara quando a propriedade life chega a zero.
import Range

sensor = Range.logic.getCurrentController().sensors["Property"]

sensor.mode = Range.logic.KX_PROPSENSOR_EQUAL
sensor.propName = "life"
sensor.value = "0"
```

```python
# Dispara quando o valor está dentro de um intervalo.
import Range

sensor = Range.logic.getCurrentController().sensors["Property"]

sensor.mode = Range.logic.KX_PROPSENSOR_INTERVAL
sensor.propName = "life"
sensor.min = "1"
sensor.max = "20"
```

### mode

Tipo de verificação da propriedade. Pode ser uma `destas constantes`

**Tipo:** integer.

### propName

a propriedade com que o sensor opera.

**Tipo:** string

### value

o valor que o sensor compara com o valor da propriedade.

**Tipo:** string

### min

o valor mínimo do intervalo usado para avaliar a propriedade no modo interval.

**Tipo:** string

### max

o valor máximo do intervalo usado para avaliar a propriedade no modo interval.

**Tipo:** string

