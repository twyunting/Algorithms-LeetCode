class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        
        odd_parity, even_parity = 0, 0
        
        for i in chips:
            if i % 2 == 0:
                even_parity += 1
            else:
                odd_parity += 1
            
        return min(even_parity, odd_parity)
    
    

