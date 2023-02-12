"""
Time complexity => O(slogs+tlogt)
Space complexity => O(1)

To reduce space complexity, we can sue sorting.
Sorting is inplace so we do not need additional space.
"""


def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
