"""Some examples of tender, loving fucntion definitions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


print(love("Holly"))


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    index: int = 0 
    while index < n:
        love_note += love(to) + "\n"
        index += 1
    return love_note