from __future__ import annotations

from typing import TypeVar, Generic, Any

from pycommons.lang.function import Supplier

_T = TypeVar("_T")


class Atomic(Generic[_T], Supplier[_T]):
    def get(self) -> _T:
        return self._object

    def __init__(self, t: _T = None):
        self._object = t

    def set(self, t: _T) -> None:
        self._object = t

    def set_and_get(self, t: _T) -> _T:
        self._object = t
        return self._object

    def get_and_set(self, t: _T) -> _T:
        old_object = self._object
        self._object = t
        return old_object

    @classmethod
    def with_none(cls) -> Atomic[Any]:
        return cls()
