def canConstruct(ransomNote, magazine):
	"""
	:type ransomNote: str
	:type magazine: str
	:rtype: bool
	"""
	letters = {}
	for i in magazine:
		if i not in letters:
			letters[i] = 1
		else:
			letters[i] += 1 # make a dic 
	return letters

print(canConstruct(ransomNote = "a", magazine = "aaavvvvvv"))