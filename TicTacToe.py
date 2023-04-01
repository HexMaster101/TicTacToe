class TicTacToe:

    def __init__(self, first_char):
        self.first_char = first_char
        self.Game_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.count = 0

        if self.first_char == "X":
            self.second_char = "O"
        elif self.first_char == "O":
            self.second_char = "X"

    def display(self):
        self.no_of_high = 11
        print(
            f' {self.Game_list[0][0]} | {self.Game_list[0][1]} | {self.Game_list[0][2]} ')
        print("-" * self.no_of_high)
        print(
            f' {self.Game_list[1][0]} | {self.Game_list[1][1]} | {self.Game_list[1][2]} ')
        print("-" * self.no_of_high)
        print(
            f' {self.Game_list[2][0]} | {self.Game_list[2][1]} | {self.Game_list[2][2]} ')

    def play(self, coords):
        if self.count % 2 == 0:
            self.current_step_char = self.first_char
        else:
            self.current_step_char = self.second_char

        self.coords = coords
        if self.coords == 1:
            self.Game_list[0][0] = self.current_step_char
        elif self.coords == 2:
            self.Game_list[0][1] = self.current_step_char
        elif self.coords == 3:
            self.Game_list[0][2] = self.current_step_char
        elif self.coords == 4:
            self.Game_list[1][0] = self.current_step_char
        elif self.coords == 5:
            self.Game_list[1][1] = self.current_step_char
        elif self.coords == 6:
            self.Game_list[1][2] = self.current_step_char
        elif self.coords == 7:
            self.Game_list[2][0] = self.current_step_char
        elif self.coords == 8:
            self.Game_list[2][1] = self.current_step_char
        elif self.coords == 9:
            self.Game_list[2][2] = self.current_step_char

        print()
        print()
        game.display()
        self.count += 1


game = TicTacToe(input())
print()
print()
print(
    '  1 | 2 | 3  ')
print("-" * 11)
print(
    '  4 | 5 | 6  ')
print("-" * 11)
print(
    '  7 | 8 | 9  ')
print()
print()
game.play(int(input()))
print()
print()
print()
game.play(int(input()))
print()
print()
print()
game.play(int(input()))
print()
print()
print()
game.play(int(input()))
print()
print()
print()
game.play(int(input()))
print()
print()
print()
game.play(int(input()))
print()
print()
print()
game.play(int(input()))
print()
print()
print()
game.play(int(input()))
print()
print()
print()
game.play(int(input()))
