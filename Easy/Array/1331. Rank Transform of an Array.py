class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        arrSort = sorted(set(arr)) # cancelled the redundant index
        d = {}
        result = []
        
        for i , j in enumerate(arrSort):
            d[j] = i+1
        
        for i in arr:
            result.append(d[i])
            
        return result
        
        
        
