def longestCommonPrefix(strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	res = ""
	if not strs:
		return ""

	for i in zip(*strs):
		if len(set(i)) == 1:
			res += i[0]
		else:
			return res
	return res

print(longestCommonPrefix(["flower","flow","flight"]))
