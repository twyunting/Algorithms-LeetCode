def isValid(s):
	"""
	:type s: str
	:rtype: bool
	"""
	d = {"(":")", "{":"}", "[":"]"}
	res = []

	for i in s:
		if i in d:
			res.append(d[i]) # save the values in dict
		elif res:
			stack = res.pop() 
			if i != stack:
				return False
		else:
			return False

	if len(res) != 0:
		return False
	return True


print(isValid("()[]{}"))
