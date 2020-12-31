#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # expand out from a middle letter
        # stop when: 
            # 1. two letters are not the same
            # 2. edge of the string

        def getLength(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1  # return the length of substring
        
        start = 0
        length = 0

        for i in range(len(s)):
            cur = max(getLength(i, i),
                      getLength(i, i + 1))
            if length >= cur:
                continue
            length = cur
            start = i - (cur - 1) // 2
        return s[start:start+length]



        
# @lc code=end

