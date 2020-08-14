class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        
        Awords = A.split()
        Bwords = B.split()
        
        d, res = Counter(Awords) + Counter(Bwords), []   
        
        for i, j in d.items():
            if j == 1:
                res.append(i)
        return res
        
        
