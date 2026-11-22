# Range.texture - attributes

Part of [Range.texture](Range.texture.md).

## status

Video status. (readonly)

**Type:** int

**Value:** `see `FFmpeg Video and Image Status`_.`

## range

The start and stop time of the video playback, expressed in seconds from beginning.
By default the entire video.

**Type:** sequence of two floats

## repeat

Number of times to replay the video, -1 for infinite repeat.

**Type:** int

## framerate

Relative frame rate, <1.0 for slow, >1.0 for fast.

**Type:** float

## valid

Tells if an image is available. (readonly)

**Type:** bool

## image

Image data. (readonly)

**Type:** `Buffer` or None

## size

Image size. (readonly)

**Type:** tuple of two ints

## scale

Set to True to activate fast nearest neighbor scaling algorithm.
Texture width and height must be a power of 2.
If the video picture size is not a power of 2, rescaling is required.
By default `Range.texture` uses the precise but slow `gluScaleImage()` function.
Best is to rescale the video offline so that no scaling is necessary at runtime!

**Type:** bool

## flip

If True the imaged will be flipped vertically.
FFmpeg always delivers the image upside down, so this attribute is set to True by default.

**Type:** bool

## filter

An additional filter that is applied on the video before sending it to the GPU.

**Type:** one of: * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## preseek

Number of frames of preseek.

**Type:** int

## deinterlace

Deinterlace image.

**Type:** bool

## status

Image status. (readonly)

**Type:** int

**Value:** `see `FFmpeg Video and Image Status`_.`

## valid

Tells if an image is available. (readonly)

**Type:** bool

## image

Image data. (readonly)

**Type:** `Buffer` or None

## size

Image size. (readonly)

**Type:** tuple of two ints

## scale

Fast scale of image (near neighbour).

**Type:** bool

## flip

Flip image vertically.

**Type:** bool

## filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## flip

Flip image vertically.

**Type:** bool

## image

Image data. (readonly)

**Type:** `Buffer` or None

## scale

Fast scale of image (near neighbour).

**Type:** bool

## size

Image size. (readonly)

**Type:** tuple of two ints

## valid

Tells if an image is available. (readonly)

**Type:** bool

## alpha

Use alpha in texture.

**Type:** bool

## horizon

Horizon color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

## zenith

Zenith color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

## background

**Type:** float list [r, g, b, a] in [0.0, 1.0]

Deprecated use :py`Range.texture.ImageMirror.horizon` or :py`Range.texture.ImageMirror.zenith` instead.

## updateShadow

Choose to force shadow buffer update if there is a gap beetween image rendered and shadows.

**Type:** bool

## colorBindCode

Off-screen color texture bind code.

**Type:** integer

## capsize

Size of render area.

**Type:** sequence of two ints

## clip

Clipping distance.

**Type:** float in [0.01, 5000.0]

## filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## flip

Flip image vertically.

**Type:** bool

## image

Image data. (readonly)

**Type:** `Buffer` or None

## scale

Fast scale of image (near neighbour).

**Type:** bool

## size

Image size (readonly).

**Type:** tuple of two ints

## valid

Tells if an image is available. (readonly)

**Type:** bool

## whole

Use whole viewport to render.

**Type:** bool

## filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## flip

Flip image vertically.

**Type:** bool

## image

Image data. (readonly)

**Type:** `Buffer` or None

## scale

Fast scale of image (near neighbour).

**Type:** bool

## size

Image size. (readonly)

**Type:** tuple of two ints

## valid

Tells if an image is available. (readonly)

**Type:** bool

## alpha

Use alpha in texture.

**Type:** bool

## horizon

Horizon color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

## zenith

Zenith color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

## background

Background color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

Deprecated use :py`Range.texture.ImageRender.horizon` or :py`Range.texture.ImageRender.zenith` instead.

## updateShadow

Choose to force shadow buffer update if there is a gap beetween image rendered and shadows.

**Type:** bool

## colorBindCode

Off-screen color texture bind code.

**Type:** integer

## capsize

Size of render area.

**Type:** sequence of two ints

## filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## flip

Flip image vertically.

**Type:** bool

## image

Image data. (readonly)

**Type:** `Buffer` or None

## scale

Fast scale of image (near neighbour).

**Type:** bool

## size

Image size. (readonly)

**Type:** tuple of two ints

## valid

Tells if an image is available. (readonly)

**Type:** bool

## whole

Use whole viewport to render.

**Type:** bool

## depth

Use depth component of render as array of float - not suitable for texture source,
should only be used with Range.texture.imageToArray(mode='F').

**Type:** bool

## zbuff

Use depth component of render as grayscale color - suitable for texture source.

**Type:** bool

## alpha

Use alpha in texture.

**Type:** bool

## capsize

Size of viewport area being captured.

**Type:** sequence of two ints

## filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## flip

Flip image vertically.

**Type:** bool

## image

Image data. (readonly)

**Type:** `Buffer` or None

## position

Upper left corner of the captured area.

**Type:** sequence of two ints

## scale

Fast scale of image (near neighbour).

**Type:** bool

## size

Image size. (readonly)

**Type:** tuple of two ints

## valid

Tells if an image is available. (readonly)

**Type:** bool

## whole

Use whole viewport to capture.

**Type:** bool

## depth

Use depth component of viewport as array of float - not suitable for texture source,
should only be used with `Range.texture.imageToArray(mode='F')`.

**Type:** bool

## zbuff

Use depth component of viewport as grayscale color - suitable for texture source.

**Type:** bool

## status

Status of the capture: 1=ready to use, 2=capturing, 3=stopped

**Type:** int

## framerate

Capture frame rate as computed from the video format.

**Type:** float

## valid

Tells if the image attribute can be used to retrieve the image.
Always False in this implementation (the image is not available at python level)

**Type:** bool

## image

The image data. Always None in this implementation.

**Type:** `Buffer` or None

## size

The size of the frame in pixel.
Stereo frames have double the height of the video frame, i.e. 3D is delivered to the GPU
as a single image in top-bottom order, left eye on top.

**Type:** (int,int)

## scale

Not used in this object.

**Type:** bool

## flip

Not used in this object.

**Type:** bool

## filter

Not used in this object.

## bindId

OpenGL Bind Name. (readonly)

**Type:** int

## mipmap

Mipmap texture.

**Type:** bool

## source

Source of texture.

**Type:** one of... * `VideoFFmpeg` * `VideoDeckLink` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

## source

This attribute must be set to one of the image sources. If the image size does not fit exactly
the frame size, the extend attribute determines what to do.

For best performance, the source image should match exactly the size of the output frame.
A further optimization is achieved if the image source object is ImageViewport or ImageRender
set for whole viewport, flip disabled and no filter: the GL frame buffer is copied directly
to the image buffer and directly from there to the DeckLink card (hence no buffer to buffer
copy inside VideoTexture).

**Type:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

## right

If the video format is stereo 3D, this attribute should be set to an image source object
that will produce the right eye images.  If the goal is to render the BGE scene in 3D,
it can be achieved with 2 cameras, one for each eye, used by 2 ImageRender with an offscreen
render buffer that is just the size of the video frame.

**Type:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

## keying

Specify if keying is enabled. False (default): the output frame is sent unmodified on
the output interface (in that case no input video is required). True: the output frame
is mixed with the input video, using the alpha channel to blend the two images and the
combination is sent on the output interface.

**Type:** bool

## level

If keying is enabled, sets the keying level from 0 to 255. This value is a global alpha value
that multiplies the alpha channel of the image source. Use 255 (the default) to keep the alpha
channel unmodified, 0 to make the output frame totally transparent.

**Type:** int

## extend

Determines how the image source should be mapped if the size does not fit the video frame size.
* False (the default): map the image pixel by pixel.
If the image size is smaller than the frame size, extra space around the image is filled with
0-alpha black. If it is larger, the image is cropped to fit the frame size.
* True: the image is scaled by the nearest neighbor algorithm to fit the frame size.
The scaling is fast but poor quality. For best results, always adjust the image source to
match the size of the output video.

**Type:** bool

## color

Reference color.

**Type:** sequence of three ints

**default:** (0, 0, 255)

## limits

Reference color limits.

**Type:** sequence of two ints

**default:** (64, 64)

## previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## matrix

Matrix [4][5] for color calculation.

**Type:** sequence of four sequences of five ints

**default:** ((256, 0, 0, 0, 0), (0, 256, 0, 0, 0), (0, 0, 256, 0, 0), (0, 0, 0, 256, 0))

## previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## levels

Levels matrix [4] (min, max).

**Type:** sequence of four sequences of two ints

**default:** ((0, 255), (0, 255), (0, 255), (0, 255))

## previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

## colorIdx

Index of color used to calculate normal (0 - red, 1 - green, 2 - blue, 3 - alpha).

**Type:** int in [0, 3]

**default:** 0

## depth

Depth of relief.

**Type:** float

**default:** 4.0

## previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`
