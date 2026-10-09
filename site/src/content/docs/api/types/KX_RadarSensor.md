---
title: "KX_RadarSensor"
description: "Referência da classe Range.types.KX_RadarSensor"
---

Classe base: [`KX_NearSensor`](../kx_nearsensor/)



Radar sensor is a near sensor with a conical sensor object.

### coneOrigin

The origin of the cone with which to test. The origin is in the middle of the cone. (read-only).

**Tipo:** `mathutils.Vector`

### coneTarget

The center of the bottom face of the cone with which to test. (read-only).

**Tipo:** `mathutils.Vector`

### distance

The height of the cone with which to test.

**Tipo:** float

### angle

The angle of the cone (in degrees) with which to test.

**Tipo:** float

### axis

The axis on which the radar cone is cast.

**Tipo:** integer from 0 to 5

KX_RADAR_AXIS_POS_X, KX_RADAR_AXIS_POS_Y, KX_RADAR_AXIS_POS_Z,
KX_RADAR_AXIS_NEG_X, KX_RADAR_AXIS_NEG_Y, KX_RADAR_AXIS_NEG_Z

