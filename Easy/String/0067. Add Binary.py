def addBinary(a, b):
	"""
	:type a: str
	:type b: str
	:rtype: str
	"""
	# int("x", base) is change to binary number : 2, 4, 8, 16
	return "{a:b}".format(int(a, 2) + int(b, 2))

	
	