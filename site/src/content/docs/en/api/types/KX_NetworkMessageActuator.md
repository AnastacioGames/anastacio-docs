---
title: "KX_NetworkMessageActuator"
description: "Range.types.KX_NetworkMessageActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Message Actuator

```python
# Send a message to objects in the scene.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Message"]

act.subject = "door_open"
act.body = "north"
act.usePropBody = False
cont.activate(act)
```

### propName

Messages will only be sent to objects with the given property name.

**Type:** string

### subject

The subject field of the message.

**Type:** string

### body

The body of the message.

**Type:** string

### usePropBody

Send a property instead of a regular body message.

**Type:** boolean

