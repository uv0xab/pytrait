from __future__ import annotations
from trait.trait import Trait

from typing import Type
from types import MethodType, FunctionType


class TraitHub:
    """ A class is extensible iff. it inherits :class:`TraitHub`.

    When the programmers add a class which inherits :class:`TraitHub`,
    any further subclass definition will trigger the trait scanning
    process. In turn, all the implementation of trait methods will be
    copied to the base class itself.

    For further documentation, please visit our wiki page at
    `Pytrait <https://github.com/uv0xab/pytrait/wiki>`_.
    """

    def __init_subclass__(cls):
        if issubclass(cls, Trait):
            """ A subclass is a trait implementation iff. it inherits both
            :class:`TraitHub` and :class:`Trait`. """
            TraitHub.__register_trait_impl(cls)

    @staticmethod
    def __register_trait_impl(cls_impl: Type[Trait]):
        """ This function registers the trait implementation so that the
        implemented methods and properties are accessible from the base
        class. """

        if len(cls_impl.__bases__) != 2:
            msg = "the trait implemention {cls_impl} should inherit " + \
                f"exactly two base classes, {cls_impl.__bases__} found"

            raise TypeError(msg)

        cls_base = TraitHub.__get_base_class(cls_impl)
        cls_trait = TraitHub.__get_trait_class(cls_impl)

        for name, item in cls_trait.__dict__.items():
            if not isinstance(item, (property, FunctionType, MethodType)):
                continue

            if hasattr(cls_base, name):
                msg = f"cannot implement the trait {cls_trait} for " + \
                    f"{cls_base} because the name {name} is used " + \
                    "in both classes"

                raise NameError(msg)

        names_to_link = set([*cls_impl.__dict__.keys(),
                             *cls_trait.__dict__.keys()])

        for name in names_to_link:
            item = getattr(cls_impl, name)
            if not isinstance(item, (property, FunctionType, MethodType)):
                """ register the method/property (implemented in cls_impl)
                to the base class cls_base """
                continue

            if not hasattr(cls_trait, name) and hasattr(cls_base, name):
                msg = f"the trait {cls_trait.__name__} overwrites " + \
                    f"the attribute '{name}' in its base class " + \
                    f" {cls_base.__name__}"

                raise NameError(msg)

            setattr(cls_base, name, item)

    @staticmethod
    def __get_base_class(cls_impl: type) -> Type[TraitHub]:
        """ Auxiliary function to get the base class of a trait implementation,
        i.e. the class which we want to extend with the specified trait. """

        for base in cls_impl.__bases__:
            if issubclass(base, TraitHub):
                return base

        raise TypeError(f"trait implementation {cls_impl} has no base class")

    @staticmethod
    def __get_trait_class(cls_impl: type) -> Type[Trait]:
        """ Auxiliary function to get the trait class of a trait
        implementation, i.e. the trait which we want to extend on the
        specified base class. """

        for cls in cls_impl.__bases__:
            if not issubclass(cls, TraitHub) and issubclass(cls, Trait):
                return cls

        raise TypeError(f"trait implementation {cls_impl} has no trait class")
