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
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                if t[i] != dict[s[i]]:
                    return False
            elif t[i] in dict.values():
                return False
            else:
                dict[s[i]] = t[i]
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
    
    
    
        
        
