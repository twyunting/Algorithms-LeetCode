class Solution:
    def fib(self, N: int) -> int:
        
        if N == 0:
            return 0
        if N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)
        
        
        
 # elegant method

class Solution:
    def fib(self, N: int) -> int:
        
        cache = {0:0, 1:1}
        
        for i in range(2, N+1):
            # Since range is exclusive and we want to include N, we need to put N+1.
            cache[i] =  cache[i-1] + cache[i-2]
        
        return cache[N]
    
    
    
