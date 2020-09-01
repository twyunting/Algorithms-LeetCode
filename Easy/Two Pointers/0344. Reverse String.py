def reverseString(s):
	"""
	:type s: List[str]
	:rtype: None Do not return anything, modify s in-place instead.
	"""

	res = []
	for i in s:
		res.append(s.pop())
	return res

s = [1,2,3,4,5]
print(reverseString(s))


