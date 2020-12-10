def longestPalindrome(height):
	"""
	:type s: str
	:rtype: str
	"""
	a_pointer, b_pointer = 0, len(height)-1
	maxArea = 0
	while a_pointer < b_pointer:
		if height[a_pointer] < height[b_pointer]:
			maxArea = max(maxArea, height[a_pointer] * (b_pointer - a_pointer))
			a_pointer += 1
		else:
			maxArea = max(maxArea, height[b_pointer] * (b_pointer - a_pointer))
			b_pointer -= 1
	return maxArea
print(longestPalindrome([1,8,6,2,5,4,8,3,7]))