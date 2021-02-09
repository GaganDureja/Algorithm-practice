# This problem was asked by Google.

# Given a word W and a string S, find all starting indices in S which are anagrams of W.

# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.













def anagram(w,s):
	res = []
	for x in range(len(s)):
		word = s[x:x+len(w)]		
		if word==w or word==w[::-1]:
			res.append(x)
	return res



print(anagram('ab','abxaba'))