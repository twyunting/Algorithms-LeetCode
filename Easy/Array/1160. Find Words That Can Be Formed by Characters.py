class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        result = 0
        c = Counter(chars)
        
        for i in words:
            if len(Counter(i) - c) == 0:
                result += len(i)
        return result
        
        
