from typing import Any, Union


class Stack:

    def __init__(self) -> None:
        self.stack = []

    def is_empty(self) -> bool:
        if len(self.stack) != 0:
            return False
        return True

    def push(self, item: Any) -> None:
        self.stack.append(item)
        return

    def pop(self) -> Union[Any, None]:
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self) -> Union[Any, None]:
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)
