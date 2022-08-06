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

    rs = RichSet.from_list(
        [
            Something(1, "john"),
            Something(2, "jane"),
            Something(3, "john"),  # name duplicated
        ]
    )

    with pytest.raises(ValueError) as err:
        rs.to_dict(lambda r: r.name)
    assert str(err.value) == "duplicate keys"

    with pytest.raises(ValueError) as err:
        rs.to_dict(lambda r: r.name, duplicated="error")
    assert str(err.value) == "duplicate keys"

    assert rs.to_dict(lambda r: r.name, duplicated="first") == {
        "john": Something(1, "john"),
        "jane": Something(2, "jane"),
    }

    assert rs.to_dict(lambda r: r.name, duplicated="last") == {
        "john": Something(3, "john"),
        "jane": Something(2, "jane"),
    }

    with pytest.raises(ValueError) as err:
        rs.to_dict(lambda r: r.name, duplicated="invalid")  # type: ignore
    assert str(err.value) == "invalid duplicated value"


def test_richset_to_dict_of_list() -> None:
    rs = RichSet.from_list(
        [
            Something(1, "john"),
            Something(2, "jane"),
            Something(3, "john"),  # name duplicated
        ]
    )
    assert rs.to_dict_of_list(lambda r: r.name) == {
        "john": [Something(1, "john"), Something(3, "john")],
        "jane": [Something(2, "jane")],
    }
