# Objective
Group the anagrams together.
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

# Approach

## Basic approach
* We sort strings and compare

### Time complexity
```
Average string size = n
Total number of strings = m
Sorting complexity = nlogn
Total = m.(nlogn)
```

## Hashmap approach
* Count the occurences in each string
* String with same occurences -> group them together in values of hashmap -> `key: ["eat", "tea", "ate]`
* `key` will be character count
  

### Time complexity
```
O(m.n.26) => O(m.n) # 26 because a-z are 26 characters
m => total strings
n => average length of strings 
```