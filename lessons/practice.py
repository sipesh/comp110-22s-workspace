win = 9


def game(y: int) -> int:
    global win
    win += 2
    return win


print(game(2))