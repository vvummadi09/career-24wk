# Python Recall Log
Things I couldn't recall from memory. Re-test these in future drills.

## Mon Nov 2 — dicts
- d.get(k) → None if missing; d.get(k, 0) → 0
- d.items() → for k, v in d.items()
- d.setdefault(k, []).append(x)
- from collections import defaultdict; d = defaultdict(list); d[k].append(x)
- `if d.get(k)` fails when the value is 0 / "" / [] → use `if k in d`
- Use a set when you only need "seen it?" (no values): seen = set(); seen.add(x)
- Sequential loops = ADD complexity (O(n)+O(n) = O(n)); nested loops = MULTIPLY (O(n²))
- a, b = x, y → sets both at once (tuple unpacking)
- Chained .get(): default must be {} not 0 → links.get("next", {}).get("url")
- One venv per project: cd into project, `source .venv/bin/activate`; `deactivate` to leave
- ALWAYS call the function + run before saying done

## Tue Nov 3 — lists + strings
- s[::-1] → reversed string (blank start/stop = whole string, step -1 = backwards)
- s[1:4] → chars at index 1,2,3 (stop is NOT included; step 1 is default)
- " | ".join(words) → separator goes BEFORE .join
- s.split(" | ") → back to a list
- for i, w in enumerate(words): print(i, w) → index + value together
- sorted(words, key=len) → pass the function, don't call it (not key=len(x))
- `for x in nums` = values; `for i in range(n)` = indexes
- range(start, stop, step): stop NOT included; range(n-2, -1, -1) counts down to 0
- No `return` → function gives back None
- list → .append(x) adds ONE item; .extend(list) adds EACH item; dict → .update()
- f"{len(x)}#{x}" — f-string inside a generator (271)
- Check for a built-in before writing a loop
- Never change the input data to make the output look right
- Never name things str / list / dict / sort / sum (built-in names)
- No output → save, call the function, print. Check those 3 first.
- Cmd+S before git add; check "files changed" + insertion count after commit
- git status before every git add — read the list

## Wed Nov 4 — Counter, sets, tuples, comprehensions
- from collections import Counter; Counter("banana").most_common(2) → [('a', 3), ('n', 2)]
- sorted(dict) sorts KEYS only; by value → sorted(d, key=d.get, reverse=True)
- a & b = in both · a | b = in either · a - b = only in a
- x, y = y, x → swap in one line
- [n * n for n in range(1, 6)] → list comprehension: [EXPR for ITEM in ITERABLE]
- {w: len(w) for w in words} → dict comprehension
- {} = empty DICT; set() = empty set; colons = dict
- d[k] = v → store v under key k (overwrites if k exists); d[k] reads it (KeyError if missing)