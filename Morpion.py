import builtins


def number_to_base(n, b=3):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    digits = digits[::-1]
    number = ""
    for i in range(9-len(digits)):
        number += "0"
    for digit in digits:
        number += str(digit)
    return number


def layout_to_console(layout):
    index = 0
    dct_digit_str = {"0": " ", "1": "x", "2": "o"}
    layout = number_to_base(layout)
    for i in range(3):
        print("\n| ", end="")
        for j in range(3):
            print(dct_digit_str[layout[index]], end=" | ")
            index += 1


def get_winner(layout):
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    layout = number_to_base(layout)
    for comb in win_combinations:
        if layout[comb[0]] == layout[comb[1]] == layout[comb[2]] != "0":
            return layout[comb[0]]
    return None


class ConsoleRunner:
    def __init__(self):
        self.layout = 0
        self.players = (1, 2)
        self.toggle_turn = 0

