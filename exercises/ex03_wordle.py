"""structured wordle."""
__author__ = "730469262"


def contains_char(secret: str, character: str) -> bool:
    """Testing length of string."""
    assert len(character) == 1
    index: int = 0
    while index < len(secret):
        if secret[index] == character:
            return True
        index = index + 1 
    return False 


def emojified(guess: str, secret: str) -> str:
    """Codifying guess."""
    assert len(guess) == len(secret)
    index: int = 0
    final_emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(secret):
        if guess[index] == secret[index]:
            final_emoji = final_emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[index]) is True:
                final_emoji = final_emoji + YELLOW_BOX
            else:
                final_emoji = final_emoji + WHITE_BOX           
        index = index + 1
    return (final_emoji)


def input_guess(expectedlength: int) -> str:
    """Promting user for a guess."""
    guess: str = input(f"Enter a {expectedlength} character word: ")
    while len(guess) != expectedlength:  
        guess = input(f"That wasn't {expectedlength} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    tries: int = 1
    searching_forguess: bool = True
    secret: str = "codes"
    while tries <= 6 and searching_forguess:
        print(f"=== Turn {tries}/6 ===")
        guess = (input_guess(5)) 
        print(emojified(guess, secret))
        if guess == secret:
            searching_forguess = False
            print(f"You won in {tries}/6 turns!")
        tries = tries + 1
    if tries > 6 and searching_forguess:
        print("X/6 - Sorry, try again tomorrow!")
      