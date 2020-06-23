class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) == 2:
            return True
        
        x1 = coordinates[0][0]
        x2 = coordinates[1][0]
        y1 = coordinates[0][1]
        y2 = coordinates[1][1]
        
        for i in range(len(coordinates)):
            (x3, y3) = coordinates[i]
            if (y2-y1) * (x3-x2) != (x2-x1) * (y3-y2):  # not equal means avoid to divide zero
                return False
        return True 
        
        
"""
Slope Formula:

slope = rise垂直 / run水平 
=> (y2-y1) / (x2-x1) == (y3-y2) / (x3-x2)
=> (y2-y1) * (x3-x2) == (x2-x1) * (y3-y2)

then set 3 spots to compare
"""


