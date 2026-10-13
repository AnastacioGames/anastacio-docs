---
title: "BL_ActionActuator"
description: "Referência da classe Range.types.BL_ActionActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)

:::tip[Veja também]
[`KX_GameObject`](../../types/kx_gameobject/), [`BL_ArmatureObject`](../../types/bl_armatureobject/), [`KX_AnimationEventManager`](../../types/kx_animationeventmanager/)
:::



Os atuadores Action aplicam uma action a um ator.

### action

O nome da action a usar como action atual.

**Tipo:** string

### frameStart

Define o frame inicial da animação.

**Tipo:** float

### frameEnd

Define o frame final da animação.

**Tipo:** float

### blendIn

Define o número de frames de animação gerados nas transições entre actions.

**Tipo:** float

### priority

Define a prioridade deste atuador. Atuadores com número de prioridade menor sobrepõem os de número maior.

**Tipo:** integer

### frame

Define o frame atual da animação.

**Tipo:** float

### propName

Define a propriedade usada no modo de reprodução FromProp.

**Tipo:** string

### mode

O modo de operação do atuador. Pode ser uma `destas constantes`.

**Tipo:** integer

### useContinue

A opção continue das actions, True ou False. Com True, a action sempre toca de onde parou; senão, eventos negativos neste atuador voltam ela ao frame inicial.

**Tipo:** boolean

### framePropName

O nome da propriedade que recebe o número do frame atual.

**Tipo:** string

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### layer

 <small>atributo</small>

Camada de animação (0 a 7) em que o atuador toca a ação. Camadas diferentes tocam ao mesmo tempo.

### layerWeight

 <small>atributo</small>

Peso da camada, de 0.0 a 1.0: quanto esta ação se mistura com as camadas de baixo.

