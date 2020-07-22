class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = 0
        target.sort()
        arr.sort()
        for i in range(len(target)):
            if target[i] == arr[i]:
                count += 1
               
        if count == len(target):
            return True
        else:
            return False
            

# One line solution

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
        
        
