class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        arrays.sort(key = lambda x: x[0])
        d1 = max(number[-1] for number in arrays[1:]) - arrays[0][0]
        
        arrays.sort(key = lambda x: x[-1])
        d2 = arrays[-1][-1] - min(number[0] for number in arrays[:-1])
        
        return max(d1, d2)
