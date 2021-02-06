# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

# For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False. 











def list_palindrome(n):
	s = n.replace('-','').replace('>','')
	return s==s[::-1]

	




print(list_palindrome('1 -> 4 -> 3 -> 4 -> 1'))

print(list_palindrome('1 -> 4'))