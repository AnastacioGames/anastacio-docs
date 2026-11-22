# Range.logic - attributes

Part of [Range.logic](Range.logic.md).

## globalDict

A dictionary that is saved between loading blend files so you can use it to store inventory and other variables you want to store between scenes and blend files.
It can also be written to a file and loaded later on with the game load/save actuators.

> **Note:**
only python built in types such as int/string/bool/float/tuples/lists can be saved, GameObjects, Actuators etc will not work as expected.

## keyboard

The current keyboard wrapped in an `SCA_PythonKeyboard` object.

## mouse

The current mouse wrapped in an `SCA_PythonMouse` object.

## motion

Device motion sensors (gyroscope, accelerometer, tilt) wrapped in a `KX_PythonMotion` object.

## joysticks

A list of attached `SCA_PythonJoystick`.
The list size is the maximum number of supported joysticks.
If no joystick is available for a given slot, the slot is set to None.

## inputSystem

The input maps of the game, a `KX_InputSystem`. They are loaded from the JSON files in the KeyMapping folder, next to the game file.
