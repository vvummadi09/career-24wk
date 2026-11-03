def print_reverse():
    s = "identity"
    rev = s[::-1]
    d = s[1:4:1]
    print(s)
    print(f"Reverse: {rev}")
    print(f"3 chars:{d}")

def split(s):
    back = s.split(" | ")     # string.split(separator)
    return back

def enu():
    words = ["okta ", "scim ", "oauth "]
    return "".join(f"{i} {k}"for i, k in enumerate(words)) 

def sort_by_len():
    words = ["okta", "scim", "ad", "oauth"]
    return sorted(words,key=len)

def join():
    words = ["okta", "scim", "ad", "oauth"]
    joined = " | ".join(words)     # separator.join(list)
    return joined



        
print(sort_by_len())
print(split(join()))
