from types import TracebackType
from typing import Optional, Any


class CommonsException(Exception):
    def __init__(self, *args: Any):
        self._message: Optional[str] = None if len(args) == 0 else args[0]
        super().__init__(*args)

    @property
    def message(self) -> Optional[str]:
        return self._message

    @property
    def cause(self) -> Optional[BaseException]:
        return self.__cause__

    @property
    def traceback(self) -> Optional[TracebackType]:
        return self.__traceback__

    @property
    def detailed_message(self) -> Optional[str]:
        return str(self.cause) if self.cause is not None else None
