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


class Player:
    def __init__(self):
        self.layout = 0
        self.players = (1, 2)
        self.toggle_turn = 0
        self.layout_str = "000000000"
        self.winner = self.get_winner()

    def get_winner(self):
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
        if "0" in self.layout_str:
            for comb in win_combinations:
                if self.layout_str[comb[0]] == self.layout_str[comb[1]] == self.layout_str[comb[2]] != "0":
                    return self.layout_str[comb[0]]
        else:
            return "0"
        return None

    def check_move(self, move: int):
        if self.layout_str[-(move+1)] == "0" and self.winner is None:
            return True
        else:
            return False

    def do_move(self, move: int):
        if self.check_move(move):
            self.layout += 3**move*self.players[self.toggle_turn]
            self.layout_str = number_to_base(self.layout)
            self.toggle_turn = int(not self.toggle_turn)
            self.winner = self.get_winner()

    def send_to_console(self):
        index = 0
        dct_digit_str = {"1": "x", "2": "o"}
        for i in range(3):
            print("\n| ", end="")
            for j in range(3):
                if self.layout_str[index] != "0":
                    print(dct_digit_str[self.layout_str[index]], end=" | ")
                else:
                    print(8-index, end=" | ")
                index += 1
        print(f"\n c'est au tour du joueur {self.players[self.toggle_turn]}")

    def run_console(self):
        while self.winner is None:
            self.send_to_console()
            move = input("veuillez entrer un nombre parmi ceux qui restent à l'écran : ")
            if not move.isdigit() or int(move) not in range(9):
                print("\nvous avez entré un/des caractère(s) invalide(s)")
                move = int(move)
            if not self.check_move(move):
                print("\nCe mouvement n'est pas jouable")
                continue
            self.do_move(move)
        if self.winner != "0":
            print(f"\nle gagnant est le joueur {self.winner}")
        else:
            print("\nc'est une égalité!")


game = Player()
game.run_console()
