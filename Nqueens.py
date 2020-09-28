''' N-1 queens on N*N board '''

N = int(input().strip())


def printChess(board): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 

def safe(board, row, col): 
  
    for i in range(col): 
        if board[row][i] == 1: 
            return False
  
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    for i, j in zip(range(row, N, 1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True


def solveQueens(board,col):
    if col >= N:
        return True
    
    for i in range(N):
        if safe(board,i,col):
            board[i][col]=1
            if solveQueens(board,col+1)==True:
                return True
            board[i][col]=0
    return False


def solve(n):
    board = [[0]*n]*n
    solveQueens(board,0)
    printChess(board)


solve(N)
