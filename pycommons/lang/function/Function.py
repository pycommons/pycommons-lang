from __future__ import annotations

from typing import TypeVar, Generic, Callable

_T = TypeVar("_T")
_U = TypeVar("_U")


class Function(Generic[_T, _U]):

    @classmethod
    def of(cls, function: Callable[[_T], _U]) -> Function[_U]:
        class BasicFunction(Function):
            def apply(self, t: _T) -> None:
                function(t)

        return BasicFunction()

    def apply(self, t: _T) -> _U:
        pass

    def __call__(self, *args, **kwargs):
        return self.apply(args[0])
