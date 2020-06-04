class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        maxnumber = max(nums) # 取最大值
        i = nums.index(maxnumber) # 最大值位置 為i
        nums[i] = 0 # 把最大值設為 0
        
        if maxnumber >= 2 * max(nums): # 現在array裡 max(nums)為第二大的值
            return i 
        else:
            return -1
