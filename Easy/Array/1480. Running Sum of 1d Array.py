class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ttl = 0
        res = []
        
        for i in nums:
            ttl += i
            res.append(ttl)
        return res
   

# Traversal Method

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = []
        
        res.append(nums[0])
        for i in range(1,len(nums)):
            res.append(res[i-1] + nums[i])
        return res   
    

# itertools.accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        return itertools.accumulate(nums)
    
    
