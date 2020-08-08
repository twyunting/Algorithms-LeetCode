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
        
        return sum( i % 2 != 0 for i in collections.Counter(s).values()) <= 1
    
    
"""
From looking at different types of strings, we can conclude:
A string is a palindrome if and only if we have zero or at most one letter that occurs an odd number of times.
Everything else cannot be a palindrome.

Examples: aaacbbb (one letter occurs an odd number of times, thus, is a palindrome)
aaa: one letter occurs an odd number of times, thus, is a palindrome
aabb: zero letters occur an odd number of times, thus, is a palindrome
aabbcd: two letters occur an odd number of times, thus, is not a palindrome
"""
