class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        temp = 0
        result = float("-inf")
    
        for i, j in enumerate(nums):
            temp += j
            if i >= k:
                temp -= nums[i-k]  
            if i >= k-1:
                result = max(result, temp)
        
        return result / k
        
        
