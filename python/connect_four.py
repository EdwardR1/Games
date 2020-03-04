SPACE = '-'
MARKER1 = "x"
MARKER2 = "o"
board = []
rows = []


def initializeBoard(n):
    global board
    for i in range(n):
        board.append([])
        for _ in range(n):
            board[i].append(SPACE)


def initializeRows():
    global rows
    for _ in range(len(board)):
        rows.append(len(board) - 1)


def getRowVal(col):
    return rows[col]


def columnAvailable(col):
    return getRowVal(col) != -1


def place(col, marker):
    global board, rows
    if(columnAvailable(col)):
        row = getRowVal(col)
        board[row][col] = marker
        rows[col] -= 1
        return True
    else:
        print("Column full!")
        return False


def printBoard():
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()


def checkVertical(marker):
    for i in range(len(board) - 1, 2, -1):
        for j in range(len(board)):
            if(board[i][j] == marker and board[i - 1][j] == marker and board[i - 2][j] == marker and board[i - 3][j] == marker):
                return True
    return False


def checkHorizontal(marker):
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board) - 3):
            if(board[i][j] == marker and board[i][j + 1] == marker and board[i][j + 2] == marker and board[i][j + 3] == marker):
                return True
    return False


def checkDiagonal(marker):
    for i in range(len(board) - 3):
        for j in range(len(board) - 1, 2, -1):
            if(board[i][j] == marker and board[i + 1][j - 1] == marker and board[i + 2][j - 2] == marker and board[i + 3][j - 3] == marker):
                return True
    for i in range(len(board) - 1, 2, -1):
        for j in range(len(board) - 1, 2, -1):
            if(board[i][j] == marker and board[i - 1][j - 1] == marker and board[i - 2][j - 2] == marker and board[i - 3][j - 3] == marker):
                return True
    return False


def hasEmptySpaces():
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == SPACE):
                return True
    return False


def canStillPlay():
    return hasEmptySpaces() and (not checkDiagonal(MARKER1) and not checkDiagonal(MARKER2)) and (not checkHorizontal(MARKER1) and not checkHorizontal(MARKER2)) and (not checkVertical(MARKER1) and not checkVertical(MARKER2))


def getWinner():
    if(not hasEmptySpaces()):
        return "Tie!"
    elif(checkDiagonal(MARKER1)):
        return "Player 1 won Diagonally!"
    elif(checkDiagonal(MARKER2)):
        return "Player 2 won Diagonally!"
    elif(checkHorizontal(MARKER1)):
        return "Player 1 won Horizontally!"
    elif(checkHorizontal(MARKER2)):
        return "Player 2 won Horizontally!"
    elif(checkVertical(MARKER1)):
        return "Player 1 won Vertically!"
    elif(checkVertical(MARKER2)):
        return "Player 2 won Vertically!"
    else:
        return "No winners!"


def getSizeOfBoard():
    try:
        size = int(input("Please input the size of the board: "))
        if(size < 4):
            raise ValueError
        return size
    except ValueError:
        print("Invalid input!")
        return getSizeOfBoard()


def getPlacement():
    try:
        col = int(input("Please input a column: "))
        if(col < 0 or col > len(board) - 1):
            raise ValueError
        return col
    except ValueError:
        print("Invalid column input!")
        return getPlacement()


def setup():
    initializeBoard(getSizeOfBoard())
    initializeRows()


def run():
    setup()
    while(canStillPlay()):
        print("Player 1:")
        player1 = getPlacement()
        place(player1, MARKER1)
        printBoard()
        if(not canStillPlay()):
            break
        print("Player 2:")
        player2 = getPlacement()
        place(player2, MARKER2)
        printBoard()
    print(getWinner())


run()
