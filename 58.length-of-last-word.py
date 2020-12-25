#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if count == 0:
                    continue
                else:
                    return count
            else:
                count += 1
        return count
     
# @lc code=end

