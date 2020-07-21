class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
    
        for direction, amount in shift:
            amount %= len(s) #optional
            
            if direction == 0: #left shift
                s = s[amount:] + s[:amount]
            else: #right shift
                s = s[-amount:] + s[:-amount]
        return s
        
        
# Second Method

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0
        for x, y in shift:
            if x == 0:
                move -= y
            else:
                move += y
        move %= len(s)
        return s[-move:] + s[:-move]
    
    
