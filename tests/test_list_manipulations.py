from dataclasses import dataclass

from richset import RichSet


@dataclass(frozen=True)
class Something:
    id: int
    name: str


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
