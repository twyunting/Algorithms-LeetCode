class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        minDiff = float("inf")
        minList = []
        
        for index in range(len(arr) - 1):
            minDiff = min(minDiff, abs(arr[index+1] - arr[index]))
            
        for index in range(len(arr) - 1):
            if abs(arr[index+1] - arr[index]) == minDiff:
                minList.append([arr[index],arr[index + 1]])
                
        return minList
        
        
       
    # Dictionary Method
        
        class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        dic = {}
        arr.sort()
        
        for i in range(len(arr)-1):
            d = arr[i+1] - arr[i]
            
            if d not in dic:
                dic[d] = []
            
            dic[d].append([arr[i], arr[i+1]])
        
        return dic[min(dic)]
        
        
