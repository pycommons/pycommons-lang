from __future__ import annotations

import typing
from abc import ABC, abstractmethod
from collections import UserList
from typing import TypeVar, Generic, Union, Any

_L = TypeVar("_L")
_R = TypeVar("_R")


class Pair(ABC, Generic[_L, _R]):
    @classmethod
    def of(cls, left: _L, right: _R) -> ImmutablePair[_L, _R]:
        return ImmutablePair(left, right)

    @property
    def left(self) -> _L:
        return typing.cast(_L, self[0])

    @property
    def right(self) -> _R:
        return typing.cast(_R, self[1])

    @property
    def key(self) -> _L:
        return self.left

    @property
    def value(self) -> _R:
        return self.right

    def get_left(self) -> _L:
        return self.left

    def get_right(self) -> _R:
        return self.right

    def get_key(self) -> _L:
        return self.left

    def get_value(self) -> _R:
        return self.right

    @abstractmethod
    def __getitem__(self, item: Any) -> Any:
        ...  # pragma: no cover

    def __str__(self) -> str:
        return self.to_string("({0}, {1})")

    def to_string(self, fmt: str) -> str:
        return fmt.format(self.left, self.right)


class ImmutablePair(tuple, Pair[_L, _R], Generic[_L, _R]):  # type: ignore
    def __getitem__(self, item: Any) -> Any:
        return typing.cast(Union[_L, _R], tuple.__getitem__(self, item))

    def __new__(cls, left: _L, right: _R) -> ImmutablePair[_L, _R]:
        return super().__new__(cls, [left, right])  # type: ignore


class MutablePair(UserList, Pair, Generic[_L, _R]):  # type: ignore
    def __getitem__(self, item: Any) -> Any:
        return typing.cast(Union[_L, _R], UserList.__getitem__(self, item))

    def __init__(self, left: _L, right: _R) -> None:
        super().__init__([left, right])

    @property
    def left(self) -> _L:
        return typing.cast(_L, super().left)

    @left.setter
    def left(self, left: _L) -> None:
        self[0] = left

    @property
    def right(self) -> _R:
        return typing.cast(_R, super().right)

    @right.setter
    def right(self, right: _R) -> None:
        self[1] = right

    def set_left(self, key: _L) -> None:
        self.left = key

    def set_right(self, value: _R) -> None:
        self.right = value
