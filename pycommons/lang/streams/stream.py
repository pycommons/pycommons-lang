from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, Optional as TypingOptional, Iterator, Any

from pycommons.lang.bases.optional import Optional
from pycommons.lang.function import Predicate, Function, Consumer

_T = TypeVar("_T", bound=Any)
_R = TypeVar("_R", bound=Any)


class Stream(Generic[_T]):
    @abstractmethod
    def iterator(self) -> Iterator[_T]:
        ...

    @abstractmethod
    def chain(self, stream: Stream[_T]) -> Stream[_T]:
        ...

    @abstractmethod
    def filter(self, predicate: Predicate[_T]) -> Stream[_T]:
        ...

    @abstractmethod
    def map(self, mapper: Function[_T, _R]) -> Stream[_R]:
        ...

    @abstractmethod
    def flat_map(self, mapper: Function[_T, Stream[_R]]) -> Stream[_R]:
        ...

    @abstractmethod
    def limit(self, max_size: int) -> Stream[_T]:
        ...

    @abstractmethod
    def skip(self, n: int) -> Stream[_T]:
        ...

    @abstractmethod
    def take_while(self, predicate: Predicate[_T]) -> Stream[_T]:
        ...

    @abstractmethod
    def drop_while(self, predicate: Predicate[_T]) -> Stream[_T]:
        ...

    @abstractmethod
    def for_each(
        self,
        consumer: Consumer[_T],
        *,
        break_before_accept: TypingOptional[Predicate[_T]] = None,
        break_on_accept: TypingOptional[Predicate[_T]] = None,
        continue_before_accept: TypingOptional[Predicate[_T]] = None,
    ) -> None:
        ...

    def peek(
        self,
        consumer: Consumer[_T],
        *,
        break_before_accept: TypingOptional[Predicate[_T]] = None,
        break_on_accept: TypingOptional[Predicate[_T]] = None,
        continue_before_accept: TypingOptional[Predicate[_T]] = None,
    ) -> Stream[_T]:
        self.for_each(
            consumer,
            break_before_accept=break_before_accept,
            break_on_accept=break_on_accept,
            continue_before_accept=continue_before_accept,
        )
        return self

    @abstractmethod
    def count(self) -> int:
        ...

    @abstractmethod
    def any_match(self, predicate: Predicate[_T]) -> bool:
        ...

    @abstractmethod
    def all_match(self, predicate: Predicate[_T]) -> bool:
        ...

    @abstractmethod
    def none_match(self, predicate: Predicate[_T]) -> bool:
        ...

    @abstractmethod
    def find_first(
        self, predicate: TypingOptional[Predicate[_T]] = None
    ) -> Optional[_T]:  # type: ignore
        ...
