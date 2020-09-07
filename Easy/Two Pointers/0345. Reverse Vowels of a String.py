def reverseVowels(s):

	i, j = 0, len(s)-1
	s = list(s)

	vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
	
	while i < j:
		while i < j and s[i] not in vowels:
			i += 1
		while i < j and s[j] not in vowels:
			j -= 1 

		s[i], s[j] = s[j], s[i]
		i += 1
		j -= 1

		return "".join(s)


s = "A man, a plan, a canal: Panama"

print(reverseVowels(s))