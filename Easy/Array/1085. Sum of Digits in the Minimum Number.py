class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        
        minimal = str(min(A))
        result = 0
        
        for i in minimal:
            result += int(i)
            
        if result % 2 == 0:
            return 1
        else:
            return 0
                
                
