class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S, T = self.recheck(S), self.recheck(T)
        return S == T
    
    def recheck(self, strings):
        stack = []
        for i in strings:
            if i != "#":
                stack.append(i)
            elif stack:
                stack.pop()
        return stack
        
