# Range.texture - methods and functions

Part of [Range.texture](Range.texture.md).

## play()

Play (restart) video.

**Returns:** Whether the video was ready or stopped.

**Return type:** bool

## pause()

Pause video.

**Returns:** Whether the video was playing.

**Return type:** bool

## stop()

Stop video (play will replay it from start).

**Returns:** Whether the video was playing.

**Return type:** bool

## refresh(buffer=None, format="RGBA", timestamp=-1.0)

Refresh video - get its status and optionally copy the frame to an external buffer.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str
- **`timestamp`**: An optional timestamp (in seconds from the start of the movie) of the frame to be copied to the buffer.
  - type: float

**Returns:** see `FFmpeg Video and Image Status`_.

**Return type:** int

## refresh(buffer=None, format="RGBA")

Refresh image, get its status and optionally copy the frame to an external buffer.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

**Returns:** see `FFmpeg Video and Image Status`_.

**Return type:** int

## reload(newname=None)

Reload image, i.e. reopen it.

- **`newname`**: Path to a new image. (optional)
  - type: str

## load(imageBuffer, width, height)

Load image from buffer.

- **`imageBuffer`**: Buffer to load the image from.
  - type: `Buffer` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Width of the image to load.
  - type: int
- **`height`**: Height of the image to load.
  - type: int

## plot(imageBuffer, width, height, positionX, positionY, mode=IMB_BLEND_COPY)

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

## refresh(buffer=None, format="RGBA")

Refresh image - render and copy the image to an external buffer (optional)
then invalidate its current content.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is rendered and copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

## getSource(id)

Get image source.

- **`id`**: Identifier of the source to get.
  - type: str

**Returns:** Image source.

**Return type:** one of... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

## getWeight(id)

Get image source weight.

- **`id`**: Identifier of the source.
  - type: str

**Returns:** Weight of the source.

**Return type:** int

## refresh(buffer=None, format="RGBA")

Refresh image - calculate and copy the image to an external buffer (optional)
then invalidate its current content.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is calculated and copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

## setSource(id, image)

Set image source - all sources must have the same size.

- **`id`**: Identifier of the source to set.
  - type: str
- **`image`**: Image source of type... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

## setWeight(id, weight)

Set image source weight - the sum of the weights should be 256 to get full color intensity in the output.

- **`id`**: Identifier of the source.
  - type: str
- **`weight`**: Weight of the source.
  - type: int

## render()

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

## refresh()

## refresh(buffer, format="RGBA")

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

## refresh(buffer=None, format="RGBA")

Refresh video - copy the viewport to an external buffer (optional) then invalidate its current content.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown. The transfer to the buffer is optimal if no processing of the image is needed. This is the case if `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` and no filter is set.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

## play()

Kick-off the capture after creation of the object.

**Returns:** True if the capture could be started, False otherwise.

**Return type:** bool

## pause()

Temporary stops the capture. Use play() to restart it.

**Returns:** True if the capture could be paused, False otherwise.

**Return type:** bool

## stop()

Stops the capture.

**Returns:** True if the capture could be stopped, False otherwise.

**Return type:** bool

## close()

Close dynamic texture and restore original.

## refresh(refresh_source, timestamp=-1.0)

Refresh texture from source.

- **`refresh_source`**: Whether to also refresh the image source of the texture.
  - type: bool
- **`timestamp`**: If the texture controls a VideoFFmpeg object: timestamp (in seconds from the start of the movie) of the frame to be loaded; this can be used for video-sound synchonization by passing `time` to it. (optional)
  - type: float

## close()

Close the DeckLink device and release all resources. After calling this method,
the object cannot be reactivated, it must be destroyed and a new DeckLink object
created from fresh to restart the output.

## refresh(refresh_source,ts)

This method must be called frequently to update the output frame in the DeckLink device.

- **`refresh_source`**: True if the source objects image buffer should be invalidated after being used to compute the output frame. This triggers the recomputing of the source image on next refresh, which is normally the desired effect. False if the image source buffer should stay valid and reused on next refresh. Note that the DeckLink device stores the output frame and replays until a new frame is sent from the host. Thus, it is not necessary to refresh the DeckLink object if it is known that the image source has not changed.
  - type: bool
- **`ts`**: The timestamp value passed to the image source object to compute the image. If unspecified, the BGE clock is used.
  - type: float

## getLastError()

Last error that occurred in a Range.texture function.

**Returns:** The description of the last error occurred in a Range.texture function.

**Return type:** str

## imageToArray(image, mode)

Returns a `Buffer` corresponding to the current image stored in a texture source object.

- **`image`**: Image source object of type: * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`
- **`mode`**: Optional argument representing the pixel format. - You can use the characters R, G, B for the 3 color channels, A for the alpha channel, 0 to force a fixed 0 color channel and 1 to force a fixed 255 color channel. Examples: - "BGR" will return 3 bytes per pixel with the Blue, Green and Red channels in that order. - "RGB1" will return 4 bytes per pixel with the Red, Green, Blue channels in that order and the alpha channel forced to 255. - A special mode "F" allows to return the image as an array of float. This mode should only be used to retrieve the depth buffer of the class:`ImageViewport` and `ImageRender` objects. The default mode is "RGBA".
  - type: str

**Returns:** An object representing the image as one dimensional array of bytes of size (pixel_size*width*height), line by line starting from the bottom of the image. The pixel size and format is determined by the mode parameter. For mode 'F', the array is a one dimensional array of float of size (width*height).

**Return type:** `Buffer`

## materialID(object, name)

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

## setLogFile(filename)

Sets the name of a text file in which runtime error messages will be written,
in addition to the printing of the messages on the Python console.
Only the runtime errors specific to the VideoTexture module are written in that file,
ordinary runtime time errors are not written.

- **`filename`**: Name of the error log file.
  - type: str

**Returns:** -1 if the parameter name is invalid (not of type string), else 0.

**Return type:** int
