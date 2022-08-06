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
    Something(3, 'three'),
])
```

### Conversions

```python
richset.to_list()  # => [Something(1, 'one'), Something(2, 'one'), Something(3, 'three')]
richset.to_tuple()  # => (Something(1, 'one'), Something(2, 'one'), Something(3, 'three'))
richset.to_dict(lambda s: s.id)  # => {1: Something(1, 'one'), 2: Something(2, 'one'), 3: Something(3, 'three')}
```

`to_dict()` takes second argument `duplicated` which is a choice of `'error'`, `'first'` or `'last'`.

if `duplicated` is `'error'`, then `to_dict()` raises `ValueError` if there are duplicated key
if `duplicated` is `'first'`, then `to_dict()` picks the first one of duplicated key.
if `duplicated` is `'last'`, then `to_dict()` picks the last one of duplicated key.

`to_dict_of_list()` is similar to `to_dict()` but it returns a dict of list.

```python
richset.to_dict_of_list(lambda s: s.name)  # => {'one': [Something(1, 'john'), Something(2, 'john')], 'three': [Something(3, 'jane')]}
```

### List accessors

```python
richset.first()  # => returns first item `Something(1, 'one')` or raise Error (if empty)
richset.get_first()  # => returns first item `Something(1, 'one')` or None (if empty)
richset.last()  # => returns last item `Something(3, 'three')` or raise Error (if empty)
richset.get_last()  # => returns last item `Something(3, 'three')` or None (if empty)
richset.nth(2)  # => returns 3rd item `Something(3, 'three')` or raise Error (if empty)
richset.get_nth(2)  # => returns 3rd item `Something(3, 'three')` or None (if empty)
```

Note: `get_first`, `get_last` and `get_nth` accept `default` argument that returns specified value instead of None.

```python
richset.get_nth(100, default=Something(-1, 'default'))  # => Something(-1, 'default')
```

### List basic manipulations

```python
richset.pushed(Something(4, 'four')).to_list()  # => [Something(1, 'one'), Something(2, 'two'), Something(3, 'three'), Something(4, 'four')]
richset.unshift(Something(4, 'four')).to_list()  # => [Something(4, 'four'), Something(1, 'one'), Something(2, 'two'), Something(3, 'three')]
richset.popped()  # => Something(3, 'three'), RichSet([Something(1, 'one'), Something(2, 'two')])
richset.shift()  # => Something(1, 'one'), RichSet([Something(2, 'two'), Something(3, 'three')])
richset.slice(1, 2).to_list()  # => [Something(2, 'two')]
richset.divide_at(1)  # => RichSet([Something(1, 'one')]), RichSet([Something(2, 'two'), Something(3, 'three')])
```

`pushed_all()` and `unshift_all()` are similar to `pushed()` and `unshift()` but they accept multiple items.
`popped_n()` and `shift_n()` are similar to `popped()` and `shift()` but they accept count of items.

### List functional manipulations

```python
richset.unique(lambda s: s.id)  # => unique by id
richset.map(lambda s: s.id).to_list()  # => [1, 2]
richset.filter(lambda s: s.id > 1).to_list()  # => [Something(2, 'two'), Something(3, 'three')]
```

### Search

```python
richset.index(lambda s: s.id == 2)  # => 1
richset.indices(lambda s: s.id == 2)  # => [1]
richset.search_first(lambda s: s.id == 2)  # => Something(2, 'two')
richset.search_last(lambda s: s.id == 2)  # => Something(2, 'two')
richset.search_all(lambda s: s.id == 2)  # => [Something(2, 'two')]
```

### Sorts

```python
richset.sorted(key=lambda s: s.name, reverse=True).to_list()  # => [Something(2, 'two'), Something(3, 'three'), Something(1, 'one')]
richset.reversed().to_list()  # => [Something(3, 'three'), Something(2, 'two'), Something(1, 'one')]
```

### Statistics

```python
richset.is_empty()  # => True if empty
richset.is_not_empty()  # => True if not empty
richset.size()  # => 3
richset.count(lambda s: s.id > 1)  # => 2
```

# LICENSE

The 3-Clause BSD License. See also LICENSE file.
