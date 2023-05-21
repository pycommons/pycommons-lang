import string
from typing import Optional

from .bases import Char, CharType


class CharUtils:
    ASCII_SPACE = Char(" ")

    # region: Whitespaces
    WHITESPACES: set = set([Char(c) for c in string.whitespace])

    WHITESPACES.add(Char("\u001C"))
    WHITESPACES.add(Char("\u001D"))
    WHITESPACES.add(Char("\u001E"))
    WHITESPACES.add(Char("\u001F"))

    # endregion

    @classmethod
    def is_ascii_printable(cls, c: CharType):
        char: Optional[Char] = cls.to_character(c)
        return char is not None and cls.ASCII_SPACE < char < 127

    @classmethod
    def is_letter(cls, c: CharType):
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char.isalpha()

    @classmethod
    def is_letter_or_digit(cls, c: CharType):
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char.isalnum()

    @classmethod
    def is_uppercase(cls, c: CharType):
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char.isupper()

    @classmethod
    def is_lowercase(cls, c: CharType):
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char.islower()

    @classmethod
    def is_whitespace(cls, c: CharType):
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char in cls.WHITESPACES

    @classmethod
    def to_character(cls, c: CharType) -> Optional[Char]:
        if c is None:
            return None
        else:
            return Char(c)

    @classmethod
    def is_equal(cls, c: CharType, other: CharType):
        if c is None or other is None:
            return False
        return Char(c) == Char(other)
