class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
    
    # the maxixum odd number of palindrome is once time
        
        count = collections.Counter(s)
        odd = 0
        for i in count.values():
            if i % 2 != 0:
                odd += 1
                
        if odd > 1:
            return False
        else:
            return True
            
 # one line

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        return sum( i % 2 for i in collections.Counter(s).values()) <= 1
    
    