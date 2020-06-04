class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftsum = 0
        total = sum(nums)
        
        for i, j in enumerate(nums):
            if leftsum == total - j - leftsum:
                return i
            leftsum += j
            
        return -1
