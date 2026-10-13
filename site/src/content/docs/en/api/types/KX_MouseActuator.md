---
title: "KX_MouseActuator"
description: "Range.types.KX_MouseActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



The mouse actuator gives control over the visibility of the mouse cursor and rotates the parent object according to mouse movement.

### reset()

Undoes the rotation caused by the mouse actuator.

### visible

The visibility of the mouse cursor.

**Type:** boolean

### use_axis_x

Mouse movement along the x axis effects object rotation.

**Type:** boolean

### use_axis_y

Mouse movement along the y axis effects object rotation.

**Type:** boolean

### threshold

Amount of movement from the mouse required before rotation is triggered.

**Type:** `mathutils.Vector`

The values in the list should be between 0.0 and 0.5.

### reset_x

Mouse is locked to the center of the screen on the x axis.

**Type:** boolean

### reset_y

Mouse is locked to the center of the screen on the y axis.

**Type:** boolean

### object_axis

The object's 3D axis to rotate with the mouse movement. ([x, y])

**Type:** list (vector of 2 integers from 0 to 2)

* KX_ACT_MOUSE_OBJECT_AXIS_X
* KX_ACT_MOUSE_OBJECT_AXIS_Y
* KX_ACT_MOUSE_OBJECT_AXIS_Z

### local_x

Rotation caused by mouse movement along the x axis is local.

**Type:** boolean

### local_y

Rotation caused by mouse movement along the y axis is local.

**Type:** boolean

### sensitivity

The amount of rotation caused by mouse movement along the x and y axis.

**Type:** `mathutils.Vector`

Negative values invert the rotation.

### limit_x

The minimum and maximum angle of rotation caused by mouse movement along the x axis in degrees.
limit_x[0] is minimum, limit_x[1] is maximum.

**Type:** `mathutils.Vector`

### limit_y

The minimum and maximum angle of rotation caused by mouse movement along the y axis in degrees.
limit_y[0] is minimum, limit_y[1] is maximum.

**Type:** `mathutils.Vector`

### angle

The current rotational offset caused by the mouse actuator in degrees.

**Type:** `mathutils.Vector`

