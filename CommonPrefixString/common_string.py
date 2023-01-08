import itertools

strs = ["flower","flow","flight"]

def longestCommonPrefix(strs: list) -> str:
	combinations = []
	len_dict = {}
	
	shortest_string = sorted(strs, key=len)[0]
	
	for i in range(0, len(shortest_string)+1):
		com_set = itertools.combinations(shortest_string, i)
		for ele in com_set:
			combinations.append(ele)
		
	combinations = combinations[1:]

	for ele in combinations:
		str_ele = "".join(ele)
		length = 0

		flag = all(str_ele in _str for _str in strs)
		if flag == True:
			len_dict[str_ele] = len(str_ele)

	if len(len_dict) > 0:
	    return max(len_dict, key=len_dict.get)
	else:
		return ""


_dict = longestCommonPrefix(strs)
print(_dict)


# sorted(strs, key=len)[0]  ->  sort list elements by length
# com_set = itertools.combinations(shortest_string, i)  ->  find combinations
# str_ele = "".join(ele)  ->  join tuple elements into one string
# flag = all(str_ele in _str for _str in strs)  ->  check a condition on all elements
# max(len_dict, key=len_dict.get)  ->  return key with max value