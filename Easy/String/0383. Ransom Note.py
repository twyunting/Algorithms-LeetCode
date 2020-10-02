def canConstruct(ransomNote, magazine):
	"""
	:type ransomNote: str
	:type magazine: str
	:rtype: bool
	"""
	from collections import Counter
	letters = Counter(magazine)

	for j in ransomNote:
		if letters[j] <= 0: 
			return False
			letters[j] -= 1 # minus values 
	return True

print(canConstruct(ransomNote = "a", magazine = "aab"))