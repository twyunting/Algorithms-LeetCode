def longestCommonPrefix(strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	res = ""
	if not strs:
		return ""

	return zip(*strs)

print(longestCommonPrefix(["flower","flow","flight"]))
