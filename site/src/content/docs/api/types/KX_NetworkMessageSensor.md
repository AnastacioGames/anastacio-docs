---
title: "KX_NetworkMessageSensor"
description: "Referência da classe Range.types.KX_NetworkMessageSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



The Message Sensor logic brick.

Currently only loopback (local) networks are supported.

### subject

The subject the sensor is looking for.

**Tipo:** string

### frameMessageCount

The number of messages received since the last frame. (read-only).

**Tipo:** integer

### subjects

The list of message subjects received. (read-only).

**Tipo:** list of strings

### bodies

The list of message bodies received. (read-only).

**Tipo:** list of strings

