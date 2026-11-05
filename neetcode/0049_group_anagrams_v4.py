"""
49. Group Anagrams — re-solve from blank (v4)
Time: O(n · k log k)  Space: O(n · k)
Hints: none
"""


def group_anagrams(strs):
    grp_ana = {}
    for s in strs:
        s_sort = sorted(s)
        key = "".join(s_sort)
        if key not in grp_ana:
            grp_ana[key] = []
        grp_ana[key].append(s)
    return(list(grp_ana.values()))



print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))