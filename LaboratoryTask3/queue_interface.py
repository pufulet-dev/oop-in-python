from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')

class Queue(ABC, Generic[T]):
    @abstractmethod
    def enqueue(self, item: T) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> T:
        pass

    @abstractmethod
    def peek(self) -> T:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    def _ensure_not_empty(self) -> None:
        if self.is_empty():
            raise IndexError("Operation not allowed on an empty queue")


class NumberQueue(Queue[int]):
    def __init__(self):
        self.queue: List[int] = []

    def enqueue(self, item: int) -> None:
        self.queue.append(item)

    def dequeue(self) -> int:
        self._ensure_not_empty()
        return self.queue.pop(0)

    def peek(self) -> int:
        self._ensure_not_empty()
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0


class StringQueue(Queue[str]):
    def __init__(self):
        self.queue: List[str] = []

    def enqueue(self, item: str) -> None:
        self.queue.append(item)

    def dequeue(self) -> str:
        self._ensure_not_empty()
        return self.queue.pop(0)

    def peek(self) -> str:
        self._ensure_not_empty()
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0


class BooleanQueue(Queue[bool]):
    def __init__(self):
        self.queue: List[bool] = []

    def enqueue(self, item: bool) -> None:
        self.queue.append(item)

    def dequeue(self) -> bool:
        self._ensure_not_empty()
        return self.queue.pop(0)

    def peek(self) -> bool:
        self._ensure_not_empty()
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0