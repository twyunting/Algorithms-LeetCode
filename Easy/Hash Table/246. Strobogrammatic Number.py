# zip

class Solution:
    def isStrobogrammatic(self, num):
        
        d = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        for i, j in zip(num, num[::-1]):
            if i not in d or d[i] != j:
                return False
        return True
        
# two pointers

class Solution:
    def isStrobogrammatic(self, num):
    
        d = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        start, end = 0, len(num)-1 # end is index's position
        while start <= end:
            if num[start] not in d:
                return False
            if d[num[start]] != num[end]:
                return False    
            start += 1
            end -= 1
        return True
        
        
        
