class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ttl = 0
        res = []
        
        for i in nums:
            ttl += i
            res.append(ttl)
        return res
            
            
