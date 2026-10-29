class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d_strs = {}
        for s in strs:
            s_sort = sorted(s)
            key = "".join(s_sort)
            if key not in d_strs:      
                d_strs[key] = []    
            d_strs[key].append(s)
        return list(d_strs.values())