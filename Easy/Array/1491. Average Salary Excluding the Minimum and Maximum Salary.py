class Solution:
    def average(self, salary: List[int]) -> float: 
        
        salarySort = sorted(salary)
        salarySort  = salarySort [1:-1]
        return sum(salarySort) / (len(salary)-2)
        
        
# Straightforward

class Solution:
    def average(self, salary: List[int]) -> float: 
        
        return (sum(salary)-max(salary)-min(salary)) / (len(salary)-2)
    
    
