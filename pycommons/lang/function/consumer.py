from __future__ import annotations

from typing import TypeVar, Generic, Callable, Any

_T = TypeVar("_T")


class Consumer(Generic[_T]):
    @classmethod
    def of(cls, consumer: Callable[[_T], None]) -> Consumer[_T]:
        class BasicConsumer(Consumer[_T]):
            def accept(self, value: _T) -> None:
                consumer(value)

        return BasicConsumer()

    def accept(self, value: _T) -> None:
        pass

    def and_then(self, after: Consumer[_T]) -> Consumer[_T]:
        def _impl(_t: _T) -> None:
            self.accept(_t)
            after.accept(_t)

        return Consumer.of(_impl)

    def __call__(self, *args: _T, **kwargs: Any) -> None:
        self.accept(args[0])
