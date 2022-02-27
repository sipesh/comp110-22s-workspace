"""Unit Tests for dictionary."""
__author__ = "730469262"

import pytest
from dictionary import invert, favorite_color, count


def test_invert_one_key_one_value() -> None:
    """Tests to see if the function inverts one key and one value."""
    x: dict[str, str] = {"apple": "cat"}
    assert invert(x) == {'cat': 'apple'}


def test_invert_two_samekeys_two_values() -> None:
    """Tests when two keys are the same."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_two_keys_and_values() -> None:
    """Tests to see if the function inverts two keys and two values."""
    x: dict[str, str] = {"UNC": "Ramses", "NCSU": "Tuffy"}
    assert invert(x) == {'Ramses': 'UNC', 'Tuffy': 'NCSU'}


def test_favorite_color_blue() -> None:
    """Tests when the function is given two values that are the same."""
    x: dict[str, str] = {"Ramses": "blue", "Benny": "blue", "Tuffy": "red"}
    assert favorite_color(x) == "blue"


def test_favorite_color_onecolor() -> None:
    """Tests when the function is given one value and one key."""
    x: dict[str, str] = {"Ramses": "blue"}
    assert favorite_color(x) == "blue"


def test_favorite_color() -> None:
    """Tests if when given two values that are the same and two other values that are also the same, with only one value that doesn't have a pair, if the function returns the first color that was counted first."""
    x: dict[str, str] = {"Elaine": "yellow", "George": "blue", "Jerry": "yellow", "Michael": "blue", "Sally": "pink"}
    assert favorite_color(x) == "yellow"


def test_count_onetime() -> None:
    """Counts number of times an item is in a list."""
    x: list[str] = ["apple", "orange", "radicchio"]
    assert count(x) == {"apple": 1, "orange": 1, "radicchio": 1}


def test_count_empty() -> None:
    """Tests if there if the list is empty."""
    x: list[str] = []
    assert count(x) == {}


def test_count_manytimes() -> None:
    """Tests when there are a lot of the same number of items in the list."""
    x: list[str] = ["Jerry", "Jerry", "Elaine", "Jerry", "George", "Kosmo", "Kosmo", "George"]
    assert count(x) == {"Jerry": 3, "Elaine": 1, "Kosmo": 2, "George": 2}
