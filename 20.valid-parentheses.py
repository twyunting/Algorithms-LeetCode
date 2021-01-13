#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {")":"(", "]":"[", "}":"{"}
        stack = []

        for ch in s:
            if ch not in d:
                stack.append(ch)
                print(stack[-1])
            else:
                corresponding_bracket = d[ch]
                #print(corresponding_bracket)
                if not stack or stack[-1] != corresponding_bracket:
                    return False
                stack.pop()
        if stack:
            return False
        return True    
        

        
# @lc code=end

