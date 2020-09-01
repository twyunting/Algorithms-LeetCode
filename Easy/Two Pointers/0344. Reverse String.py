def reverseString(s):
	"""
	:type s: List[str]
	:rtype: None Do not return anything, modify s in-place instead.
	"""

	for i in range(len(s)):
		s.insert(i, s.pop()) # i= index order, s.pop()= element
	return s

s = ["h","e","l","l","o"]
print(reverseString(s))


"""
offical answer

class Solution:
    def reverseString(self, s):
        
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

# Mine

 i, j = 0, len(s) - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
"""