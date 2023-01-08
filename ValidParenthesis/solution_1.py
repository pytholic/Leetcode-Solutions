string = "[](){}"

def is_valid(s: str) -> bool:
	for i in range(len(s)):
		if i+1 < len(s):
			flag = False
			if s[i] == "(" and s[i+1] != ")":
				flag = False
				break
			elif s[i] == "(" and s[i+1] == ")":
				flag = True
			elif s[i] == "[" and s[i+1] != "]":
				flag = False
				break
			elif s[i] == "[" and s[i+1] == "]":
				flag = True
			elif s[i] == "{" and s[i+1] != "}":
				flag = False
				break
			elif s[i] == "{" and s[i+1] == "}":
				flag = True

	return flag


flag = is_valid(string)
print(flag)