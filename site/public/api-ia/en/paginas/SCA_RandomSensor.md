# SCA_RandomSensor

Base class: [`SCA_ISensor`](SCA_ISensor.md)

This sensor activates randomly.

```python
# Use a fixed seed to repeat the same sequence.
import Range

sensor = Range.logic.getCurrentController().sensors["Random"]

sensor.seed = 1234
print(sensor.lastDraw)
```

## lastDraw

The seed of the random number generator.

**Type:** integer

### seed

The seed of the random number generator.

**Type:** integer
