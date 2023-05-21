from __future__ import annotations

from typing import TypeVar, Callable

_T = TypeVar("_T")


class Runnable:
    @classmethod
    def of(cls, runnable: Callable[[], None]) -> Runnable:
        class BasicRunnable(Runnable):
            def run(self):
                runnable()

        return BasicRunnable()

    def run(self):
        pass

    def __call__(self, *args, **kwargs) -> None:
        self.run()
