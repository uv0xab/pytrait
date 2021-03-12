pytrait
=======

The project aims to support the *trait* approach to extend classes
while do not hijack into their definitions. Besides, it should be
type-checkable under modern python3 type checkers, e.g. mypy.


Examples
--------

*example 1*

```python
class Trait1(Trait):
    def method1(self):
        pass


class A(TraitHub):
    pass


class ATrait1Impl(A, Trait1):
    def method1(self):
        return "some thing"


# test ;)
print(A().method1())

```
