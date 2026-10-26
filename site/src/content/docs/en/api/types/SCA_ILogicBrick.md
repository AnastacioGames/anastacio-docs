---
title: "SCA_ILogicBrick"
description: "Range.types.SCA_ILogicBrick class reference"
---

Base class: [`EXP_Value`](../exp_value/)



Base class for all logic bricks.

### executePriority

This determines the order controllers are evaluated, and actuators are activated (lower priority is executed first).

**Type:** executePriority: int

### owner

The game object this logic brick is attached to (read-only).

**Type:** `KX_GameObject` or None in exceptional cases.

### name

The name of this logic brick (read-only).

**Type:** string

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### fireCount

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

