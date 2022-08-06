from dataclasses import dataclass

import pytest

from richset import RichSet


@dataclass(frozen=True)
class Something:
    id: int
    name: str


def test_richset_get_first() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
        ]
    )
    assert rs.get_first() == Something(1, "one")
    rs2 = RichSet[Something].from_list([])
    assert rs2.get_first() is None


def test_richset_first() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
        ]
    )
    assert rs.first() == Something(1, "one")

    with pytest.raises(IndexError):
        RichSet.from_list([]).first()


def test_richset_get_last() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
        ]
    )
    assert rs.get_last() == Something(2, "two")
    rs2 = RichSet[Something].from_list([])
    assert rs2.get_last() is None


def test_richset_last() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
        ]
    )
    assert rs.last() == Something(2, "two")

    with pytest.raises(IndexError):
        RichSet.from_list([]).last()
