# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single
# count and character. For example, the string "AAAABBBCCDAA" would be
# encoded as "4A3B2C1D2A".









def len_encode(txt):
	lst = [txt[0]]
	for x in txt[1:]:
		if lst[-1][-1]==x:
			lst[-1]+=x
		else:
			lst.append(x)
	return ''.join((str(len(x))+x[0]) for x in lst)
	
	


def len_decode(txt):
	return ''.join(int(txt[x])*txt[x+1] for x in range(0,len(txt),2))




	
print(len_encode('AAAABBBCCDAA'))
print(len_decode('4A3B2C1D2A'))


print(len_encode('QWER'))
print(len_decode('1Q1W1E1R'))

