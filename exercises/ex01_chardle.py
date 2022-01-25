"""EX01 - Chardle - Wordle.""" 

__author__ = "730469262"


word: str = input("Enter a five character word:")
if len(word) < 5 or len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character:")
if len(letter) > 1 or len(letter) < 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word)

new_count: int = 0 
if word[0] == letter:
    print(letter, "found at index 0")
    new_count = new_count + 1
if word[1] == letter:   
    print(letter, "found at index 1")
    new_count = new_count + 1 
if word[2] == letter:
    print(letter, "found at index 2")
    new_count = new_count + 1
if word[3] == letter:
    print(letter, "found at index 3")
    new_count = new_count + 1
if word[4] == letter:
    print(letter, "found at index 4")
    new_count = new_count + 1

if new_count == 0:
    print("No instances of", letter, "found in", word)
else:
    if new_count == 1:
        print("1 instance of", letter, "found in", word)
    if new_count == 2 or new_count == 3 or new_count == 4 or new_count == 5:
        print(new_count, "instances of", letter, "found in", word)