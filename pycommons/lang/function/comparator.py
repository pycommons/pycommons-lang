from __future__ import annotations

from abc import abstractmethod
from typing import TypeVar, Generic

_T = TypeVar("_T")
_U = TypeVar("_U")


class Comparator(Generic[_T, _U]):
    @abstractmethod
    def compare_to(self, t: _T, u: _U) -> int:
        ...

    def reversed(self) -> Comparator[_T, _U]:
        return ReverseOrderComparator(self)

    def __call__(self, t: _T, u: _U, *args, **kwargs) -> int:
        return self.compare_to(t, u)


class NaturalOrderComparator(Comparator[_T, _U]):
    def compare_to(self, t: _T, u: _U) -> int:
        if t < u:
            return -1
        elif t == u:
            return 0
        else:
            return 1


class ReverseOrderComparator(Comparator[_T, _U]):
    def __init__(self, comparator: Comparator[_T, _U]):
        self.comparator = comparator

    def compare_to(self, t: _T, u: _U) -> int:
        return self.comparator.compare_to(u, t)


class Comparators:
    NATURAL_ORDER_COMPARATOR: Comparator[_T, _U] = NaturalOrderComparator()
