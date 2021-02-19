# This problem was asked by Google.

# Given a string which we can delete at most k, return whether you can make a palindrome.

# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.















def palindrome(word,k):	
	return True if len([x for x in sorted(word) if sorted(word).count(x)%2 ])<=k else False


	



print(palindrome("waterrfetawx",2))
print(palindrome("waterrfetawxee",2))
print(palindrome("waterrfeqtawx",2))
