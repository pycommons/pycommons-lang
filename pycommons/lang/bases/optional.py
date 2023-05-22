from __future__ import annotations

from typing import Generic, TypeVar, Optional as TypingOptional, Any

from pycommons.lang.exception import NoSuchElementError
from pycommons.lang.function.consumer import Consumer
from pycommons.lang.function.function import Function
from pycommons.lang.function.predicate import Predicate
from pycommons.lang.function.runnable import Runnable
from pycommons.lang.function.supplier import Supplier
from pycommons.lang.objectutils import ObjectUtils

_T = TypeVar("_T", Any, None)
_U = TypeVar("_U", Any, None)
_E = TypeVar("_E", RuntimeError, Exception)


class Optional(Generic[_T]):
    """
    Identical implementation of Java's Optional.
    A container object which may or may not contain a non-null value

    See Also
        https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html
    """

    _value: _T

    def __init__(self, value: TypingOptional[_T]):
        self._value = value

    def get(self) -> _T:
        if self._value is None:
            raise NoSuchElementError("No value present")
        return self._value

    def is_present(self) -> bool:
        return self._value is not None

    def is_empty(self) -> bool:
        return not self.is_present()

    def if_present(self, consumer: Consumer[_T]) -> None:
        ObjectUtils.require_not_none(consumer)
        if self.is_present():
            consumer.accept(self._value)

    def if_present_or_else(self, consumer: Consumer[_T], runnable: Runnable) -> None:
        ObjectUtils.require_not_none(consumer)
        if self.is_present():
            consumer.accept(self._value)
        else:
            runnable.run()

    def filter(self, predicate: Predicate[_T]) -> Optional[_T]:
        ObjectUtils.require_not_none(predicate)
        if self.is_empty():
            return self

        return self if predicate.test(self._value) else Optional.empty()

    def map(self, mapper: Function[_T, _U]) -> Optional[_U]:
        ObjectUtils.require_not_none(mapper)
        if self.is_empty():
            return Optional.empty()

        return Optional.of_nullable(mapper.apply(self._value))

    def flat_map(self, mapper: Function[_T, Optional[_U]]) -> Optional[_U]:
        ObjectUtils.require_not_none(mapper)
        if self.is_empty():
            return Optional.empty()

        return ObjectUtils.get_not_none(mapper.apply(self._value))

    def in_turn(self, supplier: Supplier[Optional[_T]]) -> Optional[_T]:
        if self.is_present():
            return self

        return ObjectUtils.get_not_none(supplier.get())

    def or_else(self, other: _T) -> _T:
        return self._value if self.is_present() else other

    def or_else_get(self, supplier: Supplier[_T]) -> _T:
        return self._value if self.is_present() else supplier.get()

    def or_else_throw(self, supplier: TypingOptional[Supplier[_E]] = None) -> _T:
        if self.is_empty():
            if supplier:
                raise supplier.get()
            raise NoSuchElementError("No value present")
        return self._value

    @classmethod
    def of(cls, value: _T) -> Optional[_T]:
        if value is None:
            raise TypeError("Value cannot be None")
        return cls(value)

    @classmethod
    def of_nullable(cls, value: _T) -> Optional[_T]:
        return cls(value)

    @classmethod
    def empty(cls) -> Optional[_T]:
        return cls(None)
