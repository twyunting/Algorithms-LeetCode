def isPalindrome(s):
	"""
	:type s: str
	:rtype: bool
	"""

	p1, p2 = 0, len(s)-1

	while p1 < p2:
		while p1 < p2 and not s[p1].isalnum(): #Check if all the characters in the text are alphanumeric
			p1 += 1
		while p1 < p2 and not s[p2].isalnum():
			p2 -= 1

		if  s[p1].lower() != s[p2].lower():
			return False

		p1 += 1
		p2 -= 1

	return True		


s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))
print(len(s))

"""
# Two pointers:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1
        while left < right:
            str_left = s[left].lower()
            str_right = s[right].lower()
            if str_left.isalnum() and str_right.isalnum():
                if str_left != str_right:
                    return False
                left += 1
                right -= 1
            else:
                if not str_left.isalnum():
                    left += 1
                if not str_right.isalnum():
                    right -= 1
        return True 
"""

# elegant method

def isPalindrome(s):
        
    string = "".join(i for i in s if i.isalnum())
    low_string = string.lower()
        
    return low_string == low_string[::-1]


s = "race a car"

print(isPalindrome(s))
print(len(s))        

# same method with another type of for loop

def isPalindrome(s):
        
    string = ""
    for i in s:
        if i.isalnum():
            string += string.join(i)
    low_string = string.lower()

    return low_string == low_string[::-1]


s = "race a car"

print(isPalindrome(s))
# test zone

def isPalindrome(s):
        
    string = "".join(i for i in s if i.isalnum())
    low_string = string.lower()
        
    return low_string


s = "race a car"

print(isPalindrome(s))


def isPalindrome(s):
        
    string = ""
    for i in s:
        if i.isalnum():
            string += string.join(i)
    low_string = string.lower()

    return low_string


s = "race a car"

print(isPalindrome(s))
