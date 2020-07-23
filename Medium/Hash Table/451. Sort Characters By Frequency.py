class Solution:
    def frequencySort(self, s: str) -> str:
        
        test = collections.Counter(s)
        res = ''
        
        for i in sorted(test, key=test.get, reverse=True): 
            res += i * test[i]
        return res
    
    """
    sorted先大寫在小寫
    get = get values
    """
    
    
