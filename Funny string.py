#Link: https://www.hackerrank.com/challenges/funny-string/problem


def funnyString(s):
	for x in range(1,len(s)):
		if abs(ord(s[x])-ord(s[x-1]))!= abs(ord(s[-x])-ord(s[-x-1])):
			return 'Not Funny'
	return 'Funny'



print(funnyString('bcxz'))