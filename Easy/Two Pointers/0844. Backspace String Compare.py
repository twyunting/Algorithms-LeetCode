def backspaceCompare(S, T):
	"""
	:type S: str
	:type T: str
	:rtype: bool

	"""
	Sarr, Tarr = [], []
	for i in S:
		if i != "#":
			Sarr.append(i)
		elif len(Sarr) > 0: # make sure len(Sarr) not equal to 0
			Sarr.pop()


	for j in T:
		if j != "#":
			Tarr.append(j)
		elif len(Tarr) > 0: # make sure len(Tarr) not equal to 0
			Tarr.pop()

	return Sarr == Tarr
	
print(backspaceCompare(S = "ab##", T = "c#d#"))



"""
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
        
"""

