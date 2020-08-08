class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = {}
        for i in s:
            d[i] = d.get(i,0) +1
        
        for i in s:
            if i in d and d[i] == 1:
                return s.index(i)
        return -1
        
        
