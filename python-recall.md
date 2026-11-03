# Python Recall Log
Things I couldn't recall from memory. Re-test these in future drills.

## Mon Nov 2 — dicts
- d.get(k) → None if missing; d.get(k, 0) → 0
- d.items() → for k, v in d.items()
- d.setdefault(k, []).append(x)
- from collections import defaultdict; d = defaultdict(list); d[k].append(x)
- ALWAYS call the function + run before saying done

## Tue Nov 3 — lists + strings
- s[::-1] → reversed string (blank start/stop = whole string, step -1 = backwards)
- s[1:4] → chars at index 1,2,3 (stop is NOT included; step 1 is default)
- " | ".join(words) → separator goes BEFORE .join
- s.split(" | ") → back to a list
- for i, w in enumerate(words): print(i, w) → index + value together
- sorted(words, key=len) → pass the function, don't call it (not key=len(x))
- Check for a built-in before writing a loop
- Never change the input data to make the output look right
- Never name things str / list / dict / sort / sum (built-in names)
- No output → save, call the function, print. Check those 3 first.
- Monday leftover: f"{len(x)}#{x}" — f-string inside a generator for 271