# Dictionary Method

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        d = {}
        if arr[0] == 0:
            return True
        
        for i in arr:
            if i not in d and i != 0:
                d[i * 2] = i
                d[i / 2] = i
                
            if i in d:
                return True
                    
        return False
 
 
 # Set Method
 
 class Solution(object):
    def checkIfExist(self, arr):
        seen = set()
        for val in arr:
            if val * 2 in seen:
                return True
            if val / 2 in seen:
                return True
            seen.add(val)
        return False
                
                
   
