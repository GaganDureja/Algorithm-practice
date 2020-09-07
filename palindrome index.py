#Link: https://www.hackerrank.com/challenges/palindrome-index/problem



def palindromeIndex(s):
	if s==s[::-1]: return -1	
	for x in range(len(s)):		
		if s[x]!= s[-(x+1)]:
			first = [alpha for alpha in s]
			last = [alpha for alpha in s]
			first.pop(x)
			last.pop(-(x+1))
			return x if first==first[::-1] else len(s)-(x+1)
	return -1
			







print(palindromeIndex('quyjjdcgsvvsgcdjjyq'))
print(palindromeIndex('aaab'))