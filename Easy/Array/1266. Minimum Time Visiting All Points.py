class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        x1, x2 = points[0]
        count = 0
        
        for i in range(1, len(points)):
            y1, y2 = points[i]
            count += max(abs(x1 - y1), abs(x2 - y2))
            x1, x2 = points[i]
        
        return count
            
