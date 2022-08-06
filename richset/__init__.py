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

    def filter(self, f: Callable[[T], bool]) -> RichSet[T]:
        """Returns a new RichSet with filtered records."""
        return RichSet.from_list(list(filter(f, self.records)))

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

    def slice(self, start: int, stop: int) -> RichSet[T]:
        """Returns a new RichSet with sliced records."""
        return RichSet.from_list(self.records[start:stop])

    def divide_at(self, index: int) -> tuple[RichSet[T], RichSet[T]]:
        """Returns a tuple of two RichSets,
        where the first contains records before the index,
        and the second contains records after the index."""
        return (
            self.slice(0, index),
            self.slice(index, self.size()),
        )

    # search

    def index_of(self, predicate: Callable[[T], bool]) -> int:
        """Returns the index of the first record satisfying the predicate.

        returns -1 if no record satisfies the predicate."""
        for i, r in enumerate(self.records):
            if predicate(r):
                return i
        return -1

    def indices_of(self, predicate: Callable[[T], bool]) -> list[int]:
        """Returns a list of indices of records satisfying the predicate."""
        return [i for i, r in enumerate(self.records) if predicate(r)]

    def search_first(
        self,
        predicate: Callable[[T], bool],
    ) -> tuple[int, T | None]:
        """Returns the first record satisfying the predicate.

        if no record satisfies the predicate, returns (-1, None)."""
        idx = self.index_of(predicate)
        if idx == -1:
            return (-1, None)
        return (idx, self.records[idx])

    def search_all(
        self,
        predicate: Callable[[T], bool],
    ) -> list[tuple[int, T]]:
        """Returns a list of tuples of indices and records
        satisfying the predicate.

        returns an empty list if no record satisfies the predicate."""
        indices = self.indices_of(predicate)
        return [(i, self.records[i]) for i in indices]

    # statistics

    def is_empty(self) -> bool:
        """Returns True if the RichSet is empty."""
        return not self.records

    def is_non_empty(self) -> bool:
        """Returns True if the RichSet is non-empty."""
        return not self.is_empty()

    def size(self) -> int:
        """Returns the number of records in the RichSet."""
        return len(self.records)

    def count(self, predicate: Callable[[T], bool]) -> int:
        """Returns the number of records satisfying the predicate."""
        return sum(1 for r in self.records if predicate(r))
