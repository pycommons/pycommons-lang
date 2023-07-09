from unittest import TestCase

from pycommons.lang import BooleanUtils
from tests.parametrized import TestData, cases


class TestBooleanUtils(TestCase):
    @cases(
        TestData(data=(True, True, True), expected=True),
        TestData(data=(True, True, False), expected=False),
        TestData(data=(True, False, False), expected=False),
        TestData(data=(False, True, True), expected=False),
        TestData(data=(False, False, False), expected=False),
    )
    def test_and_args(self, test_data: TestData):
        self.assertEqual(test_data.expected, BooleanUtils.and_args(*test_data.data))

    @cases(
        TestData(data=(True, True, True), expected=True),
        TestData(data=(True, True, False), expected=True),
        TestData(data=(True, False, False), expected=True),
        TestData(data=(False, True, True), expected=True),
        TestData(data=(False, False, False), expected=False),
    )
    def test_or_args(self, test_data: TestData):
        self.assertEqual(test_data.expected, BooleanUtils.or_args(*test_data.data))

    @cases(
        TestData(data=(True, True), expected=0),
        TestData(data=(True, False), expected=1),
        TestData(data=(False, True), expected=-1),
        TestData(data=(False, False), expected=0),
    )
    def test_compare(self, test_data: TestData):
        self.assertEqual(test_data.expected, BooleanUtils.compare(*test_data.data))

    @cases(
        TestData(data=True, expected=True),
        TestData(data=False, expected=False),
        TestData(data=None, expected=False),
    )
    def test_is_true(self, test_data: TestData):
        self.assertEqual(test_data.expected, BooleanUtils.is_true(test_data.data))
        self.assertEqual(not test_data.expected, BooleanUtils.is_not_true(test_data.data))

    @cases(
        TestData(data=True, expected=False),
        TestData(data=False, expected=True),
        TestData(data=None, expected=False),
    )
    def test_is_false(self, test_data: TestData):
        self.assertEqual(test_data.expected, BooleanUtils.is_false(test_data.data))
        self.assertEqual(not test_data.expected, BooleanUtils.is_not_false(test_data.data))

    @cases(
        TestData(data=True, expected=False),
        TestData(data=False, expected=True),
        TestData(data=None, expected=None),
    )
    def test_negate(self, test_data: TestData):
        self.assertEqual(test_data.expected, BooleanUtils.negate(test_data.data))

    @cases(
        TestData(data=True, expected=True),
        TestData(data=False, expected=False),
        TestData(data=None, expected=False),
        TestData(data=0, expected=False),
        TestData(data=1, expected=True),
        TestData(data=-1, expected=True),
        TestData(data="true", expected=True),
        TestData(data="yes", expected=True),
        TestData(data="y", expected=True),
        TestData(data="T", expected=True),
        TestData(data="on", expected=True),
        TestData(data="True", expected=True),
        TestData(data="false", expected=False),
        TestData(data="off", expected=False),
        TestData(data="no", expected=False),
        TestData(data="n", expected=False),
    )
    def test_to_boolean(self, test_data: TestData):
        self.assertEqual(test_data.expected, BooleanUtils.to_boolean(test_data.data))
