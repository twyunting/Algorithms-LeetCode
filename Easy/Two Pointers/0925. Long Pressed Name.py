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