"""
Time complexity => O(s+t)
Space complexity => O(s+t)
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    count_s = Counter(s)
    count_t = Counter(t)
    print(count_s == count_t)


s = "hello"
t = "hello"

is_anagram(s, t)
