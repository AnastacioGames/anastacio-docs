# EXP_BaseListValue

Class `Range.types.EXP_BaseListValue`.

```python
# Look for an object without an error if it does not exist.
import Range

objects = Range.logic.getCurrentScene().objects

door = objects.get("Door")
if door is not None:
    print(objects.index(door))
```

```python
# Filter by name and property. Both are regular expressions.
import Range

objects = Range.logic.getCurrentScene().objects

for enemy in objects.filter("Enemy.*", "life"):
    print(enemy.name)
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### append(item)

 `method`

Adds an item at the end of the list. Only works on lists created by the script; internal engine lists (e.g. `scene.objects`) can't be changed.

### count(item)

 `method`

How many times the item appears in the list.

**Returns:** `int`

### filter(name, prop='')

 `method`

New list with only the items whose name contains `name` and that have the game property `prop`. At least one of the two must be given.

**Returns:** `EXP_ListValue`

### from_id(id)

 `method`

Finds the item by its Python `id()`. Useful to store a reference to an object as a number.

**Returns:** `object`

### get(key, default=None)

 `method`

Item with that name, or `default` if it doesn't exist. E.g. `scene.objects.get('Player')`.

**Returns:** `object`

### index(item)

 `method`

Position of the item in the list. Raises an error if it isn't there.

**Returns:** `int`

### reverse()

 `method`

Reverses the list order. Only on lists created by the script.
