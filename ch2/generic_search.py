from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional, Protocol
from heapq import heappush, heappop

T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False


C = TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        return self == other

    def __lt__(self: C, other: C) -> bool:
        return self < other

    def __gt__(self: C, other: C) -> bool:
        return self > other

    def __le__(self: C, other: C) -> bool:
        return self <= other

    def __ge__(self: C, other: C) -> bool:
        return self >= other


def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    hi: int = len(sequence) - 1
    while low <= hi:
        mid: int = (hi + low) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            hi = mid - 1
        else:
            return True
    return False