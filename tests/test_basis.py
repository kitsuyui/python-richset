from dataclasses import dataclass

import pytest

from richset import RichSet


@dataclass(frozen=True)
class Something:
    id: int
    name: str


def test_richset_to_list() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
        ]
    )
    assert rs.to_list() == [Something(1, "one"), Something(2, "two")]


def test_richset_iter() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
        ]
    )
    for i, r in enumerate(rs):
        if i == 0:
            assert r == Something(1, "one")
        elif i == 1:
            assert r == Something(2, "two")


def test_richset_to_dict() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
        ]
    )
    assert rs.to_dict(lambda r: r.id) == {
        1: Something(1, "one"),
        2: Something(2, "two"),
    }


def test_richset_unique() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
            Something(1, "one"),
        ]
    )
    assert rs.unique(lambda r: r.id).to_list() == [
        Something(1, "one"),
        Something(2, "two"),
    ]


def test_richset_map() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
        ]
    )
    assert rs.map(lambda r: r.id).to_list() == [1, 2]


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


def test_richset_is_empty() -> None:
    assert RichSet.from_list([]).is_empty()
    assert not RichSet.from_list([Something(1, "one")]).is_empty()
