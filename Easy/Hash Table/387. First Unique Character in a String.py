# dic

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = {}
        for i in s:
            d[i] = d.get(i,0) +1
        
        for i in s:
            if i in d and d[i] == 1:
                return s.index(i)
        return -1
        
# Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = Counter(s)
        
        for i, j in enumerate(s):
            if count[j] == 1:
                return i
        return -1
            
