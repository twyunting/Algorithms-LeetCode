#
# @lc app=leetcode id=43 lang=python
#
# [43] Multiply Strings
#

# @lc code=start
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
    n1, n2 = int(num1), int(num2)

    return str(n1*n2)
# @lc code=end

