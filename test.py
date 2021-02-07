import numpy as np
a = 60
c = 0
m = 2**(31) -1
x = 0.1

for i in range(100):

	x= np.mod((a*x+c),m)

	uniform = x/m # generation of a uniform distribution in the range of [0, 1]

	print(uniform)
