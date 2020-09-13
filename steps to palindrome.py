#Link: https://edabit.com/challenge/WyttgdGuQGaRBqhhP



def min_palindrome_steps(txt):
	for x in range(len(txt)):
		res = txt + txt[:x][::-1]
		if txt[x] == txt[-1] and res== res [::-1]:
		 	return x
	





print(min_palindrome_steps("mirror"))