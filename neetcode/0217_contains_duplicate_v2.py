def contains_duplicate(nums):
    seen = set()
    for val in nums:
        if val in seen:
            return True
        seen.add(val)
    return False


  


print(contains_duplicate([1,2,3,1]))  # True
print(contains_duplicate([1,2,3,4]))  # False
print(contains_duplicate([]))         # False
print(contains_duplicate([0, 0]))  # should be True