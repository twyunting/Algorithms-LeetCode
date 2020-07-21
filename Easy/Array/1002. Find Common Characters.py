class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        text = collections.Counter(A[0])
        
        for i in A:
            text &= collections.Counter(i)
            # All text = text and i in A loop totally
             
        return list(text.elements())
    
    # https://docs.python.org/3/library/collections.html
    """
    Example:
    
    c = Counter(a=4, b=2, c=0, d=-2)
    sorted(c.elements())
    ['a', 'a', 'a', 'a', 'b', 'b']
    
   """ 
    
