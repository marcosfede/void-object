# void-object
Python Void Object

### Example use case:

```python
from void_object import Void

void = Void()

void.this_method_does_not_exist()
void.random_attribute
void['asd'][1]
with void as ctx:
    ctx.asd()

```