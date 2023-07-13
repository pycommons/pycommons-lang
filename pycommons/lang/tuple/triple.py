from __future__ import annotations

import typing
from abc import ABC, abstractmethod
from collections import UserList
from typing import TypeVar, Generic, Union, Tuple, Any

_L = TypeVar("_L")
_M = TypeVar("_M")
_R = TypeVar("_R")


class Triple(ABC, Generic[_L, _M, _R]):
    @classmethod
    def of(cls, left: _L, middle: _M, right: _R) -> ImmutableTriple[_L, _M, _R]:
        return ImmutableTriple(left, middle, right)

    @property
    def left(self) -> _L:
        return typing.cast(_L, self[0])

    @property
    def middle(self) -> _M:
        return typing.cast(_M, self[1])

    @property
    def right(self) -> _R:
        return typing.cast(_R, self[2])

    def get_left(self) -> _L:
        return self.left

    def get_middle(self) -> _M:
        return self.middle

    def get_right(self) -> _R:
        return self.right

    @abstractmethod
    def __getitem__(self, item: Any) -> Any:  # pragma: no cover
        ...

    def __str__(self) -> str:
        return self.to_string("({0}, {1}, {2})")

    def to_string(self, fmt: str) -> str:
        return fmt.format(self.left, self.middle, self.right)


class ImmutableTriple(Tuple, Triple[_L, _M, _R], Generic[_L, _M, _R]):  # type: ignore
    def __getitem__(self, item: Any) -> Any:
        return typing.cast(Union[_L, _M, _R], tuple.__getitem__(self, item))

    def __new__(cls, left: _L, middle: _M, right: _R) -> ImmutableTriple[_L, _M, _R]:
        return super().__new__(cls, [left, middle, right])  # type: ignore


class MutableTriple(UserList, Triple[_L, _M, _R], Generic[_L, _M, _R]):  # type: ignore
    def __getitem__(self, item: Any) -> Any:
        return typing.cast(Union[_L, _M, _R], UserList.__getitem__(self, item))

    def __init__(self, left: _L, middle: _M, right: _R) -> None:
        super().__init__([left, middle, right])

    @property
    def left(self) -> _L:
        return super().left

    @left.setter
    def left(self, left: _L) -> None:
        self[0] = left

    @property
    def middle(self) -> _M:
        return super().middle

    @middle.setter
    def middle(self, middle: _M) -> None:
        self[1] = middle

    @property
    def right(self) -> _R:
        return super().right

    @right.setter
    def right(self, right: _R) -> None:
        self[2] = right

    def set_left(self, left: _L) -> None:
        self.left = left

    def set_middle(self, middle: _M) -> None:
        self.middle = middle

    def set_right(self, right: _R) -> None:
        self.right = right
