
"""
49. Group Anagrams — v3 from memory (defaultdict)
Time: O(n · k log k)  Space: O(n · k)
Hints: first version copied; this one from memory
"""
from collections import defaultdict

def group_anagrams(strs):
       groups = defaultdict(list)
       for s in strs:
           s_sort = sorted(s)
           key = "".join(s_sort)# line 1: make the key (sorted letters → string)  
           groups[key].append(s)
       return list(groups.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))