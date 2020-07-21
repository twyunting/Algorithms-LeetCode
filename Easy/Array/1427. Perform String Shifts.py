class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
    
        for direction, amount in shift:
            amount %= len(s)
            
            if direction == 0: #left shift
                s = s[amount:] + s[:amount]
            else: #right shift
                s = s[-amount:] + s[:-amount]
        return s
        
        
