"""
36. Valid Sudoku (Medium) — NeetCode 150, Arrays & Hashing

Time: O(?)  Space: O(?)
Hints: yes (box formula, dict of sets)
"""
from collections import defaultdict


def is_valid_sudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            d = board[r][c]
            if d != '.':    # 1. if d is "." → skip to the next cell (which keyword?)
                if d in rows[r] or d in cols[c] or d in boxes[r//3,c//3]:
                    return False # 2. if d is already in rows[r] OR cols[c] OR boxes[(r//3, c//3)] → return False
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
    [".",".",".",".","8",".",".","7","9"]
    ]

bad = [row[:] for row in board]
bad[0][0] = "8"   # column 0 now has two 8s
bad_box = [row[:] for row in board]
bad_box[0][2] = "9"   # box (0,0) already has a 9 at (2,1); row 0 and col 2 have no 9
print(is_valid_sudoku(bad_box))   # should be False

print(is_valid_sudoku(board))  # True
print(is_valid_sudoku(bad))    # False