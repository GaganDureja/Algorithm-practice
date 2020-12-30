# This problem was asked by Microsoft.

# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.




def sum10(n):
	return [str(n)+str(x) for x in range(1,10) if n+x==10][0]





print(sum10(1))
print(sum10(2))

