
"""
128. Longest Consecutive Sequence — re-solve from blank (v2)

Problem: Given a list of numbers, find the longest sequence
of consecutive numbers and return its length.
The numbers don't need to be in order.

Approach: COnvert to set to remove duplicates and check for each number if previous number exists and go on untill 
previosu num is abset and count numbers in large and reset large , compare against best and return best.

First convert the list into a set to remove duplicates.
Go through each number and check if the previous number exists
in the set. Keep counting backwards until there is no previous
number. Update the longest count and reset the counter for the
next number.

Time: O(n²) worst case  Space: O(n)
Hints: none
"""


def longest_consecutive(nums):
    num_set = set(nums)
    best,large = 0,1
    for i in num_set:
            if i - 1 not in num_set:          # x is a START
                large = 1
                while i + large in num_set:
                    large += 1
                best = max(best,large)
    return best



print(longest_consecutive([100, 4, 200, 1, 3, 2]))          # 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print(longest_consecutive([]))                              # 0
