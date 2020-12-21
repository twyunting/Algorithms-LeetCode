#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = set(nums)
        # print(nums)
        for idx, num in enumerate(nums):
            n = nums[:idx] + nums[idx+1:]
            for i in self.permuteUnique(n):
                result.append([num] + i)
        return result

# @lc code=end


