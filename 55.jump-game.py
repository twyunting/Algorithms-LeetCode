#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPosition = len(nums)-1
        for i in range(len(nums)-1, -1, -1): # backtracking
            if i + nums[i] >= lastPosition:
                lastPosition = i
        return lastPosition == 0 # make sure end with first index
    
        
# @lc code=end

