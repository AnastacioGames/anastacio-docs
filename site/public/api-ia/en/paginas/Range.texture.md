# Range.texture

> **See also:**
[`Texture`](Texture.md), [`KX_BlenderMaterial`](KX_BlenderMaterial.md), [`BL_Texture`](BL_Texture.md)

```python
# Show a video on the material of the object.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

if "video" not in own:
    matID = texture.materialID(own, "MAscreen")
    tex = texture.Texture(own, matID)
    tex.source = texture.VideoFFmpeg(Range.logic.expandPath("//movie.mp4"))
    tex.source.play()
    own["video"] = tex

own["video"].refresh(True)
```

```python
# Swap the image of a material while the game runs.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageFFmpeg(Range.logic.expandPath("//poster.png"))
tex.refresh(False)
own["poster"] = tex
```

```python
# Make a mirror image with another camera.
import Range
from Range import texture

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageRender(scene, scene.objects["SecurityCamera"])
own["monitor"] = tex
own["monitor"].refresh(True)
```

## Introduction

The `Range.texture` module allows you to manipulate textures during the game.
Several sources for texture are possible: video files, image files, video capture,
memory buffer, camera render or a mix of that.
The video and image files can be loaded from the Internet using a URL instead of a file name.
In addition, you can apply filters on the images before sending them to the GPU,
allowing video effect: blue screen, color band, gray, normal map.
`Range.texture` uses FFmpeg to load images and videos.
All the formats and codecs that FFmpeg supports are supported by `Range.texture`,
including but not limited to:

* AVI
* Ogg
* Xvid
* Theora
* dv1394 camera
* video4linux capture card (this includes many webcams)
* videoForWindows capture card (this includes many webcams)
* JPG

## How it works

The principle is simple: first you identify a texture on an existing object using the
`materialID` function, then you create a new texture with dynamic content
and swap the two textures in the GPU.

The game engine is not aware of the substitution and continues to display the object as always,
except that you are now in control of the texture.

When the texture object is deleted, the new texture is deleted and the old texture restored.

## Game Preparation

Before you can use the `Range.texture` module,
you must have objects with textures applied appropriately.

Imagine you want to have a television showing live broadcast programs in the game.
You will create a television object and UV-apply a different texture at the place of the screen,
for example `tv.png`. What this texture looks like is not important;
probably you want to make it dark gray to simulate power-off state.
When the television must be turned on, you create a dynamic texture from a video capture card
and use it instead of `tv.png`: the TV screen will come to life.

You have two ways to define textures that `Range.texture` can grab:

- Simple UV texture.
- Blender material with image texture channel.

Because `Range.texture` works at texture level, it is compatible with all
the Blender Game Engine's fancy texturing features: GLSL, multi-texture, custom shaders, etc.

## Examples

## Video classes

## Class `VideoFFmpeg(file, capture=-1, rate=25.0, width=0, height=0)`

FFmpeg video source, used for video files, video captures, or video streams.

- **`file`**: Path to the video to load; if capture >= 0 on Windows, this parameter will not be used.
  - type: str
- **`capture`**: Capture device number; if >= 0, the corresponding webcam will be used. (optional)
  - type: int
- **`rate`**: Capture rate. (optional, used only if capture >= 0)
  - type: float
- **`width`**: Capture width. (optional, used only if capture >= 0)
  - type: int
- **`height`**: Capture height. (optional, used only if capture >= 0)
  - type: int

## Class `ImageFFmpeg(file)`

FFmpeg image source, used for image files and web based images.

- **`file`**: Path to the image to load.
  - type: str

## Class `ImageBuff(width, height, color=0, scale=False)`

Image from application memory.
For computer generated images, drawing applications.

- **`width`**: Width of the image.
  - type: int
- **`height`**: Height of the image.
  - type: int
- **`color`**: Value to initialize RGB channels with. The initialized buffer will have all pixels set to (color, color, color, 255). (optional)
  - type: int in [0, 255]
- **`scale`**: Image uses scaling. (optional)
  - type: bool

## Class `ImageMirror(scene, observer, mirror, material=0, width, height, samples, hdr)`

Image source from mirror.

- **`scene`**: Scene in which the image has to be taken.
  - type: `KX_Scene`
- **`observer`**: Reference object for the mirror (the object from which the mirror has to be looked at, for example a camera).
  - type: `KX_GameObject`
- **`mirror`**: Object holding the mirror.
  - type: `KX_GameObject`
- **`material`**: ID of the mirror's material to be used for mirroring. (optional)
  - type: int
- **`width`**: Off-screen render buffer width (optional).
  - type: integer
- **`height`**: Off-screen render buffer height (optional).
  - type: integer
- **`samples`**: Off-screen render buffer samples (optional).
  - type: integer
- **`hdr`**: Off-screen image format (optional).
  - type: One of `these constants`

## Class `ImageMix`

Image mixer used to mix multiple image sources together.

## Class `ImageRender(scene, camera, width, height, samples, hdr)`

Image source from a render of a non active camera.
The render is done on a custom framebuffer object if fbo is specified,
otherwise on the default framebuffer.

- **`scene`**: Scene in which the image has to be taken.
  - type: `KX_Scene`
- **`camera`**: Camera from which the image has to be taken.
  - type: `KX_Camera`
- **`width`**: Off-screen render buffer width (optional).
  - type: integer
- **`height`**: Off-screen render buffer height (optional).
  - type: integer
- **`samples`**: Off-screen render buffer samples (optional).
  - type: integer
- **`hdr`**: Off-screen image format (optional).
  - type: One of `these constants`

## Class `ImageViewport`

Image source from viewport rendered by the active camera.
To render from a non active camera see `ImageRender`.

## Class `VideoDeckLink(format, capture=0)`

Image source from an external video stream captured with a DeckLink video card from
Black Magic Design.
Before this source can be used, a DeckLink hardware device must be installed, it can be a PCIe card
or a USB device, and the 'Desktop Video' software package (version 10.4 or above must be installed)
on the host as described in the DeckLink documentation.
If in addition you have a recent nVideo Quadro card, you can benefit from the 'GPUDirect' technology
to push the captured video frame very efficiently to the GPU. For this you need to install the
'DeckLink SDK' version 10.4 or above and copy the 'dvp.dll' runtime library to Blender's
installation directory or to any other place where Blender can load a DLL from.

- **`format`**: string describing the video format to be captured.
  - type: str
- **`capture`**: Card number from which the input video must be captured.
  - type: int
The format argument must be written as `<displayMode>/<pixelFormat>[/3D][:<cacheSize>]`
where `<displayMode>` describes the frame size and rate and <pixelFormat> the encoding of the pixels.
The optional `/3D` suffix is to be used if the video stream is stereo with a left and right eye feed.
The optional `:<cacheSize>` suffix determines the number of the video frames kept in cache, by default 8.
Some DeckLink cards won't work below a certain cache size. The default value 8 should be sufficient for all cards.
You may try to reduce the cache size to reduce the memory footprint. For example the The 4K Extreme is known
to work with 3 frames only, the Extreme 2 needs 4 frames and the Intensity Shuttle needs 6 frames, etc.
Reducing the cache size may be useful when Decklink is used in conjunction with GPUDirect:
all frames must be locked in memory in that case and that puts a lot of pressure on memory.
If you reduce the cache size too much, you'll get no error but no video feed either.

The valid `<displayMode>` values are copied from the `BMDDisplayMode` enum in the DeckLink API
without the 'bmdMode' prefix. In case a mode that is not in this list is added in a later version
of the SDK, it is also possible to specify the 4 letters of the internal code for that mode.
You will find the internal code in the `DeckLinkAPIModes.h` file that is part of the SDK.
Here is for reference the full list of supported display modes with their equivalent internal code:

Internal Codes
- NTSC 'ntsc'
- NTSC2398 	'nt23'
- PAL		'pal '
- NTSCp		'ntsp'
- PALp		'palp'
HD 1080 Modes
- HD1080p2398	'23ps'
- HD1080p24	'24ps'
- HD1080p25	'Hp25'
- HD1080p2997	'Hp29'
- HD1080p30	'Hp30'
- HD1080i50	'Hi50'
- HD1080i5994	'Hi59'
- HD1080i6000	'Hi60'
- HD1080p50	'Hp50'
- HD1080p5994	'Hp59'
- HD1080p6000	'Hp60'
HD 720 Modes
- HD720p50	'hp50'
- HD720p5994	'hp59'
- HD720p60	'hp60'
2k Modes
- 2k2398	'2k23'
- 2k24		'2k24'
- 2k25		'2k25'
4k Modes
- 4K2160p2398	'4k23'
- 4K2160p24	'4k24'
- 4K2160p25	'4k25'
- 4K2160p2997	'4k29'
- 4K2160p30	'4k30'
- 4K2160p50	'4k50'
- 4K2160p5994	'4k59'
- 4K2160p60	'4k60'

Most of names are self explanatory. If necessary refer to the DeckLink API documentation for more information.

Similarly, <pixelFormat> is copied from the BMDPixelFormat enum.

Here is for reference the full list of supported pixel format and their equivalent internal code:

Pixel Formats
- 8BitYUV	'2vuy'
- 10BitYUV	'v210'
- 8BitARGB	* no equivalent code *
- 8BitBGRA	'BGRA'
- 10BitRGB	'r210'
- 12BitRGB	'R12B'
- 12BitRGBLE	'R12L'
- 10BitRGBXLE	'R10l'
- 10BitRGBX	'R10b'

Refer to the DeckLink SDK documentation for a full description of these pixel format.
It is important to understand them as the decoding of the pixels is NOT done in VideoTexture
for performance reason. Instead a specific shader must be used to decode the pixel in the GPU.
Only the '8BitARGB', '8BitBGRA' and '10BitRGBXLE' pixel formats are mapped directly to OpenGL RGB float textures.
The '8BitYUV' and '10BitYUV' pixel formats are mapped to openGL RGB float texture but require a shader to decode.
The other pixel formats are sent as a `GL_RED_INTEGER` texture (i.e. a texture with only the
red channel coded as an unsigned 32 bit integer) and are not recommended for use.

Example: `HD1080p24/10BitYUV/3D:4` is equivalent to `24ps/v210/3D:4`
and represents a full HD stereo feed at 24 frame per second and 4 frames cache size.

Although video format auto detection is possible with certain DeckLink devices, the corresponding
API is NOT implemented in the BGE. Therefore it is important to specify the format string that
matches exactly the video feed. If the format is wrong, no frame will be captured.
It should be noted that the pixel format that you need to specify is not necessarily the actual
format in the video feed. For example, the 4K Extreme card delivers 8bit RGBs pixels in the
'10BitRGBXLE' format. Use the 'Media Express' application included in 'Desktop Video' to discover
which pixel format works for a particular video stream.

## Class `Texture(gameObj, materialID=0, textureID=0, textureObj=None)`

Class that creates the `Texture` object that loads the dynamic texture on the GPU.

- **`gameObj`**: Game object to be created a video texture on.
  - type: `KX_GameObject`
- **`materialID`**: Material ID default, 0 is the first material. (optional)
  - type: int
- **`textureID`**: Texture index in case of multi-texture channel, 0 = first channel by default. In case of UV texture, this parameter should always be 0. (optional)
  - type: int
- **`textureObj`**: Reference to another `Texture` object with shared bindId which he user might want to reuse the texture. If this argument is used, you should not create any source on this texture and there is no need to refresh it either: the other `Texture` object will provide the texture for both materials/textures.(optional)
  - type: `Texture`

## Class `DeckLink(cardIdx=0, format="")`

Certain DeckLink devices can be used to playback video: the host sends video frames regularly
for immediate or scheduled playback. The video feed is outputted on HDMI or SDI interfaces.
This class supports the immediate playback mode: it has a source attribute that is assigned
one of the source object in the Range.texture module. Refreshing the DeckLink object causes
the image source to be computed and sent to the DeckLink device for immediate transmission
on the output interfaces.  Keying is supported: it allows to composite the frame with an
input video feed that transits through the DeckLink card.

- **`cardIdx`**: Number of the card to be used for output (0=first card). It should be noted that DeckLink devices are usually half duplex: they can either be used for capture or playback but not both at the same time.
  - type: int
- **`format`**: String representing the display mode of the output feed.
  - type: str
The default value of the format argument is reserved for auto detection but it is currently
not supported (it will generate a runtime error) and thus the video format must be explicitly
specified. If keying is the goal (see keying attributes), the format must match exactly the
input video feed, otherwise it can be any format supported by the device (there will be a
runtime error if not).
The format of the string is `<displayMode>[/3D]`.

Refer to `VideoDeckLink` to get the list of acceptable `<displayMode>`.
The optional `/3D` suffix is used to create a stereo 3D feed.
In that case the 'right' attribute must also be set to specify the image source for the right eye.

Note: The pixel format is not specified here because it is always BGRA. The alpha channel is
used in keying to mix the source with the input video feed, otherwise it is not used.
If a conversion is needed to match the native video format, it is done inside the DeckLink driver
or device.

## Class `FilterBGR24`

Source filter BGR24.

## Class `FilterBlueScreen`

Filter for Blue Screen.
The RGB channels of the color are left unchanged, while the output alpha is obtained as follows:

- if the square of the euclidian distance between the RGB color
and the filter's reference color is smaller than the filter's lower limit,
the output alpha is set to 0;
- if that square is bigger than the filter's upper limit, the output alpha is set to 255;
- otherwise the output alpha is linarly extrapoled between 0 and 255 in the interval of the limits.

## Class `FilterColor`

Filter for color calculations.
The output color is obtained by multiplying the reduced 4x4 matrix with the input color
and adding the remaining column to the result.

## Class `FilterGray`

Filter for grayscale effect.
Proportions of R, G and B contributions in the output grayscale are 28:151:77.

## Class `FilterLevel`

Filter for levels calculations. Each output color component is obtained as follows:

* if it is smaller than its corresponding min value, it is set to 0;

* if it is bigger than its corresponding max value, it is set to 255;

* Otherwise it is linearly extrapoled between 0 and 255 in the (min, max) interval.

## Class `FilterNormal`

Normal map filter.

## Class `FilterRGB24`

Returns a new input filter object to be used with `ImageBuff` object when the image passed
to the `ImageBuff.load` function has the 3-bytes pixel format BGR.

## Class `FilterRGBA32`

Source filter RGBA32.

## Image Blending Modes

See Wikipedia's [Blend Modes](https://en.wikipedia.org/wiki/Blend_modes) for reference.

Overview. The items are in the parts below:

- [attributes](Range.texture--props.md) (101 items)
- [methods and functions](Range.texture--funcs.md) (29 items)
- [constants](Range.texture--consts.md) (32 items)
