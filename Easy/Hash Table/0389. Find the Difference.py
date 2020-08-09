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
                
