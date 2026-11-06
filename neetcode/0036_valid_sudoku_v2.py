
"""
36. Valid Sudoku — re-solve from blank (v2)

Problem: Given a 9x9 Sudoku board, check if it is valid.
Each number should appear only once in each row, column,
and 3x3 box. Ignore empty cells.

Approach: Use three dictionaries with sets to store the numbers
in each row, column, and 3x3 box. Go through every cell and
check if the number is already present in any of them.
If it is, return False. Otherwise, add the number to the sets.
If there are no duplicates, return True.

Time: O(1)  Space: O(1)
"""

from collections import defaultdict

def is_valid_sudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            d = board[r][c]
            if d != '.': 
                if (d in rows[r] or d in cols[c] or d in boxes[r//3,c//3]):
                    return False
                rows[r].add(d)
                cols[c].add(d)
                boxes[r//3,c//3].add(d)
    return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]

bad_col = [row[:] for row in board]
bad_col[0][0] = "8"     # column 0 now has two 8s

bad_box = [row[:] for row in board]
bad_box[0][2] = "9"     # box (0,0) now has two 9s

print(is_valid_sudoku(board))    # True
print(is_valid_sudoku(bad_col))  # False
print(is_valid_sudoku(bad_box))  # False
