class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res = []
        
        for word in words:
            i = set(word.lower())
            if i&row1 == i:
                res.append(word)
            elif i&row2 == i:
                res.append(word)
            elif i&row3 == i:
                res.append(word)
        return res
        
 # same way

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = set("QWERTYUIOPqwertyuiop")
        row2 = set("ASDFGHJKLasdfghjkl")
        row3 = set("ZXCVBNMzxcvbnm")
        res = []
        
        for word in words:
            i = set(word)
            if i&row1 == i:
                res.append(word)
            elif i&row2 == i:
                res.append(word)
            elif i&row3 == i:
                res.append(word)
        return res
    
