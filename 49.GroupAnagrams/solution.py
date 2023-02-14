# Basic solution
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:

    res = defaultdict(list)  # mapping char_count to list of anagrams

    for s in strs:
        # count will be same for anagrams
        # 0 and 1 on exact indexes
        count = [0] * 26  # a-z

        for c in s:
            # suppose a = 80, then 80 - 80 = 0
            # z will be 25 then
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)  # tuple because dict cannot be used as keys
    return res.values()


test_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(test_arr))
