#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        if len(strs) <= 1:
            return [strs]
        else:
            for i in range(len(strs)):
                reg = strs[i]
                # print(reg)
                regSort = "".join(sorted(reg))
                # print(regSort)
                if regSort in d:
                    d[regSort].append(reg)
                else:
                    d[regSort] = [reg]
        return d.values()

# @lc code=end

