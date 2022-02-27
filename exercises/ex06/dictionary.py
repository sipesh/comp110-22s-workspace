"""Ex_06 Dictionary."""
__author__ = "730469262"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in dictionary."""
    dict1: dict[str, str] = {}
    for a in x:
        if x[a] in dict1:
            raise KeyError("This value has already been used.")
        dict1[x[a]] = a
    return dict1

        
def favorite_color(x: dict[str, str]) -> str:
    """Returns the value in dictionary that is listed the highest number of times."""
    dict1: dict[str, int] = {}
    for names in x:
        color: str = x[names]
        if color in dict1:
            dict1[color] += 1
        else:
            dict1[color] = 1 
    max_color: str = ""
    max_count: int = 0
    for colors in dict1:
        value: int = dict1[colors]
        if value > max_count:
            max_count = value
            max_color = colors
    return max_color


def count(x: list[str]) -> dict[str, int]:
    """Count of the number of times that value appeared in the input list."""
    newdict: dict[str, int] = {}
    for a in x:
        if a in newdict:
            newdict[a] += 1
        else: 
            newdict[a] = 1
    return newdict
