class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    
        arr = []
        sortedNums = sorted(nums)
        
        for i in nums:
            arr.append(sortedNums.index(i))
        
        return arr
            
            
            
