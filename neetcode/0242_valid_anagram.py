class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for n in s:
            counts[n] = counts.get(n, 0) + 1
        countt = {}
        for m in t:
            countt[m] = countt.get(m, 0) + 1
        return counts == countt
# Alternative: return sorted(s) == sorted(t)   # O(n log n)

print(Solution().isAnagram("anagram", "nagaram"))   # expect True
print(Solution().isAnagram("rat", "car"))           # expect False  