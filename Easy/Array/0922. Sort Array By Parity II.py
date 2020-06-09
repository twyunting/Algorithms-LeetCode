class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        odd, even = [], []
        
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
            
        result = []
        
        for i in range(len(A)):
            if i % 2 == 0:
                result.append(even.pop())
            else:
                result.append(odd.pop())
                
        return result
        
        
