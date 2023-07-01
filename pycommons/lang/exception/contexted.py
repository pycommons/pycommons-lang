from __future__ import annotations

from typing import Any

from pycommons.base.maps import Map

from pycommons.lang.exception.exception import CommonsException


class ContextedException(CommonsException):
    """
    Wrap another exception using the ContextedException and rethrow by adding
    context key value pairs. The context can be propagated through the exception
    traceback and the necessary logging, handling can be done with the
    context key values

    Examples:
        ```python
        try:
            ...
        except RuntimeError as exc:
            raise ContextedException().set_context_value(
                "transactionId", "1234567890"
            ) from exc
        ```
    """

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self._context: Map[str, Any] = Map()

    @property
    def context(self) -> Map[str, Any]:
        """
        Gets the context key-value pairs for this exception

        Returns:
            The context map
        """
        return self._context

    def with_context(self, key: str, value: Any) -> ContextedException:
        """
        Adds the key-value pair to the context map and returns the exception (Like a builder)
        Args:
            key: key
            value: value

        Returns:
            The exception object
        """
        self._context.put(key, value)
        return self

    def with_context_values(self, **kwargs: Any) -> ContextedException:
        """
        Adds multiple key value pairs to the context map and returns the exception

        Args:
            **kwargs: key-value pairs

        Returns:
            The exception object
        """
        self._context.put_all(kwargs)
        return self
