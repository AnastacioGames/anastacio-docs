# KX_2DFilterManager

Base class: [`EXP_PyObjectPlus`](EXP_PyObjectPlus.md)

> **See also:**
[`KX_2DFilter`](KX_2DFilter.md), [`KX_2DFilterOffScreen`](KX_2DFilterOffScreen.md), [`KX_Camera`](KX_Camera.md)

2D filter manager used to add, remove and find filters in a scene.

```python
# Add a built-in filter, then a custom one.
import Range

manager = Range.logic.getCurrentScene().filterManager

manager.addFilter(0, Range.logic.RAS_2DFILTER_SEPIA)

GLSL = """
uniform sampler2D bgl_RenderedTexture;
in vec4 bgl_TexCoord;
out vec4 fragColor;

void main()
{
    fragColor = texture(bgl_RenderedTexture, bgl_TexCoord.xy) * 0.5;
}
"""
manager.addFilter(1, Range.logic.RAS_2DFILTER_CUSTOMFILTER, GLSL)
```

```python
# Remove a filter.
import Range

manager = Range.logic.getCurrentScene().filterManager

if manager.getFilter(0) is not None:
    manager.removeFilter(0)
```

```python
# Adjust the effects of the graphics options.
import Range

manager = Range.logic.getCurrentScene().filterManager

manager.changeBloomValues(True, 0.6, 0.8)
manager.changeFxaaValues(True)
manager.changeGrainValues(True, 0.1)
```

## addFilter(index, type, fragmentProgram="", owner=None, mipmap=False)

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

 `method`

Turns the scene Bloom on/off and changes intensity and brightness threshold.

### changeFxaaValues(enabled)

 `method`

Turns the scene FXAA (anti-aliasing) on or off.

### changeGrainValues(enabled, strength)

 `method`

Turns film grain on/off and changes its strength.

### changeLightScatterValues(enabled, step_max, step_size, threshold, intensity)

 `method`

Turns light scattering (light rays) on/off and changes steps, step size, threshold and intensity.

### changeSSAOValues(enabled, samples, strength, distance, attenuation)

 `method`

Turns ambient occlusion (SSAO) on/off and changes samples, strength, distance and attenuation.

### changeSSGIValues(enabled, radius=3.0, strength=1.0, rays=4, steps=8, thickness=0.1, divisor=0)

 `method`

Turns screen-space global illumination (SSGI) on/off and changes its parameters. `divisor` 1, 2 or 4 changes the tracing resolution; 0 keeps it. SSGI must be enabled in the scene before Play.

### changeSSRValues(enabled, step_max, bias, max_distance)

 `method`

Turns screen-space reflections (SSR) on/off and changes steps, bias and maximum distance.

### changeTonemapValues(enabled, exposure, gamma)

 `method`

Turns tonemapping on/off and changes exposure and gamma.

### compositor

*(new in Anastacio)* `attribute · read-only`

Filter generated from the scene's Compositor tree (Use Nodes). Value and RGB nodes change live with `compositor.setUniform()`. Read-only.

### fxaaEdgeThreshold

*(new in Anastacio)* `attribute`

Minimum relative contrast for an edge to get FXAA, from 0.0 to 1.0. Lower values smooth more edges.

### fxaaEdgeThresholdMin

*(new in Anastacio)* `attribute`

Minimum absolute contrast for FXAA to act, from 0.0 to 1.0. Avoids processing dark areas.

### fxaaEnabled

*(new in Anastacio)* `attribute`

Turns the scene FXAA on or off (Scene > Post-process). `True` or `False`.

### fxaaSearchSteps

*(new in Anastacio)* `attribute`

Number of FXAA edge search steps (integer, 2 or more). More steps catch longer edges and cost more.

### fxaaSubpix

*(new in Anastacio)* `attribute`

How much FXAA smooths details smaller than a pixel, from 0.0 to 1.0.

### grainEnabled

*(new in Anastacio)* `attribute`

Turns the scene film grain on or off.

### grainStrength

*(new in Anastacio)* `attribute`

Film grain strength, from 0.0 to 1.0.

### taaEnabled

*(new in Anastacio)* `attribute`

Turns the scene TAA (temporal anti-aliasing) on or off (Render > TAA). `True` or `False`. Smooths edges by blending frames with a slightly shifted camera. In split screen and stereo only the sharpening runs.

### taaSharpen

*(new in Anastacio)* `attribute`

Sharpening applied after TAA, from 0.0 to 1.0 (default 0.25). Makes up for the slight blur of frame blending.

### taaUpscale

*(new in Anastacio)* `attribute`

TAA temporal upscaling (Scene > TAA > Upscaling): `0` Off, `1` Quality, `2` Balanced, `3` Performance. The scene renders smaller and TAA scales it up to the window size; overlay (HUD) scenes draw at window size. Other values raise `ValueError`.
