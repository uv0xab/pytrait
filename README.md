pytrait
=======

The project aims to support the *trait* approach to extend classes
while do not hijack into their definitions. Besides, it should be
type-checkable under modern python3 type checkers, e.g. mypy.

Installation
------------

For now the package is not available from *pypi*, hence you need to
manually install from github, by

    pip install wheel
    pip install git+https://github.com/uv0xab/pytrait.git


What Can I Do Using *pytrait*?
------------------------------

Developers, especially working on large-scale python projects, would
be happy if implementation of certain features can be separated from
the original definitions of these objects. This obviously avoid
mixture between data models and the business logic upon them.

### A Motivating Example

```python
from trait import TraitHub


class Model1(TraitHub):
    # in package p1.p11, very stable, rarely modified
    pass

class Model2(TraitHub):
    # in package p2.p22, very stable, rarely modified
    pass

class JsonSerializable(Trait):
    def to_json(self) -> str:
        pass

class Model1JsonSerializable(Model1, JsonSerializable):
    def to_json(self) -> str:
        # blabla ...
        pass

class Model2JsonSerializable(Model1, JsonSerializable):
    def to_json(self) -> str:
        # blabla ...
        pass
```
