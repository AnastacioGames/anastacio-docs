---
title: "KX_TrackToActuator"
description: "Range.types.KX_TrackToActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Edit Object actuator in Track To mode.

:::caution
Track To Actuators will be ignored if at game start, the object to track to is invalid.

This will generate a warning in the console:

```text

GameObject 'Name' no object in EditObjectActuator 'ActuatorName'
```
:::

### object

the object this actuator tracks.

**Type:** `KX_GameObject` or None

### time

the time in frames with which to delay the tracking motion.

**Type:** integer

### use3D

the tracking motion to use 3D.

**Type:** boolean

### upAxis

The axis that points upward.

**Type:** integer from 0 to 2

* KX_TRACK_UPAXIS_POS_X
* KX_TRACK_UPAXIS_POS_Y
* KX_TRACK_UPAXIS_POS_Z

### trackAxis

The axis that points to the target object.

**Type:** integer from 0 to 5

* KX_TRACK_TRAXIS_POS_X
* KX_TRACK_TRAXIS_POS_Y
* KX_TRACK_TRAXIS_POS_Z
* KX_TRACK_TRAXIS_NEG_X
* KX_TRACK_TRAXIS_NEG_Y
* KX_TRACK_TRAXIS_NEG_Z

