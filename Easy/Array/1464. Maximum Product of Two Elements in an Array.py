class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        sortNums = sorted(nums)
        return (sortNums[-1]-1) * (sortNums[-2]-1)
        
# Second

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        res = 0
        
        for i in range(len(nums)-1):
            res = max((nums[i]-1)*(nums[i+1]-1),res)
        return res
        
# Third

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
	    maxx=0
	    smax=0
	    for i in nums:
		    if i > maxx:
			    smax=maxx
			    maxx=i
		    elif i > smax:
			    smax=i
	    return (maxx-1)*(smax-1)
      
      
