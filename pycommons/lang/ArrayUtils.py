from typing import Sized


class ArrayUtils:
    @classmethod
    def get_length(cls, arr: Sized):
        return len(arr) if arr is not None else 0

    @classmethod
    def is_empty(cls, arr: Sized):
        return cls.get_length(arr) == 0
