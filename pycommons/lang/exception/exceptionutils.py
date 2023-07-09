import traceback
from contextlib import AbstractContextManager
from types import TracebackType
from typing import TypeVar, Type, Optional, Union, Generic, NoReturn

from pycommons.base.utils.utils import UtilityClass

_E = TypeVar("_E", Exception, BaseException)


class ExceptionUtils(UtilityClass):
    @classmethod
    def raise_error(cls, exception: _E) -> NoReturn:
        raise exception

    @classmethod
    def get_cause(cls, exception: Optional[_E]) -> Optional[BaseException]:
        return exception.__cause__ if exception is not None else None

    @classmethod
    def ignored(cls, exception_type: Type[_E] = Exception) -> "IgnoredExceptionContext[_E]":
        return IgnoredExceptionContext(exception_type)


class IgnoredExceptionContext(AbstractContextManager, Generic[_E]):  # type: ignore
    def __init__(self, exception_type: Type[BaseException]):
        self._expected_exc_type: Type[BaseException] = exception_type
        self._exception: Optional[Union[_E, BaseException]] = None

    @property
    def exception(self) -> Optional[Union[_E, BaseException]]:
        return self._exception

    def __exit__(
        self,
        __exc_type: Optional[Type[BaseException]],
        __exc_value: Optional[BaseException],
        __traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        self._exception = __exc_value
        if (
            __exc_type is not None
            and __traceback is not None
            and (
                __exc_type == self._expected_exc_type
                or issubclass(__exc_type, self._expected_exc_type)
            )
        ):
            traceback.clear_frames(__traceback)
            return True

        if __exc_type is not None and __exc_type != self._expected_exc_type:
            return False

        return None
