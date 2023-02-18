def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}  # count occurences
    freq = [[] for i in range(len(nums) + 1)]  # buket sort array

    for n in nums:
        count[n] = 1 + count.get(n, 0)  # use get to return default value
    for n, c in count.items():
        freq[c].append(n)  # append value to count(index) list

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:  # because every item of freq is a sublist
            res.append(n)
            if len(res) == k:
                return res


# return inside the loop is guaranteed to run
# we don;t have to put outside the loop

nums = [1, 1, 1, 2, 2, 3]
res = topKFrequent(nums, k=2)
print(res)
