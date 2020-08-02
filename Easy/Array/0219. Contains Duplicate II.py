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
    
 """
哈希表= {}

遍歷摘要：

若nums [i] nums [i]不在hashhash中，則令nums [i] nums [i]為鍵，值為當前的索引i。
若已存在：
如果滿足，返回True。
將索引更新為當前索引，hash [nums [i]] = ihash [nums [i]] = i
返回False

"""

