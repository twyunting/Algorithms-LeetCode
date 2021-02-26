
def solution(data, n): 
	dic = {}
	res = []
	for i in data:
		if i not in dic:
			dic[i] = 1
		else:
			dic[i] += 1
	for idx,item in enumerate(data):
		if dic[item] <= n:
			res.append(item)
	return res



# ans is 1, 4
"""
def solution(data, n): 
    dict={}
    removeSet=[]
    for i in data:
        try:
            if dict[i]:
                dict[i]+=1
                if dict[i]>=n:
                    print("in")
                    removeSet.append(i)
        except:
            dict[i]=1
    print(removeSet)
    for i in data:
        if i in removeSet:
            data.remove(i)
    return data
    
print(solution([1, 2, 3], 0))
"""