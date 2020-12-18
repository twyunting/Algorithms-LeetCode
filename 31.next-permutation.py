# @before-stub-for-debug-begin
from python3problem31 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivotFirst=-1
        i=len(nums)-1
        tmp=nums[-1]
        while i>=0:
            if nums[i]>=tmp:
                tmp=nums[i]
                i-=1
            else:
                pivotFirst=i
                break
        #print(pivotFirst)
        if pivotFirst==-1:
            nums.reverse()
            return
        pivotFirst=i
        pivotSecond=-1
        j=len(nums)-1
        while(j>pivotFirst):
            if nums[j]>nums[pivotFirst]:
                pivotSecond=j
                break
            j-=1

        #print(pivotFirst,pivotSecond)

        nums[pivotSecond],nums[pivotFirst]=nums[pivotFirst],nums[pivotSecond]
        l,r = pivotFirst+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
# @lc code=end

