def addBinary(a, b):
	"""
	:type a: str
	:type b: str
	:rtype: str
	"""
	# int("x", base) is change to binary number : 2, 4, 8, 16
	return "{:b}".format(int(a, 2) + int(b, 2)) # :b is Binary format

print(addBinary(a = "1010", b = "1011"))

# reference: https://www.w3schools.com/python/ref_string_format.asp
