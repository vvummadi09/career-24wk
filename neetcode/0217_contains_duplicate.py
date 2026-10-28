class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

print(Solution().hasDuplicate([1, 2, 3, 1]))   # expect True
print(Solution().hasDuplicate([1, 2, 3, 4]))   # expect False