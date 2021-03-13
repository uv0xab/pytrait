from unittest import TestCase
from trait import TraitHub, Trait


class TestCorrectTraitImpl(TestCase):

    def test_1(self):

        class A(TraitHub):
            pass

        class T(Trait):
            def method(self) -> int:
                pass

        class TImplForA(A, T):
            def method(self) -> int:
                return 0

        self.assertEqual(A().method(), 0)

    def test_pre_created_obj_1(self):

        class A(TraitHub):
            pass

        a = A()

        class T(Trait):
            def method(self) -> int:
                pass

        class TImplForA(A, T):
            def method(self) -> int:
                return 0

        self.assertEqual(a.method(), 0)
