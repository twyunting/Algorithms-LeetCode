class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        
        result = -1
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] + A[j] < K:
                    result = max(A[i] + A[j], result)
        
        return result
   
   
   
