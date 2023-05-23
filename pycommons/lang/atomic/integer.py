from pycommons.lang.atomic import Atomic


class AtomicInteger(Atomic[int]):
    def __init__(self, value=0):
        super(AtomicInteger, self).__init__(value)

    def add(self, val: int) -> None:
        return self.set(self.get() + val)

    def add_and_get(self, val: int) -> int:
        return self.set_and_get(self.get() + val)

    def get_and_add(self, val: int) -> int:
        return self.get_and_set(self._value + val)

    def increment(self) -> None:
        return self.add(1)

    def increment_and_get(self) -> int:
        return self.add_and_get(1)

    def get_and_increment(self) -> int:
        return self.get_and_add(1)

    def subtract(self, val: int) -> None:
        return self.add(-val)

    def subtract_and_get(self, val: int) -> int:
        return self.add_and_get(-val)

    def get_and_subtract(self, val: int) -> int:
        return self.get_and_add(-val)

    def __int__(self) -> int:
        return self.get()

    def __le__(self, other) -> int:
        return self.get() <= other

    def __lt__(self, other) -> bool:
        return self.get() < other

    def __ge__(self, other) -> bool:
        return self.get() >= other

    def __gt__(self, other) -> bool:
        return self.get() > other

    def __eq__(self, other):
        return self.get() == other
