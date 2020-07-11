class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        result = []
        
        zero = 0
        one = 1
        
        while zero < len(nums):
            for i in range(nums[zero]):
                result.append(nums[one])
            
            zero += 2
            one += 2
        
        return result
        
        
