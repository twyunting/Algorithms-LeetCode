def isLongPressedName(name, typed):
	"""
	:type name: str
	:type typed: str
	:rtpe: bool
		"""
	if len(name) > len(typed):
		return False

	i, j = 0, 0
	while i < len(name) and j < len(typed):
		if name[i] == typed[j]:
			i += 1 # add the length of name
			j += 1 # add the length of typed
		elif typed[j] == name[i-1]:
			j += 1 # add the length of typed
		else:
			return False

		if i == len(name):
			return True
	return False

print(isLonzgPressedName(name = "alex", typed = "aaleex"))

