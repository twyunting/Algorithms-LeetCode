def reverseString(s):
	"""
	:type s: List[str]
	:rtype: None Do not return anything, modify s in-place instead.
	"""

	for i in range(len(s)):
		s.insert(i, s.pop())
	return s

s = ["h","e","l","l","o"]
print(reverseString(s))


