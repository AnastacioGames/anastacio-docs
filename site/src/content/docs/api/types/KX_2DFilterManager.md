---
title: "KX_2DFilterManager"
description: "Referência da classe Range.types.KX_2DFilterManager"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



2D filter manager used to add, remove and find filters in a scene.

### addFilter(index, type, fragmentProgram)

Add a filter to the pass index `index`, type `type` and fragment program if custom filter.

- **`index`**: The filter pass index.
  - tipo: integer
- **`type`**: The filter type, one of: * `Range.logic.RAS_2DFILTER_BLUR` * `Range.logic.RAS_2DFILTER_DILATION` * `Range.logic.RAS_2DFILTER_EROSION` * `Range.logic.RAS_2DFILTER_SHARPEN` * `Range.logic.RAS_2DFILTER_LAPLACIAN` * `Range.logic.RAS_2DFILTER_PREWITT` * `Range.logic.RAS_2DFILTER_SOBEL` * `Range.logic.RAS_2DFILTER_GRAYSCALE` * `Range.logic.RAS_2DFILTER_SEPIA` * `Range.logic.RAS_2DFILTER_CUSTOMFILTER`
  - tipo: integer
- **`fragmentProgram`**: The filter shader fragment program. Used only if `type` is `Range.logic.RAS_2DFILTER_CUSTOMFILTER`, if empty or not specified the filter is created without shader, waiting call to `BL_Shader.setSourceList`. (optional)
  - tipo: string

**Retorna:** The 2D Filter.

**Tipo do retorno:** `KX_2DFilter`

### removeFilter(index)

Remove filter to the pass index `index`.

- **`index`**: The filter pass index.
  - tipo: integer

### getFilter(index)

Return filter to the pass index `index`.

**warning:** If the 2D Filter is added with a `SCA_2DFilterActuator`, the filter will be available only after the 2D Filter program is linked. The python script to get the filter has to be executed one frame later. A delay sensor can be used.

- **`index`**: The filter pass index.
  - tipo: integer

**Retorna:** The filter in the specified pass index or None.

**Tipo do retorno:** `KX_2DFilter` or None

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### changeBloomValues()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### changeFxaaValues()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### changeGrainValues()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### changeLightScatterValues()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### changeSSAOValues()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### changeSSRValues()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### changeTonemapValues()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### fxaaEdgeThreshold

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### fxaaEdgeThresholdMin

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### fxaaEnabled

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### fxaaSearchSteps

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### fxaaSubpix

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### grainEnabled

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### grainStrength

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

