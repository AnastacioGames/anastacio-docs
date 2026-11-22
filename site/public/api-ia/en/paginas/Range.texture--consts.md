# Range.texture - constants

Part of [Range.texture](Range.texture.md).

## SOURCE_ERROR

Video or image source status: error opening or reading the file or device (value -1). One of the possible values of `status`.

## SOURCE_EMPTY

Source status: nothing loaded yet (value 0). One of the possible values of `status`.

## SOURCE_READY

Source status: loaded and ready to play (value 1). One of the possible values of `status`.

## SOURCE_PLAYING

Source status: playing (value 2). One of the possible values of `status`.

## SOURCE_STOPPED

Source status: stopped or paused after playing (value 3). One of the possible values of `status`.

## IMB_BLEND_MIX

Blend mode for the `mode` argument of `ImageBuff.plot`. Normal mix: the source is laid over the destination according to its alpha. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_ADD

Blend mode for the `mode` argument of `ImageBuff.plot`. Adds the source colors to the destination (max 255). The destination alpha is unchanged. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_SUB

Blend mode for the `mode` argument of `ImageBuff.plot`. Subtracts the source colors from the destination (min 0). The destination alpha is unchanged. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_MUL

Blend mode for the `mode` argument of `ImageBuff.plot`. Multiplies the destination colors by the source, which darkens. The destination alpha is unchanged. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_LIGHTEN

Blend mode for the `mode` argument of `ImageBuff.plot`. Keeps the lighter of source and destination in each color channel. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_DARKEN

Blend mode for the `mode` argument of `ImageBuff.plot`. Keeps the darker of source and destination in each color channel. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_ERASE_ALPHA

Blend mode for the `mode` argument of `ImageBuff.plot`. Leaves the colors alone: lowers the destination alpha by the source alpha, which erases the region. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_ADD_ALPHA

Blend mode for the `mode` argument of `ImageBuff.plot`. Leaves the colors alone: raises the destination alpha by the source alpha (max 255). The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_OVERLAY

Blend mode for the `mode` argument of `ImageBuff.plot`. Overlay, as in image editors: multiplies in the destination shadows and screens in the highlights. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_HARDLIGHT

Blend mode for the `mode` argument of `ImageBuff.plot`. Hard Light, as in image editors. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_COLORBURN

Blend mode for the `mode` argument of `ImageBuff.plot`. Color Burn, as in image editors: darkens the destination. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_LINEARBURN

Blend mode for the `mode` argument of `ImageBuff.plot`. Linear Burn: adds source and destination and subtracts 255 (min 0), which darkens. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_COLORDODGE

Blend mode for the `mode` argument of `ImageBuff.plot`. Color Dodge, as in image editors: lightens the destination. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_SCREEN

Blend mode for the `mode` argument of `ImageBuff.plot`. Screen: inverts, multiplies and inverts again, which lightens. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_SOFTLIGHT

Blend mode for the `mode` argument of `ImageBuff.plot`. Soft Light, as in image editors: a gentle version of overlay. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_PINLIGHT

Blend mode for the `mode` argument of `ImageBuff.plot`. Pin Light, as in image editors. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_VIVIDLIGHT

Blend mode for the `mode` argument of `ImageBuff.plot`. Vivid Light, as in image editors. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_LINEARLIGHT

Blend mode for the `mode` argument of `ImageBuff.plot`. Linear Light, as in image editors. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_DIFFERENCE

Blend mode for the `mode` argument of `ImageBuff.plot`. Difference: absolute difference between source and destination in each channel. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_EXCLUSION

Blend mode for the `mode` argument of `ImageBuff.plot`. Exclusion: similar to difference, with lower contrast. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_HUE

Blend mode for the `mode` argument of `ImageBuff.plot`. Takes the hue from the source and keeps the destination saturation and value. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_SATURATION

Blend mode for the `mode` argument of `ImageBuff.plot`. Takes the saturation from the source and keeps the destination hue and value. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_LUMINOSITY

Blend mode for the `mode` argument of `ImageBuff.plot`. Takes the value (brightness) from the source and keeps the destination hue and saturation. The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_COLOR

Blend mode for the `mode` argument of `ImageBuff.plot`. Takes hue and saturation from the source and keeps the destination value (brightness). The effect is weighted by the source image alpha; where it is 0, nothing changes.

## IMB_BLEND_COPY

Blend mode for the `mode` argument of `ImageBuff.plot` (default): copies the source over the destination, RGB and alpha, with no blending.

## IMB_BLEND_COPY_RGB

Blend mode for the `mode` argument of `ImageBuff.plot`: copies only the source colors (RGB) and keeps the destination alpha.

## IMB_BLEND_COPY_ALPHA

Blend mode for the `mode` argument of `ImageBuff.plot`: copies only the source alpha and keeps the destination colors.
