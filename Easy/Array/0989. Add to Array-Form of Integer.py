class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        string = ""
        
        for i in A:
            string += str(i) # int() argument must be a string, not list
        
        value = int(string) + K
        
        valueString = str(value)
        
        return  valueString

    """
     1. convert A to string 
     2. then convert str(A) to integer 
     3. A + K
     
    """
    
    
