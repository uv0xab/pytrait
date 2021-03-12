from __future__ import annotations
from trait.trait import Trait

from typing import Type
from types import MethodType, FunctionType


class TraitHub:
    """ A class is extensible iff. it implements :class:`TraitHub`. """

    def __init_subclass__(cls):
        if issubclass(cls, Trait):
            TraitHub.__register_trait_impl(cls)

    @staticmethod
    def __register_trait_impl(cls_impl: Type[Trait]):
        cls_base = TraitHub.__get_base_class(cls_impl)
        cls_trait = TraitHub.__get_trait_class(cls_impl)

        for name, item in cls_impl.__dict__.items():
            if isinstance(item, (property, FunctionType, MethodType)):
                """ register the method/property (implemented in cls_impl)
                to the base class cls_base """

                if not hasattr(cls_trait, name) and hasattr(cls_base, name):
                    assert False, "name conflict between impl class and base class"

                setattr(cls_base, name, item)

    def __get_base_class(cls_impl: type) -> Type[TraitHub]:
        for base in cls_impl.__bases__:
            if issubclass(base, TraitHub):
                return base

    def __get_trait_class(cls_impl: type) -> Type[Trait]:
        for cls in cls_impl.__bases__:
            if not issubclass(cls, TraitHub) and issubclass(cls, Trait):
                return cls
