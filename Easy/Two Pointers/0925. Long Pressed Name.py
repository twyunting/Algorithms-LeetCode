def isLongPressedName(name, typed):
	"""
	:type name: str
	:type typed: str
	:rtpe: bool
	"""
	if len(name) > len(typed):
		return False

	i = 0
	for j in range(len(typed)):
		if i < len(name) and name[i] == typed[j]: #make sure i must < len(name) to save time complexity
			i += 1
		elif j == 0 or typed[j] != typed[j-1]: # index 0 cannot minus i
			return False
	return i == len(name)

print(isLongPressedName(name = "alex", typed = "aaleex"))


"""
LeetCode answer

class Solution:
    def isLongPressedName(self, A: str, B: str) -> bool:
        M = len(A)
        N = len(B)
        i = 0
        j = 0
        last = 0
        while not (i == M and j == N):
            if i < M and j < N and A[i] == B[j]:
                last = A[i]
                i += 1
                j += 1
            elif j < N and last == B[j]:
                j += 1
            else:
                return False
        return True
"""