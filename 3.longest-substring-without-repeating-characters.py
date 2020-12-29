#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end = -1, 0
        d = {}

        for i in range(len(s)):
            # s[i] in d.....
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i
            else:
            # s[i] not in d...
                d[s[i]] = i
                if i - start > end:
                    end = i - start
        return end       
# @lc code=end

