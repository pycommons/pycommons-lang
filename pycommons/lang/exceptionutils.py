import traceback
from contextlib import AbstractContextManager
from types import TracebackType
from typing import TypeVar, Type, Optional

from pycommons.base.utils.utils import UtilityClass

_E = TypeVar("_E", Exception, BaseException)


class ExceptionUtils(UtilityClass):
    @classmethod
    def get_cause(cls, exception: _E) -> Optional[BaseException]:
        return exception.__cause__

    @classmethod
    def ignored(cls, exception_type: Type[_E] = Exception) -> "IgnoredExceptionContext":
        return IgnoredExceptionContext(exception_type)


class IgnoredExceptionContext(AbstractContextManager):
    def __init__(self, exception_type: Type[BaseException]):
        self._expected_exc_type: Type[BaseException] = exception_type
        self._exception: Optional[_E] = None

    @property
    def exception(self) -> Optional[_E]:
        return self._exception

    def __exit__(
        self,
        __exc_type: Optional[Type[BaseException]],
        __exc_value: Optional[BaseException],
        __traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        self._exception: Optional[BaseException] = __exc_value
        if (
            __exc_type is not None
            and (
                __exc_type == self._expected_exc_type
                or issubclass(__exc_type, self._expected_exc_type)
            )
            and __traceback is not None
        ):
            traceback.clear_frames(__traceback)
            return True

        if __exc_type is not None and __exc_type != self._expected_exc_type:
            return False

        return None
