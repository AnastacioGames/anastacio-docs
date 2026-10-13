---
title: "Range.texture"
description: "Range.texture module reference"
---

:::tip[See also]
[`Texture`](../../types/texture/), [`KX_BlenderMaterial`](../../types/kx_blendermaterial/), [`BL_Texture`](../../types/bl_texture/)
:::

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

### status

Video status. (readonly)

**Type:** int

**Value:** `see `FFmpeg Video and Image Status`_.`

### range

The start and stop time of the video playback, expressed in seconds from beginning.
By default the entire video.

**Type:** sequence of two floats

### repeat

Number of times to replay the video, -1 for infinite repeat.

**Type:** int

### framerate

Relative frame rate, <1.0 for slow, >1.0 for fast.

**Type:** float

### valid

Tells if an image is available. (readonly)

**Type:** bool

### image

Image data. (readonly)

**Type:** `Buffer` or None

### size

Image size. (readonly)

**Type:** tuple of two ints

### scale

Set to True to activate fast nearest neighbor scaling algorithm.
Texture width and height must be a power of 2.
If the video picture size is not a power of 2, rescaling is required.
By default `Range.texture` uses the precise but slow `gluScaleImage()` function.
Best is to rescale the video offline so that no scaling is necessary at runtime!

**Type:** bool

### flip

If True the imaged will be flipped vertically.
FFmpeg always delivers the image upside down, so this attribute is set to True by default.

**Type:** bool

### filter

An additional filter that is applied on the video before sending it to the GPU.

**Type:** one of: * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### preseek

Number of frames of preseek.

**Type:** int

### deinterlace

Deinterlace image.

**Type:** bool

### play()

Play (restart) video.

**Returns:** Whether the video was ready or stopped.

**Return type:** bool

### pause()

Pause video.

**Returns:** Whether the video was playing.

**Return type:** bool

### stop()

Stop video (play will replay it from start).

**Returns:** Whether the video was playing.

**Return type:** bool

### refresh(buffer=None, format="RGBA", timestamp=-1.0)

Refresh video - get its status and optionally copy the frame to an external buffer.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str
- **`timestamp`**: An optional timestamp (in seconds from the start of the movie) of the frame to be copied to the buffer.
  - type: float

**Returns:** see `FFmpeg Video and Image Status`_.

**Return type:** int

## Image classes

FFmpeg image source, used for image files and web based images.

- **`file`**: Path to the image to load.
  - type: str

### status

Image status. (readonly)

**Type:** int

**Value:** `see `FFmpeg Video and Image Status`_.`

### valid

Tells if an image is available. (readonly)

**Type:** bool

### image

Image data. (readonly)

**Type:** `Buffer` or None

### size

Image size. (readonly)

**Type:** tuple of two ints

### scale

Fast scale of image (near neighbour).

**Type:** bool

### flip

Flip image vertically.

**Type:** bool

### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### refresh(buffer=None, format="RGBA")

Refresh image, get its status and optionally copy the frame to an external buffer.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

**Returns:** see `FFmpeg Video and Image Status`_.

**Return type:** int

### reload(newname=None)

Reload image, i.e. reopen it.

- **`newname`**: Path to a new image. (optional)
  - type: str

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

### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### flip

Flip image vertically.

**Type:** bool

### image

Image data. (readonly)

**Type:** `Buffer` or None

### load(imageBuffer, width, height)

Load image from buffer.

- **`imageBuffer`**: Buffer to load the image from.
  - type: `Buffer` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Width of the image to load.
  - type: int
- **`height`**: Height of the image to load.
  - type: int

### plot(imageBuffer, width, height, positionX, positionY, mode=IMB_BLEND_COPY)

Update image buffer.

- **`imageBuffer`**: Buffer to load the new data from.
  - type: `Buffer`, `ImageBuff` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Width of the data to load.
  - type: int
- **`height`**: Height of the data to load.
  - type: int
- **`positionX`**: Left boundary of the region to be drawn on.
  - type: int
- **`positionY`**: Upper boundary of the region to be drawn on.
  - type: int
- **`mode`**: Drawing mode, see `Image Blending Modes`_.
  - type: int

### scale

Fast scale of image (near neighbour).

**Type:** bool

### size

Image size. (readonly)

**Type:** tuple of two ints

### valid

Tells if an image is available. (readonly)

**Type:** bool

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

### alpha

Use alpha in texture.

**Type:** bool

### horizon

Horizon color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

### zenith

Zenith color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

### background

**Type:** float list [r, g, b, a] in [0.0, 1.0]

Deprecated use :py`Range.texture.ImageMirror.horizon` or :py`Range.texture.ImageMirror.zenith` instead.

### updateShadow

Choose to force shadow buffer update if there is a gap beetween image rendered and shadows.

**Type:** bool

### colorBindCode

Off-screen color texture bind code.

**Type:** integer

### capsize

Size of render area.

**Type:** sequence of two ints

### clip

Clipping distance.

**Type:** float in [0.01, 5000.0]

### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### flip

Flip image vertically.

**Type:** bool

### image

Image data. (readonly)

**Type:** `Buffer` or None

### refresh(buffer=None, format="RGBA")

Refresh image - render and copy the image to an external buffer (optional)
then invalidate its current content.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is rendered and copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

### scale

Fast scale of image (near neighbour).

**Type:** bool

### size

Image size (readonly).

**Type:** tuple of two ints

### valid

Tells if an image is available. (readonly)

**Type:** bool

### whole

Use whole viewport to render.

**Type:** bool

Image mixer used to mix multiple image sources together.

### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### flip

Flip image vertically.

**Type:** bool

### getSource(id)

Get image source.

- **`id`**: Identifier of the source to get.
  - type: str

**Returns:** Image source.

**Return type:** one of... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

### getWeight(id)

Get image source weight.

- **`id`**: Identifier of the source.
  - type: str

**Returns:** Weight of the source.

**Return type:** int

### image

Image data. (readonly)

**Type:** `Buffer` or None

### refresh(buffer=None, format="RGBA")

Refresh image - calculate and copy the image to an external buffer (optional)
then invalidate its current content.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is calculated and copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

### scale

Fast scale of image (near neighbour).

**Type:** bool

### size

Image size. (readonly)

**Type:** tuple of two ints

### setSource(id, image)

Set image source - all sources must have the same size.

- **`id`**: Identifier of the source to set.
  - type: str
- **`image`**: Image source of type... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

### setWeight(id, weight)

Set image source weight - the sum of the weights should be 256 to get full color intensity in the output.

- **`id`**: Identifier of the source.
  - type: str
- **`weight`**: Weight of the source.
  - type: int

### valid

Tells if an image is available. (readonly)

**Type:** bool

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

### alpha

Use alpha in texture.

**Type:** bool

### horizon

Horizon color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

### zenith

Zenith color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

### background

Background color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

Deprecated use :py`Range.texture.ImageRender.horizon` or :py`Range.texture.ImageRender.zenith` instead.

### updateShadow

Choose to force shadow buffer update if there is a gap beetween image rendered and shadows.

**Type:** bool

### colorBindCode

Off-screen color texture bind code.

**Type:** integer

### capsize

Size of render area.

**Type:** sequence of two ints

### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### flip

Flip image vertically.

**Type:** bool

### image

Image data. (readonly)

**Type:** `Buffer` or None

### scale

Fast scale of image (near neighbour).

**Type:** bool

### size

Image size. (readonly)

**Type:** tuple of two ints

### valid

Tells if an image is available. (readonly)

**Type:** bool

### whole

Use whole viewport to render.

**Type:** bool

### depth

Use depth component of render as array of float - not suitable for texture source,
should only be used with Range.texture.imageToArray(mode='F').

**Type:** bool

### zbuff

Use depth component of render as grayscale color - suitable for texture source.

**Type:** bool

### render()

Render the scene but do not extract the pixels yet.
The function returns as soon as the render commands have been send to the GPU.
The render will proceed asynchronously in the GPU while the host can perform other tasks.
To complete the render, you can either call `refresh`
directly of refresh the texture of which this object is the source.
This method is useful to implement asynchronous render for optimal performance: call render()
on frame n and refresh() on frame n+1 to give as much as time as possible to the GPU
to render the frame while the game engine can perform other tasks.

**Returns:** True if the render was initiated, False if the render cannot be performed (e.g. the camera is active)

**Return type:** bool

### refresh()

### refresh(buffer, format="RGBA")

Refresh video - render and optionally copy the image to an external buffer then invalidate its current content.
The render may have been started earlier with the `render` method,
in which case this function simply waits for the render operations to complete.
When called without argument, the pixels are not extracted but the render is guaranteed
to be completed when the function returns.
This only makes sense with offscreen render on texture target (see `offScreenCreate`).

- **`buffer`**: An object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown. The transfer to the buffer is optimal if no processing of the image is needed. This is the case if `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` and no filter is set.
  - type: any buffer type of sufficient size
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

**Returns:** True if the render is complete, False if the render cannot be performed (e.g. the camera is active)

**Return type:** bool

Image source from viewport rendered by the active camera.
To render from a non active camera see `ImageRender`.

### alpha

Use alpha in texture.

**Type:** bool

### capsize

Size of viewport area being captured.

**Type:** sequence of two ints

### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### flip

Flip image vertically.

**Type:** bool

### image

Image data. (readonly)

**Type:** `Buffer` or None

### position

Upper left corner of the captured area.

**Type:** sequence of two ints

### refresh(buffer=None, format="RGBA")

Refresh video - copy the viewport to an external buffer (optional) then invalidate its current content.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown. The transfer to the buffer is optimal if no processing of the image is needed. This is the case if `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` and no filter is set.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

### scale

Fast scale of image (near neighbour).

**Type:** bool

### size

Image size. (readonly)

**Type:** tuple of two ints

### valid

Tells if an image is available. (readonly)

**Type:** bool

### whole

Use whole viewport to capture.

**Type:** bool

### depth

Use depth component of viewport as array of float - not suitable for texture source,
should only be used with `Range.texture.imageToArray(mode='F')`.

**Type:** bool

### zbuff

Use depth component of viewport as grayscale color - suitable for texture source.

**Type:** bool

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

### status

Status of the capture: 1=ready to use, 2=capturing, 3=stopped

**Type:** int

### framerate

Capture frame rate as computed from the video format.

**Type:** float

### valid

Tells if the image attribute can be used to retrieve the image.
Always False in this implementation (the image is not available at python level)

**Type:** bool

### image

The image data. Always None in this implementation.

**Type:** `Buffer` or None

### size

The size of the frame in pixel.
Stereo frames have double the height of the video frame, i.e. 3D is delivered to the GPU
as a single image in top-bottom order, left eye on top.

**Type:** (int,int)

### scale

Not used in this object.

**Type:** bool

### flip

Not used in this object.

**Type:** bool

### filter

Not used in this object.

### play()

Kick-off the capture after creation of the object.

**Returns:** True if the capture could be started, False otherwise.

**Return type:** bool

### pause()

Temporary stops the capture. Use play() to restart it.

**Returns:** True if the capture could be paused, False otherwise.

**Return type:** bool

### stop()

Stops the capture.

**Returns:** True if the capture could be stopped, False otherwise.

**Return type:** bool

## Texture classes

Class that creates the `Texture` object that loads the dynamic texture on the GPU.

- **`gameObj`**: Game object to be created a video texture on.
  - type: `KX_GameObject`
- **`materialID`**: Material ID default, 0 is the first material. (optional)
  - type: int
- **`textureID`**: Texture index in case of multi-texture channel, 0 = first channel by default. In case of UV texture, this parameter should always be 0. (optional)
  - type: int
- **`textureObj`**: Reference to another `Texture` object with shared bindId which he user might want to reuse the texture. If this argument is used, you should not create any source on this texture and there is no need to refresh it either: the other `Texture` object will provide the texture for both materials/textures.(optional)
  - type: `Texture`

### bindId

OpenGL Bind Name. (readonly)

**Type:** int

### close()

Close dynamic texture and restore original.

### mipmap

Mipmap texture.

**Type:** bool

### refresh(refresh_source, timestamp=-1.0)

Refresh texture from source.

- **`refresh_source`**: Whether to also refresh the image source of the texture.
  - type: bool
- **`timestamp`**: If the texture controls a VideoFFmpeg object: timestamp (in seconds from the start of the movie) of the frame to be loaded; this can be used for video-sound synchonization by passing `time` to it. (optional)
  - type: float

### source

Source of texture.

**Type:** one of... * `VideoFFmpeg` * `VideoDeckLink` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

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

### source

This attribute must be set to one of the image sources. If the image size does not fit exactly
the frame size, the extend attribute determines what to do.

For best performance, the source image should match exactly the size of the output frame.
A further optimization is achieved if the image source object is ImageViewport or ImageRender
set for whole viewport, flip disabled and no filter: the GL frame buffer is copied directly
to the image buffer and directly from there to the DeckLink card (hence no buffer to buffer
copy inside VideoTexture).

**Type:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

### right

If the video format is stereo 3D, this attribute should be set to an image source object
that will produce the right eye images.  If the goal is to render the BGE scene in 3D,
it can be achieved with 2 cameras, one for each eye, used by 2 ImageRender with an offscreen
render buffer that is just the size of the video frame.

**Type:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

### keying

Specify if keying is enabled. False (default): the output frame is sent unmodified on
the output interface (in that case no input video is required). True: the output frame
is mixed with the input video, using the alpha channel to blend the two images and the
combination is sent on the output interface.

**Type:** bool

### level

If keying is enabled, sets the keying level from 0 to 255. This value is a global alpha value
that multiplies the alpha channel of the image source. Use 255 (the default) to keep the alpha
channel unmodified, 0 to make the output frame totally transparent.

**Type:** int

### extend

Determines how the image source should be mapped if the size does not fit the video frame size.
* False (the default): map the image pixel by pixel.
If the image size is smaller than the frame size, extra space around the image is filled with
0-alpha black. If it is larger, the image is cropped to fit the frame size.
* True: the image is scaled by the nearest neighbor algorithm to fit the frame size.
The scaling is fast but poor quality. For best results, always adjust the image source to
match the size of the output video.

**Type:** bool

### close()

Close the DeckLink device and release all resources. After calling this method,
the object cannot be reactivated, it must be destroyed and a new DeckLink object
created from fresh to restart the output.

### refresh(refresh_source,ts)

This method must be called frequently to update the output frame in the DeckLink device.

- **`refresh_source`**: True if the source objects image buffer should be invalidated after being used to compute the output frame. This triggers the recomputing of the source image on next refresh, which is normally the desired effect. False if the image source buffer should stay valid and reused on next refresh. Note that the DeckLink device stores the output frame and replays until a new frame is sent from the host. Thus, it is not necessary to refresh the DeckLink object if it is known that the image source has not changed.
  - type: bool
- **`ts`**: The timestamp value passed to the image source object to compute the image. If unspecified, the BGE clock is used.
  - type: float

## Filter classes

Source filter BGR24.

Filter for Blue Screen.
The RGB channels of the color are left unchanged, while the output alpha is obtained as follows:

- if the square of the euclidian distance between the RGB color
and the filter's reference color is smaller than the filter's lower limit,
the output alpha is set to 0;
- if that square is bigger than the filter's upper limit, the output alpha is set to 255;
- otherwise the output alpha is linarly extrapoled between 0 and 255 in the interval of the limits.

### color

Reference color.

**Type:** sequence of three ints

**default:** (0, 0, 255)

### limits

Reference color limits.

**Type:** sequence of two ints

**default:** (64, 64)

### previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

Filter for color calculations.
The output color is obtained by multiplying the reduced 4x4 matrix with the input color
and adding the remaining column to the result.

### matrix

Matrix [4][5] for color calculation.

**Type:** sequence of four sequences of five ints

**default:** ((256, 0, 0, 0, 0), (0, 256, 0, 0, 0), (0, 0, 256, 0, 0), (0, 0, 0, 256, 0))

### previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

Filter for grayscale effect.
Proportions of R, G and B contributions in the output grayscale are 28:151:77.

### previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

Filter for levels calculations. Each output color component is obtained as follows:

* if it is smaller than its corresponding min value, it is set to 0;

* if it is bigger than its corresponding max value, it is set to 255;

* Otherwise it is linearly extrapoled between 0 and 255 in the (min, max) interval.

### levels

Levels matrix [4] (min, max).

**Type:** sequence of four sequences of two ints

**default:** ((0, 255), (0, 255), (0, 255), (0, 255))

### previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

Normal map filter.

### colorIdx

Index of color used to calculate normal (0 - red, 1 - green, 2 - blue, 3 - alpha).

**Type:** int in [0, 3]

**default:** 0

### depth

Depth of relief.

**Type:** float

**default:** 4.0

### previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

Returns a new input filter object to be used with `ImageBuff` object when the image passed
to the `ImageBuff.load` function has the 3-bytes pixel format BGR.

Source filter RGBA32.

## Functions

### getLastError()

Last error that occurred in a Range.texture function.

**Returns:** The description of the last error occurred in a Range.texture function.

**Return type:** str

### imageToArray(image, mode)

Returns a `Buffer` corresponding to the current image stored in a texture source object.

- **`image`**: Image source object of type: * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`
- **`mode`**: Optional argument representing the pixel format. - You can use the characters R, G, B for the 3 color channels, A for the alpha channel, 0 to force a fixed 0 color channel and 1 to force a fixed 255 color channel. Examples: - "BGR" will return 3 bytes per pixel with the Blue, Green and Red channels in that order. - "RGB1" will return 4 bytes per pixel with the Red, Green, Blue channels in that order and the alpha channel forced to 255. - A special mode "F" allows to return the image as an array of float. This mode should only be used to retrieve the depth buffer of the class:`ImageViewport` and `ImageRender` objects. The default mode is "RGBA".
  - type: str

**Returns:** An object representing the image as one dimensional array of bytes of size (pixel_size*width*height), line by line starting from the bottom of the image. The pixel size and format is determined by the mode parameter. For mode 'F', the array is a one dimensional array of float of size (width*height).

**Return type:** `Buffer`

### materialID(object, name)

Returns a numeric value that can be used in `Texture` to create a dynamic texture.

The value corresponds to an internal material number that uses the texture identified
by name. name is a string representing a texture name with `IM` prefix if you want to
identify the texture directly. This method works for basic tex face and for material,
provided the material has a texture channel using that particular texture in first
position of the texture stack. name can also have `MA` prefix if you want to identify
the texture by material. In that case the material must have a texture channel in first
position.

If the object has no material that matches name, it generates a runtime error.
Use try/except to catch the exception.

Ex: `Range.texture.materialID(obj, 'IMvideo.png')`

- **`object`**: The game object that uses the texture you want to make dynamic.
  - type: `KX_GameObject`
- **`name`**: Name of the texture/material you want to make dynamic.
  - type: str

**Returns:** The internal material number.

**Return type:** int

### setLogFile(filename)

Sets the name of a text file in which runtime error messages will be written,
in addition to the printing of the messages on the Python console.
Only the runtime errors specific to the VideoTexture module are written in that file,
ordinary runtime time errors are not written.

- **`filename`**: Name of the error log file.
  - type: str

**Returns:** -1 if the parameter name is invalid (not of type string), else 0.

**Return type:** int

## Constants

## FFmpeg Video and Image Status

### SOURCE_ERROR

### SOURCE_EMPTY

### SOURCE_READY

### SOURCE_PLAYING

### SOURCE_STOPPED

## Image Blending Modes

See Wikipedia's [Blend Modes](https://en.wikipedia.org/wiki/Blend_modes) for reference.

### IMB_BLEND_MIX

### IMB_BLEND_ADD

### IMB_BLEND_SUB

### IMB_BLEND_MUL

### IMB_BLEND_LIGHTEN

### IMB_BLEND_DARKEN

### IMB_BLEND_ERASE_ALPHA

### IMB_BLEND_ADD_ALPHA

### IMB_BLEND_OVERLAY

### IMB_BLEND_HARDLIGHT

### IMB_BLEND_COLORBURN

### IMB_BLEND_LINEARBURN

### IMB_BLEND_COLORDODGE

### IMB_BLEND_SCREEN

### IMB_BLEND_SOFTLIGHT

### IMB_BLEND_PINLIGHT

### IMB_BLEND_VIVIDLIGHT

### IMB_BLEND_LINEARLIGHT

### IMB_BLEND_DIFFERENCE

### IMB_BLEND_EXCLUSION

### IMB_BLEND_HUE

### IMB_BLEND_SATURATION

### IMB_BLEND_LUMINOSITY

### IMB_BLEND_COLOR

### IMB_BLEND_COPY

### IMB_BLEND_COPY_RGB

### IMB_BLEND_COPY_ALPHA

