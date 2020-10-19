def rotatedDigits(N):
	"""
	:type N: int
	:rtype: int
	"""
	count = 0
	for i in range(1, N+1): # ex: input = 10 so input 1~10
		nums = str(i)
		if "3" in nums or "4" in  nums or "7" in nums:
			continue
		if "2" in nums or "5" in nums or "6" in nums or "9" in nums:
			count += 1

	return count

print(rotatedDigits())