import typing
from typing import Optional, List

from .arrayutils import ArrayUtils
from .bases.char import Char
from .charutils import CharUtils
from .function import Supplier


class StringUtils:
    EMPTY: str = ""

    @classmethod
    def contains(cls, char_sequence: Optional[str], search_string: Optional[str]) -> bool:
        if char_sequence is not None and search_string is not None:
            search_length: int = len(search_string)
            max_iterations: int = len(char_sequence) - search_length

            for i in range(0, max_iterations + 1):
                if cls.region_matches(char_sequence, False, i, search_string, 0, search_length):
                    return True
        return False

    @classmethod
    def contains_any(cls, char_sequence: Optional[str], *search_strings: str) -> bool:
        if char_sequence is not None and ArrayUtils.is_not_empty(search_strings):
            for search_string in search_strings:
                if cls.contains(char_sequence, search_string):
                    return True
        return False

    @classmethod
    def contains_ignore_case(
        cls, char_sequence: Optional[str], search_string: Optional[str]
    ) -> bool:
        if char_sequence is not None and search_string is not None:
            search_length: int = len(search_string)
            max_iterations: int = len(char_sequence) - search_length

            for i in range(0, max_iterations + 1):
                if cls.region_matches(char_sequence, True, i, search_string, 0, search_length):
                    return True
        return False

    @classmethod
    def get_first_non_blank(cls, *args: Optional[str]) -> Optional[str]:
        if ArrayUtils.is_empty(args):
            return None

        for char_sequence in args:
            if not cls.is_blank(char_sequence):
                return char_sequence

        return None

    @classmethod
    def get_first_non_empty(cls, *args: Optional[str]) -> Optional[str]:
        if ArrayUtils.is_empty(args):
            return None

        for char_sequence in args:
            if not cls.is_empty(char_sequence):
                return char_sequence

        return None

    @classmethod
    def get_bytes(cls, char_sequence: Optional[str], encoding: str = "utf-8") -> Optional[bytes]:
        if char_sequence is None:
            return None
        return char_sequence.encode(encoding)

    @classmethod
    def get_digits(cls, char_sequence: Optional[str]) -> str:
        if cls.is_empty(char_sequence):
            return cls.EMPTY

        digits: List[str] = []
        for c in typing.cast(str, char_sequence):
            if CharUtils.is_digit(c):
                digits.append(c)

        return cls.EMPTY.join(digits)

    @classmethod
    def get_if_blank(cls, char_sequence: Optional[str], default_supplier: Supplier[str]) -> str:
        if cls.is_not_blank(char_sequence):
            return typing.cast(str, char_sequence)
        return default_supplier.get()

    @classmethod
    def get_if_empty(cls, char_sequence: Optional[str], default_supplier: Supplier[str]) -> str:
        if cls.is_not_empty(char_sequence):
            return typing.cast(str, char_sequence)
        return default_supplier.get()

    @classmethod
    def is_all_lower_case(cls, char_sequence: Optional[str]) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_lowercase(char):
                return False
        return True

    @classmethod
    def is_all_upper_case(cls, char_sequence: Optional[str]) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_uppercase(char):
                return False
        return True

    @classmethod
    def is_alpha(cls, char_sequence: Optional[str]) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_letter(char):
                return False
        return True

    @classmethod
    def is_alphanumeric(cls, char_sequence: Optional[str]) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_letter_or_digit(char):
                return False
        return True

    @classmethod
    def is_alphanumeric_space(cls, char_sequence: Optional[str]) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_letter_or_digit(char) and CharUtils.is_equal(
                char, str(CharUtils.ASCII_SPACE)
            ):
                return False
        return True

    @classmethod
    def is_alpha_space(cls, char_sequence: Optional[str]) -> bool:
        if char_sequence is None:
            return False

        for char in char_sequence:
            if not CharUtils.is_letter(char) and CharUtils.is_equal(
                char, str(CharUtils.ASCII_SPACE)
            ):
                return False
        return True

    @classmethod
    def is_any_blank(cls, *args: Optional[str]) -> bool:
        if ArrayUtils.is_empty(args):
            return False

        for char_sequence in args:
            if cls.is_blank(char_sequence):
                return True
        return False

    @classmethod
    def is_any_empty(cls, *args: Optional[str]) -> bool:
        if ArrayUtils.is_empty(args):
            return False

        for char_sequence in args:
            if cls.is_empty(char_sequence):
                return True
        return False

    @classmethod
    def is_ascii_printable(cls, char_sequence: Optional[str]) -> bool:
        if char_sequence is None:
            return False

        for c in char_sequence:
            if not CharUtils.is_ascii_printable(cls.to_character(c)):
                return False
        return True

    @classmethod
    def is_blank(cls, char_sequence: Optional[str]) -> bool:
        length: int = cls.length(char_sequence)
        if 0 == length:
            return True

        for char in typing.cast(str, char_sequence):
            if not CharUtils.is_whitespace(cls.to_character(char)):
                return False
        return True

    @classmethod
    def is_empty(cls, char_sequence: Optional[str]) -> bool:
        return char_sequence is None or len(char_sequence) == 0

    @classmethod
    def is_not_blank(cls, char_sequence: Optional[str]) -> bool:
        return not cls.is_blank(char_sequence)

    @classmethod
    def is_not_empty(cls, char_sequence: Optional[str]) -> bool:
        return not cls.is_empty(char_sequence)

    @classmethod
    def length(cls, char_sequence: Optional[str]) -> int:
        return 0 if char_sequence is None else len(char_sequence)

    @classmethod
    def region_matches(
        cls,
        char_sequence: str,
        ignore_case: bool,
        this_start: int,
        sub_string: str,
        start: int,
        length: int,
    ) -> bool:
        index1 = this_start
        index2 = start
        tmp_length = length
        src_length = len(char_sequence) - this_start
        other_length = len(sub_string) - start

        if this_start >= 0 and start >= 0 and length >= 0:
            if src_length >= length and other_length >= length:
                while tmp_length > 0:

                    c1 = char_sequence[index1]
                    c2 = sub_string[index2]

                    index1 += 1
                    index2 += 1

                    if c1 != c2:
                        if not ignore_case:
                            return False

                        u1 = CharUtils.to_uppercase(c1)
                        u2 = CharUtils.to_uppercase(c2)
                        if u1 != u2 and CharUtils.to_lowercase(u1) != CharUtils.to_lowercase(u2):
                            return False

                    tmp_length -= 1
                return True
            return False
        return False

    @classmethod
    def to_character(cls, c: str) -> Optional[Char]:
        return CharUtils.to_character(c)
