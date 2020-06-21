class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        from datetime import datetime
        
        return days[date(year, month, day).weekday()]
    
    """
    date.weekday()
    Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    For example, date(2002, 12, 4).weekday() == 2, a Wednesday.  
    # 0: Mon, 1: Tue, 2: Wed
    
    """
    
    
