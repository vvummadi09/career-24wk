def encode(strs: list[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strs)

# 5#hello5#world
# 3#a,b1#c
# 0#0#
# 5#5#abc1##

def decode(s):
    res, i = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j+1 : j+1+length])
        i = j + 1 + length
    return res



for x in [["hello","world"], ["a,b","c"], ["", ""], ["5#abc","#"], []]:
    print(decode(encode(x)) == x)
