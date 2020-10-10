#Link: https://www.hackerrank.com/challenges/two-strings/problem



def twoStrings(s1, s2):
	return 'Yes' if set(s1) & set(s2) else 'No'







print(twoStrings('h','world'))
print(twoStrings('hello','world'))
