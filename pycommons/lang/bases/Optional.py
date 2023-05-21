from __future__ import annotations

from typing import Generic, TypeVar, Union

from pycommons.lang import ObjectUtils
from pycommons.lang.exception import NoSuchElementError
from pycommons.lang.function import Consumer, Runnable, Predicate, Function, Supplier

_T = TypeVar("_T")
_U = TypeVar("_U")
_E = TypeVar("_E", RuntimeError, Exception)


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
        ObjectUtils.require_not_none(consumer)
        if self.is_present():
            consumer.accept(self._value)

    def if_present_or_else(self, consumer: Consumer[_T], runnable: Runnable):
        ObjectUtils.require_not_none(consumer)
        if self.is_present():
            consumer.accept(self._value)
        else:
            runnable.run()

    def filter(self, predicate: Predicate[_T]) -> Optional[_T]:
        ObjectUtils.require_not_none(predicate)
        if self.is_empty():
            return self
        else:
            return self if predicate.test(self._value) else Optional.empty()

    def map(self, mapper: Function[_T, _U]) -> Optional[_U]:
        ObjectUtils.require_not_none(mapper)
        if self.is_empty():
            return Optional.empty()
        else:
            return Optional.of_nullable(mapper.apply(self._value))

    def flat_map(self, mapper: Function[_T, Optional[_U]]) -> Optional[_U]:
        ObjectUtils.require_not_none(mapper)
        if self.is_empty():
            return Optional.empty()
        else:
            return ObjectUtils.get_not_none(mapper.apply(self._value))

    def in_turn(self, supplier: Supplier[Optional[_T]]) -> Optional[_T]:
        if self.is_present():
            return self
        else:
            return ObjectUtils.get_not_none(supplier.get())

    def or_else(self, other: _T):
        return self._value if self.is_present() else other

    def or_else_get(self, supplier: Supplier[_T]):
        return self._value if self.is_present() else supplier.get()

    def or_else_throw(self, supplier: Optional[Supplier[_E]] = None):
        if self.is_empty():
            if supplier:
                raise supplier.get()
            else:
                raise NoSuchElementError("No value present")
        return self._value

    @classmethod
    def of(cls, value: _T):
        if value is None:
            raise TypeError("Value cannot be None")
        return cls(value)

    @classmethod
    def of_nullable(cls, value: _T):
        return cls(value)

    @classmethod
    def empty(cls):
        return cls(None)
