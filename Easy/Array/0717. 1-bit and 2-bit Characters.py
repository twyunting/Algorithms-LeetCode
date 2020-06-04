class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        index = 0
        n = len(bits)
        
        while index < n:
            
            if bits[index] == 0 and index == n-1:
                return True
            
            if bits[index] == 0:
                index += 1
                
            if bits[index] == 1:
                index += 2
        
        return False
