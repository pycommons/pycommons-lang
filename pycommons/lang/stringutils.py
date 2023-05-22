from typing import Optional

from .arrayutils import ArrayUtils
from .bases.char import Char
from .charutils import CharUtils


class StringUtils:
    @classmethod
    def is_all_lower_case(cls, char_sequence: str) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_lowercase(char):
                return False
        return True

    @classmethod
    def is_all_upper_case(cls, char_sequence: str) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_uppercase(char):
                return False
        return True

    @classmethod
    def is_alpha(cls, char_sequence: str) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_letter(char):
                return False
        return True

    @classmethod
    def is_alphanumeric(cls, char_sequence: str) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_letter_or_digit(char):
                return False
        return True

    @classmethod
    def is_alphanumeric_space(cls, char_sequence: str) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_letter_or_digit(char) and CharUtils.is_equal(
                char, str(CharUtils.ASCII_SPACE)
            ):
                return False
        return True

    @classmethod
    def is_alpha_space(cls, char_sequence: str) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_letter(char) and CharUtils.is_equal(
                char, str(CharUtils.ASCII_SPACE)
            ):
                return False
        return True

    @classmethod
    def is_any_blank(cls, *args: str) -> bool:
        if ArrayUtils.is_empty(args):
            return False

        for char_sequence in args:
            if cls.is_blank(char_sequence):
                return True
        return False

    @classmethod
    def is_any_empty(cls, *args: str) -> bool:
        if ArrayUtils.is_empty(args):
            return False

        for char_sequence in args:
            if cls.is_empty(char_sequence):
                return True
        return False

    @classmethod
    def is_ascii_printable(cls, char_sequence: str) -> bool:
        if char_sequence is None:
            return False

        for c in char_sequence:
            if not CharUtils.is_ascii_printable(cls.to_character(c)):
                return False
        return True

    @classmethod
    def is_blank(cls, char_sequence: str) -> bool:
        length: int = cls.length(char_sequence)
        if 0 == length:
            return True

        for char in char_sequence:
            if not CharUtils.is_whitespace(cls.to_character(char)):
                return False
        return True

    @classmethod
    def is_empty(cls, cs: str) -> bool:
        return cs is None or len(cs) == 0

    @classmethod
    def length(cls, cs: str) -> int:
        return 0 if cs is None else len(cs)

    @classmethod
    def to_character(cls, c: str) -> Optional[Char]:
        return CharUtils.to_character(c)
