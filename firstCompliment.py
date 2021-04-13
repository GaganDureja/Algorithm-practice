T# his problem was asked by Facebook.

# Given a 32-bit integer, return the number with its bits reversed.

# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
# return 0000 1111 0000 1111 0000 1111 0000 1111.








def firstCompliment(number):
	res = ""
	for x in number:
		if x=='1':
			res+='0'
		elif x=='0':
			res+='1'
		else:
			res+=' '
	return res


	






print(firstCompliment('1111 0000 1111 0000 1111 0000 1111 0000'))