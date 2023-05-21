from typing import Generic, TypeVar, Union

from pycommons.lang.exception import NoSuchElementError
from pycommons.lang.types.callable import Consumer, Runnable

_T = TypeVar("_T")


class Optional(Generic[_T]):
    _value: _T

    def __init__(self, value: Union[_T, None]):
        self._value = value

    def get(self):
        if self._value is None:
            raise NoSuchElementError("No value present")
        return self._value

    def is_present(self):
        return self._value is not None

    def is_empty(self):
        return not self.is_present()

    def if_present(self, consumer: Consumer[_T]):
        if self.is_present():
            consumer.accept(self._value)

    def if_present_or_else(self, consumer: Consumer[_T], runnable: Runnable):
        if self.is_present():
            consumer.accept(self._value)
        else:
            runnable.run()

    @classmethod
    def of(cls, value: _T):
        if value is None:
            raise TypeError("Value cannot be null")
        return cls(value)

    @classmethod
    def of_nullable(cls, value: _T):
        return cls(value)

    @classmethod
    def empty(cls):
        return cls(None)
