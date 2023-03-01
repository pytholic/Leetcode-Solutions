def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0

    for n in nums:
        # check if it is the start of a sequence
        if (n - 1) not in num_set:
            length = 0
            # length increases by 1, so we keep chekcing consecutive items
            while (n + length) in num_set:
                length += 1
            longest = max(length, longest)
    return longest


nums = [100, 4, 200, 1, 3, 2]
res = longestConsecutive(nums)
print(res)
