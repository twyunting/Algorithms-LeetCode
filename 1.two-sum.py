# @before-stub-for-debug-begin

# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
# 
# print("hello")

class Solution:
    def twoSum(self, nums, target) :

        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target-nums[i]], i]
            else:
                d[nums[i]] = i  
# @lc code=end

