class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
      
        d = {}
        strr = str.split() #default() is blank
        
        if len(pattern) != len(strr):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in d and strr[i] not in d.values():
                d[pattern[i]] = strr[i]
            elif pattern[i] not in d:
                    return False
            elif strr[i] not in d.values():
                return False
            elif d[pattern[i]] != strr[i]:
                    return False
        return True
                
                
# Second

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
      
        d = {}
        strr = str.split() #default() is blank
        
        if len(pattern) != len(strr):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != strr[i]:
                    return False
            elif strr[i] in d.values():
                return False
            else:
                d[pattern[i]] = strr[i]
        return True
                
# set method

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
      
        strr = str.split() #default() is blank
        if len(pattern) != len(strr):
            return False
        
        return len(set(pattern)) == len(set(zip(pattern, strr))) == len(set(strr))
    
    
                
