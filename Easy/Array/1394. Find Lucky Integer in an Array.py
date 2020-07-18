class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        result = -1
        
        for i, j in Counter(arr).items():
            if i == j and i > result:
                result = i
        
        return result
        
        
# Brute Force

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        max_num = -1
        
        for i in arr:
            temp = arr.count(i)
        
            if i == temp and i > max_num:
                max_num = i
        
        return max_num
        
        
