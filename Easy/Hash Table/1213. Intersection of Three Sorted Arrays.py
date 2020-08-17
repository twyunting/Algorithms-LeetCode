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
        
        
# Three pointers

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        p1 = p2 = p3 = 0
        res = []
        
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                res.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
                continue
                
            maxp = max(arr1[p1], arr2[p2], arr3[p3])
            
            if arr1[p1] < maxp:
                p1 += 1
            if arr2[p2] < maxp:
                p2 += 1
            if arr3[p3] < maxp:
                p3 += 1
                
        return res
                
    
        
