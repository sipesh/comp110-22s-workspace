"""EX01 - Chardle - Wordle."""

__author__ = "730469262"

word: str = input("Enter a five letter word:")
if len(word) < 5 or len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character:")
if len(letter) > 1:
    print("Error: Character must be a single character")
    exit()
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
        print("no letter found")


count: int = word.count(letter)

if count == 0:
    print("No instances of", letter, "found in", word)
else:
    if count == 1:
        print("1 instance of", letter, "found in", word)
    if count == 2 or count == 3 or count == 4 or count == 5:
        print(count, "instances of", letter, "found in", word)

    
