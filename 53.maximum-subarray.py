#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr = nums[0]
        maxsum = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr+nums[i])
            maxsum = max(maxsum, curr)
        return maxsum

# @lc code=end

