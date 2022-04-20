"""Tests for linked list utils."""

# from pytest import pytest
import pytest
from exercises.ex10.linked_list import Node, last, value_at

__author__ = "730469262"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_index_of_list() -> None:
    """Tests to see if function returns node at specific index."""
    node_list = Node(10, Node(20, Node(30, None)))
    index: int = 2
    assert value_at(node_list, index) == 30


def test_index_at() -> None:
    """Tests a list that is empty."""
    with pytest.raises(IndexError):
        value_at(None, 3)


def test_max_value() -> None:
    """Tests a list and returns max value in that list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max_empty() -> None:
    """Tests a list an empty list for max value."""
    with pytest.raises(ValueError):
        value_at(None)


def linkify() -> None:
    """Tests a list to see if it returns items."""
    list_items = [10, 20, 30, 40]
    assert linkify(list_items[1]) == 20