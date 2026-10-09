---
title: "Range.render"
description: "Referência do módulo Range.render"
---

## Intro

Example of using a `Range.types.SCA_MouseSensor`,
and two `Range.types.KX_ObjectActuator` to implement MouseLook:

:::note
This can also be achieved with the `Range.types.KX_MouseActuator`.
:::

```python

# To use a mouse movement sensor "Mouse" and a
# motion actuator to mouse look:
import Range

# scale sets the speed of motion
scale = 1.0, 0.5

co = Range.logic.getCurrentController()
obj = co.owner
mouse = co.sensors["Mouse"]
lmotion = co.actuators["LMove"]
wmotion = co.actuators["WMove"]

# Transform the mouse coordinates to see how far the mouse has moved.
def mousePos():
   x = (Range.render.getWindowWidth() / 2 - mouse.position[0]) * scale[0]
   y = (Range.render.getWindowHeight() / 2 - mouse.position[1]) * scale[1]
   return (x, y)

pos = mousePos()

# Set the amount of motion: X is applied in world coordinates...
wmotion.useLocalTorque = False
wmotion.torque = ((0.0, 0.0, pos[0]))

# ...Y is applied in local coordinates
lmotion.useLocalTorque = True
lmotion.torque = ((-pos[1], 0.0, 0.0))

# Activate both actuators
co.activate(lmotion)
co.activate(wmotion)

# Centre the mouse
Range.render.setMousePosition(int(Range.render.getWindowWidth() / 2), int(Range.render.getWindowHeight() / 2))
```

## Constants

### KX_TEXFACE_MATERIAL

Deprecated.

Materials as defined by the texture face settings.

### KX_BLENDER_MULTITEX_MATERIAL

Deprecated.

Materials approximating blender materials with multitexturing.

### KX_BLENDER_GLSL_MATERIAL

Deprecated.

Materials approximating blender materials with GLSL.

Disables vsync
Enables vsync
Enables adaptive vsync if supported.
Adaptive vsync enables vsync if the framerate is above the monitors refresh rate.
Otherwise, vsync is diabled if the framerate is too low.

### LEFT_EYE

Left eye being used during stereoscopic rendering.

### RIGHT_EYE

Right eye being used during stereoscopic rendering.

.. _render-hdr:

## HDR

### HDR_NONE

Use 8 bit per channel image format.

### HDR_HALF_FLOAT

Use 16 bit float per channel image format.

### HDR_FULL_FLOAT

Use 32 bit float per channel image format.

## Functions

### getWindowWidth()

Gets the width of the window (in pixels)

**Tipo do retorno:** integer

### getWindowHeight()

Gets the height of the window (in pixels)

**Tipo do retorno:** integer

### setWindowSize(width, height)

Set the width and height of the window (in pixels). This also works for fullscreen applications.

:::note
Only works in the standalone player, not the Blender-embedded player.
:::

- **`width`**: width in pixels
  - tipo: integer
- **`height`**: height in pixels
  - tipo: integer

### setFullScreen(enable)

Set whether or not the window should be fullscreen.

:::note
Only works in the standalone player, not the Blender-embedded player.
:::

- **`enable`**: `True` to set full screen, `False` to set windowed.
  - tipo: bool

### getFullScreen()

Returns whether or not the window is fullscreen.

:::note
Only works in the standalone player, not the Blender-embedded player; there it always returns False.
:::

**Tipo do retorno:** bool

### getDisplayDimensions()

Get the display dimensions, in pixels, of the display (e.g., the
monitor). Can return the size of the entire view, so the
combination of all monitors; for example, `(3840, 1080)` for two
side-by-side 1080p monitors.

**Tipo do retorno:** tuple (width, height)

### makeScreenshot(filename)

Writes an image file with the displayed image at the frame end.

The image is written to *'filename'*.
The path may be absolute (eg. `/home/foo/image`) or relative when started with
`//` (eg. `//image`). Note that absolute paths are not portable between platforms.
If the filename contains a `#`,
it will be replaced by an incremental index so that screenshots can be taken multiple
times without overwriting the previous ones (eg. `image-#`).

Settings for the image are taken from the render settings (file format and respective settings,
gamma and colospace conversion, etc).
The image resolution matches the framebuffer, meaning, the window size and aspect ratio.
When running from the standalone player, instead of the embedded player, only PNG files are supported.
Additional color conversions are also not supported.

- **`filename`**: path and name of the file to write
  - tipo: string

### enableVisibility(visible)

Deprecated; doesn't do anything.

### showMouse(visible)

Enables or disables the operating system mouse cursor.

- **`visible`**: 
  - tipo: boolean

### setMousePosition(x, y)

Sets the mouse cursor position.

- **`x`**: X-coordinate in screen pixel coordinates.
  - tipo: integer
- **`y`**: Y-coordinate in screen pixel coordinates.
  - tipo: integer

### setBackgroundColor(rgba)

Deprecated and no longer functional. Use `Range.types.KX_WorldInfo.horizonColor` or `Range.types.KX_WorldInfo.zenithColor` instead.

### setEyeSeparation(eyesep)

Sets the eye separation for stereo mode. Usually Focal Length/30 provides a confortable value.

- **`eyesep`**: The distance between the left and right eye.
  - tipo: float

### getEyeSeparation()

Gets the current eye separation for stereo mode.

**Tipo do retorno:** float

### setFocalLength(focallength)

Sets the focal length for stereo mode. It uses the current camera focal length as initial value.

- **`focallength`**: The focal length.
  - tipo: float

### getFocalLength()

Gets the current focal length for stereo mode.

**Tipo do retorno:** float

### getStereoEye()

Gets the current stereoscopy eye being rendered.
This function is mainly used in a `Range.types.KX_Scene.pre_draw` callback
function to customize the camera projection matrices for each
stereoscopic eye.

**Tipo do retorno:** LEFT_EYE, RIGHT_EYE

### setMaterialMode(mode)

Deprecated and no longer functional.

Set the material mode to use for OpenGL rendering.

- **`mode`**: material mode
  - tipo: KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL

:::note
Changes will only affect newly created scenes.
:::

### getMaterialMode(mode)

Deprecated and no longer functional.

Get the material mode to use for OpenGL rendering.

**Tipo do retorno:** KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL

### setGLSLMaterialSetting(setting, enable)

Enables or disables a GLSL material setting.

- **`setting`**: 
  - tipo: string (lights, shaders, shadows, ramps, nodes, extra_textures)
- **`enable`**: 
  - tipo: boolean

### getGLSLMaterialSetting(setting)

Get the state of a GLSL material setting.

- **`setting`**: 
  - tipo: string (lights, shaders, shadows, ramps, nodes, extra_textures)

**Tipo do retorno:** boolean

### setAnisotropicFiltering(level)

Set the anisotropic filtering level for textures.

- **`level`**: The new anisotropic filtering level to use
  - tipo: integer (must be one of 1, 2, 4, 8, 16)

:::note
Changing this value can cause all textures to be recreated, which can be slow.
:::

### getAnisotropicFiltering()

Get the anisotropic filtering level used for textures.

**Tipo do retorno:** integer (one of 1, 2, 4, 8, 16)

### setAntiAliasing(level)

Set the anti aliasing level.

- **`level`**: The new anti aliasing level to use
  - tipo: integer (must be one of 0, 2, 4, 8, 16)

:::note
Changing this value cause all off screens to be recreated, which can be slow.
:::

### getAntiAliasing()

Get the anti aliasing level setting.

**Tipo do retorno:** integer (one of 0, 2, 4, 8, 16)

### setMipmapping(value)

Change how to use mipmapping.

  - tipo: RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR

:::note
Changing this value can cause all textures to be recreated, which can be slow.
:::

### getMipmapping()

Get the current mipmapping setting.

**Tipo do retorno:** RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR

### drawLine(fromVec,toVec,color)

Draw a line in the 3D scene.

- **`fromVec`**: the origin of the line
  - tipo: list [x, y, z]
- **`toVec`**: the end of the line
  - tipo: list [x, y, z]
- **`color`**: the color of the line
  - tipo: list [r, g, b, a]

### enableMotionBlur(factor)

Enable the motion blur effect.

- **`factor`**: the ammount of motion blur to display.
  - tipo: float [0.0 - 1.0]

### disableMotionBlur()

Disable the motion blur effect.

### showFramerate(enable)

Show or hide the framerate.

- **`enable`**: 
  - tipo: boolean

### showProfile(enable)

Show or hide the profile.

- **`enable`**: 
  - tipo: boolean

### showProperties(enable)

Show or hide the debug properties.

- **`enable`**: 
  - tipo: boolean

### autoDebugList(enable)

Enable or disable auto adding debug properties to the debug list.

- **`enable`**: 
  - tipo: boolean

### clearDebugList()

Clears the debug property list.

### setVsync(value)

Set the vsync value

- **`value`**: One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE
  - tipo: integer

### getVsync()

Get the current vsync value

**Tipo do retorno:** One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE

### setDynamicResolution(enabled, targetFPS=60, minScale=50, maxScale=100, step=5)

Runtime version of the scene's Dynamic Resolution settings. The 3D scene is rendered at a
scale of the window size and stretched to the screen; the window itself does not change.
With dynamic resolution the scale goes down by `step` when the GPU time of a frame is above
the target and back up when there is time left. `minScale == maxScale` gives a fixed render
scale. Paused while "Show Render Queries" is on (both use a GPU timer query).

- **`enabled`**: False renders at 100%.
  - tipo: boolean
- **`targetFPS`**: Frame rate the GPU time is compared to.
  - tipo: integer
- **`minScale`**: Lowest scale, in percent (25-100).
  - tipo: integer
- **`maxScale`**: Highest scale, in percent (25-100).
  - tipo: integer
- **`step`**: Scale change per adjustment, in percent (1-25).
  - tipo: integer

### getRenderScale()

Current render scale, 1.0 = full resolution.

**Tipo do retorno:** float

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### getMasterVolume()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

**Retorna:** `volume`

### getStereoMode()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

get the stereo mode

### getVRChromaticAberration()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

get the VR lens chromatic aberration correction

### getVRLensStrength()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

get the VR lens distortion strength

### setCustomMouse(string path)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setMasterVolume(volume)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

-- volume in [0, 1], applies to the engine's actual audio device

### setStereoMode()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

set the stereo mode (STEREO_* constants)

### setVRChromaticAberration()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

set the VR lens chromatic aberration correction (0..0.1, default 0.01)

### setVRLensStrength()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

set the VR lens distortion strength (0..1, default 0.3)

### showDebugPhysics(bool debug)

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### RAS_MIPMAP_LINEAR

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_MIPMAP_NEAREST

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_MIPMAP_NONE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### STEREO_ABOVEBELOW

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### STEREO_ANAGLYPH

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### STEREO_INTERLACED

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### STEREO_NOSTEREO

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### STEREO_SIDEBYSIDE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### VSYNC_ADAPTIVE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### VSYNC_OFF

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### VSYNC_ON

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

