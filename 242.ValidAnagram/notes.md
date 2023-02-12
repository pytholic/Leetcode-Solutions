# 242.Valid Anagram

I can count number of occurrences in both

# Python

## Solution 1

```python
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
```

## Solution 2

Same as 1, but from scratch

```python
"""
Time complexity => O(s+t)
Space complexity => O(s+t)
"""

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False
    return True

s = "hello"
t = "helloo"

print(isAnagram(s, t))
```

## Solution 3

To reduce space complexity, we can use sorting

Sorting is inplakce so we do not need additional space.

```python
"""
Time complexity => O(slogs+tlogt)
Space complexity => O(1)
"""

def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

## Solution 4

- Optimizing solution 3.
    - Instead of two hashmaps, we can use one
    
    ```
    count_s[c] == count_t[c] is same as count_s[c] - count_t[c] = 0
    ```
    

---

# JavaScript

## Solution 1

```jsx
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

function isAnagram(s, t) {
  if (s.length !== t.length) return false;

  const count = {};

  for (let i = 0; i < s.length; i++) {
    if (!count[s[i]]) count[s[i]] = 0;
    if (!count[t[i]]) count[t[i]] = 0;
    count[s[i]]++;
    count[t[i]]--;
  };
  for (let c in count) {
      if (count[c] !== 0) return false;
    }
    return true;
}
```