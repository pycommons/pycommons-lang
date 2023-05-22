from typing import Sized, Optional


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
