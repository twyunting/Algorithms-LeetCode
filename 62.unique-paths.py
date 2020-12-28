#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table = [[0]*n for _ in range(m)]

        for i in range(m): # initialize to 1 
            table[i][0] = 1
        for j in range(n): # initialize to 1 
            table[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1] # return the last point
        
# @lc code=end

