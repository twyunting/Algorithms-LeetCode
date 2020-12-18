# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
# @lc code=end
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target-nums[i]], i]
            else:
                d[nums[i]] = i
