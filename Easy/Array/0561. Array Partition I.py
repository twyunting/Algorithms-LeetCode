class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
         
        nums = (sorted(nums))
        return sum(nums[::2])
    
    
    """
    range(10)[::2] = seq[start:end:step]
    reference: https://blog.csdn.net/Evan123mg/article/details/49232089
    """
