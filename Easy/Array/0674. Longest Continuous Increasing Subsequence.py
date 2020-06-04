class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        count = 1
        result = 1
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
                result = max(count, result)
            else:
                count = 1
        
        return result
