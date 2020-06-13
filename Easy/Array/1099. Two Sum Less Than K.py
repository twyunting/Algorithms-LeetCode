class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        
        result = -1
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] + A[j] < K:
                    result = max(A[i] + A[j], result)
        
        return result
   
   
   
# Two pointer solution

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        
        A.sort()
        result = -1
        left, right = 0, len(A)-1
        
        
        while left < right:
            if A[left] + A[right] < K:
                result = max(result, A[left] + A[right])
                left += 1
            else:
                right -= 1
        
        return result
    
    
