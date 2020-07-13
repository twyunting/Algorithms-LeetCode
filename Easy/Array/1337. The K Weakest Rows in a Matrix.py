class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        d = {}
        
        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if j == 1:
                    count += 1
                else:
                    break
            
            d[i] = count
        
        
        index = sorted(d, key = d.get) # get the value in the dictionary
        return index[0:k]
    
    """
    https://www.runoob.com/python/python-dictionary.html
    
    d.get = value
    d.key = key
    
    """
    
    
    
