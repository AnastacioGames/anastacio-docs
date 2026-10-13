---
title: "BL_Shader"
description: "Range.types.BL_Shader class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`KX_BlenderMaterial`](../../types/kx_blendermaterial/), [`KX_2DFilter`](../../types/kx_2dfilter/)
:::



BL_Shader is a class used to compile and use custom shaders scripts. It supports vertex, fragment and geometry shader scripts.
The shader is compiled with a generated header for the three shaders scripts.
This header set the `#version` directive, so the user must not define his own `#version`.

### enabled

Set shader enabled to use.

**Type:** boolean

### objectCallbacks

The list of python callbacks executed when the shader is used to render an object.
All the functions can expect as argument the object currently rendered.

```python

def callback(object):
    print("render object %r" % object.name)
```

**Type:** list of functions and/or methods

### bindCallbacks

The list of python callbacks executed when the shader is begin used to render.

**Type:** list of functions and/or methods

### setUniformfv(name, fList)

Set a uniform with a list of float values

- **`name`**: the uniform name
  - type: string
- **`fList`**: a list (2, 3 or 4 elements) of float values
  - type: list[float]

### delSource()

Clear the shader. Use this method before the source is changed with `setSource`.

### getFragmentProg()

Returns the fragment program.

**Returns:** The fragment program.

**Return type:** string

### getVertexProg()

Get the vertex program.

**Returns:** The vertex program.

**Return type:** string

### isValid()

Check if the shader is valid.

**Returns:** True if the shader is valid

**Return type:** boolean

### setAttrib(enum)

Set attribute location. (The parameter is ignored a.t.m. and the value of "tangent" is always used.)

- **`enum`**: attribute location value
  - type: integer

### setSampler(name, index)

Set uniform texture sample index.

- **`name`**: Uniform name
  - type: string
- **`index`**: Texture sample index.
  - type: integer

### setSource(vertexProgram, fragmentProgram, apply)

Set the vertex and fragment programs

- **`vertexProgram`**: Vertex program
  - type: string
- **`fragmentProgram`**: Fragment program
  - type: string
- **`apply`**: Enable the shader.
  - type: boolean

### setSourceList(sources, apply)

Set the vertex, fragment and geometry shader programs.

- **`sources`**: Dictionary of all programs. The keys `vertex`, `fragment` and `geometry` represent shader programs of the same name. `geometry` is an optional program. This dictionary can be similar to: .. code-block:: python sources = { "vertex" : vertexProgram, "fragment" : fragmentProgram, "geometry" : geometryProgram }
  - type: dict
- **`apply`**: Enable the shader.
  - type: boolean

### setUniform1f(name, fx)

Set a uniform with 1 float value.

- **`name`**: the uniform name
  - type: string
- **`fx`**: Uniform value
  - type: float

### setUniform1i(name, ix)

Set a uniform with an integer value.

- **`name`**: the uniform name
  - type: string
- **`ix`**: the uniform value
  - type: integer

### setUniform2f(name, fx, fy)

Set a uniform with 2 float values

- **`name`**: the uniform name
  - type: string
- **`fx`**: first float value
  - type: float
- **`fy`**: second float value
  - type: float

### setUniform2i(name, ix, iy)

Set a uniform with 2 integer values

- **`name`**: the uniform name
  - type: string
- **`ix`**: first integer value
  - type: integer
- **`iy`**: second integer value
  - type: integer

### setUniform3f(name, fx, fy, fz)

Set a uniform with 3 float values.

- **`name`**: the uniform name
  - type: string
- **`fx`**: first float value
  - type: float
- **`fy`**: second float value
  - type: float
- **`fz`**: third float value
  - type: float

### setUniform3i(name, ix, iy, iz)

Set a uniform with 3 integer values

- **`name`**: the uniform name
  - type: string
- **`ix`**: first integer value
  - type: integer
- **`iy`**: second integer value
  - type: integer
- **`iz`**: third integer value
  - type: integer

### setUniform4f(name, fx, fy, fz, fw)

Set a uniform with 4 float values.

- **`name`**: the uniform name
  - type: string
- **`fx`**: first float value
  - type: float
- **`fy`**: second float value
  - type: float
- **`fz`**: third float value
  - type: float
- **`fw`**: fourth float value
  - type: float

### setUniform4i(name, ix, iy, iz, iw)

Set a uniform with 4 integer values

- **`name`**: the uniform name
  - type: string
- **`ix`**: first integer value
  - type: integer
- **`iy`**: second integer value
  - type: integer
- **`iz`**: third integer value
  - type: integer
- **`iw`**: fourth integer value
  - type: integer

### setUniformDef(name, type)

Define a new uniform

- **`name`**: the uniform name
  - type: string
- **`type`**: uniform type, one of `these constants`
  - type: integer

### setUniformMatrix3(name, mat, transpose)

Set a uniform with a 3x3 matrix value

- **`name`**: the uniform name
  - type: string
- **`mat`**: A 3x3 matrix [[f, f, f], [f, f, f], [f, f, f]]
  - type: 3x3 matrix
- **`transpose`**: set to True to transpose the matrix
  - type: boolean

### setUniformMatrix4(name, mat, transpose)

Set a uniform with a 4x4 matrix value

- **`name`**: the uniform name
  - type: string
- **`mat`**: A 4x4 matrix [[f, f, f, f], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
  - type: 4x4 matrix
- **`transpose`**: set to True to transpose the matrix
  - type: boolean

### setUniformiv(name, iList)

Set a uniform with a list of integer values

- **`name`**: the uniform name
  - type: string
- **`iList`**: a list (2, 3 or 4 elements) of integer values
  - type: list[integer]

### setUniformEyef(name)

Set a uniform with a float value that reflects the eye being render in stereo mode:
0.0 for the left eye, 0.5 for the right eye. In non stereo mode, the value of the uniform
is fixed to 0.0. The typical use of this uniform is in stereo mode to sample stereo textures
containing the left and right eye images in a top-bottom order.

- **`name`**: the uniform name
  - type: string

### validate()

Validate the shader object.

