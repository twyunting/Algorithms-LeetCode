#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) <= 1:
            return [nums]

        for idx, num in enumerate(nums):
            n = nums[:idx] + nums[idx+1: ]
            for y in self.permute(n):
                result.append([num] + y)
        return result 
# @lc code=end

