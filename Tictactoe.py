class TicTacToe():
    board = [
        {"cell1": 0, "cell2": 0, "cell3": 0},
        {"cell4": 0, "cell5": 0, "cell6": 0},
        {"cell7": 0, "cell8": 0, "cell9": 0},
    ]

    player = "P1"
    isInvalidMove = False
    isGameOver = False

    def move(self, position):
        if self.isGameOver:
            print("The Game Is Over")
            return

        player = self.player
        for row in self.board:
            self.updateBoard(player, row, position)

        if self.isInvalidMove:
            self.isInvalidMove = False
        else:
            self.togglePlayer()

        if  self.isWon():
            self.isGameOver = True
            print("Player " + self.player + " has won!")
        elif self.isBoardFull() and not self.isWon():
            self.isGameOver = True
            print("The game is draw")
        else:
            print(self.player + "'s move")

    def togglePlayer(self):
        if self.player == "P1":
            self.player = "P2"
        else:
            self.player = "P1"

    def updateBoard(self, player, row, position):
        if row.get(position) != None and row.get(position) == 0:
            row[position] = player
        elif row.get(position):
            print(player + ": Invalid move: " + position)

            self.isInvalidMove = True

    def isBoardFull(self):
        isBoardFull = True

        for row in self.board:
            for cell in row:
                if row[cell] == 0:
                    isBoardFull = False

        return isBoardFull

    def isDiagonalLeft(self):
        isDiagonal = True

        rowIndex = 1
        cellIndex = 1

        row1Cell1 = False
        row2Cell2 = False
        row3Cell3 = False

        for row in self.board:

            cellIndex = 1

            for cell in row.items():
                if rowIndex == 1 and cellIndex == 1:
                    row1Cell1 = cell[1] == self.player
                elif rowIndex == 2 and cellIndex == 2:
                    row2Cell2 = cell[1] == self.player
                elif rowIndex == 3 and cellIndex == 3:
                    row3Cell3 = cell[1] == self.player
                cellIndex = cellIndex + 1

            rowIndex = rowIndex + 1
        return row1Cell1 and row2Cell2 and row3Cell3

    def isDiagonalRight(self):
        isDiagonal = True

        rowIndex = 1
        cellIndex = 1

        row1Cell3 = False
        row2Cell2 = False
        row3Cell1 = False

        for row in self.board:

            cellIndex = 1

            for cell in row.items():
                if rowIndex == 1 and cellIndex == 3:
                    row1Cell3 = cell[1] == self.player
                elif rowIndex == 2 and cellIndex == 2:
                    row2Cell2 = cell[1] == self.player
                elif rowIndex == 3 and cellIndex == 1:
                    row3Cell1 = cell[1] == self.player
                cellIndex = cellIndex + 1

            rowIndex = rowIndex + 1
        return row1Cell3 and row2Cell2 and row3Cell1

    def isVerticalLeft(self):
        isVertical = True

        rowIndex = 1
        cellIndex = 1

        row1Cell1 = False
        row2Cell4 = False
        row3Cell7 = False

        for row in self.board:

            cellIndex = 1

            for cell in row.items():
                if rowIndex == 1 and cellIndex == 1:
                    row1Cell1 = cell[1] == self.player
                elif rowIndex == 2 and cellIndex == 1:
                    row2Cell4 = cell[1] == self.player
                elif rowIndex == 3 and cellIndex == 1:
                    row3Cell7 = cell[1] == self.player
                cellIndex = cellIndex + 1

            rowIndex = rowIndex + 1
        return row1Cell1 and row2Cell4 and row3Cell7

    def isVerticalCenter(self):
        isVertical = True

        rowIndex = 1
        cellIndex = 1

        row1Cell2 = False
        row2Cell5 = False
        row3Cell8 = False

        for row in self.board:

            cellIndex = 1

            for cell in row.items():
                if rowIndex == 1 and cellIndex == 2:
                    row1Cell2 = cell[1] == self.player
                elif rowIndex == 2 and cellIndex == 2:
                    row2Cell5 = cell[1] == self.player
                elif rowIndex == 3 and cellIndex == 2:
                    row3Cell8 = cell[1] == self.player
                cellIndex = cellIndex + 1

            rowIndex = rowIndex + 1
        return row1Cell2 and row2Cell5 and row3Cell8

    def isVerticalRight(self):
        isVertical = True

        rowIndex = 1
        cellIndex = 1

        row1Cell3 = False
        row2Cell6 = False
        row3Cell9 = False

        for row in self.board:

            cellIndex = 1

            for cell in row.items():
                if rowIndex == 1 and cellIndex == 3:
                    row1Cell3 = cell[1] == self.player
                elif rowIndex == 2 and cellIndex == 3:
                    row2Cell6 = cell[1] == self.player
                elif rowIndex == 3 and cellIndex == 3:
                    row3Cell9 = cell[1] == self.player
                cellIndex = cellIndex + 1

            rowIndex = rowIndex + 1
        return row1Cell3 and row2Cell6 and row3Cell9

    def isHorizontalTop(self):

        rowIndex = 1
        cellIndex = 1

        row1Cell1 = False
        row1Cell2 = False
        row1Cell3 = False

        for row in self.board:

            cellIndex = 1

            for cell in row.items():
                if rowIndex == 1 and cellIndex == 1:
                    row1Cell1 = cell[1] == self.player
                elif rowIndex == 1 and cellIndex == 2:
                    row1Cell2 = cell[1] == self.player
                elif rowIndex == 1 and cellIndex == 3:
                    row1Cell3 = cell[1] == self.player
                cellIndex = cellIndex + 1

            rowIndex = rowIndex + 1
        return row1Cell1 and row1Cell2 and row1Cell3

    def isHorizontalMiddle(self):

        rowIndex = 1
        cellIndex = 1

        row2Cell1 = False
        row2Cell2 = False
        row2Cell3 = False

        for row in self.board:

            cellIndex = 1

            for cell in row.items():
                if rowIndex == 2 and cellIndex == 1:
                    row2Cell1 = cell[1] == self.player
                elif rowIndex == 2 and cellIndex == 2:
                    row2Cell2 = cell[1] == self.player
                elif rowIndex == 2 and cellIndex == 3:
                    row3Cell3 = cell[1] == self.player
                cellIndex = cellIndex + 1

            rowIndex = rowIndex + 1
        return row2Cell1 and row2Cell2 and row2Cell3

    def isHorizontalBottom(self):

        rowIndex = 1
        cellIndex = 1

        row3Cell1 = False
        row3Cell2 = False
        row3Cell3 = False

        for row in self.board:

            cellIndex = 1

            for cell in row.items():
                if rowIndex == 3 and cellIndex == 1:
                    row3Cell1 = cell[1] == self.player
                elif rowIndex == 3 and cellIndex == 2:
                    row3Cell2 = cell[1] == self.player
                elif rowIndex == 3 and cellIndex == 3:
                    row3Cell3 = cell[1] == self.player
                cellIndex = cellIndex + 1

            rowIndex = rowIndex + 1
        return row3Cell1 and row3Cell2 and row3Cell3

    def isWon(self):
        return self.isDiagonalLeft() or self.isDiagonalRight() \
               or self.isVerticalLeft() or self.isVerticalCenter() or self.isVerticalRight() \
               or self.isHorizontalTop() or self.isHorizontalMiddle() or self.isHorizontalBottom()

    def resetBoard(self):
        self.isGameOver = False
        for row in self.board:
            for cell in row:
                row[cell] = 0


tictac = TicTacToe()


def testP1WinnerLeftDiagonal():
    tictac.move("cell1")  # P1
    tictac.move("cell2")  # P2

    tictac.move("cell5")  # P1
    tictac.move("cell3")  # P2

    tictac.move("cell9")  # P1
    tictac.move("cell6")  # P2


def testP1WinnerRightDiagonal():
    print("test P1 Winner Right Diagonal")

    tictac.move("cell3")  # P1
    tictac.move("cell2")  # P2

    tictac.move("cell5")  # P1
    tictac.move("cell1")  # P2

    tictac.move("cell7")  # P1
    tictac.move("cell6")  # P2


def testP1WinnerLeftVertical():
    print("test P1 Winner Left Vertical")

    tictac.move("cell1")  # P1
    tictac.move("cell3")  # P2

    tictac.move("cell4")  # P1
    tictac.move("cell2")  # P2

    tictac.move("cell7")  # P1
    tictac.move("cell6")  # P2


def testP1WinnerCenterVertical():
    print("test P1 Winner Center Vertical")

    tictac.move("cell2")  # P1
    tictac.move("cell3")  # P2

    tictac.move("cell5")  # P1
    tictac.move("cell1")  # P2

    tictac.move("cell8")  # P1
    tictac.move("cell6")  # P2


def testP1WinnerRightVertical():
    print("test P1 Winner Right Vertical")

    tictac.move("cell3")  # P1
    tictac.move("cell4")  # P2

    tictac.move("cell6")  # P1
    tictac.move("cell1")  # P2

    tictac.move("cell9")  # P1
    tictac.move("cell6")  # P2


def testP1WinnerTopHorizontal():
    print("test P1 Winner Top Horizontal")

    tictac.move("cell1")  # P1
    tictac.move("cell4")  # P2

    tictac.move("cell2")  # P1
    tictac.move("cell5")  # P2

    tictac.move("cell3")  # P1
    tictac.move("cell6")  # P2D


def testP1WinnerMiddleHorizontal():
    print("test P1 Winner Middle Horizontal")

    tictac.move("cell4")  # P1
    tictac.move("cell1")  # P2

    tictac.move("cell5")  # P1
    tictac.move("cell2")  # P2

    tictac.move("cell6")  # P1
    tictac.move("cell3")  # P2D


def testP1WinnerBottomHorizontal():
    print("test P1 Winner Bottom Horizontal")

    tictac.move("cell7")  # P1
    tictac.move("cell1")  # P2

    tictac.move("cell8")  # P1
    tictac.move("cell2")  # P2

    tictac.move("cell9")  # P1
    tictac.move("cell3")  # P2


def testDraw():
    print("test Draw")

    tictac.move("cell1")  # P1
    tictac.move("cell2")  # P2

    tictac.move("cell3")  # P1
    tictac.move("cell4")  # P2

    tictac.move("cell5")  # P1
    tictac.move("cell6")  # P2

    tictac.move("cell7")  # P1
    tictac.move("cell8")  # P1
    tictac.move("cell9")  # P2


tictac.resetBoard()
testP1WinnerLeftDiagonal()

tictac.resetBoard()
testP1WinnerRightDiagonal()

tictac.resetBoard()
testP1WinnerLeftVertical()

tictac.resetBoard()
testP1WinnerCenterVertical()

tictac.resetBoard()
testP1WinnerTopHorizontal()

tictac.resetBoard()
testP1WinnerMiddleHorizontal()

tictac.resetBoard()
testP1WinnerBottomHorizontal()

# tictac.resetBoard()
# testDraw()