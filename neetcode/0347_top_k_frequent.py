class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_dict = {}
        for n in nums:
            k_dict[n] = k_dict.get(n,0) + 1s
        top = sorted(k_dict, key=k_dict.get, reverse=True)
        return top[:k]