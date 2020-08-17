class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        d = {}
        
        for i in range(len(order)):
            if i not in d:
                d[order[i]] = i
            else:
                continue
        
        for i in range(len(words)-1):
            front = words[i]
            behind = words[i+1]
            
            for j in range(len(front)):
                if j > len(behind)-1:
                    return False
                if d[front[j]] > d[behind[j]]:
                    return False
                if d[front[j]] < d[behind[j]]:
                    break
        return True  
        
        
