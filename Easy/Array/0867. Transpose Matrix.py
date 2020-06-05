class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        row = len(A)
        column = len(A[0])
        result = []
        
        for i in range(column):
            temp = []
            for j in range(row):
                temp.append(A[j][i])
            result.append(temp)
            
        return result
