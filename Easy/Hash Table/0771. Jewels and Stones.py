class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        d = {}
        count = 0
        
        for i in J:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in S:
            if i in d:
                count += 1
        return count
        
# one line

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        return sum(i in J for i in S)
    
    
