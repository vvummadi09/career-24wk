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
a, b = {1, 2, 3}, {2, 3, 4}
print(a & b)
print(a | b)
print(a - b)

x, y = 3, 5
x, y = y, x
print(x, y)

print([n * n for n in range(1, 6)])
print({w: len(w) for w in ["okta", "scim", "oauth"]})
