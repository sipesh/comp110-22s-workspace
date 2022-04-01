from __future__ import annotations


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"
    
    def __add__(self, rhs: str) -> StrArray:
        """Vectorized concatenation operator."""
        result: list[str] = []
        # Loop through each item in self.items
        for item in self.items:
            result.append(item + rhs)
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
print(result)