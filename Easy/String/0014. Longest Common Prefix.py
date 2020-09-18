def longestCommonPrefix(strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	res = ""
	if not strs:
		return ""

	for i in zip(*strs):
		if len(set(i)) == 1:
			res += i[0]
		else:
			return res
	return res

print(longestCommonPrefix(["flower","flow","flight"]))


"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        res = ""
        strs.sort()
        # Sort the string array first, then we only need to find out the longest common prefix between the first and last word.
        
        head = strs[0] 
        tail = strs[-1]
        limit = min(len(head), len(tail)) 

        for i in range(limit):
            if head[i] == tail[i]:
                res += head[i]
            else:
                break
        return res
"""
