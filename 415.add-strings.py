#
# @lc app=leetcode id=415 lang=python
#
# [415] Add Strings
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = int(num1)
        num2 = int(num2)
        return str(num1+num2)
        
# @lc code=end

