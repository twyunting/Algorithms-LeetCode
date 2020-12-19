#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if target >= nums[0]:
                if nums[mid] >= nums[0] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # target < nums[0]
                if nums[mid] >= nums[0] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

            
# @lc code=end

