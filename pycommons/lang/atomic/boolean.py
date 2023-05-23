from pycommons.lang.atomic import Atomic


class AtomicBoolean(Atomic[bool]):
    def __init__(self, flag: bool = False):
        super(AtomicBoolean, self).__init__(flag)

    def true(self) -> bool:
        return self.set_and_get(True)

    def false(self) -> bool:
        return self.set_and_get(False)

    def compliment(self) -> bool:
        return self.set_and_get(not self.get())

    @classmethod
    def with_true(cls):
        return cls(True)

    @classmethod
    def with_false(cls):
        return cls(False)
