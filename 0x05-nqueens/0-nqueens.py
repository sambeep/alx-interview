#!/usr/bin/python3
import sys

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

solutions = []
board = [-1] * n
row = 0

# Stack-based approach for backtracking
stack = [(0, 0)]  # (row, col) pairs to place queens

while stack:
    row, col = stack.pop()

    # Backtracking: if we have tried all columns in a row, reset it
    if col >= n:
        board[row - 1] = -1
        continue

    # Place the queen at (row, col)
    safe = True
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            safe = False
            break

    # If safe, set queen and go to the next row
    if safe:
        board[row] = col
        if row == n - 1:
            # Solution found
            solutions.append([[i, board[i]] for i in range(n)])
            board[row] = -1
        else:
            # Move to the next row, start from column 0
            stack.append((row, col + 1))
            stack.append((row + 1, 0))
    else:
        # If not safe, try the next column in the current row
        stack.append((row, col + 1))

for solution in solutions:
    print(solution)
