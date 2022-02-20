"""Three different functions that are then each tested."""
__author__ = "730469262"


def only_evens(a: list[int]) -> list[int]:
    """Given a list of ints, only prints the even numbers in the list."""
    even_numbers: list[int] = []
    i: int = 0
    while i < len(a):
        if a[i] % 2 == 0:
            even_numbers.append(a[i])
        i = i + 1
    return even_numbers


def sub(a_list: list[int], y: int, z: int) -> list[int]:
    """Prints numbers in a given range."""
    empty_list: list[int] = [] 
    if len(a_list) == 0 or y > len(a_list) or z <= 0:
        return empty_list
    if y < 0: 
        y = 0
    if z > len(a_list):
        z = len(a_list)
    while y < z:
        empty_list.append(a_list[y])
        y = y + 1
    return empty_list


def concat(x: list[int], y: list[int]) -> list[int]:
    """Concatenates two given lists together."""
    empty_list: list[int] = []
    i: int = 0
    while i < len(x):
        empty_list.append(x[i])
        i = i + 1
    j: int = 0
    while j < len(y):
        empty_list.append(y[j])
        j = j + 1
    return empty_list
