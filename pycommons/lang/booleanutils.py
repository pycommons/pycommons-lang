from typing import ClassVar, Optional, overload, Union

from pycommons.base.utils import UtilityClass, ObjectUtils


class BooleanUtils(UtilityClass):
    TRUE: ClassVar[str] = str(True).lower()
    FALSE: ClassVar[str] = str(False).lower()

    T: ClassVar[str] = "t"
    F: ClassVar[bool] = "f"

    YES: ClassVar[str] = "yes"
    NO: ClassVar[str] = "no"

    Y: ClassVar[str] = "y"
    N: ClassVar[str] = "n"

    OFF: ClassVar[str] = "off"
    ON: ClassVar[str] = "on"

    @classmethod
    def and_args(cls, *args: bool) -> bool:
        for flag in args:
            ObjectUtils.require_not_none(flag)
            if not flag:
                return False

        return True

    @classmethod
    def or_args(cls, *args: bool) -> bool:
        for flag in args:
            ObjectUtils.require_not_none(flag)
            if flag:
                return True

        return False

    @classmethod
    def compare(cls, x: bool, y: bool) -> int:
        if x == y:
            return 0
        if (not x) and y:
            return -1
        # x and (not y)
        return 1

    @classmethod
    def is_false(cls, flag: Optional[bool]) -> bool:
        return flag is False

    @classmethod
    def is_not_false(cls, flag: Optional[bool]) -> bool:
        return flag is not False

    @classmethod
    def is_true(cls, flag: Optional[bool]) -> bool:
        return flag is True

    @classmethod
    def is_not_true(cls, flag: Optional[bool]) -> bool:
        return flag is not True

    @classmethod
    def negate(cls, flag: Optional[bool]) -> Optional[bool]:
        if flag is None:
            return None
        return not flag

    @classmethod
    @overload
    def to_boolean(cls, x: Optional[bool]) -> bool:
        ...

    @classmethod
    @overload
    def to_boolean(cls, value: int) -> bool:
        ...

    @classmethod
    @overload
    def to_boolean(cls, value: Optional[str]) -> bool:
        ...

    @classmethod
    def to_boolean(cls, x) -> bool:
        if x is None:
            return False

        if isinstance(x, bool):
            return x

        if isinstance(x, int):
            return x != 0

        if isinstance(x, str):
            _x = x.lower()
            return cls.or_args(_x == cls.TRUE, _x == cls.T, _x == cls.Y, _x == cls.YES, _x == cls.ON)

    @classmethod
    @overload
    def parse_bool(cls, value: Optional[int], true_value: Optional[int],
                   false_value: Optional[int]):
        ...

    @classmethod
    @overload
    def parse_bool(cls, value: Optional[str], true_value: Optional[str],
                   false_value: Optional[str]):
        ...

    @classmethod
    def parse_bool(cls, value: Optional[Union[int, str]], true_value: Optional[Union[int, str]],
                   false_value: Optional[Union[int, str]]) -> bool:
        if value == true_value:
            return True

        if value == false_value:
            return False

        raise ValueError("value does not match either of true_value or false_value")

    @classmethod
    def get_boolean(cls, flag: Optional[bool], default_value: bool = False) -> bool:
        if flag is None:
            return default_value

        return flag

    @classmethod
    @overload
    def to_bool_object(cls, value: Optional[Union[int]], true_value: Optional[Union[int]],
                       false_value: Optional[Union[int]], none_value: Optional[Union[int]]) -> Optional[bool]:
        ...

    @classmethod
    @overload
    def to_bool_object(cls, value: Optional[Union[str]], true_value: Optional[Union[str]],
                       false_value: Optional[Union[str]], none_value: Optional[Union[str]]) -> Optional[bool]:
        ...

    @classmethod
    def to_bool_object(cls, value: Optional[Union[int, str]], true_value: Optional[Union[int, str]],
                       false_value: Optional[Union[int, str]], none_value: Optional[Union[int, str]]) -> Optional[bool]:
        if value == true_value:
            return True

        if value == false_value:
            return False

        if value == none_value:
            return None

        raise ValueError("value does not match either of true_value or false_value or null_value")

    @classmethod
    @overload
    def to_boolean_object(cls, x: Optional[bool]) -> Optional[bool]:
        ...

    @classmethod
    @overload
    def to_boolean_object(cls, value: int) -> Optional[bool]:
        ...

    @classmethod
    @overload
    def to_boolean_object(cls, value: Optional[str]) -> Optional[bool]:
        ...

    @classmethod
    def to_boolean_object(cls, flag) -> Optional[bool]:
        if flag is None:
            return None

        if isinstance(flag, bool):
            return flag

        if isinstance(flag, int):
            return flag != 0

        if isinstance(flag, str):
            _flag = flag.lower()
            if cls.or_args(_flag == cls.TRUE, _flag == cls.T, _flag == cls.Y, _flag == cls.YES, _flag == cls.ON):
                return True

            if cls.or_args(_flag == cls.FALSE, _flag == cls.F, _flag == cls.N, _flag == cls.NO, _flag == cls.OFF):
                return False

            return None

    @classmethod
    def to_int(cls, flag: bool, true_value: int = 1, false_value: int = 0) -> int:
        return true_value if flag else false_value

    @classmethod
    def to_int_from_boolean_object(cls, flag: Optional[bool], true_value: int, false_value: int,
                                   none_value: int) -> int:
        if flag is None:
            return none_value

        return cls.to_int(flag, true_value, false_value)

    @classmethod
    def to_int_object_from_boolean_object(cls, flag: Optional[bool], true_value: Optional[int],
                                          false_value: Optional[int],
                                          none_value: Optional[int]) -> int:
        if flag is None:
            return none_value

        return true_value if flag else false_value

    @classmethod
    def to_str(cls, flag: bool, true_value: str, false_value: str) -> str:
        return true_value if flag else false_value

    @classmethod
    def to_str_from_boolean_object(cls, flag: Optional[bool], true_value: str, false_value: str,
                                   none_value: str) -> str:
        if flag is None:
            return none_value

        return cls.to_str(flag, true_value, false_value)

    @classmethod
    def to_str_object_from_boolean_object(cls, flag: Optional[bool], true_value: Optional[str],
                                          false_value: Optional[str],
                                          none_value: Optional[str]) -> str:
        if flag is None:
            return none_value

        return true_value if flag else false_value

    @classmethod
    def to_str_true_false(cls, flag: Optional[bool]) -> Optional[str]:
        return cls.to_str_object_from_boolean_object(flag, cls.TRUE, cls.FALSE, None)

    @classmethod
    def to_str_on_off(cls, flag: Optional[bool]) -> Optional[str]:
        return cls.to_str_object_from_boolean_object(flag, cls.ON, cls.OFF, None)

    @classmethod
    def to_str_yes_no(cls, flag: Optional[bool]) -> Optional[str]:
        return cls.to_str_object_from_boolean_object(flag, cls.YES, cls.NO, None)
