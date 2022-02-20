"""Tests for utils."""
__author__ = "730469262"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_one_value() -> None:
    """Tests if the input is only one value."""
    a: list[int] = [0]
    assert only_evens(a) == [0]


def test_only_evens_return_even() -> None:
    """Tests if given a list of ints, if the function returns only even numbers."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(a) == [2, 4, 6]


def test_only_evens_negative() -> None:
    """Tests if given a list of ints, if the functions includes the negative even number."""
    a: list[int] = [14, 16, -22, 35]
    assert only_evens(a) == [14, 16, -22]


def test_sub_list() -> None:
    """Given a list of ints, tests if the output is in the range."""
    a_list: list[int] = [10, 20, 40, 50]
    y = 1
    z = 3
    assert sub(a_list, y, z) == [a_list, 20, 40]


def test_sub_negative() -> None:
    """Tests the list if a negative number is in the list."""
    a_list: list[int] = [-1, -8, 15, 17, 16]
    y = 1
    z = 3
    assert sub(a_list, y, z) == [-8, 15]


def test_sub_empty() -> None:
    """Tests an empty list."""
    a_list: list[int] = []
    y = 0
    z = 1
    assert sub(a_list, y, z) == []


def test_concat_list() -> None:
    """Concatenates two lists together."""
    x: list[int] = [1, 2]
    y: list[int] = [3, 4]
    assert concat(x, y) == [1, 2, 3, 4]


def test_concat_empty() -> None:
    """Tests if a x is an empty list of ints, and if y is a list of ints."""
    x: list[int] = []
    y: list[int] = [234, 897]
    assert concat(x, y) == [234, 897]


def test_concat_negative() -> None: 
    """Tests is the function still concatenates two lists if one of the lists has a negative int."""
    x: list[int] = [-1, -2, 0, -4]
    y: list[int] = [0, 1, 2]
    assert concat(x, y) == [-1, -2, 0, -4, 0, 1, 2]
