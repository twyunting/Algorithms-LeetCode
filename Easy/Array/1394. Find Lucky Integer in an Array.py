# First

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        result = -1
        
        for i, j in Counter(arr).items():
            if i == j:
                result = max(i, result)
        
        return result
    
# Second
    
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        max_num = -1
        count = Counter(arr)
        
        for i in count.values():
            if count[i] == i:
                max_num = max(i, max_num)
                
        return max_num
    
    
    
    
        
# Brute Force

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        max_num = -1
        
        for i in arr:
            temp = arr.count(i)
        
            if i == temp and i > max_num:
                max_num = i
        
        return max_num
        
        
