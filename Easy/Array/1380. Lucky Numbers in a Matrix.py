class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        for i in matrix:
            minNum = min(i)
            minNumIndex = i.index(min(i))
            
            for j in range(len(matrix)):
                if minNum >= matrix[j][minNumIndex]: # fixed the columns
                    continue
                else:
                    minNum = 0
                    break
            if minNum == 0:
                continue
            else:
                return [minNum]
                
                
                
