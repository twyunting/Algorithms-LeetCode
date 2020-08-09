class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
            
            
# Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        aaa = Counter(nums)
        count = 0
        
        for x, y in aaa.items():
            count += (y* (y-1)//2)
        return int(count)
    

    
    
    
