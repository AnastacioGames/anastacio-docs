---
title: "KX_MouseActuator"
description: "Referência da classe Range.types.KX_MouseActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



O atuador Mouse controla a visibilidade do cursor do mouse e gira o objeto pai conforme o movimento do mouse.

### reset()

Desfaz a rotação causada pelo atuador Mouse.

### visible

A visibilidade do cursor do mouse.

**Tipo:** boolean

### use_axis_x

O movimento do mouse no eixo x afeta a rotação do objeto.

**Tipo:** boolean

### use_axis_y

O movimento do mouse no eixo y afeta a rotação do objeto.

**Tipo:** boolean

### threshold

Quanto o mouse precisa andar antes de a rotação começar.

**Tipo:** `mathutils.Vector`

Os valores da lista devem ficar entre 0.0 e 0.5.

### reset_x

O mouse fica travado no centro da tela no eixo x.

**Tipo:** boolean

### reset_y

O mouse fica travado no centro da tela no eixo y.

**Tipo:** boolean

### object_axis

O eixo 3D do objeto que gira com o movimento do mouse. ([x, y])

**Tipo:** list (vector of 2 integers from 0 to 2)

* KX_ACT_MOUSE_OBJECT_AXIS_X
* KX_ACT_MOUSE_OBJECT_AXIS_Y
* KX_ACT_MOUSE_OBJECT_AXIS_Z

### local_x

A rotação causada pelo movimento do mouse no eixo x é local.

**Tipo:** boolean

### local_y

A rotação causada pelo movimento do mouse no eixo y é local.

**Tipo:** boolean

### sensitivity

Quanto de rotação o movimento do mouse nos eixos x e y causa.

**Tipo:** `mathutils.Vector`

Valores negativos invertem a rotação.

### limit_x

Os ângulos mínimo e máximo de rotação causada pelo movimento do mouse no eixo x, em graus. limit_x[0] é o mínimo, limit_x[1] é o máximo.

**Tipo:** `mathutils.Vector`

### limit_y

Os ângulos mínimo e máximo de rotação causada pelo movimento do mouse no eixo y, em graus. limit_y[0] é o mínimo, limit_y[1] é o máximo.

**Tipo:** `mathutils.Vector`

### angle

O deslocamento de rotação atual causado pelo atuador Mouse, em graus.

**Tipo:** `mathutils.Vector`

