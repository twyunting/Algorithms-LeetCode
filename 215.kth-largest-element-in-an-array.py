#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
    
        nums = sorted(nums)
        return nums[-k]
# @lc code=end

