from __future__ import annotations

from typing import TypeVar, Generic, Callable

from pycommons.lang import ObjectUtils

_T = TypeVar("_T")


class Predicate(Generic[_T]):

    @classmethod
    def of(cls, predicate: Callable[[_T], bool]) -> Predicate[_T]:
        ObjectUtils.require_not_none(predicate)

        class BasicPredicate(Predicate):
            def test(self, value: _T):
                predicate(value)

        return BasicPredicate()

    def test(self, value: _T) -> bool:
        pass

    def __call__(self, *args, **kwargs) -> bool:
        return self.test(args[0])
