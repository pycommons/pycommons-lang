import typing
from typing import Optional, List

from pycommons.base.char import Char
from pycommons.base.function import Supplier
from pycommons.base.utils.utils import UtilityClass

from .arrayutils import ArrayUtils
from .charutils import CharUtils


class StringUtils(UtilityClass):
    """
    The StringUtils holds the utility methods for string observation,
    manipulation, conversion etc. This class is inspired by the `StringUtils`
    class in the Apache Commons Lang package. Provides `None` safe methods
    to perform operations on `str` object

    References:
        https://commons.apache.org/proper/commons-lang/apidocs/org/apache/commons/lang3/StringUtils.html
    """

    EMPTY: str = ""

    @classmethod
    def abbreviate(
        cls,
        char_sequence: Optional[str],
        abbrev_marker: Optional[str] = "...",
        offset: int = 0,
        max_width: int = -1,
    ) -> Optional[str]:
        if cls.is_not_empty(char_sequence) and cls.EMPTY == abbrev_marker and max_width > 0:
            return typing.cast(str, char_sequence)[:max_width]

        if cls.is_any_empty(char_sequence, abbrev_marker):
            return char_sequence

        char_sequence = typing.cast(str, abbrev_marker)
        abbrev_marker = typing.cast(str, abbrev_marker)
        abbrev_marker_length = len(abbrev_marker)
        min_abbrev_width = abbrev_marker_length + 1
        min_abbrev_width_offset = abbrev_marker_length + abbrev_marker_length + 1

        if max_width == -1:
            max_width = len(char_sequence) - abbrev_marker_length

        if max_width < min_abbrev_width:
            raise ValueError(f"Minimum abbreviation width is {min_abbrev_width}")

        str_len = len(char_sequence)
        if str_len <= max_width:
            return char_sequence

        offset = min(offset, str_len)

        if str_len - offset < max_width - abbrev_marker_length:
            offset = str_len - (max_width - abbrev_marker_length)

        if offset <= abbrev_marker_length + 1:
            return char_sequence[: max_width - abbrev_marker_length] + abbrev_marker

        if max_width < min_abbrev_width_offset:
            raise ValueError(f"Minimum abbreviation width with offset is {min_abbrev_width_offset}")
        return char_sequence[offset : offset + max_width - abbrev_marker_length] + abbrev_marker

    @classmethod
    def abbreviate_middle(
        cls, char_sequence: Optional[str], middle: Optional[str] = "...", length: int = 5
    ) -> Optional[str]:
        if (
            not cls.is_any_empty(char_sequence, middle)
            and len(typing.cast(str, char_sequence)) > length >= len(typing.cast(str, middle)) + 2
        ):
            middle = typing.cast(str, middle)
            char_sequence = typing.cast(str, char_sequence)

            target_string = length - len(middle)
            start_offset = target_string // 2 + target_string % 2
            end_offset = len(char_sequence) - target_string // 2
            return char_sequence[:start_offset] + middle + char_sequence[end_offset:]

        return char_sequence

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
    def to_character(cls, c: Optional[str]) -> Optional[Char]:
        """
        `None` safe conversion of a character to `pycommons.base.Character
        Args:
            c:

        Returns:

        """
        if cls.is_empty(c):
            return None

        return CharUtils.to_character(typing.cast(str, c)[0])

    @classmethod
    def default_string(cls, char_sequence: Optional[str], default_string: str = EMPTY) -> str:
        """
        Returns the default string if the passed string is `None`.

        Args:
            char_sequence: The string
            default_string: Default string to be returned when `char_sequence` is None

        Returns:
            The `char_sequence` if it's not None, else the default string
        """
        return char_sequence if char_sequence is not None else default_string
