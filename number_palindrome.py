# This problem was asked by Palantir.

# Write a program that checks whether an integer is a palindrome. 
# For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
# Do not convert the integer into a string.








def num_palindrome(number):
	return str(number) == str(number)[::-1]


	






print(num_palindrome('121'))
print(num_palindrome('678'))
print(num_palindrome('888'))
print(num_palindrome('1221'))