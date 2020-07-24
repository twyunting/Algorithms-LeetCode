class Solution:
    def average(self, salary: List[int]) -> float: 
        
        salarySort = sorted(salary)
        salarySort  = salarySort [1:-1]
        return sum(salarySort) / (len(salary)-2)
        
        
