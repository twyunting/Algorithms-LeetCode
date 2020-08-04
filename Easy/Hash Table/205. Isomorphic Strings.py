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
    
    
# Dic second solution

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        d = {}
      
        for i in range(len(s)):
            if s[i] not in d and t[i] not in d.values():
                d[s[i]] = t[i]
            elif s[i] not in d or t[i] not in d.values():
                return False
            elif d[s[i]] != t[i]:
                return False
        return True
          

# Two Hashmap

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]] = t[i]
            else:
                if ds[s[i]] != t[i]:
                    return False
                else:
                    continue
        
        for j in range(len(t)):
            if t[j] not in dt:
                dt[t[j]] = s[j]
            else:
                if dt[t[j]] != s[j]:
                    return False
                else:
                    continue
        return True
    
    
    
        
        
