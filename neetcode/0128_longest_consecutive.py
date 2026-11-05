"""
128. Longest Consecutive Sequence (Medium) — NeetCode 150, Arrays & Hashing

Problem: (your words)
Approach: (after it works)
Time: O(?)  Space: O(?)
Hints: (none / yes — what)
"""


def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for x in num_set:                     # loop the set: duplicates gone
        if x - 1 not in num_set:          # x is a START
            length = 1
            while x + length in num_set:  # walk forward: x+1, x+2, ...
                length += 1
            best = max(best, length)
    return best
        


print(longest_consecutive([100, 4, 200, 1, 3, 2]))         # 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # 9
print(longest_consecutive([]))                             # 0