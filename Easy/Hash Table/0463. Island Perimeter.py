class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        result = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result += 4
                    
                    # i-1: check left 
                    if i > 0 and grid[i-1][j] == 1: #the first index must be 4 so i>0
                        result -= 2
                    # j-1: check up
                    if j > 0 and grid[i][j-1] == 1: #the first index must be 4 so j>0
                        result -= 2 
        
        return result
                
"""
Approach 2: Better Counting
Approach 2 has the same time and space complexity as Approach 1. 
Even though they have the same time and space complexities, Approach 2 is slightly more efficient than the Approach 1. 
Rather than checking 4 surrounding neighbors, we only need to check two neighbors (LEFT and UP) in Approach 2.

"""        

