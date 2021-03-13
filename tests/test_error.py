from unittest import TestCase
from trait import TraitHub, Trait


class TestTraitError(TestCase):

    def test_name_conflict_1(self):

        class A(TraitHub):
            def f(self):
                return 0

        class T(Trait):
            def f(self):
                pass

        with self.assertRaises(NameError):
            class TImpl(A, T):
                pass

    def test_name_conflict_2(self):

        class A(TraitHub):
            def f(self):
                pass

        class T(Trait):
            pass

        with self.assertRaises(NameError):
            class TImpl(A, T):
                def f(self):
                    pass

    def test_invalid_trait_impl_1(self):
        class A(TraitHub):
            pass

        class T(Trait):
            pass

        with self.assertRaises(TypeError):
            class TImpl(A, T, Exception):
                pass
