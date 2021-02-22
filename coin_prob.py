# This problem was asked by Microsoft.

# You have n fair coins and you flip them all at the same time. Any that come up tails you set aside.
# The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

# Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.


















def coin_prob(n):
	count = 0
	while n!=1:
		n//=2
		count+=1
	return count
	

print(coin_prob(5))

print(coin_prob(8))
