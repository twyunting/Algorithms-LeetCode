#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def twoSum(nums, target):
            res = set()
            hashset = set()
            for num in nums:
                if target - num in hashset:
                    res.add((target - num, num))
                hashset.add(num)
            return res

    
        if len(nums) < 3:
            return []

        res = set()
        for idx in range(len(nums)-2):
            a = nums[idx]
            nums_remaining = nums[idx+1:]
            target_remaining = 0 - a 

            for b, c in twoSum(nums_remaining, target_remaining):
                res.add((a, b, c))
        return res

# @lc code=end

