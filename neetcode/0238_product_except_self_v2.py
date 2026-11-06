"""
238. Product of Array Except Self — re-solve from blank (v2)

Problem: Given a list of numbers, return a new list where each position contains the product of all the other numbers except the number at that position.
Approach: First we will calculate the product of numbers to the left.
    Then we will calculate the product of numbers to the right.
    after that multiply both to get the answer.
Time: O(n)  Space: O(n)
Hints: none
"""


def product_except_self(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    ans =[1] * n
    for i in range(1,n):
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
    for i in range(0,n):
        ans[i] = left[i] * right[i]
    return ans
 



print(product_except_self([1, 2, 3, 4]))       # [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]