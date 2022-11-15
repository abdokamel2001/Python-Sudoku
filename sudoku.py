from random import sample
  
def printBoard(board):
    if type(board[0][0]) != int: 
        for i in range(len(board)): 
            if board[i] == [[0] * 9 for _ in range(9)]: 
                print("No more solutions\n") 
                return 
            print(f"the solution num {i + 1} :") 
            printBoard(board[i]) 
    else: 
        for y in range(9): 
            if y % 3 == 0: print("-" * 37) 
            for x in range(9): 
                if x % 3 == 0: print("|", end = "  ") 
                if board[y][x] == 0: print(" ", end = "  ") 
                else: print(board[y][x], end = "  ") 
            print("|") 
        print("-" * 37, end = "\n" * 3) 
  
def possible(board, y, x, n):
    for i in range(9): 
        if board[y][i] == n or board[i][x] == n: return False 
    y0 = 3 * (y // 3) 
    x0 = 3 * (x // 3) 
    for i in range(3): 
        for j in range(3): 
            if board[i + y0][j + x0] == n: return False 
    return True 

def shuffle(max): return sample([i + 1 for i in range(max)], max)

def solve(board, maxSol):
    solutions = [[[0] * 9 for _ in range(9)] for _ in range(maxSol)]
    inputsOrder = [[shuffle(9) for _ in range(9)] for _ in range(9)]
  
    def bruteForce(solNum): 
        for y in range(9): 
            for x in range(9): 
                if board[y][x] == 0: 
                    for n in inputsOrder[y][x]: 
                        if possible(board, y, x, n): 
                            board[y][x] = n 
                            if bruteForce(solNum): 
                                board[y][x] = 0 
                                return True 
                            board[y][x] = 0 
                    return False 
        for n in range(solNum): 
            if solutions[n] == board: return False 
        for y in range(9): 
            for x in range(9): solutions[solNum][y][x] = board[y][x]
        return True 
  
    for i in range(maxSol): 
        if not bruteForce(i): break 
    return solutions 
  
def generate(numOfEmpty):
    if numOfEmpty > 81 : numOfEmpty = 81
    board = solve([[0] * 9 for _ in range(9)], 1)[0] 
    emptyCells = shuffle(81) 
    for i in range(numOfEmpty): 
        board[(emptyCells[i] - 1) // 9][(emptyCells[i] - 1) % 9] = 0
    return board 
  
puzzle = generate(int(input("Number of empty cells: ")))
printBoard(puzzle)
printBoard(solve(puzzle, int(input("Number of max solutions:"))))
