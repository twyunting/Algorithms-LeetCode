def backspaceCompare(S, T):
"""
:type S: str
:type T: str
:rtype: bool
"""
	S, T = self.recheck(S), self.recheck(T)
	return S == T

	def recheck(strings):
		stack = []
		for i in nums:
			if i != "#":
				stack.append(i)
			else: # if i == #
				stack.pop(i)
		return stack

print(backspaceCompare(S = "ab#c", T = "ad#c"))
print(backspaceCompare(S = "ab##", T = "c#d#"))
print(backspaceCompare(S = "ab#c", T = "ad#c"))