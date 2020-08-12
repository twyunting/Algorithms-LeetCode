# Jerry's answer

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        ans = []
        first = ""
        minimum = ("none",9999)
        
        for i, j in enumerate(list1):
            if j not in list2:
                continue
            else:
                if list2.index(j) + i < minimum[1]:
                    first = j
                    minimum = (j, list2.index(j)+i)
                elif list2.index(j) + i == minimum[1]:
                    ans.append(j)
        ans.append(first)
        
        return ans
    
    
# brute force with 3 dic

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        d1 = {}
        d2 = {}
        dtotal = {}
        res = float('inf')
        
        for i, j in enumerate(list1):
            d1[j] = i
        
        for i, j in enumerate(list2):
            d2[j] = i
        
        for i in d1:
            if i in d2:
                if d1[i] + d2[i] in dtotal:
                    dtotal[d1[i]+d2[i]].append(i)
                else:
                    dtotal[d1[i]+d2[i]] = [i]
            
                    res = min(res, d1[i]+d2[i])
        return dtotal[res]
        
        
