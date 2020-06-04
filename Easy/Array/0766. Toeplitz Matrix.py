class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(len(matrix)-1): # i = row
            for j in range(len(matrix[i])-1): # j = col
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        
        return True
