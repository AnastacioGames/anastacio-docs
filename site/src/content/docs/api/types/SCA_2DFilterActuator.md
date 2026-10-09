---
title: "SCA_2DFilterActuator"
description: "Referência da classe Range.types.SCA_2DFilterActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Create, enable and disable 2D filters.

The following properties don't have an immediate effect. You must active the actuator to get the result. The actuator is not persistent: it automatically stops itself after setting up the filter but the filter remains active. To stop a filter you must activate the actuator with 'type' set to `RAS_2DFILTER_DISABLED` or `RAS_2DFILTER_NOFILTER`.

### shaderText

shader source code for custom shader.

**Tipo:** string

### disableMotionBlur

action on motion blur: 0=enable, 1=disable.

**Tipo:** integer

### mode

Type of 2D filter, use one of `these constants`.

**Tipo:** integer

### passNumber

order number of filter in the stack of 2D filters. Filters are executed in increasing order of passNb.

Only be one filter can be defined per passNb.

**Tipo:** integer (0-100)

### value

argument for motion blur filter.

**Tipo:** float (0.0-100.0)

