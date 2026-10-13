---
title: "KX_2DFilterManager"
description: "Range.types.KX_2DFilterManager class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`KX_2DFilter`](../../types/kx_2dfilter/), [`KX_2DFilterOffScreen`](../../types/kx_2dfilteroffscreen/), [`KX_Camera`](../../types/kx_camera/)
:::



2D filter manager used to add, remove and find filters in a scene.

### addFilter(index, type, fragmentProgram="", owner=None, mipmap=False)

Add a filter to the pass index `index`, type `type` and fragment program if custom filter.

- **`index`**: The filter pass index.
  - type: integer
- **`type`**: The filter type, one of: * `Range.logic.RAS_2DFILTER_BLUR` * `Range.logic.RAS_2DFILTER_DILATION` * `Range.logic.RAS_2DFILTER_EROSION` * `Range.logic.RAS_2DFILTER_SHARPEN` * `Range.logic.RAS_2DFILTER_LAPLACIAN` * `Range.logic.RAS_2DFILTER_PREWITT` * `Range.logic.RAS_2DFILTER_SOBEL` * `Range.logic.RAS_2DFILTER_GRAYSCALE` * `Range.logic.RAS_2DFILTER_SEPIA` * `Range.logic.RAS_2DFILTER_OUTLINE` * `Range.logic.RAS_2DFILTER_CUSTOMFILTER`
  - type: integer
- **`fragmentProgram`**: The filter shader fragment program. Used only if `type` is `Range.logic.RAS_2DFILTER_CUSTOMFILTER`, if empty or not specified the filter is created without shader, waiting call to `BL_Shader.setSourceList`. (optional)
  - type: string
- **`owner`**: Object whose game properties feed the uniforms of the same name, like the Filter 2D actuator. (optional)
  - type: `KX_GameObject`
- **`mipmap`**: Generate mipmaps of the filter input. (optional)
  - type: boolean

**Returns:** The 2D Filter.

**Return type:** `KX_2DFilter`

### setBuiltinFilterEnabled(type, enabled=True)

Turn a built-in filter on or off with its current values, like the Filter 2D actuator.

- **`type`**: `Range.logic.RAS_2DFILTER_FXAA`, `RAS_2DFILTER_BLOOM`, `RAS_2DFILTER_TONEMAP`, `RAS_2DFILTER_SSAO`, `RAS_2DFILTER_LIGHTSCATTER` or `RAS_2DFILTER_SSR`.
  - type: integer
- **`enabled`**: The new state.
  - type: boolean

**Returns:** False when the filter is unavailable.

**Return type:** boolean

### removeFilter(index)

Remove filter to the pass index `index`.

- **`index`**: The filter pass index.
  - type: integer

### getFilter(index)

Return filter to the pass index `index`.

**warning:** If the 2D Filter is added with a `SCA_2DFilterActuator`, the filter will be available only after the 2D Filter program is linked. The python script to get the filter has to be executed one frame later. A delay sensor can be used.

- **`index`**: The filter pass index.
  - type: integer

**Returns:** The filter in the specified pass index or None.

**Return type:** `KX_2DFilter` or None

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### changeBloomValues(enabled, intensity, threshold)

 <small>method</small>

Turns the scene Bloom on/off and changes intensity and brightness threshold.

### changeFxaaValues(enabled)

 <small>method</small>

Turns the scene FXAA (anti-aliasing) on or off.

### changeGrainValues(enabled, strength)

 <small>method</small>

Turns film grain on/off and changes its strength.

### changeLightScatterValues(enabled, step_max, step_size, threshold, intensity)

 <small>method</small>

Turns light scattering (light rays) on/off and changes steps, step size, threshold and intensity.

### changeSSAOValues(enabled, samples, strength, distance, attenuation)

 <small>method</small>

Turns ambient occlusion (SSAO) on/off and changes samples, strength, distance and attenuation.

### changeSSGIValues(enabled, radius=3.0, strength=1.0, rays=4, steps=8, thickness=0.1, divisor=0)

 <small>method</small>

Turns screen-space global illumination (SSGI) on/off and changes its parameters. `divisor` 1, 2 or 4 changes the tracing resolution; 0 keeps it. SSGI must be enabled in the scene before Play.

### changeSSRValues(enabled, step_max, bias, max_distance)

 <small>method</small>

Turns screen-space reflections (SSR) on/off and changes steps, bias and maximum distance.

### changeTonemapValues(enabled, exposure, gamma)

 <small>method</small>

Turns tonemapping on/off and changes exposure and gamma.

### fxaaEdgeThreshold

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Minimum relative contrast for an edge to get FXAA, from 0.0 to 1.0. Lower values smooth more edges.

### fxaaEdgeThresholdMin

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Minimum absolute contrast for FXAA to act, from 0.0 to 1.0. Avoids processing dark areas.

### fxaaEnabled

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns the scene FXAA on or off (Scene > Post-process). `True` or `False`.

### fxaaSearchSteps

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Number of FXAA edge search steps (integer, 2 or more). More steps catch longer edges and cost more.

### fxaaSubpix

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

How much FXAA smooths details smaller than a pixel, from 0.0 to 1.0.

### grainEnabled

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns the scene film grain on or off.

### grainStrength

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Film grain strength, from 0.0 to 1.0.

