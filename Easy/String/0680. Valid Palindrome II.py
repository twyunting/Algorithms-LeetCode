def validPalindrome(s):
	"""
	:type s: str
	:rtype: bool
	"""
	
	i, j = 0, len(s)-1

	while i < j:
		if s[i] != s[j]:
			one = s[i:j]
			two = s[i+1:j+1]
			return one == one[::-1] or two == two[::-1]
		i += 1
		j -= 1
	return True
	"""
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s)-1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.vaildRemoveChr(s, i+1, j) or self.vaildRemoveChr(s, i, j-1)
        return True
    
    def vaildRemoveChr(self, s:str, i:int, j:int) -> bool:

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
        """
print(validPalindrome("abca")) # need return True