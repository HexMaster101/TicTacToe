

class TicTacToe:

    def __init__(self, firstChar):
        self.firstChar = firstChar
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.count = 0

        if self.firstChar == "X":
            self.secondChar = "O"
        elif self.firstChar == "O":
            self.secondChar = "X"

    def display(self):
        self.noOfHigh = 11
        print(
            f' {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} ')
        print("-" * self.noOfHigh)
        print(
            f' {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} ')
        print("-" * self.noOfHigh)
        print(
            f' {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} ')

    def play(self, coords):

        if self.count % 2 == 0:
            self.currentStepChar = self.firstChar
        else:
            self.currentStepChar = self.secondChar

        self.coords = coords

        def getRowCoord(coord, row):
            return coord - (3 * row + 1)

        for i in range(3):
            if coords >= 3*i + 1 and coords <= 3*(i+1):
                col = i
                row = getRowCoord(coords, col)
                self.grid[col][row] = self.currentStepChar

        print()
        print()
        game.display()
        self.count += 1


game = TicTacToe(input())
print('\n'*2)

print(
    '  1 | 2 | 3  ')
print("-" * 11)
print(
    '  4 | 5 | 6  ')
print("-" * 11)
print(
    '  7 | 8 | 9  ')
print('\n'*2)

for i in range(9):
    game.play(int(input()))
    print('\n'*3)
