---
title: "EXP_BaseListValue"
description: "Range.types.EXP_BaseListValue class reference"
---

Class `Range.types.EXP_BaseListValue`.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### append(item)

 <small>method</small>

Adds an item at the end of the list. Only works on lists created by the script; internal engine lists (e.g. `scene.objects`) can't be changed.

### count(item)

 <small>method</small>

How many times the item appears in the list.

**Returns:** `int`

### filter(name, prop='')

 <small>method</small>

New list with only the items whose name contains `name` and that have the game property `prop`. At least one of the two must be given.

**Returns:** `EXP_ListValue`

### from_id(id)

 <small>method</small>

Finds the item by its Python `id()`. Useful to store a reference to an object as a number.

**Returns:** `object`

### get(key, default=None)

 <small>method</small>

Item with that name, or `default` if it doesn't exist. E.g. `scene.objects.get('Player')`.

**Returns:** `object`

### index(item)

 <small>method</small>

Position of the item in the list. Raises an error if it isn't there.

**Returns:** `int`

### reverse()

 <small>method</small>

Reverses the list order. Only on lists created by the script.

