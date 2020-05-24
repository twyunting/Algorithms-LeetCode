class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        result = []
        for i in range(rowIndex+1): # start with 1 row (1:1)
            result.append([])
            for j in range(i+1):
                if j in (0,i):
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1] + result[i-1][j])
        
        return result[rowIndex]
    
"""
Think like this -> First row is actually row 0, second -> row 1 and so on...because the indexing starts at zero.
Now, I need to traverse all the rows. Say rowIndex = 3.
Now when i iterate using range(rowIndex) --> 
I'll actually iterate over rows 0,1,2....but never reach to rowIndex 3 . 
Therefore, I append one to rowIndex initially to make it possible.
"""
