# dic

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d, count = {}, 0
        one  = 0
        # build a dic, Counter can be accepted also
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1 
            
        for i, j in d.items():
            if len(s) == j:
                return len(s)
            elif j % 2 == 0:
                count += j
            elif j % 2 != 0 and j >2:
                count += j-1
                
        for x in d.values():
            if x % 2 == 1 or x == 1:
                one += 1
                break
                
        return one + count
        
