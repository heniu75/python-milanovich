from unittest import TestCase
from SampleFunctions import add
from hypothesis import given, example, assume
import hypothesis.strategies as st


# example how to limit test input using assume
@given(st.integers(), st.integers())
def test_my_test_filtering_using_assume(a, b):
    assume(a > -1)
    print(f"Running test_my_test_filtering_using_assume({a}, {b})")
    assert(1 == 1)


# example how to limit test input using assume
@given(st.integers(0, 1000), st.integers(-1000, 0))
def test_my_test_filtering_using_strategy_args(a, b):
    print(f"Running test_my_test_filtering_using_strategy_args({a}, {b})")
    assert(1 == 1)


# example how to limit test input using assume
@given(st.integers().filter(lambda x: 0 < x < 1001), st.integers())
def test_my_test_filtering_using_lambda_filters(a, b):
    assume(a > -1)
    print(f"Running test_my_test_filtering_using_lambda_filters({a}, {b})")
    assert(1 == 1)


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

    # @given(a=st.integers(), b=st.integers(), c=st.just(30))
    # # @given(a=st.just(10), b=st.just(20), c=st.just(30))
    # #  @example(a=10, b=20, c=30)
    # def test_my_py_test(self, a, b, c):
    #     # a = 10
    #     # b = 20
    #     # c = 30
    #     print(f"Running test_my_py_test({a}, {b}, {c})")
    #     actual = add(a, b)
    #     assert(c == actual)


# example to show how to limit a test to a specific set of inputs
myValue = [10, 10]
myOtherValue = [10, 30]
myAnswers = [20, 40]


@given(st.just(myValue), st.just(myOtherValue), st.just(myAnswers))
def test_my_test2(a, b, c):
    print(f"Running test_my_test2({a}, {b}, {c})")
    for idx in range(len(myValue)):
        a1 = a[idx]
        b1 = b[idx]
        c1 = c[idx]
        print(f"Running subtest of test_my_test2({a1}, {b1}, {c1})")
        assert(a1 + b1 == c1)