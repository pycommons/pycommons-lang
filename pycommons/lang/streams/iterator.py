import itertools
from typing import TypeVar, Iterator, Optional as TypingOptional

from pycommons.lang.atomic.atomic import Atomic
from pycommons.lang.atomic.boolean import AtomicBoolean
from pycommons.lang.atomic.integer import AtomicInteger
from pycommons.lang.bases import Optional
from pycommons.lang.function import Consumer, Predicate, Function
from pycommons.lang.function.predicate import PassingPredicate
from pycommons.lang.streams.stream import Stream, _R

_T = TypeVar("_T")


class IteratorStream(Stream[_T]):
    def __init__(self, iterator: Iterator[_T]):
        self._iterator: Iterator[_T] = iterator

    def filter(self, predicate: Predicate[_T]) -> Stream[_T]:
        def _filter() -> Iterator[_T]:
            for _t in self._iterator:
                if predicate(_t):
                    yield _t

        return IteratorStream(_filter())

    def map(self, mapper: Function[_T, _R]) -> Stream[_R]:
        def _map() -> Iterator[_R]:
            for _t in self._iterator:
                yield mapper.apply(_t)

        return IteratorStream(_map())

    def flat_map(self, mapper: Function[_T, Stream[_R]]) -> Stream[_R]:
        stream: Stream[_R] = IteratorStream(iter(()))

        for _t in self._iterator:
            stream = stream.chain(mapper.apply(_t))

        return stream

    def iterator(self) -> Iterator[_T]:
        return self._iterator

    def chain(self, stream: Stream[_T]) -> Stream[_T]:
        return IteratorStream(itertools.chain(self._iterator, stream.iterator()))

    def limit(self, max_size: int) -> Stream[_T]:
        _count: AtomicInteger = AtomicInteger()

        def _limiter(_c: AtomicInteger) -> bool:
            _c.increment()
            return _c > max_size

        return self.drop_while(Predicate.of(lambda t: _limiter(_count)))

    def skip(self, n: int) -> Stream[_T]:
        _count: AtomicInteger = AtomicInteger()

        def _skipper(_c: AtomicInteger) -> bool:
            _c.increment()
            return _c < n

        return self.drop_while(Predicate.of(lambda t: _skipper(_count)))

    def take_while(self, predicate: Predicate[_T]) -> Stream[_T]:
        def _filter() -> Iterator[_T]:
            for _t in self._iterator:
                if predicate.test(_t):
                    yield _t

        return IteratorStream(_filter())

    def drop_while(self, predicate: Predicate[_T]) -> Stream[_T]:
        def _filter() -> Iterator[_T]:
            for _t in self._iterator:
                if not predicate.test(_t):
                    yield _t

        return IteratorStream(_filter())

    def for_each(
        self,
        consumer: Consumer[_T],
        *,
        break_before_accept: TypingOptional[Predicate[_T]] = None,
        break_on_accept: TypingOptional[Predicate[_T]] = None,
        continue_before_accept: TypingOptional[Predicate[_T]] = None,
    ) -> None:
        if break_before_accept is not None and continue_before_accept is not None:
            raise ValueError(
                "Both break_before_accept and continue_before_accept cannot be present"
            )

        for _t in self._iterator:
            if break_before_accept is not None and break_before_accept.test(_t):
                break

            if continue_before_accept is not None and continue_before_accept.test(_t):
                continue

            consumer.accept(_t)

            if break_on_accept is not None and break_on_accept.test(_t):
                break

    def count(self) -> int:
        stream_count: AtomicInteger = AtomicInteger()

        def _counter(_count: AtomicInteger) -> None:
            stream_count.increment()

        self.for_each(Consumer.of(lambda t: _counter(stream_count)))

        return stream_count.get()

    def any_match(self, predicate: Predicate[_T]) -> bool:
        _match: AtomicBoolean = AtomicBoolean.with_false()

        def _matcher(t: _T, _m: AtomicBoolean) -> None:
            if predicate.test(t):
                _m.true()

        self.for_each(
            Consumer.of(lambda t: _matcher(t, _match)),
            break_on_accept=Predicate.of(lambda t: _match.get()),
        )

        return _match.get()

    def all_match(self, predicate: Predicate[_T]) -> bool:
        _match: AtomicBoolean = AtomicBoolean.with_true()

        def _matcher(t: _T, _m: AtomicBoolean) -> None:
            if not predicate.test(t):
                _m.false()

        self.for_each(
            Consumer.of(lambda t: _matcher(t, _match)),
            break_on_accept=Predicate.of(lambda t: not _match.get()),
        )

        return _match.get()

    def none_match(self, predicate: Predicate[_T]) -> bool:
        _match: AtomicBoolean = AtomicBoolean.with_true()

        def _matcher(t: _T, _m: AtomicBoolean) -> None:
            if predicate.test(t):
                _m.false()

        self.for_each(
            Consumer.of(lambda t: _matcher(t, _match)),
            break_on_accept=Predicate.of(lambda t: not _match.get()),
        )

        return _match.get()

    def find_first(
        self, predicate: TypingOptional[Predicate[_T]] = None
    ) -> Optional[_T]:  # type: ignore
        if predicate is None:
            return self.find_first(PassingPredicate())

        _match: AtomicBoolean = AtomicBoolean.with_false()
        _found: Atomic[TypingOptional[_T]] = Atomic.with_none()

        def _matcher(t: _T, _m: AtomicBoolean, _f: Atomic[TypingOptional[_T]]) -> None:
            assert predicate is not None
            if predicate.test(t):
                _m.true()
                _f.set(t)

        self.for_each(
            Consumer.of(lambda t: _matcher(t, _match, _found)),
            break_on_accept=Predicate.of(lambda t: _match.get()),
        )

        return Optional.of_nullable(_found.get())
