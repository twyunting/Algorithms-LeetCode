class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currentsum = maxsum = nums[0]
        
        for i in range(1, len(nums)):
            currentsum = max(nums[i], currentsum + nums[i])
            maxsum = max(maxsum, currentsum)
            
        return maxsum
