# This problem was asked by Google.

# Find the minimum number of coins required to make n cents.

# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.





def min_coins(n):
	lst = []
	while n!=0:
	 	if n>= 25:
	 		lst.append(25)
	 		n-= 25
	 	elif n>=10:
	 		lst.append(10)
	 		n-= 10 		
	 	elif n>=5:
	 		lst.append(5)
	 		n-=5
	 	else:
	 		lst.append(1)
	 		n-=1
	return len(lst)







print(min_coins(100))
print(min_coins(16))