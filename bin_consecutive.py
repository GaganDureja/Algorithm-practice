# This problem was asked by Stripe.

# Given an integer n, return the length of the longest consecutive run of 
# 1s in its binary representation.

# For example, given 156, you should return 3.












def bin_consecutive(n):	
	lst = []
	count = 0
	for x in bin(n):
		if x=='1':
			count+=1
		else:
			lst.append(count)
			count=0
	return max(lst)





	


	




print(bin_consecutive(156))