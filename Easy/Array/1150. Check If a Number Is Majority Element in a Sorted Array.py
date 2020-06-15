class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        array = []
        for num in nums:
            if target == num:
                array.append(num)
        
        if len(array) > len(nums) / 2:
            return True
        else:
            return False
            
            
