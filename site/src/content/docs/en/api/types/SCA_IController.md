---
title: "SCA_IController"
description: "Range.types.SCA_IController class reference"
---

Base class: [`SCA_ILogicBrick`](../sca_ilogicbrick/)



Base class for all controller logic bricks.

### state

The controllers state bitmask. This can be used with the GameObject's state to test if the controller is active.

**Type:** int bitmask

### sensors

A list of sensors linked to this controller.

**Type:** sequence supporting index/string lookups and iteration.

:::note
The sensors are not necessarily owned by the same object.
:::

:::note
When objects are instanced in dupligroups links may be lost from objects outside the dupligroup.
:::

### actuators

A list of actuators linked to this controller.

**Type:** sequence supporting index/string lookups and iteration.

:::note
The sensors are not necessarily owned by the same object.
:::

:::note
When objects are instanced in dupligroups links may be lost from objects outside the dupligroup.
:::

### useHighPriority

When set the controller executes always before all other controllers that dont have this set.

**Type:** boolen

:::note
Order of execution between high priority controllers is not guaranteed.
:::

