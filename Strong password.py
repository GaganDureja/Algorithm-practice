#Link: https://www.hackerrank.com/challenges/strong-password/problem



numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+" 
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 4    
    if any(x in numbers for x in password):	count-=1
    if any(x in lower_case for x in password): count-=1
    if any(x in upper_case for x in password): count-=1
    if any(x in special_characters for x in password): count-=1
    return count if n+count>5 else 6-n





print(minimumNumber(3,'790'))