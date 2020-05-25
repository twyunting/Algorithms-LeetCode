class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Two pointer Solution
        
        dict = {}
        
        for i in range(len(numbers)):
            if target - numbers[i] not in dict:
                dict[numbers[i]] = i
            else:
                return[dict[target - numbers[i]]+1, i+1]
