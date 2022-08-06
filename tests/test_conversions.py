from dataclasses import dataclass

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
