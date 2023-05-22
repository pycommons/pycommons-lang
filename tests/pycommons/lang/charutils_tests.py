from unittest import TestCase

from pycommons.lang import CharUtils
from pycommons.lang.bases import Char


class CharUtilsTest(TestCase):
    def test_is_whitespace(self):
        self.assertFalse(CharUtils.is_whitespace(None))
        self.assertTrue(CharUtils.is_whitespace(" "))
        self.assertTrue(CharUtils.is_whitespace("\t"))
        self.assertTrue(CharUtils.is_whitespace("\f"))
        self.assertTrue(CharUtils.is_whitespace("\t"))
        self.assertFalse(CharUtils.is_whitespace("a"))
        self.assertTrue(CharUtils.is_whitespace(Char(" ")))
        self.assertTrue(CharUtils.is_whitespace("\u001D"))

    def test_is_ascii_printable(self):
        # self.assertTrue(CharUtils.is_ascii_printable("a"))
        # self.assertFalse(CharUtils.is_ascii_printable(" "))
        self.assertFalse(CharUtils.is_ascii_printable(None))
