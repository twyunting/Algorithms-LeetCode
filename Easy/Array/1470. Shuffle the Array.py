class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        res = []
        
        for i in range(len(nums)//2): # nums.length == 2n
            res.append(nums[i])
            res.append(nums[i+n])
        return res   
 
 #  Zip Solution
 
 class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        L , R = nums[:n], nums[n:]
        res = []
        
        for i, j in zip(L, R):
            res += i,
            res += j,
        return res
        
        
