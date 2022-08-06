# richset

[![Python](https://img.shields.io/pypi/pyversions/richset.svg)](https://badge.fury.io/py/richset)
[![PyPI version](https://img.shields.io/pypi/v/richset.svg)](https://pypi.python.org/pypi/richset/)
[![codecov](https://codecov.io/gh/kitsuyui/python-richset/branch/main/graph/badge.svg?token=LH210UT9Q0)](https://codecov.io/gh/kitsuyui/python-richset)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

## Install

```sh
$ pip install richset
```

## Usage

```python
from dataclasses import dataclass
from richset import RichSet


@dataclass(frozen=True)
class Something:
    id: int
    name: str


richset = RichSet.from_list([
    Something(1, 'one'),
    Something(2, 'two'),
])
```

### Conversions

```python
richset.to_list()  # => [Something(1, 'one'), Something(2, 'one')]
richset.to_dict(lambda s: s.id)  # => {1: Something(1, 'one'), 2: Something(2, 'one')}
```

### Access to items

```python
richset.is_empty()  # => False
richset.first()  # => returns first item or raise Error
richset.get_first()  # => returns first item or None
```

### Manipulation

```python
richset.unique(lambda s: s.id)  # => unique by id
richset.map(lambda s: s.id).to_list()  # => [1, 2]
```

# LICENSE

The 3-Clause BSD License. See also LICENSE file.
