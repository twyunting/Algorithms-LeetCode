class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        d = {}
        ans = []
        for i in items:
            stid = i[0]
            score = i[1]
            if stid not in d:
                d[stid] = [score]
            else:
                d[stid].append(score)
        
        for i in d.items():
            stid = i[0]
            score = i[1]
            score.sort(reverse = True)
            total = 0
            for j in range(5):
                total += score[j]
            ans.append([stid, total//5])
            
        return ans
        
        
