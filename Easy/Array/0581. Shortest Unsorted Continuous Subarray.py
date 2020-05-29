class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        sorted_list = sorted(nums)
        output = []
        
        if nums == sorted_list:
            return 0
        
        for i in range(len(nums)):
            if nums[i] != sorted_list[i]:
                output.append(i)
                
        return output[-1] - output[0] + 1       
    
    
    """
    []              0  1  2  3  4  5  6 
    Input           2, 6, 4, 8, 10, 9, 15
    sorted_list     2, 4, 6, 8, 9, 10, 15
    
    so output[] must choose the last one [-1] minus first one [0] then "add 1"
    
    """
