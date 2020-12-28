#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = len(grid)
        row = len(grid[0])
    
        # edit the first row
        for i in range(1, row):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        
        # edit the first column
        for j in range(1, col):
            grid[j][0] = grid[j-1][0] + grid[j][0]
        
        # edit the remaining values in the grid accordingly
        for i in range(1, col):
            for j in range(1, row):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
                
        return grid[-1][-1]





# @lc code=end

