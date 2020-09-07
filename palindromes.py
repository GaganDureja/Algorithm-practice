#Link: https://www.hackerrank.com/challenges/the-love-letter-mystery/problem


def theLoveLetterMystery(s):
	l = len(s)//2
	left = s[:l]
	right = s[l+(1 if len(s)%2 else 0):] [::-1]	
	return sum([abs(ord(left[x])-ord(right[x])) for x in range(len(left))])
	







print(theLoveLetterMystery('abcd'))