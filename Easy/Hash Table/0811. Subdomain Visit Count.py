class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        counter = Counter()
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            subs = domain.split(".")
            for i in range(len(subs)):
                counter[".".join(subs[i:])] += int(count) # bulid a 
                
        return [ f'{count} {domain}' for domain, count in counter.items()]
    
    """
    the f string is also known as the literal string to insert a variable into the string and make it part so instead of doing
    
    x = 12
    y = 10

    word_string = f'{x} plus {y} equals: {x+y}
    output: 12 plus 10 equals: 22

    Reference: https://stackoverflow.com/questions/57150426/what-is-printf#:~:text=The%20f%20means%20Formatted%20string%20literals%20and%20it%27s,which%20are%20expressions%20delimited%20by%20curly%20braces%20%7B%7D.

    """
        
