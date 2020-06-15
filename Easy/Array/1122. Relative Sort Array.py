class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        countArr1, result = collections.Counter(arr1), []
        
        for i in arr2:
            result += [i] * countArr1.pop(i)
        
        return result + sorted(countArr1.elements()) # add the remaining numbers in arr1
        
        
