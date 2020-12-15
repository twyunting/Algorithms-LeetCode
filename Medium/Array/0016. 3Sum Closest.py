def threeSumClosest(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	tmp = []
	positive = []
	for i in nums:
		tmp.append(abs(i - target))
	return tmp
	





print(threeSumClosest(nums = [-1,2,1,-4], target = 1))