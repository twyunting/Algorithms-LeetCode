class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        while n != 1 and n not in cycle:
            cycle.add(n)
            n = sum(int(i) **2 for i in str(n))
        return n == 1 
        

# My method

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            total = 0
            for i in str(n):
                total += pow(int(i),2)
            n = total
        return True
    

# Same way but different output

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            total = 0
            for i in str(n):
                total += pow(int(i),2)
            n = total
        return n == 1
    
    
    
        
