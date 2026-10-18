---
title: "KX_VideoActuator"
description: "Range.types.KX_VideoActuator class reference"
---

Class `Range.types.KX_VideoActuator`.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### mode

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Action on the Video Player: `0` Play, `1` Pause, `2` Toggle, `3` Stop, `4` Restart, `5` Seek.

### object

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Object with the Video Player controlled by the actuator (`KX_GameObject`, name or `None`).

### seconds

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Position in seconds used by Seek mode.

### useRelative

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

In Seek mode, if `True`, `seconds` is added to the current position instead of being absolute.

