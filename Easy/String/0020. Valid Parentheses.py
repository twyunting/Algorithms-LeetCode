def isValid(s):
	"""
	:type s: str
	:rtype: bool
	"""
	d = {"(":")", "{":"}", "[":"]"}
	res = ""

	for i, j in d.items():
		if i != j:
			return False
	return True

print()
