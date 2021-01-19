#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ans = []

        def backtracking(S = "", left = 0, right = 0):
            if len(S) == 2*n:
                ans.append(S)
            else:
                if left > right:
                    backtracking(S +")", left, right+1)
                if left < n:
                    backtracking(S +"(", left+1, right)
        backtracking("", 0, 0)

        return ans        
    

# @lc code=end

