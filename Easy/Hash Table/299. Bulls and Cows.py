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

# two hashmap with different output

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        secretdic, guessdic = {}, {}
        A, B = 0, 0 #A = bull, B = cow
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if secret[i] in secretdic:
                    secretdic[secret[i]] += 1
                else:
                    secretdic[secret[i]] = 1
                if guess[i] in guessdic:
                    guessdic[guess[i]] += 1
                else:
                    guessdic[guess[i]] = 1
        
        for i in secretdic:
            if i in guessdic:
                B += min(secretdic[i], guessdic[i])
        return "{}A{}B".format(A, B)
        
        
