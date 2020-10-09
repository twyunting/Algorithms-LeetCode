def repeatedSubstringPattern(s):
	"""
	:type s: str
	:rtype: bool
	"""
	return s in (s + s)[1:-1]




print(repeatedSubstringPattern("abcabc"))


# It's quite evident that if the new string contains the input string, the input string is a repeated pattern string.
