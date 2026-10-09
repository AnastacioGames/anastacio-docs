---
title: "SCA_2DFilterActuator"
description: "Referência da classe Range.types.SCA_2DFilterActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Cria, liga e desliga filtros 2D.

As propriedades a seguir não têm efeito imediato. É preciso ativar o atuador para ver o resultado. O atuador não é persistente: ele para sozinho depois de configurar o filtro, mas o filtro continua ativo. Para parar um filtro, ative o atuador com 'type' igual a `RAS_2DFILTER_DISABLED` ou `RAS_2DFILTER_NOFILTER`.

### shaderText

código-fonte do shader personalizado.

**Tipo:** string

### disableMotionBlur

ação no motion blur: 0=liga, 1=desliga.

**Tipo:** integer

### mode

Tipo de filtro 2D; use uma `destas constantes`.

**Tipo:** integer

### passNumber

número de ordem do filtro na pilha de filtros 2D. Os filtros rodam em ordem crescente de passNb.

Só pode haver um filtro por passNb.

**Tipo:** integer (0-100)

### value

argumento do filtro de motion blur.

**Tipo:** float (0.0-100.0)

