from random import sample

def printBoard(board):
    if type(board[0][0]) != int:
        for i in range(len(board)):
            if board[i] == [[0] * 9 for _ in range(9)]: break
            print(f"the solution num {i + 1} :\n")
            printBoard(board[i])
    else:
        for y in range(9):
            if y % 3 == 0 and y != 0: print("-" * 32)
            for x in range(9):
                if x % 3 == 0 and x != 0: print("|", end="  ")
                print(board[y][x], end="  ")
            print()
        print("\n")

def possible(board, y, x, n):
    for i in range(9):
        if board[y][i] == n or board[i][x] == n:
            return False
    y0 = (y // 3) * 3
    x0 = (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[i + y0][j + x0] == n:
                return False
    return True

def shuffle(maxNum):
    return sample([i + 1 for i in range(maxNum)], maxNum)

def solve(board, maxSol):
    solutions = [[[0] * 9 for _ in range(9)] for _ in range(maxSol)]
    inputsOrder = [[shuffle(9) for _ in range(9)] for _ in range(9)]
    solNum = [0]
    def bruteForce():
        for y in range(9):
            for x in range(9):
                if board[y][x] == 0:
                    for n in inputsOrder[y][x]:
                        if possible(board, y, x, n):
                            board[y][x] = n
                            if bruteForce():
                                board[y][x] = 0
                                return True
                            board[y][x] = 0
                    return False
        for i in range(solNum[0]):
            if solutions[i] == board: return False
        for y in range(9):
            for x in range(9):
                solutions[solNum[0]][y][x] = board[y][x]
        solNum[0] += 1
        return True
    for _ in range(maxSol):
        if not bruteForce(): return solutions
    return solutions

def generate(numOfEmpty):
    board = solve([[0] * 9 for _ in range(9)], 1)[0]
    emptyCells = shuffle(81)
    for i in range(numOfEmpty):
        board[(emptyCells[i] - 1) // 9][(emptyCells[i] - 1) % 9] = 0
    return board

puzzle = generate(40)          # generate a sudoku puzzle
printBoard(puzzle)             # print the puzzle
printBoard(solve(puzzle, 5))   # print 5 solutions
