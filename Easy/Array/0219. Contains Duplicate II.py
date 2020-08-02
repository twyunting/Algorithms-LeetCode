class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dic = {}
        for index, num in enumerate(nums):
            if num not in dic:
                dic[num] = index
            else:
                # index = current number, dic[nums] = previous num in dic
                if index - dic[num] <= k: 
                    return True
                dic[num] = index

# Second

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        d = {}
        for i, j in enumerate(nums):
            if j in d and i-d[j] <= k:
                return True
            d[j] = i
        return False
    
    
