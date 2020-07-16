class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    
        arr = []
        sortedNums = sorted(nums)
        
        for i in nums:
            arr.append(sortedNums.index(i))
        
        return arr
            
            

# Brute Force Method

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    
        arr = []
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    count += 1
            arr.append(count)
        return arr
            
        
        
