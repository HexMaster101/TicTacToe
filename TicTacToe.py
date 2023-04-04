class TicTacToe:

    def __init__(self, firstChar):
        self.firstChar = firstChar
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.columnSet = set()
        self.noRepeatSet = set()
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
        self.coords = coords
        if 0 < self.coords < 10:

            if self.coords not in self.noRepeatSet:
                self.noRepeatSet.add(coords)
            else:
                print(f"{coords} is already placed")
                return

            if self.count % 2 == 0:
                self.currentStepChar = self.firstChar
            else:
                self.currentStepChar = self.secondChar

            def getRowCoord(coord, row):
                return coord - (3 * row + 1)

            for i in range(3):
                if coords >= 3*i + 1 and coords <= 3*(i+1):
                    col = i
                    row = getRowCoord(coords, col)
                    self.grid[col][row] = self.currentStepChar

            print('\n'*2)
            game.display()
            print()
            if game.DidSomeoneWin():
                print(f"{self.currentStepChar} wins")
                global condition
                condition = False

            if self.count == 8:
                condition = False
            self.count += 1

        else:
            print("Type a Correct Input")

    def DidSomeoneWin(self):
        if self.count > 3:
            # checking Rows
            for i in self.grid:
                if " " not in i:
                    if i[0] == i[1] == i[2]:
                        return True

            # checking Columns
            for i in range(len(self.grid)):
                if "X" in self.grid[i] or "O" in self.grid[i]:
                    self.columnSet.update([i])

            for i in self.columnSet:
                if self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                    return True

            # checking Diagonals
            if len(self.columnSet) == 3:
                if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
                    return True
                if self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
                    return True

        else:
            return False


count = 0
game = TicTacToe(input())
print('\n'*2)

for i in range(3):
    print(f' {i + count + 1} | {i + count + 2} | {i + count + 3} ')
    if i < 2:
        print("-" * 11)
    count += 2

print('\n'*2)
condition = True
while condition:
    game.play(int(input()))
    print('\n'*3)
