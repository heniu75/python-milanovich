from unittest import TestCase
from SampleFunctions import add
from hypothesis import given, example
import hypothesis.strategies as st


class TestSampleFunctions(TestCase):
    def test_add_basic_fixed(self):
        a = 10
        b = 20
        actual = add(a, b)
        self.assertTrue(30 == actual)

    @given(a=st.integers(), b=st.integers(), e=st.none())
    @example(a=0,  b=0,  e=0)
    @example(a=10, b=10, e=20)
    def test_add_numbers(self, a, b, e):
        actual = add(a, b)
        if e:
            assert(e == actual)
        else:
            assert((a+b) == actual)
