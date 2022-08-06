from dataclasses import dataclass

from richset import RichSet


@dataclass(frozen=True)
class Something:
    id: int
    name: str


def test_richset_filter() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
            Something(3, "two"),
        ]
    )
    assert rs.filter(lambda r: r.id > 1).to_list() == [
        Something(2, "two"),
        Something(3, "two"),
    ]


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


def test_richset_slice() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "one"),
            Something(2, "two"),
            Something(3, "three"),
        ]
    )
    assert rs.slice(0, 0).to_list() == []
    assert rs.slice(1, 2).to_list() == [Something(2, "two")]
    assert rs.slice(0, 3).to_list() == rs.to_list()
    assert rs.slice(0, 4).to_list() == rs.to_list()
    assert rs.slice(1, 3).to_list() == [
        Something(2, "two"),
        Something(3, "three"),
    ]
    assert rs.slice(-1, 3).to_list() == [Something(3, "three")]
