from unittest import TestCase

from pycommons.lang import ArrayUtils
from tests.parametrized import cases, TestData


class TestArrayUtils(TestCase):
    @cases(
        TestData(expected=0, data=[]),
        TestData(expected=3, data=[1, 2, 4]),
        TestData(expected=0, data=None),
        TestData(expected=4, data="test"),
    )
    def test_get_length(self, test_data: TestData):
        self.assertEqual(test_data.expected, ArrayUtils.get_length(test_data.data))

    @cases(
        TestData(expected=True, data=[]),
        TestData(expected=False, data=[1, 2, 4]),
        TestData(expected=True, data=None),
        TestData(expected=False, data="test"),
    )
    def test_is_empty(self, test_data: TestData):
        self.assertEqual(test_data.expected, ArrayUtils.is_empty(test_data.data))
        self.assertEqual(not test_data.expected, ArrayUtils.is_not_empty(test_data.data))
