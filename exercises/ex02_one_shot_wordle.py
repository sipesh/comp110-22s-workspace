"""One shot wordle."""
__author__ = "730469262"

SECRET = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
final_emoji: str = ""
index: int = 0
new_index: int = 0
character_not_in_word: bool = False
guess: str = input("What is your 6-letter guess? ")

while len(guess) != 6:  
    guess = input("That was not 6 letters! Try again: ")
while index < len(SECRET):
    if guess[index] == SECRET[index]:
        final_emoji = final_emoji + GREEN_BOX
    else:
        while character_not_in_word is False and new_index < len(SECRET):
            if guess[index] == SECRET[new_index]:
                character_not_in_word = True 
            new_index = new_index + 1
        if character_not_in_word is True:
            final_emoji = final_emoji + YELLOW_BOX
        else:
            final_emoji = final_emoji + WHITE_BOX
        new_index = 0
        character_not_in_word = False
    index = index + 1
print(final_emoji)


if guess == SECRET:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
  
 


 
