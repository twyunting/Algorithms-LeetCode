class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        return self.isIso(s, t) and self.isIso(t, s)
    
    def isIso(self, s, t):
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False
        return True
    
 # set solution

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        return len(set(s)) == len(set(zip(s,t))) == len(set(t))
    
    
        
        
        
