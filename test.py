# Python code to reverse 
# a list using slicing 
  

a = [4,5,6,7,0,1,2]
res = []

for i in range(len(a), -1, -1):
	res.append(i)
return res
print(res)

