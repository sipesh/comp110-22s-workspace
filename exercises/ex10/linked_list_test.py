"""Tests for linked list utils."""

# from pytest import pytest
import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, is_equal, scale

__author__ = "730469262"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_index_of_list() -> None:
    """Tests to see if function returns node at specific index."""
    node_list = Node(10, Node(20, Node(30, None)))
    index: int = 2
    assert value_at(node_list, index) == 30


def test_value_at_empty() -> None:
    """Tests a list that is empty and trys to return an value at an index."""
    with pytest.raises(IndexError):
        value_at(None, 3)


def test_max_value() -> None:
    """Tests a list and returns max value in that list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max_empty() -> None:
    """Tests a list an empty list for max value."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify_list() -> None:
    """Tests a list to see if function returns a Linked List of Nodes with same value as input list."""
    linked_list = Node(10, Node(20, Node(30, None))) 
    list_items = [10, 20, 30]
    assert is_equal(linkify(list_items), linked_list) 


def test_linkify_empty() -> None:
    """Tests an empty list to see if linkify returns None."""
    linked_list = Node(10, Node(20, Node(30, None)))
    list_items = []
    assert is_equal(linkify(list_items), linked_list)


def test_scale_linked_list() -> None:
    """Tests a linked list and returns a new list of nodes scaled by the factor."""
    items = [1, 2, 3]
    assert scale(linkify(items), 2) 


def test_scale_empty() -> None:
    """Tests an empty linked list."""
    items = []
    assert scale(linkify(items), 2)