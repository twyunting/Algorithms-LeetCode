#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#

# @lc code=start
class Solution(object):

    def dfs(self, grid, r, c):
        grid[r][c] = 0
        num = 1
        lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

        for row, col in lst:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1:
                num += self.dfs(grid, row, col)
        return num


    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        areaIslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    areaIslands = max(areaIslands, self.dfs(grid, r, c))
        return areaIslands
# @lc code=end

