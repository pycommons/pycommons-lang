from __future__ import annotations

from typing import TypeVar, Generic, Callable, Any

from pycommons.lang.objectutils import ObjectUtils

_T = TypeVar("_T")


class Predicate(Generic[_T]):
    @classmethod
    def of(cls, predicate: Callable[[_T], bool]) -> Predicate[_T]:
        ObjectUtils.require_not_none(predicate)

        class BasicPredicate(Predicate[_T]):
            def test(self, value: _T) -> bool:
                return predicate(value)

        return BasicPredicate()

    def test(self, value: _T) -> bool:
        pass

    def __call__(self, *args: _T, **kwargs: Any) -> bool:
        return self.test(args[0])
