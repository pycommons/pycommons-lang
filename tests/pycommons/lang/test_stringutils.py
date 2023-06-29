from unittest import TestCase

from pycommons.lang.stringutils import StringUtils
from tests.parametrized import cases, TestData


class TestStringUtils(TestCase):
    @cases(
        TestData(data=(None, "testString"), expected="testString"),
        TestData(data=(None, None), expected=None),
        TestData(data=(), expected=None),
        TestData(data=("", "  ", "testString", None), expected="testString"),
        TestData(data=("None", None, "testString"), expected="None"),
    )
    def test_get_first_non_blank(self, test_data: TestData):
        self.assertEqual(test_data.expected, StringUtils.get_first_non_blank(*test_data.data))

    @cases(
        TestData(data=(None, "testString"), expected="testString"),
        TestData(data=(None, None), expected=None),
        TestData(data=(), expected=None),
        TestData(data=("", "  ", "testString", None), expected="  "),
        TestData(data=("None", None, "testString"), expected="None"),
    )
    def test_get_first_non_empty(self, test_data: TestData):
        self.assertEqual(test_data.expected, StringUtils.get_first_non_empty(*test_data.data))

    @cases(
        TestData(data="testString", expected=b"testString"),
        TestData(data="", expected=b""),
        TestData(data=None, expected=None),
    )
    def test_get_bytes(self, test_data: TestData):
        self.assertEqual(test_data.expected, StringUtils.get_bytes(test_data.data))

    @cases(
        TestData(data="testString", expected=""),
        TestData(data="123testString456", expected="123456"),
        TestData(data="123456", expected="123456"),
        TestData(data=None, expected=""),
        TestData(data="", expected=""),
    )
    def test_get_digits(self, test_data: TestData):
        self.assertEqual(test_data.expected, StringUtils.get_digits(test_data.data))
