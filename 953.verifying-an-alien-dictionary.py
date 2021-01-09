#
# @lc app=leetcode id=953 lang=python
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = {}
        for i in range(len(order)):
            if i not in d:
                d[order[i]] = i
            else:
                continue
        print(d)

        for word in range(len(words)-1):
            front = words[word]
            behind = words[word+1] 
        
            for j in range(len(front)):
                if j > len(behind)-1:
                    return False # ex apple, app
                if d[front[j]] > d[behind[j]]:
                    return False
                if d[front[j]] < d[behind[j]]:
                    break
        return True

                




        
# @lc code=end

