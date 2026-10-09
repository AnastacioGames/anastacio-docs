---
title: "KX_NavMeshObject"
description: "Referência da classe Range.types.KX_NavMeshObject"
---

Classe base: [`KX_GameObject`](../kx_gameobject/)



Python interface for using and controlling navigation meshes.

A navigation mesh with a Boolean game property `dynamic_navmesh` set to True is built in tiles when the game starts, so obstacles can carve it at runtime. Objects with "Create Obstacle" carve it automatically; `addObstacle` adds any other object. Paths may differ slightly from the static navigation mesh.

### dynamic

True when the navigation mesh was built in tiles and obstacles can carve it (read-only).

**Tipo:** boolean

### version

Incremented when the navigation mesh is rebuilt or finishes changing because of obstacles (read-only). Paths found with an older version may cross new obstacles.

**Tipo:** integer

### findPath(start, goal)

Finds the path from start to goal points.

- **`start`**: the start point
- **`start`**: 3D Vector
- **`goal`**: the goal point
- **`start`**: 3D Vector

**Retorna:** a path as a list of points

**Tipo do retorno:** list of points

### raycast(start, goal)

Raycast from start to goal points.

- **`start`**: the start point
- **`start`**: 3D Vector
- **`goal`**: the goal point
- **`start`**: 3D Vector

**Retorna:** the hit factor

**Tipo do retorno:** float

### draw(mode)

Draws a debug mesh for the navigation mesh. On a dynamic navigation mesh, the obstacle cylinders are drawn in yellow.

- **`mode`**: the drawing mode (one of `these constants`)
- **`mode`**: integer

**Retorna:** None

### rebuild()

Rebuild the navigation mesh.

**Retorna:** None

### addObstacle(object, radius=0.0)

Makes the object carve every dynamic navigation mesh of its scene, following it when it moves. Calling it again changes the radius. It has no effect on static navigation meshes.

- **`object`**: the obstacle, in the same scene as the navigation mesh
  - tipo: `KX_GameObject` or string
- **`radius`**: the world radius of the obstacle cylinder, 0.0 uses the object "Create Obstacle" radius or half its bounding box size
  - tipo: float

**Retorna:** None

### removeObstacle(object)

Stops the object carving the dynamic navigation meshes, including objects with "Create Obstacle".

- **`object`**: the obstacle
  - tipo: `KX_GameObject` or string

**Retorna:** None

