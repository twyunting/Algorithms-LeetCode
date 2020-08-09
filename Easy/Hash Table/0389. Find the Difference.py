# dic

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    
        ds, dt = {}, {}
        for i in s: # build s dic
            if i not in ds:
                ds[i] = 1
            else:
                ds[i] += 1
                
        for i in t: # build t dic
            if i not in dt:
                dt[i] = 1
            else:
                dt[i] += 1
        
        for i, j in dt.items():
            if i not in ds or j > ds[i]:
                return i

# dic 2

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    
        ds = Counter(s)
        
        for i in t:
            if i not in ds or ds[i] == 0:
                return i
            else:
                ds[i] -= 1
                
# sorted

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    
        S = sorted(s)
        T = sorted(t)
        i = 0
        
        while i < len(S) and i < len(T): 
            if S[i] != T[i]: 
                return T[i]
            i += 1
            
        # if no, return the last one
        return T[-1] 
                
        
    
    
