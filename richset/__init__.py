from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Hashable, Iterator, TypeVar, overload

T = TypeVar("T")
S = TypeVar("S")
Key = TypeVar("Key", bound=Hashable)


@dataclass(frozen=True)
class RichSet(Generic[T]):
    records: list[T]

    # factory classmethods

    @classmethod
    def from_list(cls, lst: list[T]) -> RichSet[T]:
        """Returns a new RichSet from a list."""
        return cls(records=lst[:])

    # magic methods

    def __iter__(self) -> Iterator[T]:
        return iter(self.records)

    # conversions

    def to_list(self) -> list[T]:
        """Returns a list of records."""
        return self.records[:]

    def to_dict(self, key: Callable[[T], Key]) -> dict[Key, T]:
        """Returns a dictionary mapping keys to values."""
        return {key(r): r for r in self.records}

    # list accessors

    @overload
    def get_first(self) -> T | None:
        ...

    @overload
    def get_first(self, default: S) -> T | S:
        ...

    def get_first(self, default: S | None = None) -> T | S | None:
        """Returns the first record in the RichSet
        or default value (None) if the RichSet is empty."""
        if self.records:
            return self.records[0]
        return default

    def first(self) -> T:
        """Returns the first record in the RichSet."""
        if self.records:
            return self.records[0]
        raise IndexError("RichSet is empty")

    @overload
    def get_last(self) -> T | None:
        ...

    @overload
    def get_last(self, default: S) -> T | S:
        ...

    def get_last(self, default: S | None = None) -> T | S | None:
        """Returns the last record in the RichSet
        or default value (None) if the RichSet is empty."""
        if self.records:
            return self.records[-1]
        return default

    def last(self) -> T:
        """Returns the last record in the RichSet."""
        if self.records:
            return self.records[-1]
        raise IndexError("RichSet is empty")

    # list manipulations

    def unique(self, key: Callable[[T], Key]) -> RichSet[T]:
        """Returns a new RichSet with unique records."""
        new_records = []
        seen = set()
        for r in self.records:
            key_ = key(r)
            if key_ not in seen:
                new_records.append(r)
                seen.add(key_)
        return RichSet.from_list(new_records)

    def map(self, f: Callable[[T], S]) -> RichSet[S]:
        """Returns a new RichSet with mapped records."""
        return RichSet.from_list(list(map(f, self.records)))

    # miscs

    def is_empty(self) -> bool:
        """Returns True if the RichSet is empty."""
        return not self.records
