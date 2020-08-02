# zip

class Solution:
    def isStrobogrammatic(self, num):
        
        d = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        for i, j in zip(num, num[::-1]):
            if i not in d or d[i] != j:
                return False
        return True
        
        
