"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730469262"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows  of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Makes a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        if N > len(table[column]):
            N = len(table[column])
        items: int = 0
        empty: list[str] = []
        while items < N:
            empty.append(table[column][items])
            items = items + 1
        result[column] = empty
    return result


def select(table: dict[str, list[str]], names_columns: list[str]) -> dict[str, list[str]]:
    """Makes a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in names_columns:
        result[column] = table[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Making a new column based table with two column based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result:
            for item in table2[column]:
                result[column].append(item) 
        else:
            result[column] = table2[column]
    return result


def count(data: list[str]) -> dict[str, int]:
    """Takes in a list[str] and returns a dict[str, int] where each key is a unique value in the given list and each value is the count of the number of times that the value appeared."""
    result: dict[str, int] = {}
    for item in data:
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result
