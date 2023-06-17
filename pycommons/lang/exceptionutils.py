import traceback
from contextlib import AbstractContextManager
from types import TracebackType
from typing import TypeVar, Type, Optional

from pycommons.base.utils.utils import UtilityClass

_E = TypeVar("_E", Exception, BaseException)


class ExceptionUtils(UtilityClass):
    @classmethod
    def get_cause(cls, exception: _E):
        return exception.__cause__

    @classmethod
    def ignored(cls, exception_type: Type[_E] = BaseException):
        return IgnoredExceptionContext(exception_type)


class IgnoredExceptionContext(AbstractContextManager):
    def __init__(self, exception_type: Type[BaseException]):
        self._expected_exc_type: Type[BaseException] = exception_type

    def __exit__(
        self,
        __exc_type: Optional[Type[BaseException]],
        __exc_value: Optional[BaseException],
        __traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        self.exception: Optional[BaseException] = __exc_value
        if __exc_type is not None and (
            __exc_type == self._expected_exc_type or issubclass(__exc_type, self._expected_exc_type)
        ):
            traceback.clear_frames(__traceback)
            return True

        if __exc_type is not None and __exc_type != self._expected_exc_type:
            return False

        return None
