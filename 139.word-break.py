#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        for i in s:
            for j in wordDict:
                for k in j:
                    if k not in s and s[i:j] not in wordDict:
                        return False
        return True




            
        
        

        

# @lc code=end

