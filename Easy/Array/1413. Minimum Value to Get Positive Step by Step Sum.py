class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
            
        if min(nums) <= 0:
            return -min(nums) + 1
        else:
            return 1
            
            
# Second

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        prefixSum = 0
        minSunValue = 1
        
        for i in nums:
            prefixSum += i
            minSunValue = max(minSunValue, 1-prefixSum)
        
        return minSunValue
    
    
    
