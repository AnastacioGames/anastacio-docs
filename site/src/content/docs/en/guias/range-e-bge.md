---
title: Range and bge
description: The two names of the main module and why Range has a capital R.
---

The engine API lives in the **`Range`** module, with a **capital R**. Range Engine chose the capital letter so it isn't confused with Python's `range()` function.

```python
import Range
from Range import logic, events
```

The old name **`bge`** also works. The engine registers each submodule under both names, so `Range.logic` and `bge.logic` are the same object:

```python
import bge
from bge import logic
```

This documentation uses `Range` in every example.

| Range | bge | What it is for |
|---|---|---|
| `Range.logic` | `bge.logic` | Scene, objects, time, global properties and file loading |
| `Range.types` | `bge.types` | Classes of game objects: objects, cameras, lights, sensors, actuators |
| `Range.render` | `bge.render` | Window, resolution, VSync, mouse cursor and debug drawing |
| `Range.events` | `bge.events` | Key, mouse button and input state constants |
| `Range.constraints` | `bge.constraints` | Physics joints, vehicles and physics engine settings |
| `Range.application` | `bge.application` | Application info, such as version and platform |
| `Range.texture` | `bge.texture` | Dynamic textures: video, image, camera and render to texture |
| `Range.imgui` | `bge.imgui` | Interface windows and controls for debugging |
| `Range.network` | `bge.network` | Multiplayer: connection, messages and object replication |

:::caution[Web export]
The Web validator warns `WEB-PY-001` when it finds `import bge` and suggests changing it to `import Range`.
:::
