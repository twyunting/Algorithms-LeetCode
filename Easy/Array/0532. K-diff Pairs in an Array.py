class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        result = 0
        counter = collections.Counter(nums)
        # Counter({1: 2, 3: 1, 4: 1, 5: 1})
        
        for i in counter:
            if k > 0 and i + k in counter or k == 0 and counter[i] > 1:
                result += 1
        
        return result
        
        # counter[i] > 1: have a double numbers in array
