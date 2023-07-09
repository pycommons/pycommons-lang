from typing import ClassVar, Optional, overload, Union

from pycommons.base.utils import UtilityClass, ObjectUtils

from .arrayutils import ArrayUtils


class BooleanUtils(UtilityClass):
    """
    BooleanUtils class that provides helper methods to operate on boolean values that mirrors the
    features provided by the Apache Commons Lang's BooleanUtils class

    References:
        https://commons.apache.org/proper/commons-lang/apidocs/org/apache/commons/lang3/BooleanUtils.html
    """

    TRUE: ClassVar[str] = str(True).lower()
    """
    The "true" string
    """
    FALSE: ClassVar[str] = str(False).lower()
    """
    The "false" string
    """

    T: ClassVar[str] = "t"
    """
    The "t" string
    """
    F: ClassVar[str] = "f"
    """
    The "f" string
    """

    YES: ClassVar[str] = "yes"
    """
    The "yes" string
    """
    NO: ClassVar[str] = "no"
    """
    The "no" string
    """

    Y: ClassVar[str] = "y"
    """
    The "y" string
    """
    N: ClassVar[str] = "n"
    """
    The "n" string
    """

    OFF: ClassVar[str] = "off"
    """
    The "off" string
    """
    ON: ClassVar[str] = "on"
    """
    The "on" string
    """

    @classmethod
    def and_args(cls, *args: bool) -> bool:
        """
        Performs `and` operation on all the arguments and returns the result
        Args:
            *args: Boolean Arguments

        Returns:
            True if all the arguments are True, False otherwise
        """
        ArrayUtils.require_not_empty(args)
        for flag in args:
            ObjectUtils.require_not_none(flag)
            if cls.is_not_true(flag):
                return False

        return True

    @classmethod
    def or_args(cls, *args: bool) -> bool:
        """
        Performs `or` operation on all the arguments and returns the result
        Args:
            *args: Boolean Arguments

        Returns:
            True if any of the arguments are True, False otherwise
        """
        ArrayUtils.require_not_empty(args)
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
        """
        Return if an optional flag is `False` by handling `None` as False
        Args:
            flag: A boolean object or None

        Returns:
            True if the flag is False, False otherwise
        """
        return flag is False

    @classmethod
    def is_not_false(cls, flag: Optional[bool]) -> bool:
        """
        Negation of [`is_false`][pycommons.lang.booleanutils.BooleanUtils.is_false]
        method by handling `None` as False
        Args:
            flag: A boolean flag or None

        Returns:
            True if the flag is not False, False otherwise
        """
        return flag is not False

    @classmethod
    def is_true(cls, flag: Optional[bool]) -> bool:
        """
        Return if an optional flag is `True` by handling `None` as False
        Args:
            flag: A boolean object or None

        Returns:
            True if the flag is True, False otherwise
        """
        return flag is True

    @classmethod
    def is_not_true(cls, flag: Optional[bool]) -> bool:
        """
        Negation of [`is_false`][pycommons.lang.booleanutils.BooleanUtils.is_true]
        method by handling `None` as False
        Args:
            flag: A boolean flag or None

        Returns:
            True if the flag is not True, False otherwise
        """
        return flag is not True

    @classmethod
    def negate(cls, flag: Optional[bool]) -> Optional[bool]:
        """
        Negate a boolean by returning `None` for `None`.
        Args:
            flag: A boolean flag or None

        Returns:
            True if False, False if True, None if None
        """
        if flag is None:
            return None
        return not flag

    @classmethod
    @overload
    def to_boolean(cls, x: Optional[bool]) -> bool:
        ...

    @classmethod
    @overload
    def to_boolean(cls, x: int) -> bool:
        ...

    @classmethod
    @overload
    def to_boolean(cls, x: Optional[str]) -> bool:
        ...

    @classmethod
    def to_boolean(cls, x: Union[int, str, bool, None]) -> bool:
        if x is None:
            return False

        if isinstance(x, bool):
            return x

        if isinstance(x, int):
            return x != 0

        if isinstance(x, str):
            _x = x.lower()
            return cls.or_args(
                _x == cls.TRUE, _x == cls.T, _x == cls.Y, _x == cls.YES, _x == cls.ON
            )

        raise ValueError("Unable to convert the value to boolean")

    @classmethod
    @overload
    def parse_bool(
        cls, value: Optional[int], true_value: Optional[int], false_value: Optional[int]
    ) -> bool:
        ...

    @classmethod
    @overload
    def parse_bool(
        cls, value: Optional[str], true_value: Optional[str], false_value: Optional[str]
    ) -> bool:
        ...

    @classmethod
    def parse_bool(
        cls,
        value: Optional[Union[int, str]],
        true_value: Optional[Union[int, str]],
        false_value: Optional[Union[int, str]],
    ) -> bool:
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
    def to_bool_object(
        cls,
        value: Optional[Union[int]],
        true_value: Optional[Union[int]],
        false_value: Optional[Union[int]],
        none_value: Optional[Union[int]],
    ) -> Optional[bool]:
        ...

    @classmethod
    @overload
    def to_bool_object(
        cls,
        value: Optional[Union[str]],
        true_value: Optional[Union[str]],
        false_value: Optional[Union[str]],
        none_value: Optional[Union[str]],
    ) -> Optional[bool]:
        ...

    @classmethod
    def to_bool_object(
        cls,
        value: Optional[Union[int, str]],
        true_value: Optional[Union[int, str]],
        false_value: Optional[Union[int, str]],
        none_value: Optional[Union[int, str]],
    ) -> Optional[bool]:
        if value == true_value:
            return True

        if value == false_value:
            return False

        if value == none_value:
            return None

        raise ValueError("value does not match either of true_value or false_value or null_value")

    @classmethod
    @overload
    def to_boolean_object(cls, value: Optional[bool]) -> Optional[bool]:
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
    def to_boolean_object(cls, value: Union[str, bool, int, None]) -> Optional[bool]:
        if value is None:
            return None

        if isinstance(value, bool):
            return value

        if isinstance(value, int):
            return value != 0

        if isinstance(value, str):
            _flag = value.lower()
            if cls.or_args(
                _flag == cls.TRUE, _flag == cls.T, _flag == cls.Y, _flag == cls.YES, _flag == cls.ON
            ):
                return True

            if cls.or_args(
                _flag == cls.FALSE,
                _flag == cls.F,
                _flag == cls.N,
                _flag == cls.NO,
                _flag == cls.OFF,
            ):
                return False

            return None

        raise ValueError("Unable to parse the argument to boolean")

    @classmethod
    def to_int(cls, flag: bool, true_value: int = 1, false_value: int = 0) -> int:
        return true_value if flag else false_value

    @classmethod
    def to_int_from_boolean_object(
        cls, flag: Optional[bool], true_value: int, false_value: int, none_value: int
    ) -> int:
        if flag is None:
            return none_value

        return cls.to_int(flag, true_value, false_value)

    @classmethod
    def to_int_object_from_boolean_object(
        cls,
        flag: Optional[bool],
        true_value: Optional[int],
        false_value: Optional[int],
        none_value: Optional[int],
    ) -> Optional[int]:
        if flag is None:
            return none_value

        return true_value if flag else false_value

    @classmethod
    def to_str(cls, flag: bool, true_value: str, false_value: str) -> str:
        return true_value if flag else false_value

    @classmethod
    def to_str_from_boolean_object(
        cls, flag: Optional[bool], true_value: str, false_value: str, none_value: str
    ) -> str:
        if flag is None:
            return none_value

        return cls.to_str(flag, true_value, false_value)

    @classmethod
    def to_str_object_from_boolean_object(
        cls,
        flag: Optional[bool],
        true_value: Optional[str],
        false_value: Optional[str],
        none_value: Optional[str],
    ) -> Optional[str]:
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
