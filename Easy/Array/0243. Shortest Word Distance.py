class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
    
        w1, w2, distance = float("inf"), float("inf"), float("inf")
        for i, j in enumerate(words):
            if j == word1:
                w1 = i
            elif j == word2:
                w2 = i
            distance = min(distance, abs(w1-w2))
        return distance
