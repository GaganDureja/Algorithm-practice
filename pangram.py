#Link: https://www.hackerrank.com/challenges/pangrams/problem


def pangrams(s):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	return 'pangram' if all(any([x.upper() in s, x in s]) for x in alpha) else 'not pangram'





print(pangrams('abcdefghIicjklmnopqrstuvwxyz'))