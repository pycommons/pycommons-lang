from __future__ import annotations

from typing import TypeVar, Generic, Callable

_T = TypeVar("_T")


class Supplier(Generic[_T]):

    @classmethod
    def of(cls, supplier: Callable[[], _T]) -> Supplier[_T]:
        class BasicSupplier(Supplier):
            def get(self) -> _T:
                supplier()

        return BasicSupplier()

    def get(self) -> _T:
        pass

    def __call__(self, *args, **kwargs):
        return self.get()
