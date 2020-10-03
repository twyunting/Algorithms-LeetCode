def firstUniqChar(s):
	"""
	:type s: str
	:rtype: int
	"""
	from collections import Counter
	countS = Counter(s)

	for i, j in enumerate(s):
		if countS[j] == 1:
			return i
	return -1

print(firstUniqChar(s = "loveleetcode"))