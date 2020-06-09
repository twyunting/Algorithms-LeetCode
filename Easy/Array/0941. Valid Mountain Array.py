class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        i = 0
        
        # walk up
        while i < len(A)-1 and A[i] < A[i+1]:
            i += 1
            
        # peak can't be first or last
        if i == 0 or i == len(A)-1:
            return False
        
        # walk down
        while i < len(A)-1 and A[i] > A[i+1]:
            i += 1
        
        return i == len(A)-1
        
        
