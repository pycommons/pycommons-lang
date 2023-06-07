from unittest import TestCase

from pycommons.lang.utils.charutils import CharUtils
from tests.parametrized import cases, TestData


class CharUtilsTest(TestCase):
    @cases(
        [
            TestData(data=" ", expected=True),
            TestData(data="\t", expected=True),
            TestData(data="\f", expected=True),
            TestData(data="\u001D", expected=True),
            TestData(data="a", expected=False),
            TestData(data="1", expected=False),
            TestData(data="*", expected=False),
            TestData(data=None, expected=False),
        ]
    )
    def test_is_whitespace(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_whitespace(test_case.data))

    @cases(
        [
            TestData(data="a", expected=True),
            TestData(data="1", expected=True),
            TestData(data="*", expected=True),
            TestData(data="\u001D", expected=False),
            TestData(data=None, expected=False),
            TestData(data="ಕ", expected=False),
        ]
    )
    def test_is_ascii_printable(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_ascii_printable(test_case.data))

    @cases(
        [
            TestData(data=" ", expected=False),
            TestData(data="\t", expected=False),
            TestData(data="a", expected=False),
            TestData(data="1", expected=True),
            TestData(data="Ⅳ", expected=False),
            TestData(data=None, expected=False),
        ]
    )
    def test_is_digit(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_digit(test_case.data))

    @cases(
        [
            TestData(data=" ", expected=False),
            TestData(data="\t", expected=False),
            TestData(data="a", expected=True),
            TestData(data="1", expected=False),
            TestData(data="Ⅳ", expected=False),
            TestData(data="ಕ", expected=True),
            TestData(data=None, expected=False),
        ]
    )
    def test_is_letter(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_letter(test_case.data))
