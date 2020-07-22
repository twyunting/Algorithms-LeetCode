class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandy = max(candies) 
        res = []
        
        for i in range(len(candies)):
            if candies[i] + extraCandies < maxCandy:
                res.append(False)
            else:
                res.append(True)
        return res
        
        
