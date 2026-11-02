from collections import defaultdict

def dict_mon_drill():
    """
    This drill is to help you practice using dictionaries in Python.
    """
    ages = {'Var': 17, 'Sow': 21, 'chintu': 30}

    return ages


def age_loop():
    """
    This drill is to help you practice using dictionaries in Python.
    """
    ages = dict_mon_drill()
    for name, age in ages.items():
        print(f"{name} is {age}")
    for name, age in ages.items():
        if age > 20:
            print(f"{name}")

def dict_fruits():
    """
    This drill is to help you practice using dictionaries in Python.
    """
    words = ["apple", "avocado", "banana", "blueberry", "cherry"]

    fruits_by_alp = {}
    for name in words:
        if fruits_by_alp.get(name[0],0) == 0:
           fruits_by_alp[name[0]] = []
        fruits_by_alp[(name[0])].append(name)
    print(fruits_by_alp)

def group_setdefault():
    words = ["apple", "avocado", "banana", "blueberry", "cherry"]
    groups = {}
    for name in words:
        groups.setdefault(name[0],[]).append(name)
    print(groups)

def group_defaultdict():
    words = ["apple", "avocado", "banana", "blueberry", "cherry"]
    groups = defaultdict(list)
    for name in words:
        groups[name[0]].append(name)
    print(dict(groups))  

dict_fruits()
group_setdefault()
group_defaultdict()