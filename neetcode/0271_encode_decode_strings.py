def encode(strs):
    return "".join(f"{len(x)}#{x}" for x in strs)

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