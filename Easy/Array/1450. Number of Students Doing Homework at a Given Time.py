class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]: # fixed the position
                count += 1
        return count
        
   
# Zip solution

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                count += 1
        return count
