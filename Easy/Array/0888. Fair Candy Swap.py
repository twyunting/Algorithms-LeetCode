class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        
        # they both have the same total amount of candy.
        # y = x + (Bob-Alice) / 2
        
        sumAlice, sumBob, setBob = sum(A), sum(B), set(B)
        
        for x in A:
            if x + (sumBob-sumAlice) / 2 in setBob:
                return [x, x + (sumBob-sumAlice) / 2]
        
        
        
