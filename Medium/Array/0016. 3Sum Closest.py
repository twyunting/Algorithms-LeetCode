def threeSumClosest(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	nums.sort()
	result = nums[0] + nums[1] + nums[len(nums)-1]

	for i in range(len(nums)-2):
		if i > 0 and nums[i] == nums[i-1]:
			continue
		l = i+1
		r = len(nums)-1

		while l < r:
			val = nums[i] + nums[l] + nums[r]
			if abs(val-target) < abs(result-target):
				result = val
			if val == target:
				return target
			elif val < target:
				l += 1
			else:
				r -= 1
	return result


print(threeSumClosest(nums = [-1,2,1,-4], target = 1))