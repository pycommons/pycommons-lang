from __future__ import annotations

from typing import TypeVar


class Char(int):
    def __new__(cls, c: CharType):
        if isinstance(c, Char):
            return super(Char, cls).__new__(cls, int(c))
        elif isinstance(c, int):
            chr(c)
            return super(Char, cls).__new__(cls, c)
        else:
            if len(c) > 1:
                raise ValueError("Illegal Character")
            return super(Char, cls).__new__(cls, ord(c))

    def __str__(self):
        return chr(int(self))

    def __len__(self):
        return 1

    def __repr__(self):
        return chr(int(self))

    def __eq__(self, other: CharType):
        return int(self) == int(Char(other))

    def __gt__(self, other: CharType):
        return int(self) > int(Char(other))

    def __ge__(self, other: CharType):
        return int(self) >= int(Char(other))

    def __lt__(self, other: CharType):
        return int(self) < int(Char(other))

    def __le__(self, other: CharType):
        return int(self) <= int(Char(other))

    def __hash__(self):
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
