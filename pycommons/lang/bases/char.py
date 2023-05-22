from __future__ import annotations

from typing import TypeVar


class Char(int):
    def __new__(cls, c: CharType) -> Char:
        if c is None:
            raise ValueError("Illegal Character")

        if isinstance(c, Char):
            return super(Char, cls).__new__(cls, int(c))

        if isinstance(c, int):
            chr(c)
            return super(Char, cls).__new__(cls, c)

        c_str: str = str(c)
        if len(c_str) > 1:
            raise ValueError("Illegal Character")
        return super(Char, cls).__new__(cls, ord(c_str))

    def __str__(self) -> str:
        return chr(int(self))

    def __len__(self) -> int:
        return 1

    def __repr__(self) -> str:
        return chr(int(self))

    def __eq__(self, other: CharType) -> bool:  # type: ignore
        return int(self) == int(Char(other))

    def __gt__(self, other: CharType) -> bool:
        return int(self) > int(Char(other))

    def __ge__(self, other: CharType) -> bool:
        return int(self) >= int(Char(other))

    def __lt__(self, other: CharType) -> bool:
        return int(self) < int(Char(other))

    def __le__(self, other: CharType) -> bool:
        return int(self) <= int(Char(other))

    def __hash__(self) -> int:
        return hash(int(self))

    def isupper(self) -> bool:
        return chr(int(self)).isupper()

    def islower(self) -> bool:
        return chr(int(self)).islower()

    def isalpha(self) -> bool:
        return chr(int(self)).isalpha()

    def isalnum(self) -> bool:
        return chr(int(self)).isalnum()

    def isascii(self) -> bool:
        return chr(int(self)).isascii()

    def isdigit(self) -> bool:
        return chr(int(self)).isdigit()

    def isspace(self) -> bool:
        return chr(int(self)).isspace()

    def upper(self) -> Char:
        return Char(chr(int(self)).upper())

    def lower(self) -> Char:
        return Char(chr(int(self)).lower())

    def swapcase(self) -> Char:
        return Char(chr(int(self)).swapcase())


CharType = TypeVar("CharType", Char, int, str, None)
