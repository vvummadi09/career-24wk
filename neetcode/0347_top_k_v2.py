"""
347. Top K Frequent Elements — re-solve with bucket sort
Time: O(n)  Space: O(n)
Hints: (none / yes)
"""
from collections import Counter


def top_k_frequent(nums, k):
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]   # index = frequency
    for num, freq in counts.items():
        buckets[freq].append(num)
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)

            if len(result) == k:
                return result

    return result


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))           # [1, 2]
print(top_k_frequent([1], 1))                          # [1]
print(top_k_frequent([4, 4, 4, 5, 5, 6, 6, 6, 6], 1))  # [6]