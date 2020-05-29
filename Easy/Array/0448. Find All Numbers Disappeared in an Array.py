class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    
        set_1 = set(range(1, len(nums)+1)) # range function is not includes the last number
        set_2 = set(nums)
        return set_1.difference(set_2)
            
        """
        https://blog.csdn.net/zhenyu5211314/article/details/19069567
        
        more detail about range
        """
            
