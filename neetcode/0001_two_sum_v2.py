class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Returns the indices of two numbers that add up to the target.

        Go through the list and check what number is needed
        to reach the target.
        If that number is already in seen, return both indices.
        Otherwise, store the current number and its index.

        Time: O(n) - we go through the list once.
        Space: O(n) - we use a dictionary to store numbers and indices.
        """
        seen = {}
        for i,n in enumerate(nums):
            new_target = target - n
            if new_target in seen:
                return[seen[new_target], i]
            seen[n] = i

print(Solution().twoSum([3, 2, 4], 6))   # expect [1, 2]
print(Solution().twoSum([2,7,11,15], 9))  # expect [0, 1]
print(Solution().twoSum([3, 3], 6))      # expect [0, 1]    
