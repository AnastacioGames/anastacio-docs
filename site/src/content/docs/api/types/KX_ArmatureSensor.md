---
title: "KX_ArmatureSensor"
description: "Referência da classe Range.types.KX_ArmatureSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



O sensor de armature detecta condições em armatures.

```python
# Reage quando o erro do IK fica grande demais.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Armature"]

sensor.type = Range.logic.KX_ARMSENSOR_LIN_ERROR_ABOVE
sensor.value = 0.1

if sensor.positive:
    print("Bone cannot reach the target:", sensor.constraint.name)
```

### type

O tipo de medida que o sensor faz quando está ativo.

Pode ser uma `destas constantes`

**Tipo:** integer.

### constraint

O objeto de constraint que este sensor observa.

**Tipo:** `BL_ArmatureConstraint`

### value

O limite usado na comparação com o erro da constraint. O erro linear só é atualizado em constraints IK CopyPose/Distance com o solver iTaSC. O erro de rotação só é atualizado em constraints IK CopyPose+rotação com o solver iTaSC. O erro linear em CopyPose é sempre >= 0: é a norma da distância entre o alvo e o bone. O erro de rotação em CopyPose é sempre >= 0: é a norma do vetor de rotação equivalente entre as orientações do bone e do alvo. O erro linear em Distance pode ser positivo se a distância entre o bone e o alvo for maior que a desejada, e negativo se for menor.

**Tipo:** float

