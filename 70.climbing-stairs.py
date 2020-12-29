#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        previous, current = 0, 1

        for i in range(n):
            previous, current = current, previous + current
        return current

# @lc code=end

