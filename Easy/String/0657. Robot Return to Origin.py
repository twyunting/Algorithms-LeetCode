def judgeCircle(moves):
	"""
	:type moves: str
	:rtype: bool
	"""

	UD = LR = 0

	for i in moves:
		if i == "R":
			LR += 1
		elif i == "L":
			LR -= 1
		elif i == "U":
			UD += 1
		elif i == "D":
			UD -= 1
	return UD == LR == 0

print(judgeCircle("RRDD"))