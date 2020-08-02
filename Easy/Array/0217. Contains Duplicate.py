class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        
# Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    
        s = collections.Counter(nums)
        
        for i in s.values():
            if i >= 2:
                return True
        return False
    
    
