#!/usr/bin/python3
import sys

def print_solution(board, n):
    """Print a solution in the required format"""
    solution = []
    for row in range(n):
        solution.append([row, board[row]])
    print(solution)

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row, board):
    """Solve the N Queens problem using backtracking"""
    if row == n:
        print_solution(board, n)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [-1] * n
    solve_nqueens(n, 0, board)

if __name__ == "__main__":
    main()
