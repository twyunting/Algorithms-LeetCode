class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        length = len(arr)
        d = {}
        
        while arr:
            val = arr.pop()
            if val in d:
                d[val] += 1
            else:
                d[val] = 1
            
        for key, value in d.items():
            if value >= length / 4:
                return key
        
        
  # One line solution
  
  class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        return collections.Counter(arr).most_common()[0][0]
