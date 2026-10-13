---
title: "KX_2DFilterManager"
description: "Referência da classe Range.types.KX_2DFilterManager"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Gerenciador de filtros 2D, usado para adicionar, remover e achar filtros numa cena.

### addFilter(index, type, fragmentProgram="", owner=None, mipmap=False)

Adiciona um filtro no passe `index`, do tipo `type`, com o fragment program se for filtro personalizado.

- **`index`**: O índice do passe do filtro.
  - tipo: integer
- **`type`**: O tipo do filtro, um destes: * `Range.logic.RAS_2DFILTER_BLUR` * `Range.logic.RAS_2DFILTER_DILATION` * `Range.logic.RAS_2DFILTER_EROSION` * `Range.logic.RAS_2DFILTER_SHARPEN` * `Range.logic.RAS_2DFILTER_LAPLACIAN` * `Range.logic.RAS_2DFILTER_PREWITT` * `Range.logic.RAS_2DFILTER_SOBEL` * `Range.logic.RAS_2DFILTER_GRAYSCALE` * `Range.logic.RAS_2DFILTER_SEPIA` * `Range.logic.RAS_2DFILTER_OUTLINE` * `Range.logic.RAS_2DFILTER_CUSTOMFILTER`
  - tipo: integer
- **`fragmentProgram`**: O fragment program do shader do filtro. Só é usado se `type` for `Range.logic.RAS_2DFILTER_CUSTOMFILTER`; se vazio ou omitido, o filtro é criado sem shader, esperando uma chamada a `BL_Shader.setSourceList` (opcional).
  - tipo: string
- **`owner`**: Objeto cujas propriedades de jogo alimentam os uniforms de mesmo nome, como no atuador Filter 2D (opcional).
  - tipo: `KX_GameObject`
- **`mipmap`**: Gera mipmaps da imagem de entrada do filtro (opcional).
  - tipo: boolean

**Retorna:** O filtro 2D.

**Tipo do retorno:** `KX_2DFilter`

### setBuiltinFilterEnabled(type, enabled=True)

Liga ou desliga um filtro embutido, mantendo os valores atuais dele, como faz o atuador Filter 2D.

- **`type`**: `Range.logic.RAS_2DFILTER_FXAA`, `RAS_2DFILTER_BLOOM`, `RAS_2DFILTER_TONEMAP`, `RAS_2DFILTER_SSAO`, `RAS_2DFILTER_LIGHTSCATTER` ou `RAS_2DFILTER_SSR`.
  - tipo: integer
- **`enabled`**: O novo estado.
  - tipo: boolean

**Retorna:** False quando o filtro não está disponível.

**Tipo do retorno:** boolean

### removeFilter(index)

Remove o filtro do passe `index`.

- **`index`**: O índice do passe do filtro.
  - tipo: integer

### getFilter(index)

Devolve o filtro do passe `index`.

**aviso:** Se o filtro 2D for adicionado por um `SCA_2DFilterActuator`, ele só fica disponível depois que o programa do filtro 2D for linkado. O script Python que pega o filtro precisa rodar um frame depois. Dá para usar um sensor Delay.

- **`index`**: O índice do passe do filtro.
  - tipo: integer

**Retorna:** O filtro no passe indicado, ou None.

**Tipo do retorno:** `KX_2DFilter` or None

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### changeBloomValues(enabled, intensity, threshold)

 <small>método</small>

Liga/desliga o Bloom da cena e muda intensidade e limiar de brilho.

### changeFxaaValues(enabled)

 <small>método</small>

Liga ou desliga o FXAA (anti-serrilhado) da cena.

### changeGrainValues(enabled, strength)

 <small>método</small>

Liga/desliga o grão de filme e muda a força.

### changeLightScatterValues(enabled, step_max, step_size, threshold, intensity)

 <small>método</small>

Liga/desliga os raios de luz (light scattering) e muda passos, tamanho do passo, limiar e intensidade.

### changeSSAOValues(enabled, samples, strength, distance, attenuation)

 <small>método</small>

Liga/desliga a oclusão de ambiente (SSAO) e muda amostras, força, distância e atenuação.

### changeSSGIValues(enabled, radius=3.0, strength=1.0, rays=4, steps=8, thickness=0.1, divisor=0)

 <small>método</small>

Liga/desliga a iluminação global em tela (SSGI) e muda seus parâmetros. `divisor` 1, 2 ou 4 muda a resolução do traçado; 0 mantém. O SSGI precisa estar ligado na cena antes do Play.

### changeSSRValues(enabled, step_max, bias, max_distance)

 <small>método</small>

Liga/desliga os reflexos em tela (SSR) e muda passos, bias e distância máxima.

### changeTonemapValues(enabled, exposure, gamma)

 <small>método</small>

Liga/desliga o tonemap e muda exposição e gamma.

### fxaaEdgeThreshold

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Contraste mínimo, relativo, para uma borda receber FXAA, de 0.0 a 1.0. Valores menores suavizam mais bordas.

### fxaaEdgeThresholdMin

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Contraste mínimo absoluto para o FXAA agir, de 0.0 a 1.0. Evita processar áreas escuras.

### fxaaEnabled

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga ou desliga o FXAA da cena (Scene > Post-process). `True` ou `False`.

### fxaaSearchSteps

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Número de passos da busca de bordas do FXAA (inteiro, a partir de 2). Mais passos pegam bordas mais longas e custam mais.

### fxaaSubpix

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Quanto o FXAA suaviza detalhes menores que um pixel, de 0.0 a 1.0.

### grainEnabled

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga ou desliga o grão de filme da cena.

### grainStrength

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Força do grão de filme, de 0.0 a 1.0.

