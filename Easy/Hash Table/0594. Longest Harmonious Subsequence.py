# dic

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        d = Counter(nums)
        res = 0
        
        for i, j in d.items():
            if i+1 in d:
                res = max(d[i]+d[i+1], res)
        return res
                
                
