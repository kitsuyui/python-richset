from dataclasses import dataclass

from richset import RichSet


@dataclass(frozen=True)
class Something:
    id: int
    name: str


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


def test_richset_is_empty() -> None:
    assert RichSet.from_list([]).is_empty()
    assert not RichSet.from_list([Something(1, "one")]).is_empty()


def test_richset_is_non_empty() -> None:
    assert RichSet.from_list([]).is_non_empty() is False
    assert RichSet.from_list([Something(1, "one")]).is_non_empty() is True


def test_richset_size() -> None:
    assert RichSet.from_list([]).size() == 0
    assert RichSet.from_list([Something(1, "one")]).size() == 1
    assert (
        RichSet.from_list(
            [
                Something(1, "one"),
                Something(2, "two"),
            ]
        ).size()
        == 2
    )
