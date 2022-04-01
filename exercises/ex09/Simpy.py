"""Utility class for numerical operations."""

from __future__ import annotations
from asyncio import start_server

from typing import Union

__author__ = "730469262"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes the values attribute to the argument passed in."""
        self.values = values

    def __str__(self) -> str:
        """Function is called when a Simpy object is converted to a str representation."""
        return f"Simpy{self.values}"
    
    def fill(self, x: float, y: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        empty: list[float] = []
        i: int = 0
        while i < y:
            empty.append(x)
            i += 1
        self.values = empty 

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Fills in the values attribute with range of values."""
        empty: list[float] = []
        while start < stop:
            empty.append(start)
            start = start + step
        self.values = empty

    def sum(self) -> float:
        return sum(self.values)
        


    # def __add__(self, rhsL Union[float, Simpy]) -> Simpy:


        
