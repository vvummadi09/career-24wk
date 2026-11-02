from collections import Counter
def is_anagram_dict(s, t): # time O(s+t) space O(s+t)
    if len(s) != len(t):
        return False
    counts = {}
    for p in s:
        counts[p] = counts.get(p,0) + 1
    countt = {}
    for p in t:
        countt[p] = countt.get(p,0) + 1
    return counts == countt

def is_anagram_sort(s, t): #time O((s+t)log (s+t)) space O(n)
    return sorted(s) == sorted(t)

def is_anagram_counter(s, t):  # time O(s+t), space O(s+t)
    return Counter(s) == Counter(t)




tests = [("anagram", "nagaram"), ("rat", "car"), ("ab", "a"), ("", "")]
for s, t in tests:
    print(is_anagram_counter(s, t), is_anagram_dict(s, t), is_anagram_sort(s,t))