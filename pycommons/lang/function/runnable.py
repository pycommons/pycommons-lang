from __future__ import annotations

from typing import TypeVar, Callable, Any

_T = TypeVar("_T")


class Runnable:
    @classmethod
    def of(cls, runnable: Callable[[], None]) -> Runnable:
        class BasicRunnable(Runnable):
            def run(self) -> None:
                runnable()

        return BasicRunnable()

    def run(self) -> None:
        pass

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        self.run()
