"""Fri Nov 6 drill — Counter, sets, swap, comprehensions (Wed redo)."""
from collections import Counter


def drill():
    s = "banana"
    counts = Counter(s)
    print(counts.most_common(2))


    a = {1, 2, 3}
    b = {2, 3, 4}
    print(a & b)
    print(a | b)
    print(a - b)

    # 3. Swap: x, y = 3, 5 → swap in one line → print x, y
    x, y = 3, 5
    y,x = x,y
    print (x,y)

    # 4. List comprehension: squares of 1–5
    print([i*i for i in range(1,6)])
        

    # 5. Dict comprehension: {word: len(word)} for ["okta", "scim", "oauth"]
    words = ["okta", "scim", "oauth"]
    print({w: len(w) for w in words})
    


drill()