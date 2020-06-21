class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def strtoFrequency(s):
            s = list(s)
            s.sort()
            c = s[0] # c is the smallest character
            freq = 0
            
            for i in s:
                if i == c:
                    freq += 1
                else:
                    return freq
            return freq
        
        def freqCompare(qFreq, wFreq):
            ansArray = []
            for i in qFreq:
                ans = 0
                for j in wFreq:
                    if j > i:
                        ans += 1
                ansArray.append(ans)
            return ansArray
        queriesFreq = [strtoFrequency(i) for i in queries]
        wordsFrreq = [strtoFrequency(i) for i in words]
            
        return freqCompare(queriesFreq, wordsFrreq)
                
            
