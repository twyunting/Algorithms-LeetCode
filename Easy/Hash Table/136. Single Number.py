class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        d = Counter(nums)
        
        for i, j in d.items():
            if j == 1:
                return i
                
                
# 7500 ms runtime HAHAHA!!!

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for i in nums:
            if nums.count(i) == 1:
                return i
            
            
