from unittest import TestCase

from pycommons.lang.charutils import CharUtils
from tests.parametrized import cases, TestData


class CharUtilsTest(TestCase):
    @cases(
        TestData(data=" ", expected=True),
        TestData(data="\t", expected=True),
        TestData(data="\f", expected=True),
        TestData(data="\u001D", expected=True),
        TestData(data="a", expected=False),
        TestData(data="1", expected=False),
        TestData(data="*", expected=False),
        TestData(data=None, expected=False),
    )
    def test_is_whitespace(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_whitespace(test_case.data))

    @cases(
        TestData(data="a", expected=True),
        TestData(data="1", expected=True),
        TestData(data="*", expected=True),
        TestData(data="\u001D", expected=False),
        TestData(data=None, expected=False),
        TestData(data="ಕ", expected=False),
    )
    def test_is_ascii_printable(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_ascii_printable(test_case.data))

    @cases(
        TestData(data=" ", expected=False),
        TestData(data="\t", expected=False),
        TestData(data="a", expected=False),
        TestData(data="1", expected=True),
        TestData(data="Ⅳ", expected=False),
        TestData(data=None, expected=False),
    )
    def test_is_digit(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_digit(test_case.data))

    @cases(
        TestData(data=" ", expected=False),
        TestData(data="\t", expected=False),
        TestData(data="a", expected=True),
        TestData(data="1", expected=False),
        TestData(data="Ⅳ", expected=False),
        TestData(data="ಕ", expected=True),
        TestData(data=None, expected=False),
    )
    def test_is_letter(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_letter(test_case.data))

    @cases(
        TestData(data=" ", expected=False),
        TestData(data="a", expected=True),
        TestData(data="1", expected=True),
        TestData(data="Ⅳ", expected=True),
        TestData(data="ಕ", expected=True),
        TestData(data=None, expected=False),
    )
    def test_is_letter_or_digit(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_letter_or_digit(test_case.data))

    @cases(
        TestData(data=" ", expected=False),
        TestData(data="a", expected=False),
        TestData(data="A", expected=True),
        TestData(data="1", expected=False),
        TestData(data="Ⅳ", expected=True),
        TestData(data="ಕ", expected=False),
        TestData(data=None, expected=False),
    )
    def test_is_uppercase(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_uppercase(test_case.data))

    @cases(
        TestData(data=" ", expected=False),
        TestData(data="a", expected=True),
        TestData(data="A", expected=False),
        TestData(data="1", expected=False),
        TestData(data="Ⅳ", expected=False),
        TestData(data="ಕ", expected=False),
        TestData(data=None, expected=False),
    )
    def test_is_lowercase(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_lowercase(test_case.data))

    @cases(
        TestData(data=" ", expected=" "),
        TestData(data="a", expected="a"),
        TestData(data="A", expected="A"),
        TestData(data="1", expected="1"),
        TestData(data="Ⅳ", expected="Ⅳ"),
        TestData(data="ಕ", expected="ಕ"),
        TestData(data=None, expected=None),
    )
    def test_to_character(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.to_character(test_case.data))

    @cases(
        TestData(data=(" ", "\t"), expected=False),
        TestData(data=("a", "a"), expected=True),
        TestData(data=("1", "1"), expected=True),
        TestData(data=(69, 78), expected=False),
        TestData(data=(None, "1"), expected=False),
        TestData(data=("1", None), expected=False),
        TestData(data=(None, None), expected=False),
    )
    def test_is_equal(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.is_equal(*test_case.data))

    @cases(
        TestData(data=" ", expected=" "),
        TestData(data="a", expected="A"),
        TestData(data="A", expected="A"),
        TestData(data="1", expected="1"),
        TestData(data="Ⅳ", expected="Ⅳ"),
        TestData(data="ಕ", expected="ಕ"),
        TestData(data=None, expected=None),
    )
    def test_to_uppercase(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.to_uppercase(test_case.data))

    @cases(
        TestData(data=" ", expected=" "),
        TestData(data="a", expected="a"),
        TestData(data="A", expected="a"),
        TestData(data="1", expected="1"),
        TestData(data="Ⅳ", expected="ⅳ"),
        TestData(data="ಕ", expected="ಕ"),
        TestData(data=None, expected=None),
    )
    def test_to_lowercase(self, test_case: TestData):
        self.assertEqual(test_case.expected, CharUtils.to_lowercase(test_case.data))
