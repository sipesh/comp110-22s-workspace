
"""EX01 - Chardle - Wordle."""

__author__ = "730469262"

word: str = input("Enter a five letter word:")
letter: str = input("Enter a single character:")
print("Searching for " + letter + " in " + word)

if word[0] == letter:
    print(letter, "is at index 0")
elif word[1] == letter:
    print(letter, "is at index 1")
elif word[2] == letter:
    print(letter, "is at index 2")
elif word[3] == letter:
    print(letter, "is at index 3")
elif word[4] == letter:
    print(letter, "is at index 4")
else:
    print("no letter in word")

    
