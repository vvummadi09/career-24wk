class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        countt = {}
        for ch in t:
            countt[ch] = countt.get(ch, 0) + 1
        return counts == countt
# Alternative: return sorted(s) == sorted(t)   # O(n log n)

print(Solution().isAnagram("anagram", "nagaram"))   # expect True
print(Solution().isAnagram("rat", "car"))           # expect False  