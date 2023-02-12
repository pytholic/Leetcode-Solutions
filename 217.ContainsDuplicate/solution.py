def contains_duplicate(nums: list[int]) -> bool:
    nums_set = set(nums)
    if len(nums) != len(nums_set):
        return True
    else:
        return False


numbers = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
result = contains_duplicate(numbers)
print(result)
