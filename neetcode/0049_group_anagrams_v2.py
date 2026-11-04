"""
49. Group Anagrams (Medium) — NeetCode 150, Arrays & Hashing

Problem: (your words, 1–2 lines)

Approach: (fill in after it works)

Time: O(?)  Space: O(?)
Hints: (none / yes — what)
"""
from collections import defaultdict


def groupAnagrams(strs) -> List[List[str]]:
    d_strs = {}
    for s in strs:
        s_sort = sorted(s)
        key = "".join(s_sort)
        if key not in d_strs:      
            d_strs[key] = []    
        d_strs[key].append(s)
    return list(d_strs.values())




    


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# expect: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]  (any order)

print(group_anagrams([""]))
# expect: [['']]

print(group_anagrams(["a"]))
# expect: [['a']]