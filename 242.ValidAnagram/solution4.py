"""
Time complexity => O(s+t)
Space complexity => O(s+t)

Optimizing solution 3. Instead of two hashmaps, we can use one because
count_s[c] == count_t[c] is same as count_s[c] - count_t[c] = 0
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for i in range(len(s)):
        count[s[i]] = 1 + count.get(s[i], 0)
        count[t[i]] = count.get(t[i], 0) - 1
    for c in count:
        if count[c] != 0:
            return False
    return True


s = "hello"
t = "hello"

print(isAnagram(s, t))
