#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:1}
        res = 0
        cusum = 0

        for i in nums:
            cusum += i
            diff = cusum - k
            if diff in d:
                res += d[diff] # value
            if cusum in d:
                d[cusum] += 1
            else:
                d[cusum] = 1
        print(d)
        return res





        
# @lc code=end

