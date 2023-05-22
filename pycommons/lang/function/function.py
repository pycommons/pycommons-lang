from __future__ import annotations

from typing import TypeVar, Generic, Callable, Any

_T = TypeVar("_T")
_U = TypeVar("_U")


class Function(Generic[_T, _U]):
    @classmethod
    def of(cls, function: Callable[[_T], _U]) -> Function[_T, _U]:
        class BasicFunction(Function[_T, _U]):
            def apply(self, t: _T) -> _U:
                return function(t)

        return BasicFunction()

    def apply(self, t: _T) -> _U:
        pass

    def __call__(self, *args: Any, **kwargs: Any) -> _U:
        return self.apply(args[0])
