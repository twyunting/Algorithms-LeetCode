# Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ds = collections.Counter(s)
        dt = collections.Counter(t)
        
        return ds == dt
        
# sorted

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)
    
# dic

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for i in t:
            if i not in d or d[i] == 0:
                return False
            else:
                d[i] -= 1
        return True
                
        
        
