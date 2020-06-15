class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        
        
        countA = collections.Counter(A)
        result = []
        
        for i in countA:
            if countA[i] == 1:
                result.append(i)
            
        if len(result) > 0:
            return max(result)
        else:
            return -1
            
            
