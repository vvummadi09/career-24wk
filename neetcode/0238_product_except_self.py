def product_except_self(nums):
    """
    Returns a list where each position has the product of all
    numbers except the number at that position.

    First, calculate the product of numbers to the left.
    Then, calculate the product of numbers to the right.
    Finally, multiply both to get the answer.

    Time: O(n) - we go through the list 3 times.
    Space: O(n) - we use left, right, and ans lists.
    """
    n = len(nums)
    left = [1] * n
    right = [1] * n
    ans = [1] * n
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]

    # loop 1: fill left, going forward (start at i = 1)
    # loop 2: fill right, going backward (start at i = n-2)
    for i in range(0,n):
        ans[i] = left[i] * right[i]
    return ans

print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))