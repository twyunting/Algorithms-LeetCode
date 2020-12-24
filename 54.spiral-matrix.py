#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        if row == 0 or len(matrix[0]) == 0:
            return []

        col = len(matrix[0])
        res = matrix[0]

        if row > 1:
            for i in range(1, row):
                res.append(matrix[i][col-1])
        
            for j in range(col-2, -1, -1): # we need to include index 0 so use -1
                res.append(matrix[row-1][j])
            
            if col > 1:
                for k in range(row-2, 0, -1):
                    res.append(matrix[k][0])
        
        inside = []
        for l in range(1, row-1):
            tmp = matrix[l][1:-1]
            inside.append(tmp)
        
        return res + self.spiralOrder(inside)

# @lc code=end

