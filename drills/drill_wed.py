from collections import Counter
print(Counter("banana").most_common(2))   # [('a', 3), ('n', 2)]
"""def top_two():
    word = "banana"
    counts = {}
    for i in word:
        counts[i] = counts.get(i,0) + 1
    print(sorted(counts)[:2])

top_two()
"""