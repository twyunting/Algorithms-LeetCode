# talented solution

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        A = sum(i == j for i, j in zip(secret, guess))
        B = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (A, sum(B.values())-A)
    
    
    """
    %d is a integer decimal representation of a numeric object. (It will raise TypeError for non-numeric objects). 
    %s is the string representation of an object(equivalent to calling str () on it).
    
    Example:
    name = 'cyborg' 
    number = 31 
    print '%s %d' % (name, number) 
    """
