from typing import Sized, Optional, TypeVar

from pycommons.base.utils import ObjectUtils

from .exception.exceptionutils import ExceptionUtils

_E = TypeVar("_E", Exception, RuntimeError)


class ArrayUtils:
    @classmethod
    def get_length(cls, arr: Optional[Sized]) -> int:
        return len(arr) if arr is not None else 0

    @classmethod
    def is_empty(cls, arr: Optional[Sized]) -> bool:
        return cls.get_length(arr) == 0

    @classmethod
    def is_not_empty(cls, arr: Optional[Sized]) -> bool:
        return not cls.is_empty(arr)

    @classmethod
    def require_not_empty(cls, arr: Optional[Sized], e: Optional[_E] = None) -> None:
        if cls.is_empty(arr):
            ExceptionUtils.raise_error(
                ObjectUtils.default_if_none(e, ValueError("Sized object cannot be empty"))
            )
