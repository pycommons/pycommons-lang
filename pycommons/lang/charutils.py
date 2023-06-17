import string
from typing import Optional, Set

from pycommons.base.char import Char, CharType


class CharUtils:
    ASCII_SPACE: Char = Char(" ")

    # region: Whitespaces
    WHITESPACES: Set[Char] = {Char(c) for c in string.whitespace}

    WHITESPACES.add(Char("\u001C"))
    WHITESPACES.add(Char("\u001D"))
    WHITESPACES.add(Char("\u001E"))
    WHITESPACES.add(Char("\u001F"))

    # endregion

    @classmethod
    def is_ascii_printable(cls, c: Optional[CharType]) -> bool:
        char: Optional[Char] = cls.to_character(c)
        return char is not None and cls.ASCII_SPACE < char < 127

    @classmethod
    def is_digit(cls, c: Optional[CharType]) -> bool:
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char.isdigit()

    @classmethod
    def is_letter(cls, c: Optional[CharType]) -> bool:
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char.isalpha()

    @classmethod
    def is_letter_or_digit(cls, c: Optional[CharType]) -> bool:
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char.isalnum()

    @classmethod
    def is_uppercase(cls, c: Optional[CharType]) -> bool:
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char.isupper()

    @classmethod
    def is_lowercase(cls, c: Optional[CharType]) -> bool:
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char.islower()

    @classmethod
    def is_whitespace(cls, c: Optional[CharType]) -> bool:
        char: Optional[Char] = cls.to_character(c)
        return char is not None and char in cls.WHITESPACES

    @classmethod
    def to_character(cls, c: Optional[CharType]) -> Optional[Char]:
        if c is None:
            return None
        return Char(c)

    @classmethod
    def to_uppercase(cls, c: Optional[CharType]) -> Optional[Char]:
        char: Optional[Char] = cls.to_character(c)
        return char.upper() if char else None

    @classmethod
    def to_lowercase(cls, c: Optional[CharType]) -> Optional[Char]:
        char: Optional[Char] = cls.to_character(c)
        return char.lower() if char else None

    @classmethod
    def is_equal(cls, c: CharType, other: CharType) -> bool:
        if c is None or other is None:
            return False
        return Char(c) == Char(other)
