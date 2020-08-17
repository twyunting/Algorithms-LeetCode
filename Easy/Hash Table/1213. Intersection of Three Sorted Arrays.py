class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        tmp = []
        final = []
        for i in arr1:
            if i in arr2:
                tmp.append(i)
        
        for i in arr3:
            if i in tmp:
                final.append(i)
        return final
        
        
