def validPalindrome(s):
	"""
	:type s: str
	:rtype: bool
	"""
	i, j = 0, len(s)-1

	while i < j:
		if s[i] != s[j]:
			one = s[i:j]
			two = s[i+1:j+1]
			return one == one[::-1] or two == two[::-1]
		i += 1
		j -= 1
	return True








print(validPalindrome("abca")) # need return True