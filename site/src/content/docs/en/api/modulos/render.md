---
title: "Range.render"
description: "Range.render module reference"
---

:::tip[See also]
[`KX_Camera`](../../types/kx_camera/), [`KX_2DFilterManager`](../../types/kx_2dfiltermanager/), [`Range.logic`](../../modulos/logic/)
:::

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

**Return type:** integer

### getWindowHeight()

Gets the height of the window (in pixels)

**Return type:** integer

### setWindowSize(width, height)

Set the width and height of the window (in pixels). This also works for fullscreen applications.

:::note
Only works in the standalone player, not the Blender-embedded player.
:::

- **`width`**: width in pixels
  - type: integer
- **`height`**: height in pixels
  - type: integer

### setFullScreen(enable)

Set whether or not the window should be fullscreen.

:::note
Only works in the standalone player, not the Blender-embedded player.
:::

- **`enable`**: `True` to set full screen, `False` to set windowed.
  - type: bool

### getFullScreen()

Returns whether or not the window is fullscreen.

:::note
Only works in the standalone player, not the Blender-embedded player; there it always returns False.
:::

**Return type:** bool

### getDisplayDimensions()

Get the display dimensions, in pixels, of the display (e.g., the
monitor). Can return the size of the entire view, so the
combination of all monitors; for example, `(3840, 1080)` for two
side-by-side 1080p monitors.

**Return type:** tuple (width, height)

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
  - type: string

### enableVisibility(visible)

Deprecated; doesn't do anything.

### showMouse(visible)

Enables or disables the operating system mouse cursor.

- **`visible`**: 
  - type: boolean

### setMousePosition(x, y)

Sets the mouse cursor position.

- **`x`**: X-coordinate in screen pixel coordinates.
  - type: integer
- **`y`**: Y-coordinate in screen pixel coordinates.
  - type: integer

### setBackgroundColor(rgba)

Deprecated and no longer functional. Use `Range.types.KX_WorldInfo.horizonColor` or `Range.types.KX_WorldInfo.zenithColor` instead.

### setEyeSeparation(eyesep)

Sets the eye separation for stereo mode. Usually Focal Length/30 provides a confortable value.

- **`eyesep`**: The distance between the left and right eye.
  - type: float

### getEyeSeparation()

Gets the current eye separation for stereo mode.

**Return type:** float

### setFocalLength(focallength)

Sets the focal length for stereo mode. It uses the current camera focal length as initial value.

- **`focallength`**: The focal length.
  - type: float

### getFocalLength()

Gets the current focal length for stereo mode.

**Return type:** float

### getStereoEye()

Gets the current stereoscopy eye being rendered.
This function is mainly used in a `Range.types.KX_Scene.pre_draw` callback
function to customize the camera projection matrices for each
stereoscopic eye.

**Return type:** LEFT_EYE, RIGHT_EYE

### setMaterialMode(mode)

Deprecated and no longer functional.

Set the material mode to use for OpenGL rendering.

- **`mode`**: material mode
  - type: KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL

:::note
Changes will only affect newly created scenes.
:::

### getMaterialMode(mode)

Deprecated and no longer functional.

Get the material mode to use for OpenGL rendering.

**Return type:** KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL

### setGLSLMaterialSetting(setting, enable)

Enables or disables a GLSL material setting.

- **`setting`**: 
  - type: string (lights, shaders, shadows, ramps, nodes, extra_textures)
- **`enable`**: 
  - type: boolean

### getGLSLMaterialSetting(setting)

Get the state of a GLSL material setting.

- **`setting`**: 
  - type: string (lights, shaders, shadows, ramps, nodes, extra_textures)

**Return type:** boolean

### setAnisotropicFiltering(level)

Set the anisotropic filtering level for textures.

- **`level`**: The new anisotropic filtering level to use
  - type: integer (must be one of 1, 2, 4, 8, 16)

:::note
clamped to the maximum of the graphics card. The exported game starts with 8.
:::

### getAnisotropicFiltering()

Get the anisotropic filtering level used for textures.

**Return type:** integer (one of 1, 2, 4, 8, 16)

### setAntiAliasing(level)

Set the anti aliasing level.

- **`level`**: The new anti aliasing level to use
  - type: integer (must be one of 0, 2, 4, 8, 16)

:::note
Changing this value cause all off screens to be recreated, which can be slow.
:::

### getAntiAliasing()

Get the anti aliasing level setting.

**Return type:** integer (one of 0, 2, 4, 8, 16)

### setMipmapping(value)

Change how to use mipmapping.

  - type: RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR

:::note
Switching between NEAREST and LINEAR or turning them off only changes the filters.
With mipmaps off textures are displayed unfiltered (nearest), useful for pixel art.
:::

### getMipmapping()

Get the current mipmapping setting.

**Return type:** RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR

### setTextureQuality(level)

Texture quality of a graphics menu: keep only the high resolution texture in the project and
drop its largest mipmap levels when it is sent to the graphics card.

* `0`: full size
* `1`: half size (1/4 of the video memory)
* `2`: quarter size (1/16 of the video memory)

Textures never go below 256 pixels on their larger side, and textures without mipmaps
(or with mipmapping off) keep their size. DDS files skip the levels stored in the file.

- **`level`**: 0, 1 or 2
  - type: integer

:::note
menu, not every frame. In the editor the value is restored when the game ends.
:::

### getTextureQuality()

**Returns:** the current texture quality (0 full, 1 half, 2 quarter).

**Return type:** integer

### drawLine(fromVec,toVec,color)

Draw a line in the 3D scene.

- **`fromVec`**: the origin of the line
  - type: list [x, y, z]
- **`toVec`**: the end of the line
  - type: list [x, y, z]
- **`color`**: the color of the line
  - type: list [r, g, b, a]

### enableMotionBlur(factor)

Enable the motion blur effect.

- **`factor`**: the ammount of motion blur to display.
  - type: float [0.0 - 1.0]

### disableMotionBlur()

Disable the motion blur effect.

### showFramerate(enable)

Show or hide the framerate.

- **`enable`**: 
  - type: boolean

### showProfile(enable)

Show or hide the profile.

- **`enable`**: 
  - type: boolean

### showProperties(enable)

Show or hide the debug properties.

- **`enable`**: 
  - type: boolean

### autoDebugList(enable)

Enable or disable auto adding debug properties to the debug list.

- **`enable`**: 
  - type: boolean

### clearDebugList()

Clears the debug property list.

### setVsync(value)

Set the vsync value

- **`value`**: One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE
  - type: integer

### getVsync()

Get the current vsync value

**Return type:** One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE

### setDynamicResolution(enabled, targetFPS=60, minScale=50, maxScale=100, step=5)

Runtime version of the scene's Dynamic Resolution settings. The 3D scene is rendered at a
scale of the window size and stretched to the screen; the window itself does not change.
With dynamic resolution the scale goes down by `step` when the GPU time of a frame is above
the target and back up when there is time left. `minScale == maxScale` gives a fixed render
scale. Paused while "Show Render Queries" is on (both use a GPU timer query).

- **`enabled`**: False renders at 100%.
  - type: boolean
- **`targetFPS`**: Frame rate the GPU time is compared to.
  - type: integer
- **`minScale`**: Lowest scale, in percent (25-100).
  - type: integer
- **`maxScale`**: Highest scale, in percent (25-100).
  - type: integer
- **`step`**: Scale change per adjustment, in percent (1-25).
  - type: integer

### getRenderScale()

Current render scale, 1.0 = full resolution.

**Return type:** float

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### getMasterVolume()

 <small>function</small>

Overall game sound volume, from 0 to 1. See `setMasterVolume()`.

**Returns:** `volume`

### getStereoMode()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

get the stereo mode

### getVRChromaticAberration()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

get the VR lens chromatic aberration correction

### getVRLensStrength()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

get the VR lens distortion strength

### setCustomMouse(path)

 <small>function</small>

Uses the image at `path` as the mouse cursor.

### setMasterVolume(volume)

 <small>function</small>

-- volume in [0, 1], applies to the engine's actual audio device

### setStereoMode()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

set the stereo mode (STEREO_* constants)

### setVRChromaticAberration()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

set the VR lens chromatic aberration correction (0..0.1, default 0.01)

### setVRLensStrength()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

set the VR lens distortion strength (0..1, default 0.3)

### showDebugPhysics(enabled)

 <small>function</small>

Shows or hides the physics collision shapes.

### RAS_MIPMAP_LINEAR

 <small>constant</small>

Linear mipmap (smoother).

### RAS_MIPMAP_NEAREST

 <small>constant</small>

Nearest mipmap.

### RAS_MIPMAP_NONE

 <small>constant</small>

No mipmap.

### STEREO_ABOVEBELOW

 <small>constant</small>

Stereo: one image above the other.

### STEREO_ANAGLYPH

 <small>constant</small>

Stereo: anaglyph (red/cyan glasses).

### STEREO_INTERLACED

 <small>constant</small>

Stereo: interlaced lines.

### STEREO_NOSTEREO

 <small>constant</small>

No stereo.

### STEREO_SIDEBYSIDE

 <small>constant</small>

Stereo: side by side.

### VSYNC_ADAPTIVE

 <small>constant</small>

Adaptive VSync: syncs, but doesn't stall when FPS drops.

### VSYNC_OFF

 <small>constant</small>

VSync off.

### VSYNC_ON

 <small>constant</small>

VSync on.

