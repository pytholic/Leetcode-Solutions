import itertools

strs = ["flower","flow","flight"]

def longestCommonPrefix(self, strs: List[str]) -> str:
    combinations = []
    len_dict = {}
    
    shortest_string = sorted(strs, key=len)[0]
    
    for i in range(0, len(shortest_string)+1):
        cmb = shortest_string[0:i]
        combinations.append(cmb)

    combinations = combinations[1:]

    for ele in combinations:
        length = 0
        flag = all(ele in _str[0:len(ele)] for _str in strs)
        if flag == True:
            len_dict[ele] = len(ele)
        else:
            break

    if len(len_dict) > 0:
        return max(len_dict, key=len_dict.get)
    else:
        return ""

#longestCommonPrefix(strs)

_dict = longestCommonPrefix(strs)
print(_dict)


# sorted(strs, key=len)[0]  ->  sort list elements by length
# com_set = itertools.combinations(shortest_string, i)  ->  find combinations
# str_ele = "".join(ele)  ->  join tuple elements into one string
# flag = all(str_ele in _str for _str in strs)  ->  check a condition on all elements
# max(len_dict, key=len_dict.get)  ->  return key with max value