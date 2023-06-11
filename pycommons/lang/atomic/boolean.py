from __future__ import annotations

from pycommons.lang.atomic.atomic import Atomic
from pycommons.lang.base.synchronized import synchronized
from pycommons.lang.container.boolean import BooleanContainer


class AtomicBoolean(BooleanContainer, Atomic[bool]):  # pylint: disable=R0901
    @synchronized
    def true(self) -> bool:
        return super().true()

    @synchronized
    def false(self) -> bool:
        return super().false()

    @synchronized
    def compliment(self) -> bool:
        return super().compliment()

    @classmethod
    def with_true(cls) -> AtomicBoolean:
        return cls(True)

    @classmethod
    def with_false(cls) -> AtomicBoolean:
        return cls(False)

    @synchronized
    def get(self) -> bool:
        return super().get()
