N = 8

def solveNQueens(board, col):
    if col == N:
        printBoard(board)
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 'Q'
            if solveNQueens(board, col + 1):
                return True
            board[i][col] = '.'
    return False

def isSafe(board, row, col):
    for x in range(col):
        if board[row][x] == 'Q':
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 'Q':
            return False
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 'Q':
            return False
    return True

def printBoard(board):
    for row in board:
        print(" ".join(row))
    print()

board = [['.' for x in range(N)] for y in range(N)]
if not solveNQueens(board, 0):
    print("No solution found")
