class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums = sorted(set(nums))
        
        if len(nums) < 3:
            return max(nums)
        else:
            return nums[-3]
        
