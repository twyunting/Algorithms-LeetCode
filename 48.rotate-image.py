#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # rotate = transpose + reverse
        column = len(matrix[0])

        # transpose matrix
        for i in range(column):
            for j in range(i, column):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        # reverse row
        for i in range(column):
            matrix[i].reverse()
        

            






# @lc code=end

