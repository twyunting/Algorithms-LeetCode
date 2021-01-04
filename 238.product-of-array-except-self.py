#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = [1] * len(nums)
        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]
        print(L)
        R = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
        
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = L[i] * R[i]
        return ans
        
        
# @lc code=end

