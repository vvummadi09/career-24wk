class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}                          # value → index
        for i, n in enumerate(nums):       # i = position, n = value
            need = target - n              # the partner I'm looking for
            if need in seen:               # O(1) lookup
                return [seen[need], i]     # partner's index, my index
            seen[n] = i          

print(Solution().twoSum([3, 2, 4], 6))   # expect [1, 2]
print(Solution().twoSum([3, 3], 6))      # expect [0, 1]       