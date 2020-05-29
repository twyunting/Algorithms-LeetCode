class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        length = len(nums)
        
        while i < length:
            if nums[i] == 0:
                nums.append(nums.pop(i)) # add 1 and cancel 1
                length -= 1
            else:
                i += 1
        
