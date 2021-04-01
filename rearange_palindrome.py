
# This problem was asked by Amazon.

# Given a string, determine whether any permutation of it is a palindrome.

# For example, carrace should return true, since it can be rearranged to form racecar,
# which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.








def str_palindrome(word):
	return sum(word.count(x)%2 for x in word)<=1


	






print(str_palindrome('carrace'))
print(str_palindrome('daily'))
print(str_palindrome('decced'))
