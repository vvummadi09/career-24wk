"""Thu Nov 5 drill — functions, *args, **kwargs, try/except, with open."""


def greet(name, greeting="Hi"):
    # print greeting + space + name
    print(greeting + " " + name)


def total(*nums):
    # return the sum of all nums (hint: what type is `nums` inside here?)
    return sum(nums)


def show(**info):
    # print each "key = value" on its own line (hint: what type is `info`?)
    for i in info.items():
        print (f"{i[0]} = {i[1]}")


def safe_int():
    # try: convert "abc" with int() and print it
    # except ValueError: print "bad number"
    try:
        print(int("abc"))
    except ValueError:
        print("bad number")
    # Code to run if a ValueError occurs
    


def file_roundtrip():
    # with open("drill.txt", "w") as f: write "hello"
    # with open("drill.txt") as f: read it and print it
    with open("drill.txt","w") as f:
        f.write("hello")
    with open("drill.txt","r") as o:
        print(o.read())


greet("Ava")
greet("Ava", "Hello")
print(total(1, 2, 3))
show(user="ava", role="admin")
safe_int()
file_roundtrip()